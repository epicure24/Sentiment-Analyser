# Sentiment Analyser Application

A Flask Application that performs the sentiment prediction of the given review.

The application can be used via `API` as well as `Web Application`

## Files and Folder Information

* `app.py` is the main application file
    
* `sentiment_analyzer.py` is the python script that runs the sentiment analysis model.
    
* `sentiment-analyzer-training-notebook.ipynb` is the training notebook
    
* `model` folder contains the trained model and tokenizer

      Model's Accuracy = 88.807 %

      Model's Loss = 0.274
      
* `templates` folder contains the html files

## How to set up the application ?

* Create virtual environment

      python3 -m venv env
      
 * Activate the virtual environment
 
       source env/bin/activate
       
 * Install the required libraries 

       pip install -r requirements.txt
       

 ## How to run the application on localhost ?
       
 * Run the flask application on localhost

       python app.py
       
       # Go to http://localhost:5000/  and perform analysis

## How to run the application on localhost ?

* Install the Web Server Gateway Interface (WSGI) Gunicorn
       
       pip install gunicorn
       
 * Create `access.log` and `error.log` file
 
 * Run the flask application using Gunicorn server

       gunicorn -b 0.0.0.0:5000 app:app --access-logfile access.log --error-logfile error.log --max-requests 10 --timeout 120 --daemon
       
*****************************************

# RUN IT AS AN API SERVICE

* Open API Running tool like `Postman`.

* Run the following API

      URL = localhost:5000/api/detect 
      
      Method = POST
      
      Body ( form-data )
      
           review = "<review text>"
      
* See the below screenshot

![Input Screen](https://github.com/epicure24/Sentiment-Analyser/blob/main/images/postman.png)

**************************************

# RUN IT AS A WEB APPLICATION
       
## Application Screenshots

INPUT SCREEN

![Input Screen](https://github.com/epicure24/Sentiment-Analyser/blob/main/images/input_screen.png)

RESULT SCREENS

![Positive Screen](https://github.com/epicure24/Sentiment-Analyser/blob/main/images/positive.png)

![Negative Screen](https://github.com/epicure24/Sentiment-Analyser/blob/main/images/negative.png)
       
