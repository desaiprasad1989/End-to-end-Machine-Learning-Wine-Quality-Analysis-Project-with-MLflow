from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from winequality.pipeline.prediction import PredictionPipeline  


app = Flask(__name__)   #initializing the flask app

@app.route('/', methods=['GET'])     # route for handling the home page
def homePage():
    return render_template('index.html')

@app.route('/train', methods=['GET'])   # route for training the model pipeline
def training():
    os.system('python main.py')        # running the main.py file to train the model pipeline
    return "Training successful!!"


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)


            if 3 <= predict[0] < 4:
                sensory_score = 'Low Quality Wine'
            elif 4 <= predict[0] < 6:
                sensory_score = 'Medium Quality Wine' 
            else:       
                sensory_score = 'High Quality Wine'

            return render_template('results.html', prediction = str(predict), sensory_score = str(sensory_score))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080, debug=True)
