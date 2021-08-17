import re
from corpus_loader import word_list, name_list

def split(word):
    return [char for char in word]

def encrypt(text,key):

    res = ""
    txtArr = split(text)
    for char in txtArr:

        if (char.isupper()):
            res += chr((ord(char) + key-65) % 26 + 65)
   
        else:
            res += chr((ord(char) + key - 97) % 26 + 97)
    return res


def decrypt(text,key):
    return encrypt(text,-key)


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
        else:
            pass
            # print('not english word or name', word)

    return word_count


def crack(text):
    
   for i in range(1,100):

        newText = decrypt(text,i)

        newTextSpace = newText.replace('n',' ')

        word_count = count_words(newTextSpace)
        percentage = int(word_count / len(newTextSpace.split()) * 100)
        if percentage > 50:
                print(text, percentage)
                print(f'Cracked sentence: {newTextSpace}')
                print(f'Key is {i}')
                return 
                


crack('Lwqzdvqwkhqehvwqriqwlphvcqlwqzdvqwkhqzruvwqriqwlphv')





