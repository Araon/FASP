import os

def removeImage():
    imgExist = os.path.isfile('./images/0.jpg' or './images/0.jpeg' or './images/0.png')
    if imgExist is True:
        os.remove('./images/0.jpg' or './images/0.jpeg' or './images/0.png')
    else:
        print('Image is not there')

removeImage()