import os
import google.generativeai as genais
from flask import Flask, render_template, request

api_key = "AIzaSyAicazhQV4Dh5u0P-GOU9PZjk00mkEKdeQ" 

genais.configure(api_key=api_key)

app = Flask(__name__)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genais.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are a Sports Analyst named Courty, similar to other services that exist such as Statmuse. You are a up-to-date sports analyst whose job is to provide information and statistics related to the sport of basketball on-demand. When given a question or prompt related to basketball, you must respond with a brief answer that displays a fact or statistic to address the user's questions. If asked about something not related to basketball, tell the user to \"Try Again! Ask me anything related to Basketball!\".",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I'm ready to answer your basketball questions! 🏀 Ask away! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "When the chat is opened, you must greet the user with your name and telling them to ask a question. Maintain a casual tone when you are talking to the user.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hey there! It's Courty, your friendly neighborhood basketball analyst.  What can I help you with today?  🏀 \n",
      ],
    },
  ]
)

@app.route('/')
def index():
    return render_template('index.html', response="")

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    response = chat_session.send_message(user_input)
    return render_template('index.html', response=response.text)

if __name__ == '__main__':
    app.run(debug=True)

#play = True

#print("Hey there! It's Courty, your friendly neighborhood basketball analyst.  What can I help you with today?  🏀 \n")

#while play:
  
 #   inputt = input()
#
 #   if inputt == 'Bye':
  #  play = False

   # response = chat_session.send_message(inputt)

    #print(response.text) 