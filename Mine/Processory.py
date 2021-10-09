# PURE DATA CLEANING
#
import os
import glob
import pandas as pd
import numpy
import pandas

# ==========================================================================================================================|
pandas.set_option('expand_frame_repr', False)
filepath = "https://raw.githubusercontent.com/LINOSNCHENA/Python-Economics-Charts/master/dataIn/sample1.csv"
df = pandas.read_csv(filepath)
df.to_csv('../dataIn/sample4.csv', index=False, quoting=1)

# PROJECT DIRECTORY - B
df.to_csv('../dataIn/sample1.csv', index=False, quoting=1)
df.to_csv('../dataIn/sample2.csv', index=False, quoting=1)
df.to_csv('../dataIn/sample3.csv', index=False, quoting=1)
df.to_csv('../dataIn/sample4.csv', index=False, quoting=1)

# 1. Print. Export to new CSV
print("==================================|DATASET|=====================1=====================")
print('---Here are all 7 lines---')
print(df)
print('---Here are the first 5 lines---')
print(df.head())
fivelinedf = df.head()
fivelinedf.to_csv('../dataIn/out_fiveline.csv', index=False, quoting=1)

# 2. Filter out rows whose last names don’t start with a capital C or capital S
print("==================================|DATASET|=====================2=====================")
print('---What is in "Last" for each row?---')
print(df['Last'])
print('---For each row, does "Last" start with capital "C" or "S"?---')
print(df['Last'].str.startswith('C') | df['Last'].str.startswith('S'))
print('---Show all columns, but only rows where "Last" starts with capital "C" or "S"---')
lastCSdf = df[df['Last'].str.startswith('C') | df['Last'].str.startswith('S')]
print(lastCSdf)
lastCSdf.to_csv('../dataIn/out_lastcs.csv', index=False, quoting=1)

# 3. Complex Cell Updates and Adding, Removing, and Renaming Columns

theseRowsLastNamesStartWithCapitalS = df['Last'].str.startswith('S')
theseRowsHaveA4InTheirId = df['Id'].astype(str).str.contains('4')
print('---Let\'s see what kind of output "df.loc[]" generates---')
print(df.loc[theseRowsLastNamesStartWithCapitalS, 'Last'])
df.loc[theseRowsLastNamesStartWithCapitalS, 'Last'] = 'aaa'
df.loc[theseRowsHaveA4InTheirId, 'Email'] = 'bbb'
df.loc[theseRowsLastNamesStartWithCapitalS, 'New1'] = 'ccc'
df.loc[theseRowsHaveA4InTheirId, 'New2'] = 'ddd'
df['New3'] = 'eee'
df = df.drop(['Id', 'Company'], axis=1)
df = df.rename(columns={'First': 'First Name',
               'Last': 'Last Name', 'Email': 'Email Address'})
print('---We have modified the Python variable "df" to have 3 new rows, plus changes in the "Last" and "Email" columns on specific rows only, and we dropped the "Id" and "Company" rows, and finally, we renamed the "First," "Last," and "Email" columns.---')
print(df)
df.to_csv('../dataIn/out_complexupdates.csv', index=False, quoting=1)

# 4. Merging 2 CSV files w/ a multi-column match
print("==================================|DATASET|======================3====================")
df1 = pandas.read_csv('../dataIn/sample1.csv', dtype=object)
df2 = pandas.read_csv('../dataIn/sample2.csv', dtype=object)
mergedf = df1.merge(df2.rename(columns={'LastName': 'Last', 'FirstName': 'First', 'Em': 'Email'}), how='outer', on=[
                    'Last', 'First'], suffixes=('_csv1', '_csv2'))
print('---Contents of DataFrame "mergedf":---')
print(mergedf)
mergedf.to_csv('../dataIn/out_outermerge.csv', index=False, quoting=1)

# 5. Filter rows based on aggregations

pandas.set_option('expand_frame_repr', False)
print(df)
df = pandas.read_csv('../dataIn/sample3.csv',
                     dtype=object, parse_dates=['Email'])
groupingByAddress = df.groupby('Email')
groupedDataFrame = groupingByAddress.apply(
    lambda x: x[x['Email'] == x['Email'].min()])
outputdf = groupedDataFrame.reset_index(drop=True)
print(outputdf)
outputdf.to_csv('../dataIn/out_oldest_person_per_address.csv',
                index=False, quoting=1)

# 6. Add new data based on aggregation
print("==================================|DATASET|======================4====================")
pandas.set_option('expand_frame_repr', False)
df = pandas.read_csv('../dataIn/sample3.csv')
pandas.set_option('expand_frame_repr', False)
df = pandas.read_csv('../dataIn/sample3.csv',
                     dtype=object, parse_dates=['Email'])
groupingByAddress = df.groupby('Email')
rowIsOldestPersonAtAddress = df['Email'] == groupingByAddress['Email'].transform(
    'min')
df['IsOldestAtAddr'] = False
df.loc[rowIsOldestPersonAtAddress, 'IsOldestAtAddr'] = True
print(df)
df.to_csv('../dataIn/out_noted_if_is_oldest_per_address.csv',
          index=False, quoting=1)
# ================================================================================================
# 7. Pivot a course-registration log to a “people and what they registered for” summary

pandas.set_option('expand_frame_repr', False)
df = pandas.read_csv('../dataIn/sample4.csv')
print(df)
df['Company'] = 'Program' + df['Company']
non_program_columns = list(filter(lambda x: x != 'Company', df.keys()))
pivotdf = pandas.pivot_table(
    df, index=non_program_columns, columns='Company', aggfunc=numpy.size)
pivotdf[pandas.notnull(pivotdf)] = 'Registered'
pivotdf.reset_index(inplace=True)
print(pivotdf)
pivotdf.to_csv('../dataIn/out_pivoted_program_registrations.csv',
               index=False, quoting=1)

# 8. Concatenate unique first+last names from every CSV in a folder, if the file has them
# ==============================================================================================
#from scipy.optimize._root import root
print("==================================|DATASET|======================5====================")
pandas.set_option('expand_frame_repr', False)
inputfolder = '../data2'
listOfDFsToConcatenate = []
os.chdir(inputfolder)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
pd = pd.concat([pd.read_csv(f) for f in all_filenames])
print(pd)
# Exit export to csv
print("==================================|DATASET|==========================================")
combined_csv.to_csv("groupedAsPemba.csv", index=False, encoding='utf-8-sig')
for file in [f for f in os.listdir(inputfolder) if f.endswith('.csv')]:
    df = df.rename(columns={'First Name': 'First',
                   'FirstName': 'First', 'Last Name': 'Last', 'LastName': 'Last'})
if 'First' in df.columns and 'Last' in df.columns:
    df = df[['First', 'Last']]
    df['SourceFilePx'] = file  # Filtering duplicates
    listOfDFsToConcatenate.append(df)
concatdf = pandas.concat(listOfDFsToConcatenate, ignore_index=True)
concatdf = concatdf.drop_duplicates(subset=['First', 'Last'])
print(concatdf)
concatdf.to_csv('../dataIn/out_concatenated_unique_names.csv',
                index=False, quoting=1)

print("==============================|Precessory_Page_145|====================================")
