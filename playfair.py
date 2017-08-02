import random

def contains(PT,character):
	for i in PT:
		if(i==character):
			return True
	return False

def contain_duplicates(PT):	
	for i in range(len(PT)-1):
		if(PT[i]==PT[i+1]):
			return True
	return False

def insert_pad(PT,pad):
	if(contain_duplicates(PT)==False):
		return PT
	for i in range(len(PT)-1):
		if(PT[i]==PT[i+1]):
			left=PT[:i+1]
			left=left+pad
			PT=left+PT[i+1:]
			if(contain_duplicates(PT)):
				PT=insert_pad(PT,pad)

	return PT

PT=raw_input("Enter PlainText:")
choice=raw_input("will you provide a key?(y/n)")
if(choice=='y')
	user_key=raw_input("Enter key please:")

pad='x'
while(contains(PT,pad)==True):
	pad=chr(97+random.randint(0,25))

if(contain_duplicates(PT)==True and len(PT)%2==1):
	PT=insert_pad(PT,pad)

if(len(PT)%2==1):
	PT=PT+pad

pairs=[]
if(len(PT)%2==0):
	for i in range(len(PT)-1):
		if(i%2==0):
			pairs.append([PT[i],PT[i+1]])




print(insert_pad("helll",'x'))