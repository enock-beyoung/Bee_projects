'''
Author @Beyoung Enoch
version: 1.00.o
Project Start date: 06/10/2023

Next update is the ability to search for words that starts with "-"
'''

from tkinter import*
from tkinter import ttk#find out
from tkinter import messagebox#find out
import webbrowser


#Function definitions
def online_dictionary():
    an_online_dictionary_url="https://www.merriam-webster.com/"
    webbrowser.open(an_online_dictionary_url)



def tip_command():
    tip_pop=Toplevel()
    tip_pop.title("Tips")
    tip_pop.resizable(False, False)
    tip_text=Text(tip_pop, wrap="word", relief="raised", bg="black", fg="red", font=("Georgia", 12), width=30, height=10)
    tip_text.insert(END, "Tip:\nFew words have a number infront of them in the definition window on the right-side. \ne.g. The definition of diet has diet1 definition listed first but it also has diet2 which continuous the definition, thus words defined with '1' infront has '2' and probably '3' for further definitions.")
    tip_text.config(state="disabled")
    tip_text.pack(fill=BOTH)


def about_command():
    about_pop=Toplevel()
    about_pop.title("About")
    about_pop.geometry("250x168")
    about_pop.resizable(False, False)
    about_label=Label(about_pop, text="\n About: \n\n This piece of code is to help beginers get used to the basic \
usage of tkinter and how to align commands to widgets. It is a very simple yet useful software for anyone to look at\
 or use.", wraplength=250, bg="lightgray", fg="black", font=("Arial", 12))
    about_label.pack(fill=BOTH)



def definitions():
    Query=entry1.get().title()
    with open(r"C:\Users\MOSES YENLI\Documents\GitHub\Bee_projects\Basic_Dictionary_Project\Wordlog.txt", "r", encoding="utf-8") as wordsearch:
        wordsread=wordsearch.read()
        if Query in wordsread:
            with open(r"C:\Users\MOSES YENLI\Documents\GitHub\Bee_projects\Basic_Dictionary_Project\OED.txt", mode="r", encoding="utf-8") as deffile:
                for line in deffile:
                    words=line.split()
                    if Query in words[0]:
                        text_widget.config(state="normal")
                        text_widget.delete("1.0", END)
                        text_widget.insert(END, f"Definition of {words[0]}: \n\n{line.strip()}")
                        text_widget.config(state="disabled")
                        break
        else:
            text_widget.config(state="normal")
            text_widget.delete("1.0", END)
            text_widget.insert("1.0", f"{Query}: \n Not defined.")
            text_widget.config(state="disabled")
            

    

#Main window configuration
m_window=Tk()
m_window.geometry("550x300")
m_window.resizable(False,False)
m_window.title("|Basic Dictionary")
m_window.iconbitmap(r"C:\Users\MOSES YENLI\Documents\GitHub\Bee_projects\Basic_Dictionary_Project\BasicDict.ico")

#Pop-ups


#Menus
menu1=Menu(m_window)

m_window.config(menu=menu1)

appmenu=Menu(menu1, tearoff=0)
helpmenu=Menu(menu1, tearoff=0)

menu1.add_cascade(label="App", menu=appmenu)
menu1.add_cascade(label="Help", menu=helpmenu)

appmenu.add_command(label="Tip", command=tip_command)
appmenu.add_command(label="Online..", command=online_dictionary)
appmenu.add_separator()
appmenu.add_command(label="Exit", command=m_window.destroy)
helpmenu.add_command(label="About", command=about_command)

#Frames
frame1 = Frame(m_window, bg='black', width=250)
frame1.pack(side='left', fill='both', expand=False)

frame2 = Frame(m_window, bg=None, width=300)
frame2.pack(side='right', fill='both', expand=True)


#Labels
label1 = Label(frame1, text="Search for: ", font=('Elephant', 12), bg='black', fg='white', width=None, height=None, anchor='w', relief='raised')
label1.grid(row=0, column=0)


#Scroll_Bars
scroll1=Scrollbar(frame2, orient="vertical")
scroll1.pack(side=LEFT, fill= Y)


#Texts
text_widget=Text(frame2, wrap="word", bg="black", fg="white", font=("Georgia", 11), width=50, height=10, yscrollcommand=scroll1.set)
scroll1.config(command=text_widget.yview)
text_widget.pack(side=RIGHT, fill=Y)


#Entries
entry1 = Entry(frame1, width=None, show=None, justify='center', borderwidth=2, bg="lightgray", fg=None, state='normal')
entry1.grid(row=0, column=1)


#Buttons
button1=Button(frame1, text= "GO ", command= definitions)
button1.grid(row=0, column=2)
m_window.bind("<Return>", lambda event= None: button1.invoke())

""" button2=Button(frame1, text="^", font=("Elephant", 11))
button2.place(x=1,y=253) """

m_window.mainloop()
