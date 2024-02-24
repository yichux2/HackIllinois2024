import requests

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/get_SimpleTex/<gloop>")
def get_request(gloop):
    #copying from simpletex
    api_url="https://server.simpletex.cn/api/latex_ocr/" # interface address
    data = {} # request data
    header={"token":"yxz25lSItTKzj596L2tIVSjziF6k5HVy9Zs3LSNHeiaK4WtXWJ6D301hzPc7XPBJ"} # Authentication information, use UAT method here
    # gloop = request.args.get("file") 
    file=[("file",("./SimpleTex_scripts/" + gloop ,open("./SimpleTex_scripts/" + gloop, 'rb')))] # request file, field name is usually file
    res = requests.post(api_url, files=file, data=data, headers=header) # Use the requests library to upload files
    print(res.status_code)
    print(res.text)
    return jsonify(res.text)
    
    