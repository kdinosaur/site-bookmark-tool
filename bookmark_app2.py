import tkinter as tk
import webbrowser

URL0 = 'https://www.cnet.com/news/'
URL1 = 'https://techcrunch.com'
URL2 = 'https://www.theverge.com'


# Event handler function: This function takes a url (defined above) as argument
def open_cp1(event):
    webbrowser.open_new_tab(URL0)

def open_cp2(event):
    webbrowser.open_new_tab(URL1)

def open_cp3(event):
    webbrowser.open_new_tab(URL2)


window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="CNET")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="Tech Crunch")
blabel.grid(column=1, row=0)

clabel = tk.Label(text="The Verge")
clabel.grid(column=2, row=0)

#Creates buttons, instructs to open new window, labels. Alignment in grid.)
button = tk.Button(window, text="CNET")
button.grid(column=0)

button2 = tk.Button(window, text="TechCrunch")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="The Verge")
button3.grid(column=2, row=1)

# Binds button function to click
button.bind("<Button-1>", open_cp1)
button2.bind("<Button-1>", open_cp2)
button3.bind("<Button-1>", open_cp3)

window.mainloop()
