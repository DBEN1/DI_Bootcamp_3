from translate import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translations = {}

# Create a translator object
translator = Translator(to_lang="en")

for word in french_words:
    translation = translator.translate(word)
    translations[word] = translation

print(translations)
