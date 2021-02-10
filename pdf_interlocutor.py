import googletrans
from googletrans import Translator
import PyPDF2   #Extract text from pdf
import pyttsx3  #Text to speech
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from fpdf import FPDF   #txt -> pdf
import os
from gtts import gTTS   #to save as mp3
import json        #to display choice of language dict

print(json.dumps(googletrans.LANGUAGES, indent = 4))
trex = Translator()
pdf = FPDF()   
myLang="en"
#msg="Select a language abbreviation from above : "
#myLang=str(input(msg))

Tk().withdraw()                             #Select Japanese PDF
filelocation = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(filelocation)
pages = pdfReader.numPages                  #total no. of pages

f = open("Saloni_new_translation.txt","w")
f.close()

for page in range(pages):                   #Translate each foreign language pages and store in .txt
    from_page = pdfReader.getPage(page)
    tt = from_page.extractText() 
    x=trex.translate(tt, dest=myLang)
    #for translation in translations:
    f = open("Saloni_new_translation.txt", "a")
    f.write(x.text)       #f.write((translation.text).encode('utf8'))         #print(translation.text,"\n") 
    f.close()

pdf.add_page()                              #Convert .txt--> .pdf
pdf.set_font("Arial", size = 15) 
f = open("Saloni_new_translation.txt", "r") 
for x in f: 
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L') 
f.close()
pdf.output("Saloni_new_translation.pdf")

pdfReader = PyPDF2.PdfFileReader("Saloni_new_translation.pdf")
pages = pdfReader.numPages                  #total no. of pages in translated txt
speaker = pyttsx3.init()
voices = speaker.getProperty('voices') 
speaker.setProperty('voice', voices[0].id)  # changing 0 to 1,2,3.. changes voices
speaker.say("hi ... Starting in 3... 2... 1...")   #Read Saloni_new_translation pdf

f= open('Saloni_new_translation.txt','r')
for i in f:
    speaker.say(i) 
    speaker.runAndWait()
f.close()

f= open("Saloni_new_translation.txt", "r")
file = f.read().replace("\n", "   ")
t=gTTS(text = str(file), lang = myLang, slow = False)
t.save("Saloni_new_translation.mp3")
f.close()

if os.path.exists("Saloni_new_translation.txt"):        #Delete intermediate txt
    os.remove("Saloni_new_translation.txt")
#os.startfile("Saloni_new_translation.mp3")
print("Translated Files Saved at: ",os.getcwd())