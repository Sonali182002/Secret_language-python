import random
import string

code=input("enter your lanaguge: ")
words=code.split(" ")
ans=input("you want code or decode: ")

def coding(code):
    print("coded message is:  ")
    nwords=[]
    for word in words:
        
        if(len(word)<=2):
          nwords.append(word[::-1])
          #print(" ".join(nwords))
          
        else:
          word= word[1:]+word[0]
          char=''.join(random.choice(string.ascii_lowercase)for _ in range(3))
          newcode=char+word+char
          nwords.append(newcode)
          #print(" ".join(nwords))
    print(" ".join(nwords))
    
          

def decode(code):
   nwords=[]
   for word in words:
        
        if(len(word)<=2):
          nwords.append(word[::-1])
          
        else:
          dchar=word[3:-3]
          dechar=dchar[-1]+dchar[:-1]
          nwords.append(dechar)
   print(" ".join(nwords))      
     
    

if(ans=="code"):
    coding(code)
else:
    decode(code)