from flask import Flask, request, jsonify
from openai import OpenAI
import requests
import json

app = Flask(__name__)


@app.route("/get_SimpleTex/<gloop>")
def get_request(gloop):
    #copying from simpletex
    api_url="https://server.simpletex.cn/api/latex_ocr/" # interface address
    data = {} # request data
    header={"token":"yxz25lSItTKzj596L2tIVSjziF6k5HVy9Zs3LSNHeiaK4WtXWJ6D301hzPc7XPBJ"} # Authentication information, use UAT method here
    # gloop = request.args.get("file") 
    file=[("file",("./SimpleTex_scripts/images/" + gloop ,open("./SimpleTex_scripts/images/" + gloop, 'rb')))] # request file, field name is usually file
    res = requests.post(api_url, files=file, data=data, headers=header) # Use the requests library to upload files
    print(res.status_code)
    print(res.text)
    return jsonify(res.text)
    
    

# Define your processing function
def process_text(question):
    # Your processing logic here
    client = OpenAI(api_key="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")

    # question = "Calculate $$\sum_{n=1}^{100} n$$"
    prompt = f"""I encounter the following question in math class: {question}. 
    And I hope you can generate 5 more similar questions, 
    questions are separated by a sepatate line. 
    After each question, generate the answer and brief explanation. Explanation should be less than 100 words and in a paragraph!
    Please return in following format, no empty lines. Thank you very much!
    Question: 
    Answer:
    Explanation:
    -------
    Question: 
    Answer:
    Explanation:
    """

    response = client.chat.completions.create(
        model="gpt-4-0125-preview", 
        messages=[{
            "role": "user", 
            "content": prompt
        }]
        
    ) 

    response_str = response.choices[0].message.content
    print(response_str)

    response_list = response_str.split('-------\n')

    print(response_list)
    context = []

    for item in response_list:
        detail = item.split('\n')
        context.append({
            "Question": json.dumps(detail[0]),
            "Answer": json.dumps(detail[1]),
            "Explanation": json.dumps(detail[2])
        })

    return context


def process_text_test(question):
    return [{"happy": "yes"}]

# Define API endpoint HERE
@app.route('/process', methods=['POST'])
def process():
    data = request.json  # Get the JSON data from the request
    text = data.get('text')  # Extract the text from the JSON data

    if text is None:
        return jsonify({'error': 'No text provided'}), 400  # Return an error if no text is provided

    result = process_text(text)  # Process the text
    # result = process_text_test(text)  # Process the text

    return jsonify(result)  # Return the processed result as JSON

if __name__ == '__main__':
    app.run(debug=True)