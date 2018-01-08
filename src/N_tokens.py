import tarfile
import sqlite3
from collections import Counter
import re


def main():


    extract_elements = False
    exportarTextFile = False


    if extract_elements:

        path2input = './data.tar.gz'
        path2output = './data'

        cf = tarfile.open(name=path2input, mode='r', bufsize=10240)

        print(cf.list())

        cf.extractall(path=path2output)


    if exportarTextFile == True:

        path2db = './data/RECLAMOS_CL'

        conn = sqlite3.connect(path2db)
        curs = conn.cursor()
        curs.execute('SELECT reclamo FROM reclamos_cl')

        textfile = 'reclamos_text.txt'

        with open(textfile, 'w') as text_file:

            for row in curs:

                text = row[0]
                text_file.write(text)


    filename = 'reclamos_text.txt'

    punctuation = '¿?.,\n'
    map_punctuation = {'¿': '<ai>', '?': '<ci>', '.': '<pt>', '\n': '<nl>', ',': '<cm>'}

    letras = set('aáeéoóíúiuübcdfghjklmnñopqrstvwxyz')
    acc_chars = set(punctuation).union(letras)

    text = open(filename).read()
    text = text.lower()


    # elimina puntuación y pon espacios donde se necesite

    char_tokens = []

    for c in text:
        to_append = ''
        if c in letras or c == ' ':
            to_append = c
        elif c in punctuation:
            to_append = ' ' + map_punctuation[c] + ' '
        char_tokens.append(to_append)


    text = re.sub(' +', ' ', ''.join(char_tokens))


    word_tokens = text.split(' ')

    # computa las palabras más comunes
    word_cnt = Counter()
    for word in word_tokens:
        word_cnt[word] += 1

    print(' N Tokens : ', len(word_tokens))


if __name__ == '__main__':
    main()
