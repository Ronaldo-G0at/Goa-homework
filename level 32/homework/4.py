def insert_word(sentence, word, index):
    sentence_list = sentence.split()
    sentence_list.insert(index, word)
    return ' '.join(sentence_list)

sentence = "Hello world, how are you?"
word = "beautiful"
index = 2
result = insert_word(sentence, word, index)
print(result)
