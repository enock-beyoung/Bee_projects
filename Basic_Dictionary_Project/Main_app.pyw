'''
Author @Beyoung Enoch
version: 1.00.o
Project Start date: 06/10/2023

'''

from tkinter import*
from tkinter.messagebox import showerror
from time import sleep
import webbrowser
import os
import sys


#File_path configuration
ico_file_path= os.path.abspath("BasicDict.ico")
words_file_path= os.path.abspath("Words.txt")
definitions_file_path= os.path.abspath("definitions.txt")

#Pre-loaded files
word_list= list()
dictionary_definitions= list()

try:
    with open(words_file_path, "r") as listing_file:
        word_list= listing_file.readlines()
except Exception:
    showerror(title= "Error", message= "WordsFile Not Found!")
    sys.exit()
    
    
try:
    with open(definitions_file_path, "r") as deffile:
        dictionary_definitions= deffile.readlines()
        
except Exception:
    showerror(title= "Error", message= "DictionaryFile Not Found!")
    sys.exit()



#Function definitions
def online_dictionary():
    an_online_dictionary_url= "https://www.merriam-webster.com/"
    webbrowser.open(an_online_dictionary_url)


#Pop-up function
def tip_command():
    tip_pop= Toplevel()
    tip_pop.title("Tips")
    tip_pop.resizable(False, False)
    tip_text= Text(tip_pop, wrap= "word", relief= "raised", bg= "black", fg= "red", font= ("Georgia", 12), width= 30, height= 10)
    tip_text.insert(END, "Tip:\n\nv.i.: intransitive verb\nv.t.: transitive verb\nn.: noun\nv. or vb.: verb\na.: adjective\np.p.: past participle\npl.: plural\nadv.: adverb\np. pr.: present participle\nimp.: past tense.")
    tip_text.config(state= "disabled")
    tip_text.pack(fill= BOTH)

#Pop-up function
def about_command():
    about_pop= Toplevel()
    about_pop.title("About")
    about_pop.geometry("250x168")
    about_pop.resizable(False, False)
    about_label=Label(about_pop, text= "\n About: \n\n This piece of code is to help beginers get used to the basic \
usage of tkinter and how to align commands to widgets. It is a very simple yet useful software for anyone to look at\
 or use.", wraplength= 250, bg= "lightgray", fg= "black", font= ("Arial", 12))
    about_label.pack(fill= BOTH)
   
    
def on_highlight(event):
    gotten_index= list_view.curselection()
    if gotten_index != ():
        gotten_index= int(gotten_index[0])
        searched= list_view.get(gotten_index).replace("\n", "")
        defined= dictionary_definitions[gotten_index]
        text_widget.config(state= "normal")
        text_widget.delete("1.0", END)
        text_widget.insert(END, f"Definition of {searched}: \n\n{defined.strip()}")
        text_widget.config(state= "disabled")
        


def definitions():
    Query= search_entry.get().strip().title()
    New_Query= Query+"\n"
    if New_Query in word_list:
        text_widget.config(state= "normal")
        text_widget.delete("1.0", END)
        text_widget.insert(END, f"Definition of {Query}: \n\n")
        needed_index= word_list.index(New_Query)
        for steps in range(needed_index, needed_index+50):
            if New_Query == word_list[needed_index+1]:
                if New_Query != word_list[steps]:
                    text_widget.config(state= "disabled")
                    break
                defined_for_search= dictionary_definitions[steps]
                text_widget.config(state= "normal")
                text_widget.insert(END, f"{defined_for_search.strip()} \n\n")
            
            else:
                defined_for_search= dictionary_definitions[needed_index]
                text_widget.insert(END, f"{defined_for_search.strip()}")
                text_widget.config(state= "disabled")
                break
    
    
    elif Query == "":
        text_widget.config(state= "normal")
        text_widget.delete("1.0", END)
        text_widget.insert("1.0", f"{Query}: \n No text input!")
        text_widget.config(state= "disabled")
        
    else:
        text_widget.config(state= "normal")
        text_widget.delete("1.0", END)
        text_widget.insert("1.0", f"{Query}: \n Not defined.")
        text_widget.config(state= "disabled")
        

    

#Main window configuration
m_window= Tk()
m_window.geometry("700x400")
m_window.resizable(False,False)
m_window.title("|Basic Dictionary")
m_window.iconbitmap(ico_file_path)


#Menus
menubar= Menu(m_window)

m_window.config(menu= menubar)

appmenu= Menu(menubar, tearoff= 0)
helpmenu= Menu(menubar, tearoff= 0)

menubar.add_cascade(label= "App", menu= appmenu)
menubar.add_cascade(label= "Help", menu= helpmenu)

appmenu.add_command(label= "Tip", command= tip_command)
appmenu.add_command(label= "Online..", command= online_dictionary)
appmenu.add_separator()
appmenu.add_command(label= "Exit", command= m_window.destroy)
helpmenu.add_command(label= "About", command= about_command)

#Frames
left_frame = Frame(m_window, bg= 'black', width= 250)
left_frame.pack(side= 'left', fill= 'both', expand= False)

right_frame = Frame(m_window, bg= None, width= 300)
right_frame.pack(side= 'right', fill= 'both', expand= True)

#Labels
Searchfor_label = Label(left_frame, text= "Search for: ", font= ('Elephant', 12), bg= 'black', fg= 'white', width= None, height= None, anchor= 'w', relief= 'raised')
Searchfor_label.grid(row= 0, column= 0)

#Scroll_Bars
definition_text_scroll= Scrollbar(right_frame, orient= "vertical")
definition_text_scroll.pack(side= LEFT, fill= Y)

word_list_scroll= Scrollbar(left_frame, orient= "vertical")
word_list_scroll.place(x= 4, y= 49, relheight= 0.852)

#Texts
text_widget= Text(right_frame, wrap= "word", bg= "black", fg= "white", font= ("Georgia", 11), width= 50, height= 10, yscrollcommand= definition_text_scroll.set)
definition_text_scroll.config(command= text_widget.yview)
text_widget.pack(side= RIGHT, fill= Y)

#Entries
search_entry = Entry(left_frame, width= None, show= None, justify= 'center', borderwidth= 2, bg= "lightgray", fg= None, state= 'normal')
search_entry.grid(row= 0, column= 1)

#Buttons
search_button= Button(left_frame, text= "GO ", command= definitions)
search_button.grid(row= 0, column= 2)
m_window.bind("<Return>", lambda event= None: search_button.invoke())

#Listboxs
list_view= Listbox(left_frame, width= 37, height= 20, yscrollcommand= word_list_scroll.set)
list_view.place(x= 20, y= 49)
word_list_scroll.config(command= list_view.yview)

for lines in word_list:
    list_view.insert(END, lines)
    
list_view.bind("<<ListboxSelect>>", on_highlight)    



m_window.mainloop()
