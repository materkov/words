import json

from navec import Navec
from main import good_words
import itertools

path = '/Users/m.materkov/Downloads/navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)

file_object = open('result.txt', 'w')
file_object.close()


global_result = {}

count = 0
total_count = len(good_words)

for good_word in good_words:
    word_sim = {}


    for word in good_words:
        if word != good_word:
            word_sim[word] = float(navec.sim(good_word, word))

    word_sim = dict(reversed(sorted(word_sim.items(), key=lambda item: item[1])))
    word_sim = dict(itertools.islice(word_sim.items(), 50))

    file_object = open('result.txt', 'a')
    file_object.write(json.dumps({
        "word": good_word,
        "sim": word_sim,
    }))
    file_object.write("\n")
    file_object.close()

    count += 1
    print(str(count/total_count*100) + "%")

print(count, total_count)
