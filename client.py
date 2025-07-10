import google.generativeai as genai

# ✅ Configure Gemini API
genai.configure("api_key")

# ✅ Create Gemini model client
model = genai.GenerativeModel('gemini-1.5-flash')

# ✅ Prompt (combining system and user)
prompt = (
    "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud.\n"
    "User: what is coding"
)

# ✅ Generate response
response = model.generate_content(prompt)

# ✅ Print result
print(response.text.strip())
