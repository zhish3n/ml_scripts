import nltk
from nltk import word_tokenize
from urllib import request

# change the path to where the nltk data is being stored
nltk.data.path.append('/Users/zhi/Documents/Programming/PROJECTS_Python/data')

s = input('Enter some text: ')
print('You typed', len(word_tokenize(s)), 'words.')
