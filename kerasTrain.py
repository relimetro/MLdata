from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import numpy as np
from datatypes import LifestyleQuestionareFromDataset, LifestyleQuestionareToNumeric

# requires tensorflow (and keras)


# 1 hidden @ 64
# Test loss: 0.2752630114555359
# Test accuracy: 0.9380000233650208

# 1 hidden @ 32
# Test loss: 0.35636627674102783
# Test accuracy: 0.8510000109672546

# 1 hidden @ 128
# Test loss: 0.07028135657310486
# Test accuracy: 0.9739999771118164

# 2 hidden @ 128 (their seems to be variability)
# Test loss: 0.16173362731933594
# Test accuracy: 0.9539999961853027
# Test loss: 0.06511779874563217
# Test accuracy: 0.968999981880188
# Test loss: 0.06337974965572357
# Test accuracy: 0.9850000143051147

# 2 hidden @ 64
# Test loss: 0.07828514277935028
# Test accuracy: 0.9760000109672546
# Test loss: 0.08978542685508728
# Test accuracy: 0.972000002861023

# 3 hidden @ 64
# Test loss: 0.13417299091815948
# Test accuracy: 0.9409999847412109
# Test loss: 0.06634949892759323
# Test accuracy: 0.9750000238418579

# NOTE: num epocs might affect score (larger having less time to train relative to size)



# DECLARE MODEL
model = Sequential() # Create a sequential model
# Input
model.add(Dense(64, activation='relu', input_shape=(22,))) # 22 input paramaters
# Hidden
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
# Output
model.add(Dense(2, activation='softmax')) # changed to double (to_categorical), chance of being true or false

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])






# GET TRAINING DATA
x_life = []
y_life = []
f = open("dataset/dementia_patients_health_data.csv","r")
for content in f.read().split("\n")[1:]: # ignore first line which is headers
	if content == "" : continue
	x = LifestyleQuestionareFromDataset(content.split(","))
	x2 = LifestyleQuestionareToNumeric(x)
	if len(x2) != 23 : raise Exception("not 23 (22 without dementia)")
	x_life.append(x2[:-1])
	y_life.append(int(x2[-1]))


# turn into np.array
x_life = np.array(x_life,dtype=int)
y_life = np.array(y_life,dtype=int)

# Preprocess the data
# x_train = x_train.reshape(-1, 784) / 255.0
# x_train = x_life.reshape(-1, 784) / 255.0
# x_test = x_test.reshape(-1, 784) / 255.0
x_life = x_life.reshape(-1,22)
y_life = to_categorical(y_life) # turn into double (chance of being each possible state)






# TRAIN MODEL
model.fit(x_life, y_life, batch_size=128, epochs=10, validation_data=(x_life, y_life))

# Evaluate the model
loss, accuracy = model.evaluate(x_life, y_life)
print(f"Test loss: {loss}")
print(f"Test accuracy: {accuracy}")

# Save model
filename = "kerasOut/model.keras"
model.save(filename)
print(f"saved as {filename}")

