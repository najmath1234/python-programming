text=input("enter a text:")
def count_words(text):
    words=text.lower().split()
    word_cound=()
    for word in words:
        if word in word_count:
            word_count[word[word]]+=1
        else:
                word_count[word]=1
    return word_count
result=count_words(text)
print(result)
