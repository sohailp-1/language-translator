from googletrans import Translator

translator = Translator()

text = input("Enter text: ")
lang = input("Enter language (hi, fr, es): ")

result = translator.translate(text, dest=lang)

print("Translated:", result.text)