from translate import Translator

translator = Translator(to_lang="fr")
try:
    with open('message.txt') as message:
        text = message.read()
        translation = translator.translate(text)
        print('english : ', text)
        print('french : ', translation)
except FileNotFoundError:
    print('file not found')
