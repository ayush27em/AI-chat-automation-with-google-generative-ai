# AI-chat-automation-with-google-generative-ai


This project involves automating responses in a chat application using Python. It utilizes PyAutoGUI for automating GUI interactions, pyperclip for clipboard operations, and Google Generative AI for generating responses based on the chat history.

## Features

- **GUI Automation**: Uses PyAutoGUI to interact with the chat application.
- **Clipboard Management**: Uses pyperclip to copy and paste text.
- **AI Response Generation**: Utilizes Google Generative AI to analyze chat history and generate appropriate responses.
- **Customizable Responses**: Configured to respond as a specific persona.

## Requirements

- Python 3.x
- PyAutoGUI
- pyperclip
- google-generativeai

## Setup

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required packages:

    ```bash
    pip install pyautogui pyperclip google-generativeai
    ```

3. Obtain an API key from [Google Generative AI](https://console.cloud.google.com/).

4. Replace the placeholder API key in the code with your actual key:

    ```python
    genai.configure(api_key="your_google_genai_api_key")
    ```

## Usage

1. Open your chat application and ensure the chat window is in focus.
2. Run the script:

    ```bash
    python chat_automation.py
    ```

3. The script will:
   - Click on the specified coordinates to activate the chat window.
   - Copy the chat history to the clipboard.
   - Analyze the chat history to determine if the last message is from a specific sender.
   - Generate a response using Google Generative AI.
   - Paste the response into the chat and send it.

## Code Explanation

- **extract_sender_and_message(text)**: Extracts the sender's name and message from a given text.
- **is_last_message_from_kishan(messages)**: Checks if the last message in the chat history is from a specified sender.
- **GUI Automation**: Uses PyAutoGUI to click, drag, and interact with the chat application.
- **Clipboard Operations**: Uses pyperclip to copy and paste text.
- **AI Response Generation**: Configures and uses Google Generative AI to generate chat responses based on the chat history.

## Future Enhancements

- Add more sophisticated message parsing and error handling.
- Extend support for multiple personas and languages.
- Improve the robustness and efficiency of the GUI interactions.

## Contributing

Feel free to fork this project, make improvements, and submit pull requests. Your contributions are highly appreciated!

