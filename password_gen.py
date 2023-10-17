#This file
import string
import random
from tkinter import *
#choices takes an element

class generator:
    def __init__(self):

        root = Tk()
        root.title('Password Generator')

        self.x=[]
        self.numbers = string.digits
        self.letters = string.ascii_letters
        self.special = ['¡','!','#','$','%','&','¿','?']

        #Result variable
        self.text = StringVar()
        self.text.set("Password")

        #Elements of the app 
        self.title = Label(root, text='Password Generator', padx=80, pady=20, font=(("Arial"), 12))
        self.Length_text = Label(root, text='Length')
        #self.result_text = Label(root, textvariable=self.text, borderwidth=1, relief="solid")
        self.result_text = Entry(root, textvariable=self.text, borderwidth=1, relief="solid")


        #Buttons
        self.varMenu = IntVar()
        self.dropMenu = OptionMenu(root, self.varMenu, *range(8,31))

        self.var_Letters = IntVar() #creates a tikter string value
        self.check_letters = Checkbutton(root, text="Letters", variable=self.var_Letters, onvalue=True, offvalue=False) #value of the on and offs
        self.check_letters.deselect() #resets a value

        self.var_numbers = IntVar() #creates a tikter string value
        self.check_numbers = Checkbutton(root, text="Numbers", variable=self.var_numbers, onvalue=True, offvalue=False) #value of the on and offs
        self.check_numbers.deselect() #resets a value

        self.var_special = IntVar() #creates a tikter string value
        self.check_special = Checkbutton(root, text="Special Characters", variable=self.var_special, onvalue=True, offvalue=False) #value of the on and offs
        self.check_special.deselect() #resets a value

        self.generate=Button(root, text="Generate", command=lambda: self.gen_pass(self.var_Letters.get(), 0.9, self.var_numbers.get(), 0.5,  self.var_special.get(), 0.5, self.varMenu.get()))


        #Put elements on screen
        self.title.grid(row=0, column=0, columnspan=3)
        self.result_text.grid(row=1, column=0, columnspan=3)

        self.Length_text.grid(row=2, column=0)
        self.dropMenu.grid(row=2, column=2)

        self.check_letters.grid(row=3, column=2)
        self.check_numbers.grid(row=4, column=2)
        self.check_special.grid(row=5, column=2)

        self.generate.grid(row=6, column=0, columnspan=3)

        root.mainloop() 

    def gen_pass(self, letters, letters_per, numbers, numbers_per, special, special_per, ammount):
        self.x = []
        if (letters == 0) and (numbers == 0) and (special == 0):
            self.x = [" "]
        else:

            if (letters == 1):
                self.x += random.choices(self.letters, k=int(ammount)) #choices take an ammount of elements base on a key

            if (numbers == 1):
                self.x += random.choices(self.numbers, k=int(ammount))

            if (special == 1): 
                self.x += random.choices(self.special, k=int(ammount))
            
            #print(self.x)
            self.x = random.sample(self.x, ammount)
            #print(self.x)
            self.x = ''.join(self.x)
            self.result_text.delete(0, END)
            self.result_text.insert(0, self.x)
        

new_generation = generator()

#new_generation.gen_pass(True, 0.7, True, 0.2, True, 0.1, 15)


