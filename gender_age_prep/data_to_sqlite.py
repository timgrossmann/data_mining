from os import listdir
import pandas as pd

from sqlalchemy import create_engine
disk_engine = create_engine('sqlite:///age_gender_data.db')

def create_table (file):
  filepath = './data/' + file
  tablename = file[:-4]
  index_start = 1

  for data_chunk in pd.read_csv(filepath, sep=',', encoding='utf-8',
                                chunksize=20000, iterator=True):
    data_chunk.index += index_start
    data_chunk.to_sql(tablename, disk_engine, if_exists='append')
    index_start = data_chunk.index[-1] + 1

for file in listdir('./data'):
  if file.endswith('.csv'):
    print '-> Adding Table ' + file[:-4]
    create_table(file)
    print file[:-4] + 'Added'