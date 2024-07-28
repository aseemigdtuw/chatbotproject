# chatbotproject
Rule-based chatbot based on pre-defined responses and dataset
This project presents "StoryWeaver," a storytelling chatbot designed to engage users in interactive narrative experiences. The chatbot interface is developed using HTML, CSS, and JavaScript, and it integrates with a Flask backend to process user inputs and generate responses.
1. Methodologies:
The frontend development of the chat application involves creating a user interface using HTML and CSS. This interface includes a chat container, a message display area, and an input field, all designed to ensure a user-friendly experience. The styling differentiates messages from the user and the bot, making the interaction clear and visually appealing. JavaScript is employed to handle dynamic elements, such as appending new messages to the chat, managing user input, and communicating with the server through the fetch API. On the backend, the Flask framework is used to process user inputs sent via HTTP POST requests. Flask handles the logic and responses necessary for the chat application to function, enabling a smooth and interactive user experience.
2. Preprocessing:
The preprocessing in the storytelling chatbot involves normalizing user input to lowercase for consistency and using regular expressions to match specific keywords. This allows the chatbot to trigger appropriate predefined responses from a dictionary. When a user requests a story, the bot lists available story keywords and waits for the user to specify a choice. It then searches for and selects a matching story from a text file, ensuring relevant and engaging responses. This preprocessing ensures efficient handling of various user inputs and smooth operation of the chatbot.
3. Tools and Technologies Used:
Python is the preferred programming language for this chat application due to its extensive libraries and powerful NLP and AI frameworks. Regular expressions, implemented through the re module, play a crucial role in identifying patterns in text, enabling the application to match user input against predefined keywords or phrases. This is achieved using the re.search function to detect keywords such as "hello," "bye," or "tell me a story." A dictionary is employed to store predefined responses, mapping specific keywords or phrases to corresponding responses, simplifying the retrieval process based on user input. For handling longer content, file handling techniques are used; the load_stories function reads stories from a file named stories.txt, splitting and storing them in a list for easy access. To add an element of randomness, the random module's random.choice function selects a random story from the list when needed. Ensuring consistency in user input, the lower() method is used for string normalization, converting all input to lowercase before processing. Keyword matching is further enhanced using re.search in conjunction with the keywords defined in the responses dictionary. For managing multi-turn interactions, context handling is implemented, allowing the bot to ask follow-up questions and respond appropriately based on the user's previous inputs, such as when requesting a specific story.
4. Results :
   The StoryWeaver chatbot successfully engages users in interactive storytelling. The interface is responsive and intuitive, with clear differentiation between user and bot messages. The chatbot responds promptly to user inputs, providing a smooth and engaging narrative experience. The integration between the frontend and backend components is robust, ensuring reliable communication and response generation.






