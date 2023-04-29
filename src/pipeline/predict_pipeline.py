import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
        Player_Name:str,
        Role_Desc:str,
        Player_team:str,
        Opposit_Team:str,
        is_manofThematch:int,
        City_Name:str):

        self.Player_Name = Player_Name

        self.Role_Desc = Role_Desc

        self.Player_team = Player_team

        self.Opposit_Team = Opposit_Team

        self.is_manofThematch = is_manofThematch

        self.City_Name = City_Name


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
               "Player_Name": [self.Player_Name],
                "Role_Desc": [self.Role_Desc],
                "Player_team": [self.Player_team],
                "Opposit_Team": [self.Opposit_Team],
                "is_manofThematch": [self.is_manofThematch],
                "City_Name": [self.City_Name],
    
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e,sys)
        
         

        
