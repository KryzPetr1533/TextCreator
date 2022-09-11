import re
import pickle as pkl

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
    with open("model.pkl", 'wb') as file:
        pkl.dump(dict_data, file)
