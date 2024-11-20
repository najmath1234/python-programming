words=input("Enter a list of words seperated by spaces:").split()
longest_word=" "
for word in words:
    if len(word) >len (longest_word):
        longest_word=word
print("length of largest word",len(longest_word))
