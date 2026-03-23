#write a program to compute the frequency of the words from the input.
# Roll Number : 92400527154 : Name : Aarchi Nakum

text = "Hello there this is python. python is good"

text = text.replace(".","").replace(".","")
words = text.split()

freq = {}

for word in words:
    word = word.capitalize()
    if word in freq:
        freq[word]+=1
    else:
        freq[word] = 1

for word in sorted(freq):
    print(f"{word} : {freq[word]}")
    

