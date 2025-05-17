 Hogwarts Summer School 2025 – Smart Telegram Chatbot
This project is a Telegram chatbot built using Python that answers questions based only on official information from the Hogwarts Summer School 2025 document (provided by New Uzbekistan University). It was created for the case study challenge during the Hogwarts Summer School selection process. I would admit that I did it with my best friend from USA

📌 What It Does
✅ Responds to user questions about the Hogwarts camp: dates, eligibility, activities, budget, and more.

✅ All answers are taken directly from the official PDF (nothing is made up).

✅ Works inside Telegram – just send a message like “When is the camp?” and it replies instantly.

✅ No ChatGPT or LLMs – only keyword matching from structured data.

🧠 How It Works
The document content was manually turned into a file called hogwarts_data.json — a list of questions, keywords and answers.

When you send a message to the bot, it searches that data for matching keywords.

If it finds a match, it replies with the correct answer. If not, it says it doesn’t know.

🗂 File Structure
📁 Project Folder/
├── chatbot.py           # Main logic for loading and matching answers
├── commands.py          # Handles Telegram commands like /start and /help
├── main.py              # Starts the bot and connects everything
├── hogwarts_data.json   # Knowledge base from the official PDF
├── apikey.py            # Contains your Telegram API key

🚀 How to Use
Install Requirements
pip install python-telegram-bot==20.0
Create Your API Keys

Start Chatting on Telegram!

Use /hello to start

Ask things like:

“Who can apply?”

“When is the deadline?”

“What are the games?”

“How much does it cost?”

📌 Example Questions
Question	Answer
Who can apply?	High school (grades 9-11) and university students.
How long is the camp?	1 week in August at Renaissance Camp.
What's the cost?	~$87 per participant. Sponsorship may be available.

✅ Requirements
Python 3.8+

python-telegram-bot v20+

👨‍💻 Author
Keldiyorov Xushnudbek – for the Hogwarts Summer School 2025 Case Study