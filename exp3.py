#!/usr/bin/env python3

print("------------Coversation Generator------------")
a = input("Answer the questions below:\nWhat is your name?\n")
b = input("Write Something below:\n")

def f1(n="MR. NOBODY",s="idiot"):
	print("So, you are",n,"\nAnd, what you wrote there is what you are...\nSo... You are",s)

def f2(s):
	print("So, you are Mr. Nobody\nAnd, what you wrote there is what you are...\nSo... You are",s)
	
if(a==''):
	if(b==''):
		f1()
	else:
		f2(b)
else:
	if(b==''):
		f1(a)
	else:
		f1(a,b)
	
f1(a,b)
