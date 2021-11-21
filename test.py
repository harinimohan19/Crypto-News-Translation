from googletrans import Translator

translator = Translator()

sentence = "Hello, how are you?"
dest_lang = "te"   # try: hi, te, ta, kn, ml, bn, ar

result = translator.translate(sentence, src="en", dest=dest_lang)

print("Original :", sentence)
print("Translated:", result.text)
