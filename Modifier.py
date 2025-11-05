import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import charset_normalizer

csv_file_directory = 'test_edited_2.csv'

#checking the encoding of the data
with open(csv_file_directory, 'rb') as rawdata:
    result = charset_normalizer.detect(rawdata.read(100000))
    print(result)

#converting the file to df and cleaning of the data
df = pd.read_csv(csv_file_directory, encoding='utf-8', header=0)
t_df = df.copy()
print(t_df.head(20), df.shape)
col_headings = df.columns
print(col_headings)




# # Removing gaps in Zip type
# t_df.drop(columns='Unnamed: 7', axis=1, inplace=True)
# adj_error_indexes = []
# error_indexes = t_df[t_df['Date FDID'].isna()].index.tolist()
# print(type(error_indexes))
# for x in error_indexes:
#     adj_error_indexes.append(x - 1)
# print(adj_error_indexes)
# print(error_indexes, '\n', len(error_indexes))
# error_values = t_df.loc[error_indexes, 'Zip Type']
# t_df.drop(error_values.index, axis =0 ,inplace=True)
# t_df.reset_index(drop=True, inplace=True)
# error_values.index -= 1
# t_df['waste'] = error_values
# combined = pd.concat([t_df['Zip Type'],t_df['waste']], ignore_index=True)
# t_df['Zip Type'] = combined
# t_df.drop(columns='waste', axis=1, inplace=True)


#stage 1 completion
#t_df.to_csv('stage1.csv', index=False, encoding='utf-8')




#terms count tool
#terms_count = t_df['Date FDID'].value_counts()
#print(terms_count)
# Removing repeating headers

error_indexes_2 = t_df[t_df['Date FDID'] == 'Date FDID'].index.tolist()
print(error_indexes_2)
t_df.drop(error_indexes_2, axis =0 ,inplace=True)
t_df.reset_index(drop=True, inplace=True)

#Stage 2 check
#t_df.to_csv('stage2.csv', index=False, encoding='utf-8')


#Stage 3: Separating cols
t_df[['Zip', 'Type']] = t_df['Zip Type'].str.split('-', n=1, expand=True)
t_df.drop(columns='Zip Type', axis=1, inplace=True)
t_df[['Date', 'FDID']] = t_df['Date FDID'].str.split(' ', n=1, expand=True)
t_df.drop(columns='Date FDID', axis=1, inplace=True)
order = ['Date', 'FDID','Incident#','Alarm', '###','Address','Suite','Zip','Type','Lgth']
t_df = t_df[order]
t_df.to_csv('stage3.csv', index=False, encoding='utf-8')




