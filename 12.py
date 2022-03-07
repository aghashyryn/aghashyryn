from gtts import gTTS
from playsound import playsound
print("please enter your text:")
user_input = str(input())
audio = 'voice.mp3'
#language = 'en'
sp = gTTS(text=user_input , lang='en' , slow=False)
sp.save(audio)
print("Your Text cvonvert tp speesch sucssufully")
user_input2 = input("Do you want play speech ? y/n \n")
if user_input2 == "y" :
    playsound(audio)
else :
    print ("ok ! NP")
