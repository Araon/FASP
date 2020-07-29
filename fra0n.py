# access token : 

#this scrip when run will post 1 photo to the facebook page

import requests
import random
import facebook
import os
from dotenv import load_dotenv
load_dotenv()


def readCounter():
    f = open("counter.txt", "r")
    content = int(f.read())
    f.close()
    return content

def updateCounter():
    content = readCounter()
    content += 1
    f = open("counter.txt", "w+")
    f.write(str(content))
    f.close()

def resetCounter():
    f = open("counter.txt", "w+")
    f.write('0')
    f.close()


def readCaption():
    f = open("captions.txt", "r")
    caption = f.read()
    f.close()
    return caption




def postImage():
    token = #YOUR_FACEBOOK_GRAPH_API_KEY_WITH_CORRECT_PERMISSONS
    fb = facebook.GraphAPI(access_token=token)
    tobePosted = readCounter()
    memeChosen = open("./images/0.jpg", 'rb')
    print('Image selected')
    message = readCaption()
    fb.put_photo(memeChosen,message=message)
    print('Image posted')
    updateCounter()
    
    #fb.put_object(parent_object='me', connection_name='feed',message='test from vscode')




postImage()


