import numpy as np
import pickle as pkl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', help='path to load the model, model.pkl by default', default="./model.pkl")
parser.add_argument('--length', help='the length of the sentence', type=int, default=10)
parser.add_argument('--prefix', help='the beginning of the sentence')
args = parser.parse_args()
with open(args.model, 'rb') as model:
    dict_data = pkl.load(model)
    n = args.length
    last_words = []
    if args.prefix is None:
        last_words = np.random.choice(list(dict_data.keys()), size=1)[0].split()
    else:
        last_words = args.prefix.split()
    for i in range(n):
        last_two = last_words[len(last_words) - 2] + " " + last_words[len(last_words) - 1]
        if dict_data.get(last_two):
            last_words.append(np.random.choice(list(dict_data[last_two].keys()), size=1)[0])
        else:
            last_two = np.random.choice(list(dict_data.keys()), size=1)[0]
            last_words.append(np.random.choice(list(dict_data[last_two].keys()), size=1)[0])

    for i in last_words:
        print(i, end=' ')
