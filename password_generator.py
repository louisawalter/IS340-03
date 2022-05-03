import tkinter
from tkinter import *
from tkinter import messagebox
import random
import string
from turtle import bgcolor
import requests


class PasswordGenerator:
    def __init__(self):
        #create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Password Generator")
        self.main_window.geometry("400x400")
    
        #create frames
        self.password_length_frame = tkinter.Frame(self.main_window, pady=10)
        self.heading_frame = tkinter.Frame(self.main_window)
        self.top_frame = tkinter.Frame(self.main_window, highlightbackground='black', highlightthickness=2)
        self.bottom_frame = tkinter.Frame(self.main_window, pady=10)
        self.password_frame = tkinter.Frame(self.main_window, pady=10)

        #pack frames
        self.password_length_frame.pack()
        self.heading_frame.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.password_frame.pack()

        #create password length enry
        self.label = Label(self.password_length_frame, text="Please enter password length:")
        self.label.pack(side="left")
        self.password_var = StringVar()
        self.password_length = Entry(self.password_length_frame, width=10, textvariable=self.password_var, text="Please enter password length:" )
        

        #pack password legnth entry
        self.password_length.pack()

        #create heading
        self.heading_var = StringVar()
        self.heading = Label(self.heading_frame, textvariable=self.heading_var, pady=3, anchor='nw')
        self.heading_var.set('Please select critera for your password:')

        #pack heading
        self.heading.pack()

        #create password output field
        self.output_var = StringVar()
        self.output = Entry(self.password_frame, width = 10, textvariable=self.output_var, show="*") #encrypts the password

        #pack password output field
        self.output.pack(pady=5, side ='left')
        
        
        #IntVar objects for the Checkbuttons
        self.criteria1_var = tkinter.IntVar() #must include numbers
        self.criteria2_var = tkinter.IntVar() #must inlcude letters
        self.criteria3_var = tkinter.IntVar() #msut inlcude upper case
        self.criteria4_var = tkinter.IntVar() #must include special characters
        self.criteria5_var = tkinter.IntVar() #must be memorizable
       

        #setting IntVar objects to 0
        self.criteria1_var.set(0) 
        self.criteria2_var.set(0)
        self.criteria3_var.set(0)
        self.criteria4_var.set(0)
        self.criteria5_var.set(0)
       

        #Checkbutton widgets
        self.criteria1 = tkinter.Checkbutton(self.top_frame, text = "Must include numbers", variable = self.criteria1_var)
        self.criteria2 = tkinter.Checkbutton(self.top_frame, text = "Must include letters", variable = self.criteria2_var)
        self.criteria3 = tkinter.Checkbutton(self.top_frame, text = "Must include upper case", variable = self.criteria3_var)
        self.criteria4 = tkinter.Checkbutton(self.top_frame, text = "Must include special characters", variable = self.criteria4_var)
        self.criteria5 = tkinter.Checkbutton(self.top_frame, text = "Must be memorizable", variable = self.criteria5_var)
       
        #pack checkbuttons
        self.criteria1.pack(anchor="w")
        self.criteria2.pack(anchor="w")
        self.criteria3.pack(anchor="w")
        self.criteria4.pack(anchor="w")
        self.criteria5.pack(anchor="w")

        #OK and Quit buttons
        self.generate_button = tkinter.Button(self.bottom_frame, text = "Generate password", command = self.create_password)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy) #closes the window

        #pack OK and Quit buttons
        self.generate_button.pack(side = "left")
        self.quit_button.pack(side = "left")

        #buttons for password
        self.new_button = tkinter.Button(self.password_frame, text = "new", command =self.generate_new_password)
        self.show_button = tkinter.Button(self.password_frame, text = "show", command = self.show_password)
        self.hide_button = tkinter.Button(self.password_frame, text="hide", command = self.hide_password)
        
        #pack password buttons
        self.show_button.pack(side="left")
        self.hide_button.pack(side="left")
        self.new_button.pack(side="left")

    
        #start mainloop
        tkinter.mainloop()

    
    #create a password based on selections
    def create_password(self):
        self.password = []
        self.characters = [] #list of characters to generate password from
        if self.password_length.get()  == '': #checks if user specified a password length
            self.show_error_message_pl
        
        password_length = int(self.password_length.get()) #gets the users entry and converts to an integer
        i = 0

        if self.criteria1_var.get() == 1: #gets the state of the IntVar 
            for char in string.digits:
                self.characters.append(char) #appends numbers to the character list
                
        if self.criteria2_var.get() == 1:
            for char in string.ascii_lowercase:
                self.characters.append(char)
                
        if self.criteria3_var.get() == 1:
            for char in string.ascii_uppercase:
                self.characters.append(char)
              
        if self.criteria4_var.get() == 1:
            for char in "!§%&/()=?$*+><,.;:":
                self.characters.append(char)

        if self.criteria5_var.get() == 1:
            word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
            response = requests.get(word_site)
            words = response.content.splitlines() #list with words of data type bytes
            random_word = random.choice(words)
            random_word = random_word.decode(encoding = "UTF-8") #converts the bytes to a string
            self.password.insert(0,random_word) #puts the word at the beginning the password
        
        #in case no selection was made
        if self.criteria1_var.get() == 0 and self.criteria1_var.get() == 0 and self.criteria2_var.get() == 0 and self.criteria3_var.get() == 0 and self.criteria4_var.get() == 0 and self.criteria5_var.get() == 0:
            self.show_error_message_checkbox()

        random.shuffle(self.characters) #shuffle the characters
    
        while i < password_length:
            self.password.append(random.choice(self.characters)) #randomly put together a password from list with characters
            i = i+1
        
        self.output_var.set("".join(self.password)) #setting the output variable to the created password, using join() to avoid spaces between characters
        
    #generates a new password
    def generate_new_password(self):
        self.create_password()

    #decrypts the password
    def show_password(self):
        self.output.config(show="")

    #encrypts the password
    def hide_password(self):
        self.output.config(show="*")

    #function to show error message for no password length
    def show_error_message_pl(self):
        messagebox.showerror("Python Error", "Please give a password lenght")

    #function to show error message for no selected criteria
    def show_error_message_checkbox(self):
        messagebox.showerror("Python Error","Please select at least one criteria")


if __name__ == "__main__":
    password_generator = PasswordGenerator()