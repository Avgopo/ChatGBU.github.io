from flask import Flask,redirect, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/chatbot", methods=["GET","POST"])
def get_chat():
    user_input = request.json
    input_text = user_input["user_input_value"]
    
    # Create chat messages
    chat_messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': input_text}]
    
    # Get response from OpenAI chat model
    chat_response = get_openai_response(chat_messages)
    
    # Get essay score using the essay scoring API
    essay_score = get_essay_score(input_text)
    
    # Combine chat response and essay score
    combined_response = f"Chat Response: {chat_response}\nEssay Score: {essay_score}"
    
    response = jsonify({'combined_response': combined_response})
    return response

def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response["choices"][0]["message"]['content']

def get_essay_score(essay_text):
    # Make a request to your essay scoring API
    # Make sure to replace 'your_essay_scoring_api_key' and 'your_essay_scoring_endpoint' with actual values
    essay_scoring_url = f"{essay_scoring_endpoint}?apiKey={essay_scoring_api_key}&essay={essay_text}"
    
    # Use appropriate HTTP library to make the request (e.g., requests library)
    # response = requests.get(essay_scoring_url)
    
    # For the sake of example, let's assume the API returns a JSON with a 'score' field
    # Replace this with actual parsing of the response from your essay scoring API
    # essay_score = response.json().get('score', 'N/A')
    
    # For demonstration purposes, using a placeholder value
    essay_score = 85.0
    
    return essay_score

if __name__ == "__main__":
    app.run(debug=True)