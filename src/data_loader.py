import pandas as pd


class AnimeDataLoader:

    #giving path of original csv file and processed csv file
    def __init__(self,original_csv:str,processed_csv:str):
        #making instance variable original_csv
        self.original_csv = original_csv      
        self.processed_csv = processed_csv

    def load_and_process(self):
        #creating a dataframe from the csv file
        #dropna is used to remove rows with any NaN values
        df = pd.read_csv(self.original_csv , encoding='utf-8' , on_bad_lines='skip').dropna()

        #only need this columns
        required_cols = {'Name' , 'Genres','sypnopsis'}
         
        #checking if all required columns are present in the dataframe
        #if not, raise ValueError with a message
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError("Missing column  in CSV File")
        
        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " +df["sypnopsis"] + "Genres : " + df["Genres"]
        )
        
        #combining the required columns into a new column 'combined_info'
        #and saving the processed dataframe to a new csv file
        df[['combined_info']].to_csv(self.processed_csv , index=False,encoding='utf-8')

        return self.processed_csv
