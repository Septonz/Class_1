intro=input("Enter Your Introduction: ")
print(intro)
charCount=0
wordCount=1
for char in intro:
    charCount=charCount+1
   
    if(char==" "):
        wordCount=wordCount+1
       
print("Number of word in the string: ")         
print(wordCount)
print("Number of charecters in the string: ")         
print(charCount)