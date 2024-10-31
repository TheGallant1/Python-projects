def wordsplit():
    sentence=input("enter a sentence : ")
    words=sentence.split()
    my_dictionary={}
    for word in words:
        my_dictionary[word]=words.count(word)
    return my_dictionary   

print(wordsplit())