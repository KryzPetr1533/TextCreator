import re
text = open("data.txt", 'r', encoding='utf-8')
text_readed = text.read().lower()
text_arr = re.split(r'\W+', text_readed)
text_arr = [i for i in text_arr if i != '']
print(text_arr)
# text_arr.pop()