import sys
import pandas as pd

reload(sys)
sys.setdefaultencoding('UTF8')

chin_eng = pd.read_csv('./data/brandMap.txt', sep=' ', encoding='utf-8')

def replace_pinyin(text):
  for row in chin_eng.iterrows():
    text = text.replace(row[0], row[1][0])

  return text

lines = []

with open('./data/' + sys.argv[1], 'r') as file:
  for line in file:
    lines.append(line)

with open('./data/' + sys.argv[1], 'w') as new_file:
  for line in lines:
    new_file.write(replace_pinyin(line.decode('utf-8')))