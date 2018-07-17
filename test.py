from random import randint
from pprint import pprint
import csv


global filename, word_dic
filename = 'data\\Lana_del_rey\\lyrics.csv'
word_dic = {}

# This NLP model use the idea of Markov chain

def get_words(str):
    words = str.split("|-|")
    output = []
    for word in words:
        w = word.split()
        w.append("\n")
        for i in w:
            temp = []
            for chr in i:
                if chr not in '!"#$%&\()*+,-./:;<=>?@[]^_`{|}~':
                    temp.append(chr)
            output.append(''.join(temp))
    return output


# update the word_dic which contains the word and the words list of possible next word (with the times it appears)
def get_words_dic(words):
    for pos in range(len(words)-1):
        try:
            word_dic[words[pos]][words[pos + 1]] += 1
        except:
            try:
                word_dic[words[pos]][words[pos + 1]] = 0
            except:
                word_dic[words[pos]] = {}
                word_dic[words[pos]][words[pos + 1]] = 0


def get_random_word(sub_word_dict):
    index = randint(0, len(sub_word_dict)-1)
    return list(sub_word_dict.keys())[index]


if __name__ == "__main__":
    lyrics = csv.reader(open(filename, 'r'))
    for row in lyrics:
        if row[2] != "":
            words = get_words(row[2])
            get_words_dic(words)
    output = ""
    current = input("Give me a word and I will get a Lana_Del_Rey style's song for you: ")
    for i in range(100):
        output += current
        output += " "
        current = get_random_word(word_dic[current])
    # pprint(word_dic)
    print("\n")
    print(output)