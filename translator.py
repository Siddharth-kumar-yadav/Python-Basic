from googletrans import Translator

translate = Translator()

out = translate.translate("कैसे",dest="en")

print(out)
