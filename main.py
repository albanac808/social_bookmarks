import tkinter as tk
import webbrowser

def linkedin(event):
    webbrowser.open('https://www.linkedin.com/in/alexalba/')

def facebook(event):
    webbrowser.open('https://www.facebook.com/alex.alba')

window=tk.Tk()
window.geometry("300x200")
window.title("Social Media Bookmark App")

label1=tk.Label(text="My Social Media", font=("Times new roman",20))
label1.grid(column=0,row=0)

button1=tk.Button(window,text="Linkedin",bg="orange")
button1.grid(column=1,row=1)
button2=tk.Button(window,text="Facebook",bg="pink")
button2.grid(column=3,row=1)
button1.bind("<Button-1>",linkedin)
button2.bind("<Button-1>",facebook)

window.mainloop()