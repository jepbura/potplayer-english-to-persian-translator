import sys
import requests
from win10toast import ToastNotifier

def translate_text(text):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=fa&dt=t&q={text}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        translation = data[0][0][0]
        return translation
    else:
        return "Translation failed."

def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)

def main():
    text_to_translate = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter the text to translate: ")
    translated_text = translate_text(text_to_translate)

    show_notification(text_to_translate, translated_text)

if __name__ == "__main__":
    main()
