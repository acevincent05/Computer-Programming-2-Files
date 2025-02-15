import re

#accesses the text file
with open("text_file.txt", "r", encoding="utf-8") as file:
    global content
    content = file.read()

#checks if third or first person perspective of writiing
if re.search(r'I|me|we|us', content):
    print(f'Essay POV: Third Person')
else:
    print(f'Essay POV: First Person')

#splits the paragraphs into sentences
sentences = re.split(r'(?<=[.!?])\s+', content)  

#for getting the words of each sentence and the number of words
sentence_words = []
num_words = []

#splits the words of each sentence
for each_sentence in sentences:
    words = re.findall(r'\b\w+\b', each_sentence)
    sentence_words.append(words)

#determines the number of words per sentence 
for words in sentence_words:
    num_words.append(len(words))

#displays the info
print(f'Total number of words: {sum(num_words)}')
print(f'Number of sentences: {len(sentence_words)}')
print(f'Highest number of words used in a sentence: {max(num_words)}')
print(f'Lowest number of words used in a sentence: {min(num_words)}')
print(f'Average words per sentence: {sum(num_words)/len(sentence_words): .2f}')