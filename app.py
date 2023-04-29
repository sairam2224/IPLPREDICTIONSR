from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
import csv

# Open the CSV file
with open('artifacts/train.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    # Extract unique player names
    player_names = set(row['Player_Name'] for row in reader)
    
    # Generate HTML for the select dropdown
    select_options = '\n'.join('<option value="{name}">{name}</option>'.format(name=name) for name in player_names)

# Insert the select dropdown into the HTML form
select_dropdown = '''
<div class="mb-3">
    <label class="form-label">Player Name</label>
    <select class="form-control" name="Player_Name" placeholder="Select Your Player" required>
        <option class="placeholder" selected disabled value="">Select a player</option>
        {options}
    </select>
</div>
'''.format(options=select_options)

application=Flask(__name__)

app=application
@app.route('/')
def index():
    return render_template('ind.html')

@app.route('/iplpredict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Player_Name=request.form.get('Player_Name'),
            Role_Desc=request.form.get('Role_Desc'),
            Player_team=request.form.get('Player_team'),
            Opposit_Team=request.form.get('Opposit_Team'),
            is_manofThematch=request.form.get('is_manofThematch'),
            City_Name=request.form.get('City_Name'),
            

        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)