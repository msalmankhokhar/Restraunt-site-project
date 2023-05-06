from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request
import os
import datetime
import json
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from markupsafe import Markup
from flask_ngrok import run_with_ngrok
from time import sleep

app = Flask(__name__)
app.secret_key = 'salman'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

application = app

host = '0.0.0.0'
port = 5000

@app.route('/')
def home():
    return 

if __name__ == "__main__":
    app.run(host, port, debug=True)