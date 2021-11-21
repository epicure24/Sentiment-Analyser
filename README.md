# Sentiment Analyser Application

A Flask Application that performs the sentiment prediction of the given review

## Files and Folder Information

* `app.py` is the main application file
    
* `sentiment_analyzer.py` is the python script that runs the sentiment analysis model.
    
* `sentiment-analyzer-training-notebook.ipynb` is the training notebook
    
* `model` folder contains the trained model and tokenizer
      
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
       
 * Run the flask application using Gunicorn server

       gunicorn -b 0.0.0.0:5000 app:app --access-logfile access.log --error-logfile error.log --max-requests 10 --timeout 120 --daemon
       
