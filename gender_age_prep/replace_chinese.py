import pandas as pd

chin_eng = pd.read_csv('./data/brandMap.txt', sep=' ', encoding='utf-8')

def replace_pinyin(text):
  for row in chin_eng.iterrows():
    text = text.replace(row[0], row[1][0])

  return text