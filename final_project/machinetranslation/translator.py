"""Translates Texts from en-->fr and fr-->en using ibm_watson"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """Translates the given Text from english to french"""
    french_text = ''
    try:
        answer = language_translator.translate(englishText, model_id='en-fr').get_result()
        french_text = answer["translations"][0]["translation"]
    except:
        french_text = ''
    return french_text

def frenchToEnglish(frenchText):
    """Translates the given Text from french to english"""
    english_text = ''
    try:
        answer = language_translator.translate(frenchText, model_id='fr-en').get_result()
        english_text = answer["translations"][0]["translation"]
    except:
        english_text = ''
    return english_text
