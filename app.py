from flask import Flask, request, jsonify, render_template
import re
import random

app = Flask(__name__)

# Define a dictionary of responses
responses = {
    'hello': 'Hello! How can I assist you today?',
    'hi': 'Hi there! What can I do for you?',
    'how are you': 'I am just a bot, but I am doing great! How can I help you?',
    'bye': 'Goodbye! Have a great day!',
    'tell me a story': 'Sure! I have stories about a brave knight, a clever fox, a magical unicorn, a kind-hearted girl, Mr. baker, a wise old man, an enchanted forest, a camel named Sahara, a clever rabbit, a generous dragon, a young elephant, the whispers of nature, the golden touch, an ugly cactus and a little mouse.',
    'default': 'I am not sure how to respond to that. Can you please rephrase?'
}

# Function to read the stories from a text file
def load_stories(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            content = file.read()
        stories = content.split('###')
        return [story.strip() for story in stories if story.strip()]
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []

# Load stories from the dataset
stories = load_stories('stories.txt')

# Function to find a response based on the user input
def find_response(user_input):
    user_input = user_input.lower()
    
    for key in responses:
        if re.search(r'\b' + key + r'\b', user_input):
            if key == 'tell me a story':
                return responses[key]
            return responses[key]

    stories_with_keyword = []
    for key in ['brave knight', 'clever fox', 'magical unicorn', 'kind-hearted girl', 'Mr. baker', 'wise old man', 'enchanted forest', 'camel named Sahara', 'clever rabbit', 'generous dragon', 'young elephant', 'whispers of nature', 'golden touch', 'ugly cactus', 'little mouse']:
        if re.search(r'\b' + key + r'\b', user_input):
            stories_with_keyword = [story for story in stories if key in story.lower()]
            break

    if stories_with_keyword:
        return random.choice(stories_with_keyword)
    else:
        return responses['default']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()
    response = find_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
