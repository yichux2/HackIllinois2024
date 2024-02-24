from openai import OpenAI
import json

client = OpenAI(api_key="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")

question = "Calculate $$\sum_{n=1}^{100} n$$"

prompt = f"""I encounter the following question in math class: {question}. 
And I hope you can generate 5 more similar questions, 
questions are separated by a sepatate line. 
After each question, generate the answer and brief explanation. Explanation should be less than 100 words and in a paragraph!
Please return in following format. Thank you very much!
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

# response.choices[0]

response_str = response.choices[0].message.content
print(response_str)

response_list = response_str.split('-------')

print(response_list)
context = []

for item in response_list:
    detail = item.split('\n')
    context.append({
        "Question": detail[0],
        "Answer": detail[1],
        "Explanation": detail[2]
    })

print(context)