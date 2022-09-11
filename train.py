import re
import pickle as pkl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', help='path to save your model, model.pkl by default', default="./model.pkl")
parser.add_argument('--input-dir', help='path to data to train the program')
args = parser.parse_args()
name = args.input_dir
if args.input_dir is None:
    print("Введите адрес директории:")
    name = input()

with open(name, 'r', encoding='utf-8') as text:
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
    with open(args.model, 'wb') as file:
        pkl.dump(dict_data, file)
