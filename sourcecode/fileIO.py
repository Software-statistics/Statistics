#-*- coding:UTF-8 -*- 

def fwrite(path, message):
	f = open(path,"w")
	f.write(message)
	f.close
	
def fread(path):
	f = open(path,"r")
	for line in f:
		print line
	f.close