# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *

# NLP Packages
from textblob import TextBlob
import spacy
from spacy.lang.en.examples import sentences 

nlp = spacy.load('en')
#nlp = spacy
 
 # Structure and Layout
window = Tk()
window.title("NLP Tasks Performer")
window.geometry("700x500")
window.config(background='Gray')

# TAB LAYOUT
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1,text='Home')
tab_control.add(tab2, text='External File')


label1 = Label(tab1, text= 'NLP Tasks',padx=5, pady=5)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'External File',padx=5, pady=5)
label2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')


# Functions FOR NLP  FOR TAB ONE
def tokens():
	#from nlpiffy.py import tokens()
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text)
	final_text = list(str(new_text.words).split(" "))
	result = '\nTokens:{}'.format(final_text)
	tab1_display.insert(tk.END,result)


def get_sentiment():
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text)
	final_text = new_text.sentiment
	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
	tab1_display.insert(tk.END,result)

def get_entities():
	raw_text = str(raw_entry.get())
	txt = nlp(raw_text)
	final_text = [(entity.text,entity.label_) for entity in txt.ents ]
	result = '\nEntities:{}'.format(final_text)
	tab1_display.insert(tk.END,result)



# Clear entry widget
def clear_entry_text():
	entry1.delete(0,END)

def clear_display_result():
	tab1_display.delete('1.0',END)


# Clear Text  with position 1.0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result of Functions
def clear_result():
	tab2_display_text.delete('1.0',END)

# Functions for TAB 2 
# Open File to Read and Process
def openfiles():
	file1 = tk.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)


def get_file_tokens():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = list(str(new_text.words).split(" "))
	result = '\nTokens:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

def get_file_sentiment():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = new_text.sentiment
	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
	tab2_display_text.insert(tk.END,result)

def get_file_entities():
	raw_text = displayed_file.get('1.0',tk.END)
	docx = nlp(raw_text)
	final_text = [(entity.text,entity.label_) for entity in docx.ents ]
	result = '\nEntities:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

# MAIN NLP TAB
l1=Label(tab1,text="Enter Text To Analysis")
l1.grid(row=1,column=0)


raw_entry=StringVar()
entry1=Entry(tab1,textvariable=raw_entry,width=50,bg='Gray')
entry1.grid(row=1,column=1)

# bUTTONS
button1=Button(tab1,text="Tokenize", width=12,command=tokens,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab1,text="Sentiment", width=12,command=get_sentiment,bg='blue',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab1,text="Entities", width=12,command=get_entities,bg='#03A9F4',fg='#fff')
button3.grid(row=4,column=2,padx=10,pady=10)


button4=Button(tab1,text="Reset", width=12,command=clear_entry_text,bg="purple",fg='#fff')
button4.grid(row=6,column=1,padx=10,pady=10)

button5=Button(tab1,text="Clear Result", width=12,command=clear_display_result)
button5.grid(row=5,column=1,padx=10,pady=10)

# Display Screen For Result
tab1_display = Text(tab1,bg='Gray')
tab1_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab1_display.config(state=NORMAL)




# FILE READING  AND PROCESSING TAB
l1=Label(tab2,text="Contents Of File")
l1.grid(row=1,column=1)


displayed_file = ScrolledText(tab2,bg='gray',height=7)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)


# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="Open File", width=12,command=openfiles,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset ", width=12,command=clear_text_file,bg="purple",fg='#fff')
b1.grid(row=3,column=1,padx=10,pady=10)

b6=Button(tab2,text="Clear Result", width=12,command=clear_result,bg='#c5cae9')
b6.grid(row=3,column=2,padx=10,pady=10)

b4=Button(tab2,text="Sentiment", width=12,command=get_file_sentiment,bg='blue',fg='#fff')
b4.grid(row=4,column=0,padx=10,pady=10)

b5=Button(tab2,text="Entities", width=12,command=get_file_entities,bg='#80d8ff')
b5.grid(row=4,column=1,padx=10,pady=10)

b2=Button(tab2,text="Tokenize", width=12,command=get_file_tokens,bg='blue',fg='#fff')
b2.grid(row=4,column=2,padx=10,pady=10)

b7=Button(tab2,text="Close", width=12,command=window.destroy)
b7.grid(row=5,column=1,padx=10,pady=10)

# Display Screen

# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2,bg='gray',height=10)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

window.mainloop()
