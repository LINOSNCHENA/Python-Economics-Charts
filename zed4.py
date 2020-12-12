import os
import glob
import pandas as pd

inputfolder = 'C:\\yay\\folder\\'
os.chdir(inputfolder)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
pd = pd.concat([pd.read_csv(f) for f in all_filenames ])
print(pd)
#export to csv
combined_csv.to_csv( "combinedPemba.csv", index=False, encoding='utf-8-sig')