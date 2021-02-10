import googletrans
from googletrans import Translator
#Extract text from pdf
import PyPDF2
#Text to speech
import pyttsx3
from tkinter import Tk
from tkinter.filedialog import askopenfilename
#.txt -> .pdf  :
from fpdf import FPDF 
import os
#to save as mp3:
from gtts import gTTS
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
'''
path = '/Users/Saloni/Downloads/'
os.chdir("C:")
os.chdir(path)
'''
print("Creating .txt file...", end ="")
f = open("Saloni_new_translation.txt","w")
f.close()


print("\rTranslating inside txt...", end ="")
for page in range(pages):                   #Translate each foreign language pages and store in .txt
    from_page = pdfReader.getPage(page)
    tt = from_page.extractText() 
    x=trex.translate(tt, dest=myLang)
    #for translation in translations:
    f = open("Saloni_new_translation.txt", "a")
    f.write(x.text)       #f.write((translation.text).encode('utf8'))         #print(translation.text,"\n") 
    f.close()
print("\rTranslated to ",myLang, "!", end =" ")

pdf.add_page()                              #Convert .txt--> .pdf
pdf.set_font("Arial", size = 15) 
f = open("Saloni_new_translation.txt", "r") 
for x in f: 
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L') 
f.close()
pdf.output("Saloni_new_translation.pdf") 
print("\rPDF created !\t\t\t", end =" ")

pdfReader = PyPDF2.PdfFileReader("Saloni_new_translation.pdf")
pages = pdfReader.numPages                  #total no. of pages
speaker = pyttsx3.init()
voices = speaker.getProperty('voices') 
speaker.setProperty('voice', voices[0].id)  # changing 0 to 1,2,3.. changes voices
speaker.say(" hi ...")
print("\rReading Txt file......", end =" ")
speaker.say("Starting in 3... 2... 1...")   #Read Saloni_new_translation pdf

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
print("\r .mp3 file Created  !!!", end =" ")

if os.path.exists("Saloni_new_translation.txt"):        #Delete intermediate txt
    os.remove("Saloni_new_translation.txt")
print("Txt file deleted...", end =" ")

#os.startfile("Saloni_new_translation.mp3")
print("\rPDF & Audio files Saved at: ",os.getcwd(), end =" ")
#print("The End :)")