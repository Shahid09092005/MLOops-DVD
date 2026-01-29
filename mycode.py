import pandas as pd
import os

# create a sample data with multi-columns
data = {
    "Name": ["Shahid Mansuri" , "Harshit Srivastava", "Anushika Chauhan" , "Vibhaw Kumar Verma"],
    "Age" : [21 , 22, 20 , 25],
    "City" : ["Kanpur" , "Etawah" , "Lucknow" , "Bihar"],
    "CGPA" : [8.2 , 9.1 , 8, 9]
}
# convert into dataframe
df = pd.DataFrame(data)


data_dir='data'
os.makedirs(data_dir, exist_ok=True) # It create a folder named 'data' and if exist then dosen't throw error
#os.path.join() safely combines folder and file name   data/sample_data.csv
file_path = os.path.join(data_dir, 'sample_data.csv')
# store the df into data folder with name as 'sample_data'
df.to_csv(file_path, index=False)

#Prints a message confirming
print(f"CSV file saved to {file_path}")


