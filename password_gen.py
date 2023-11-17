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
        self.special = ['!','@','#','$','%','&','?']
         

        #Result variable
        self.text = StringVar()
        self.text.set("Password")

        #Elements of the app 
        self.title = Label(root, text='Password Generator', padx=80, pady=15, font=(("Arial"), 12))
        self.Length_text = Label(root, text='Length')
        #self.result_text = Label(root, textvariable=self.text, borderwidth=1, relief="solid")
        self.result_text = Entry(root, textvariable=self.text, borderwidth=1, relief="solid",width=40, justify='center')


        self.letter_text = Label(root, text="Letters")
        self.numbers_text = Label(root, text="Numbers")
        self.special_text = Label(root, text="Special Characters")

        #Buttons
        self.varMenu = IntVar()
        self.dropMenu = OptionMenu(root, self.varMenu, *range(8,31))

        self.var_Letters = IntVar() #creates a tikter string value
        self.check_letters = Checkbutton(root, variable=self.var_Letters, onvalue=True, offvalue=False) #value of the on and offs
        self.check_letters.deselect() #resets a value

        self.var_numbers = IntVar() #creates a tikter string value
        self.check_numbers = Checkbutton(root, variable=self.var_numbers, onvalue=True, offvalue=False) #value of the on and offs
        self.check_numbers.deselect() #resets a value

        self.var_special = IntVar() #creates a tikter string value
        self.check_special = Checkbutton(root, variable=self.var_special, onvalue=True, offvalue=False) #value of the on and offs
        self.check_special.deselect() #resets a value

        self.generate=Button(root, text="Generate", command=lambda: self.gen_pass(self.var_Letters.get(), 1.7, self.var_numbers.get(), 1.3,  self.var_special.get(), 1.0, self.varMenu.get()))


        #Put elements on screen
        self.title.grid(row=0, column=0, columnspan=3)
        self.result_text.grid(row=1, column=0, columnspan=3)

        self.Length_text.grid(row=2, column=0)
        self.dropMenu.grid(row=2, column=2)

        self.check_letters.grid(row=3, column=2)
        self.letter_text.grid(row=3, column=0)

        self.check_numbers.grid(row=4, column=2)
        self.numbers_text.grid(row=4, column=0)

        self.check_special.grid(row=5, column=2)
        self.special_text.grid(row=5, column=0)

        self.generate.grid(row=6, column=0, columnspan=3)

        root.mainloop() 

    def gen_pass(self, letters, letters_per, numbers, numbers_per, special, special_per, ammount):
        self.x = []
        if (letters == 0) and (numbers == 0) and (special == 0):
            self.x = [" "]
        else:

            if (letters == 1):
                self.x += random.choices(self.letters, k=int(ammount*letters_per)) #choices take an ammount of elements base on a key

            if (numbers == 1):
                self.x += random.choices(self.numbers, k=int(ammount*numbers_per))

            if (special == 1): 
                self.x += random.choices(self.special, k=int(ammount*special_per))
            
            #print(self.x)
            self.x = random.sample(self.x, ammount)
            #print(self.x)
            self.x = ''.join(self.x)
            self.result_text.delete(0, END)
            self.result_text.insert(0, self.x)
        

new_generation = generator()



