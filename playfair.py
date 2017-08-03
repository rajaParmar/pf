import random

def get_coord(key,character):
	for i in range(0,5):
		for j in range(0,5):
			if(key[i][j]==character):
				return [i,j]
	return [-1,-1]			


def encrypt(PT,key):
	for i in PT

def contains(PT,character):
	for i in PT:
		if(i==character):
			return True
	return False

def create_default(alphabets,temp,alpha_index,key):
	for i in range(1,26):
		if(i%5==0):
			key.append(temp)
			temp=[]

		temp.append(alphabets[alpha_index])
		alpha_index=alpha_index+1



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

def permutate(alphabets):
	for i in range(0,25):
		ran_index=random.randint(0,25)
			alphabets[ran_index],alphabets[25-ran_index]=alphabets[25-ran_index],alphabets[ran_index]

PT=raw_input("Enter PlainText:")
choice=raw_input("will you provide a key?(y/n)")
user_key=""
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

alphabets=[]
for i in range(97,97+26):
	char=chr(i)
	if(char=='i'):
		continue
	alphabets.append(char)
#print(alphabets)
key=[]
alpha_index=0
temp=[]

create_default(alphabets,temp,alpha_index,key)

print(key)
