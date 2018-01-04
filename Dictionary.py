#import module PyDictionary
#https://pypi.python.org/pypi/PyDictionary 
from PyDictionary import PyDictionary
def dictionary_search(word):
    dictionary=PyDictionary(word)
    print('Meaning is')
    print(dictionary.getMeanings())
    print('Antonyms are ')
    print(dictionary.getAntonyms())
    print('Synonyms are ')
    print(dictionary.getSynonyms())