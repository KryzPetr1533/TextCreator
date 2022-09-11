import re
import numpy as np
import pickle as pkl

with open("model.pkl", 'rb') as model:
    dict_data = pkl.load(model)
    n = int(input())
    last_words = np.random.choice(list(dict_data.keys()), size=1)[0].split()
    for i in range(n):
        last_two = last_words[len(last_words) - 2] + " " + last_words[len(last_words) - 1]
        if dict_data.get(last_two):
            last_words.append(np.random.choice(list(dict_data[last_two].keys()), size=1)[0])
        else:
            last_two = np.random.choice(list(dict_data.keys()), size=1)[0]
            last_words.append(np.random.choice(list(dict_data[last_two].keys()), size=1)[0])

    for i in last_words:
        print(i, end=' ')
