# from openai import OpenAI

# client = OpenAI(

#     api_key="api_key"
# ) 
# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {"role": "system", "content": "You are virtual assistant named jarvis skilled in general tasks like alexa and google cloud."},
#     {"role": "user", "content": "what is coding."}
#   ]
# )

# print(completion.choices[0].message.content)
import google.generativeai as genai
import os
genai.configure(api_key="AIzaSyA50zwYQjX_b1xQBy6O3yW1I75ITd4JedY") 
model=genai.GenerativeModel('gemini-1.5-pro-latest') 
response=model.generate_content("""you are a person named ayush who speaks hindi
as well as english .you are from india and a student at college .you analyse 
  the chat history and respond like ayush """) 
