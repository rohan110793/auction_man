from django.shortcuts import render
from dotenv import load_dotenv
import pyrebase

load_dotenv()
import os

# Create your views here.

from django.http import HttpResponse

# Configuring Firebase

config = {
    "apiKey": os.environ.get("AUCTION_APP_API_KEY"),
    "authDomain": os.environ.get("AUCTION_APP_AUTH_DOMAIN"),
    "databaseURL": os.environ.get("AUCTION_APP_DATABASE_URL"),
    "projectId": os.environ.get("AUCTION_APP_PROJECT_ID"),
    "storageBucket": os.environ.get("AUCTION_APP_STORAGE_BUCKET"),
    "messagingSenderId": os.environ.get("AUCTION_APP_MESSAGING_SENDER_ID"),
    "appId": os.environ.get("AUCTION_APP_APP_ID")
}

firebase = pyrebase.initialize_app(config)
authenticate = firebase.auth()
database = firebase.database()

#this is views

def home(request):
    auction_username = database.child('Data').child('Username').get().val()
    auction_about = database.child('Data').child('About').get().val()
    # return HttpResponse("Hello, Django! and auction man")
    return render (request, 'index.html', {
        "auction_username" : auction_username,
        "auction_about" : auction_about
    })
