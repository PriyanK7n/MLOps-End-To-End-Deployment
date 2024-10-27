from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__) # entry point

app = application

## Routes to the home page
@app.route('/')
def index():
    return render_template('index.html') # searches for templates folder inside current directory and looks for index.html file inside it 


@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html') # searches for templates folder inside current directory and looks for home.html file inside it 
    
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )

        pred_df=data.get_data_as_data_frame() # returns user's input data as a pandas dataframe using CustomData class methods
        print(pred_df)

        print("Before Prediction")
        # Running inference/prediction on the user's input (pandas dataframe) 
        predict_pipeline=PredictPipeline()
        
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df) # list
        
        print("Post Prediction")
        return render_template('home.html',results=results[0]) # display the prediction results
    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)        
