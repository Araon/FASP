
# this script will download 1 image from the subreddit and save it in the images folder
# and save the caption to the caption.txt file

import urllib.request
import praw
from dotenv import load_dotenv
import os
load_dotenv()


def getPost():
    count = 0
    reddit = praw.Reddit(client_id='client_id',client_secret='client_secret',user_agent='client_name:client_id')

    # Iterate through top submissions
    for submissions in reddit.subreddit("gamingmemes+gaming+pcmasterrace").new(limit=10):

        # Get the link of the submission
        url = str(submissions.url)

        # Check if the link is an image
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):

            # Retrieve the image and save it in current folder
            urllib.request.urlretrieve(url, "./images/"f"{count}.jpg")
            print('Downloaded ' f'{count}' ' image')
            title = str(submissions.title)
            f = open("captions.txt", "w+", encoding="utf8")
            f.write(title)
            f.close()
            count += 1

            # Stop once you have 10 images
            if count == 1:
                break

getPost()