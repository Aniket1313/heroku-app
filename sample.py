#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:11:45 2021

@author: aniket
"""

import flask
from flask import request, Flask
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def testAPI():
    return "Okay this is working"

#Write a function to select first sentence from a paragpraph
@app.route('/first_sent',methods=['POST'])
def selectFirstSent():
    dataText = request.data.decode('utf-8')
    textDict = json.loads(dataText)
    text = textDict['text']
    sents = text.split('.')
    return sents[0]

app.run('localhost',5030)


#text = "This is my day.I love my dog.Take this cup."

#print(selectFirstSent(text))

# Data format :JSON
#{"text": "This is my day.I love my dog.Take this cup."}