import requests

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def get_request():
    #copying from simpletex
    api_url="https://server.simpletex.cn/xxxxx" # interface address
    data = {...} # request data
    header={"token":"yxz25lSItTKzj596L2tIVSjziF6k5HVy9Zs3LSNHeiaK4WtXWJ6D301hzPc7XPBJ"} # Authentication information, use UAT method here
    file=[("file",("test_image.jpeg",open("test_image.jpeg", 'rb')))] # request file, field name is usually file
    res = requests.post(api_url, files=file, data=data, headers=header) # Use the requests library to upload files
    print(res.status_code)
    print(res.text)
    
    