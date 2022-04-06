from django.shortcuts import render
from dotenv import load_dotenv
import pyrebase


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



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
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
auth = firebase.auth()
database = firestore.client()
# database = firebase.database()

#this is views

def home(request):
    currUser = database.collection('users').document('WXiNFxxa2vfqrysEWuQ7').get().to_dict() # I'm hardcoded here just to get an idea what we can do
    auction_username = currUser['username'] 
    auction_about = currUser['about']
    # return HttpResponse("Hello, Django! and auction man")
    return render (request, 'index.html', {
        "auction_username" : auction_username,
        "auction_about" : auction_about
    })

def signIn(request):
    return render(request, 'signin.html')

def signUp(request):
    return render(request, 'signup.html')






def postsign(request):
    email =  request.POST.get('email')
    password = request.POST.get('password')

    auth.sign_in_with_email_and_password(email, password)
    # After ^this function runs, we want to take the unique id of that user and search in our firestore database for that user
    # and take their name and pass it to our page

    return render (request, 'welcome.html', {
        "email" : email
    })

def postsignup(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confPass = request.POST.get('confPassword')

    if (password == confPass):
        userData = auth.create_user_with_email_and_password(email, password)
        userId = userData.get('localId')

        data = {
            "username": username,
            "email": email,
            "userId": userId
        }

        print(userData)
        database.collection('users').document(username).set(data)

        return render (request, 'welcome.html', {
            "username" : username
        })