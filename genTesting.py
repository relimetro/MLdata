
HF_token = "REDACTED"


from transformers import AutoTokenizer
MODEL = "google/gemma-3-1b-it"
tokenizer = AutoTokenizer.from_pretrained(MODEL,token=HF_token)


f = open("genOut.csv","r")
train_dataset = []
eval_dataset = []
for line in f.readlines():
	train_dataset.append(",".join(line.split(",")[:-1]))
	eval_dataset.append(line.split(",")[-1])
f.close()

tokenized_train_dataset = tokenizer(train_dataset,padding=True,truncation=True)
tokenized_eval_dataset = tokenizer(eval_dataset,padding=True,truncation=True)


from transformers import AutoModelForCausalLM, Trainer, TrainingArguments
model = AutoModelForCausalLM.from_pretrained(MODEL,token=HF_token)
training_args = TrainingArguments(
	output_dir="./results",
	eval_strategy="steps",
	eval_steps=500,
	learning_rate=2e-5,
	per_device_train_batch_size=8,
	num_train_epochs=3,
	weight_decay=0.01,
	save_steps=1000,
	logging_dir="./logs",
)

trainer = Trainer(
	model=model,
	args=training_args,
	train_dataset=tokenized_train_dataset,
	eval_dataset=tokenized_eval_dataset,
)
trainer.train()

model.save_pretrained("./final_model")
tokenizer.save_pretrained("./final_model")

