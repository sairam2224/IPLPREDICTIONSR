from flask import Flask, request, render_template
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Read the CSV file and get the unique values in the Player_name column
data = pd.read_csv('artifacts/train.csv')
player_names = list(data['Player_Name'].unique())

@app.route('/')
def index():
    return render_template('ind.html')

@app.route('/iplpredict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html', player_names=player_names)
    else:
        data = CustomData(
            Player_Name=request.form.get('Player_Name'),
            Role_Desc=request.form.get('Role_Desc'),
            Player_team=request.form.get('Player_team'),
            Opposit_Team=request.form.get('Opposit_Team'),
            is_manofThematch=request.form.get('is_manofThematch'),
            City_Name=request.form.get('City_Name'),
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)

        print("after Prediction")
        return render_template('home.html', results=results[0], player_names=player_names)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug='true')