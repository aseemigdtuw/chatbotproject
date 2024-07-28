# chatbotproject
Rule-based chatbot based on pre-defined responses and dataset
This project presents "StoryWeaver," a storytelling chatbot designed to engage users in interactive narrative experiences. The chatbot interface is developed using HTML, CSS, and JavaScript, and it integrates with a Flask backend to process user inputs and generate responses.
Methodologies:
1. Frontend Development: 
   - The user interface is built using HTML and CSS, featuring a chat container, message display area, and input field. Styling ensures a user-friendly experience, with differentiated message designs for user and bot interactions.
   - JavaScript handles dynamic elements, including message appending, server communication via the fetch API, and input management.
2. Backend Integration:
   - The Flask backend processes user inputs sent via HTTP POST requests. 
Preprocessing:
The preprocessing in the storytelling chatbot involves normalizing user input to lowercase for consistency and using regular expressions to match specific keywords. This allows the chatbot to trigger appropriate predefined responses from a dictionary. When a user requests a story, the bot lists available story keywords and waits for the user to specify a choice. It then searches for and selects a matching story from a text file, ensuring relevant and engaging responses. This preprocessing ensures efficient handling of various user inputs and smooth operation of the chatbot.
Tools and Technologies Used:
Python is the preferred programming language because of its vast libraries and NLP and AI frameworks. 
1. Regular Expressions (re module):
•	Purpose: Regular expressions (regex) are used to identify patterns in text. This is useful for matching user input against predefined keywords or phrases.
•	Usage in Code: The re.search function is used to check if a user's input contains certain keywords (like "hello", "bye", "tell me a story", etc.).
2. Dictionary for Responses:
•	Purpose: A dictionary is used to store predefined responses for specific keywords or phrases.
•	Usage in Code: The responses dictionary maps user inputs (keys) to corresponding responses (values). This makes it easy to retrieve responses based on the user's input.
3. File Handling:
•	Purpose: File handling is used to read stories from a text file.
•	Usage in Code: The load_stories function reads the contents of a file named stories.txt and splits it into individual stories using a delimiter (###). Each story is then stripped of any leading/trailing whitespace and stored in a list.
4. Random Module:
•	Purpose: The random module is used to select a random story from the list of stories when needed.
•	Usage in Code: The random.choice function is used to pick a random story from a list of stories that match the user's request.
5. String Normalization:
•	Purpose: Normalizing user input ensures that the bot can correctly match keywords regardless of the input's case (upper, lower, mixed).
•	Usage in Code: The lower() method is used to convert user input to lowercase before processing it.
6. Keyword Matching:
•	Purpose: Keyword matching is used to identify specific words or phrases in the user input and generate appropriate responses.
•	Usage in Code: The bot checks for keywords in the user's input using re.search and the keywords defined in the responses dictionary.
7. Context Handling:
•	Purpose: Handling context ensures that the bot can manage multi-turn interactions, such as asking the user to specify which story they want to hear.
•	Usage in Code: When the user asks for a story, the bot responds with a list of available stories and waits for the user to specify a keyword for a specific story

Results:
The StoryWeaver chatbot successfully engages users in interactive storytelling. The interface is responsive and intuitive, with clear differentiation between user and bot messages. The chatbot responds promptly to user inputs, providing a smooth and engaging narrative experience. The integration between the frontend and backend components is robust, ensuring reliable communication and response generation.
