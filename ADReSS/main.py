from os.path import isdir
from CHAFile.ChaFile import *
import os


def dirMap(func, parent: str, fil: str|None = None) -> None:
	for x in os.listdir(parent):
		path: str = parent+"/"+x
		if os.path.isdir(path):
			dirMap(func,path,fil)
		elif fil == None or x.endswith(fil) : func(path)





	
def chaFileData(cha: ChaFile, quiet: bool) -> None:
	keyList: list[str] = ['número_de_linea', 'número_de_emisión', 'hablante', 'emisión', 'bullet', 'mor', 'gra', 'destinatario']
	true: bool = True # validate data is the same

	lines: list = cha.getLines()
	for line in lines:
		if not quiet : print(type(line))
		# print(line)

		# validate
		for keyIn in line.keys():
			if keyIn not in keyList : true = False
		if len(line.keys()) != len(keyList) : true = False

		if not quiet :
			for keyIn in line.keys():
				print(f"{keyIn}: {line[keyIn]}")

		if not quiet : print()
	if not quiet : print(true)
	elif not true : raise ValueError("Data not expected")


def showLines(cha: ChaFile) -> str:
	out = ""
	talker = ""
	for line in cha.getLines():
		cTalker = line["hablante"]
		if talker != cTalker:
			talker = cTalker
			out += f"\n{talker}\n"
		out += f"{line["emisión"]}\n"
	return out


def getPar(cha: ChaFile) -> str:
	out = ""
	for line in cha.getLines():
		talker = line["hablante"]
		if talker == "PAR":
			out += f"{line["emisión"]}\n"
	return out



def to_jsonl(jsonInput:str, jsonOutput:str) -> str :
	jsonInput = jsonInput.replace("\n"," ")
	return '{"contents":[{"role":"user","parts":[{"text":"'+jsonInput+'}]},{"role":"model","parts":[{"text":"'+jsonOutput+'"}]}]},\n'


def loadMMSE() -> dict[str,str]:
	out = {}
	with open("train/cc_meta_data.txt") as f:
		for line in f.readlines():
			iden = line.split(";")[0].strip()
			mmse =  line.split(";")[3].strip()
			if iden != "ID" and mmse != "NA":
				out[iden] = mmse
	with open("train/cd_meta_data.txt") as f:
		for line in f.readlines():
			iden = line.split(";")[0].strip()
			mmse =  line.split(";")[3].strip()
			if iden != "ID" and mmse != "NA":
				out[iden] = mmse
	return out



def removeBracket(x:str, opening:str, closing:str) -> str :
	out = ""
	depth = 0
	for char in x:
		if char == opening :
			depth = depth +1
		if char == closing and depth > 0 :
			depth = depth -1
		if depth == 0:
			out = out + char
	return out

def cleanCha(x:str) -> str:
	# ampersand word
	x = x.replace(":","")
	x = x.replace("&=laughs","")
	x = x.replace("&=sighs","")
	x = x.replace("=hums","")
	x = x.replace("&uh","uh")
	x = x.replace("&um","um")
	x = x.replace("&sh","sh")
	x = x.replace("&hm","hm")
	x = x.replace("<","")
	x = x.replace(">","")
	x = x.replace("]","")
	x = x.replace("+/?","")
	x = x.replace("+...","")
	x = x.replace("[/","")
	x = x.replace(" /",",")

	x = x.replace("[+ exc",",")
	x = x.replace("[+ gram",",")
	x = x.replace("[+ jar",",")
	x = x.replace("[+ cir",",")
	x = x.replace("[+ es",",")
	x = x.replace("[*",",")
	x = x.replace("[",",")

	# in order
	x = x.replace("(.)","")
	x = x.replace("(..)","")
	x = x.replace("(...)","")
	x = x.replace("(","")
	x = x.replace(")","")

	x = x.replace("&","")
	x = x.replace("+","")

	x = x.replace("  "," ")
	x = x.replace(" .",".")
	x = x.replace(" ,",",")
	x = x.replace(".,",".")
	x = x.replace(".,",".")
	return x





def main():
	mmseData = loadMMSE()

	content = [""]
	def addToContent(x:str) -> None:
		content[0] += x

	def foo(x:str):
		iden = x.split("/")[-1].split(".")[0]
		if iden in  mmseData:
			mmse = mmseData[iden]
			x = getPar(ChaFile(x))
			x = cleanCha(x)
			return addToContent(to_jsonl(x,mmse))
		return None

	dirMap(lambda x: foo(x), ".",".cha")

	with open("out.jsonl","w") as f:
		f.write(content[0])

main()

