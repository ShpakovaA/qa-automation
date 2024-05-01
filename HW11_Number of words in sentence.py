# Number of words in sentence
sentences = """Hello  all. 
Here's pretty cold and hot..... 
 Choose yourself."""

sentences_lst = sentences.split(". ")
words_number = []

for index, sentence in enumerate(sentences_lst):
    sentence_length = len(sentences_lst[index].split())
    words_number.append(sentence_length)

print(words_number)
