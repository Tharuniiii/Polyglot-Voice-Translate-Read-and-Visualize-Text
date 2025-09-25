#  Polyglot-Voice-Translate-Read-and-Visualize-Text
Polyglot Voice is a web-based application that enables users to translate text into multiple languages, listen to translations with natural text-to-speech, and visualize content with a word cloud. Built with Python, Streamlit, and NLP libraries, it bridges the gap between languages by combining translation, speech, and visualization in one tool.

# 🚀 Features

Automatic Language Detection
Detects the language of the input text using langdetect.

Multilingual Translation
Translate input into any Google Translate-supported language using googletrans (async).

Text-to-Speech
Hear the original or translated text spoken aloud using gTTS.
Supports multiple languages with fallbacks for unsupported codes.

Word Cloud Visualization
Generates a visual word cloud for English words using NLTK + WordCloud.

Streamlit UI
Interactive, responsive, and easy-to-use interface.

# 🛠️ Installation

Clone the repository:

git clone https://github.com/YourUsername/polyglot-voice.git
cd polyglot-voice
---

(Optional) Create a virtual environment:
```
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

Install dependencies:
```
pip install -r requirements.txt
```
📦 Dependencies

streamlit – web framework

gtts – Google Text-to-Speech

googletrans – translation (async)

langdetect – detect input language

pycountry – language and country mapping

nltk – NLP processing

wordcloud – generate word clouds

matplotlib – visualization


▶️ Usage

Run the app locally:

```streamlit run app.py```


Steps:

Enter a paragraph in any language.

Detect the language automatically.

Choose target languages for translation.

Listen to the original or translated text.

View a word cloud of English words in the sidebar.

📂 Project Structure
```
polyglot-voice/
│
├─ app.py                # Main Streamlit application
├─ requirements.txt      # List of dependencies
├─ back.jpg              # Optional background image
├─ README.md             # Documentation
└─ images/               # Screenshots & visuals (optional)
```
# Demo
<img width="1828" height="825" alt="Screenshot 2025-09-24 195738" src="https://github.com/user-attachments/assets/77ff4658-1823-4b55-a6d8-f17a273b0305" />

🌟 Future Improvements

Add downloadable audio files of translations.

Extend word cloud to non-English languages.

Add speech-to-text for direct voice input.

Include sentiment analysis of input text.

👩‍💻 Author

Your Name – Tharuni

GitHub: https://github.com/Tharuniiii

LinkedIn: https://linkedin.com/in/tharuni-teegala/

