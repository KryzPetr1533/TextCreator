import re
import numpy as np

with open("data.txt", 'r', encoding='utf-8') as text:
    text_readed = text.read().lower()
    text_arr = re.split(r'\W+', text_readed)
    text_arr = [i for i in text_arr if i != '']
    dict_data = {}
    length = len(text_arr)
    for i in range(length - 2):
        pair = text_arr[i] + " " + text_arr[i + 1]
        if dict_data.get(pair, 0) is not 0:
            if dict_data[pair].get(text_arr[i + 2], 0) is not 0:
                dict_data[pair][text_arr[i + 2]] = dict_data[pair][text_arr[i + 2]] + 1
        else:
            dict_data[pair] = {text_arr[i + 2]: 1}
    print(dict_data.keys())

    n = int(input())
    last_words = np.random.choice(list(dict_data.keys()), size=1)[0].split()
    print(last_words)
    for i in range(n):
        last_two = last_words[len(last_words) - 2] + " " + last_words[len(last_words) - 1]
        if dict_data.get(last_two):
            last_words.append(
                np.random.choice(list(dict_data[last_two].keys()), size=1, p=list(dict_data[last_two].values()))[0])
        else:
            last_two = np.random.choice(list(dict_data.keys()), size=1)[0]
            last_words.append(np.random.choice(
                list(dict_data[last_two].keys()), size=1)[0])
    for i in last_words:
        print(i, end=' ')
