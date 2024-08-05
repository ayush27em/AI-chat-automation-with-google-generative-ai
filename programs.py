import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os

# def extract_message(text):
#     try:
#         # Split the string by ']' to separate the metadata from the message
#         message_part = text.split('] ')[1]
#         # Split by ': ' to remove the sender's name
#         message = message_part.split(': ', 1)[1]
#         return message
#     except IndexError:
#         return "Invalid message format"
def extract_sender_and_message(text):
    try:
        # Split the string by ']' to separate the metadata from the message
        parts = text.split('] ', 1)
        if len(parts) < 2:
            return "Invalid format", ""
        
        message_part = parts[1]
        
        # Split by ': ' to separate the sender's name from the message
        subparts = message_part.split(': ', 1)
        if len(subparts) < 2:
            return "Invalid format", ""
        
        sender_name = subparts[0].strip()
        message = subparts[1].strip()
        
        return  message
    except Exception as e:
        return f"Error: {e}", ""

def is_last_message_from_kishan(messages):
    # Split the text into individual messages 
    print(messages)
    message_list = messages.strip().split('\n')
    
    # Get the last message
    last_message = message_list[-1]
    
    print(last_message)
    # Extract the sender's name from the last message
    sender_name = last_message.split('] ')[1].split(':')[0].strip()
    # Check if the sender is Kishan Payadi
    return sender_name in ["Minti D N", "Babul", "Aashtosh bhai","ANiKeT RaNa🤫","Shreya Ene (Yuvaan)","Aman CE 1"]

# Allow some time to switch to the correct window
time.sleep(3)

# Click on the icon at (1281, 1052)
pyautogui.click(1281, 1052)
while True :
    # Allow some time for the click action to complete
    time.sleep(2)

    # Click and drag to select the text from (523, 250) to (1026, 915)
    pyautogui.moveTo(523, 250)
    pyautogui.mouseDown()
    pyautogui.moveTo(1026, 915, duration=1)  # Adjust the duration as needed
    pyautogui.mouseUp()

    # Allow some time for the text selection
    time.sleep(1)

    # Press Ctrl+C to copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(747,977)
    # Allow some time for the copy action to complete
    time.sleep(1)

    # Retrieve the text from the clipboard
    chat_history= pyperclip.paste()
  
    # Print the copied text (optional)
    print("Copied text:", chat_history) 
    if is_last_message_from_kishan(chat_history):

        genai.configure(api_key="AIzaSyA50zwYQjX_b1xQBy6O3yW1I75ITd4JedY") 
        model=genai.GenerativeModel('gemini-1.5-pro-latest') 
        response=model.generate_content(f"""you are a person named ayush who speaks hindi
        as well as english .you are from india and a student at college .you analyse 
        the chat history and respond like ayush .output should be like next chat response {chat_history} """) 
        reply_to = response.text 
        mainReply=extract_sender_and_message(reply_to) 
        pyperclip.copy(mainReply)  

        pyautogui.click(683,973) 
        time.sleep(2)

        #paste the text
        pyautogui.hotkey('ctrl' , 'v')
        time.sleep(1) 
        # press enter
        pyautogui.press('enter')

