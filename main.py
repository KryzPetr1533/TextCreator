import re
text = open("data.txt", 'r', encoding='utf-8')
text_readed = text.read()
text_arr = re.split(r'\W+', text_readed)
text_arr.remove('')
# text_arr.pop()
print(text_arr)