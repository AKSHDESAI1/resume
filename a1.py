# from gtts import gTTS  
  
# from playsound import playsound  
   
# text_val = 'All the best for your exam1.'  
  
# language = 'en'  
  
# obj = gTTS(text=text_val, lang=language, slow=False)  

# obj.save("exam.mp3")  
   
# playsound("exam.mp3")  

from googletrans import Translator
a2 = Translator()

        # arr = []
        # for i in range(1, len2+1):
        #         b = a2.translate([0:15000], dest='gu')
        #         # b = a2.translate([(15000*i-1):(15000*i+1)], dest='gu')
        #         arr.append(b.text)

b = a2.translate("hello", dest='hi')
print(b)