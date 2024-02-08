import pandas as pd
import numpy as np
import datetime
import os

def gender_by_national_id(df):
  filtered_df = df[
      (df['National ID'].astype(str).str.len() == 14) &
      df['National ID'].notna() &
      (df['National ID'] != '')
      ]

  filtered_df['Gender'] = np.where(
      filtered_df['National ID'].astype(str).str[-1].astype(int) % 2 == 0,
      'Female',
      'Male'
      )

  df.update(filtered_df['Gender'])

  return df

def main():
   # folder path to get file
   folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Data Cleaning\2024\Feb\7'

   # file name
   file_name = 'Donor Without Gender.xlsx'
   
   # combine folder path and file name
   file_path = os.path.join(folder_path, file_name)

   # read file
   df = pd.read_excel(file_path)

   # run function
   df = gender_by_national_id(df)
   
   # rename file with new name
   current_filename = file_name[:-5]
   new_file_name = f'{current_filename} - Edited.xlsx'
   
   # build output file path
   new_file_path = os.path.join(folder_path, new_file_name)
   df.to_excel(new_file_path, index = False)
   
   # successfull attempt prompt
   print(f'File {new_file_name} been saved in the folder')

if __name__ == "__main__":
    main()