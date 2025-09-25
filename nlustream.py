import streamlit as st
from gtts import gTTS
import os
import asyncio
from langdetect import detect, LangDetectException
from googletrans import Translator
import pycountry
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import nltk
from gtts.lang import tts_langs

# Download NLTK data
nltk.download('punkt')
nltk.download('words')

# Get all supported gTTS languages
gtts_languages = tts_langs()

# Function to read text aloud
def read_aloud(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("temp.mp3")
    os.system("start temp.mp3")

# Function to map pycountry code to gTTS code
def get_gtts_lang_code(pycountry_code):
    if pycountry_code in gtts_languages:
        return pycountry_code
    mapping = {
        'he': 'iw',       # Hebrew
        'zh-cn': 'zh-CN', # Chinese Simplified
        'zh-tw': 'zh-TW', # Chinese Traditional
    }
    return mapping.get(pycountry_code, 'en')  # fallback to English

# Function to generate word cloud
def generate_wordcloud(text):
    english_words = set(nltk.corpus.words.words())
    words = word_tokenize(text)
    english_words_in_text = [word for word in words if word.lower() in english_words]
    english_text = ' '.join(english_words_in_text)
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(english_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    plt.tight_layout()
    return fig

# Async function for translation
translator = Translator()
async def translate_text(text, dest='en'):
    result = await translator.translate(text, dest=dest)
    return result.text

# Main Streamlit app
st.title("Polyglot Voice: Translate, Read, and Visualize Text")

# Create a two-column layout
col1, col2 = st.columns(2)

# Get user input
with col1:
    paragraph = st.text_area("Enter one paragraph:")

with col2:
    # Get list of all languages
    all_languages = [lang.name for lang in pycountry.languages if hasattr(lang, 'name')]
    target_languages_input = st.multiselect("Select the desired languages for translation:", all_languages)

# Button to read aloud original paragraph
if st.button("Read Aloud"):
    if paragraph.strip():
        read_aloud(paragraph)

# Detect the language of the input paragraph
paragraph_language = None
if paragraph.strip():
    try:
        paragraph_language = detect(paragraph)
        language_name = pycountry.languages.get(alpha_2=paragraph_language).name
        st.write("Detected language:", language_name)
    except LangDetectException as e:
        st.error("Language detection failed: {}".format(e))
        paragraph_language = 'en'
        language_name = 'English'
    except KeyError:
        st.error("Language code not found in pycountry")
        language_name = 'Unknown'
    except Exception as e:
        st.error("Error during language detection: {}".format(e))
        paragraph_language = 'en'
        language_name = 'English'

# Translate to English if needed
translated_paragraph = paragraph
if paragraph_language and paragraph_language != 'en':
    try:
        translated_paragraph = asyncio.run(translate_text(paragraph, dest='en'))
        st.write("Translated to universal language English:", translated_paragraph)
    except Exception as e:
        st.error(f"Translation to English failed: {e}")

# Generate and display word cloud
if translated_paragraph.strip():
    try:
        translated_paragraph_utf8 = translated_paragraph.encode('utf-8', 'ignore').decode('utf-8')
        wordcloud_fig = generate_wordcloud(translated_paragraph_utf8)
        st.sidebar.subheader("Word Cloud")
        st.sidebar.pyplot(wordcloud_fig)
    except Exception as e:
        st.error(f"Error generating word cloud: {e}")

# Translate and read aloud for selected languages
if st.button("Translate and Read Aloud"):
    for lang_name in target_languages_input:
        try:
            lang_code = pycountry.languages.lookup(lang_name).alpha_2
            translated_text = asyncio.run(translate_text(paragraph, dest=lang_code))
            st.write(f"\nTranslated paragraph in {lang_name}:")
            st.write(translated_text)

            # Map to gTTS supported language
            tts_lang = get_gtts_lang_code(lang_code)
            read_aloud(translated_text, language=tts_lang)
        except Exception as e:
            st.error(f"Translation to {lang_name} failed: {e}")
