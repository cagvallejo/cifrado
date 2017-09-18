'''
Created on 18 sept. 2017

@author: vallejo
'''

global valid_words


def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may take a while to
    finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


WORDLIST_FILENAME = 'words.txt'


valid_words = load_words(WORDLIST_FILENAME)

print("caggg" in valid_words)
valid_words.append("caggg")
print("caggg" in valid_words)
