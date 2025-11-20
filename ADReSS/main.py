from os.path import isdir
from CHAFile.ChaFile import *
import os


def dirMap(func, parent: str, fil: str|None = None) -> None:
	for x in os.listdir(parent):
		path: str = parent+"/"+x
		if os.path.isdir(path):
			dirMap(func,path,fil)
		elif fil == None or x.endswith(fil) : func(path)

dirMap(lambda x: print(x), ".",".cha")



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



cha: ChaFile = ChaFile("train/transcription/cc/S001.cha")
chaFileData(cha,True)
# print(showLines(cha))

dirMap(lambda x: print("\n\n\nStart\n---\n"+showLines(ChaFile(x))), ".",".cha")
