'''
All the commands will be listed here with their description and proper syntax !

---------------------------------- I N D E X ----------------------------------

> Help   - 

> Create -

> Search -

> Show   -

> Update -

> Delete -

-------------------------------------------------------------------------------

LOG-1 09-04-2024 TUE 12:21

-> write - documentation (12:22)
-> created - helps() (13:43)
-> created - create() (13:56)
-> created - search() (14:06)
-> created - show() (14:07)
-> created - update() (16:01)
-> created - delete() (16:03)
-> write - defined create() <basic format> (16:10)
-> write - defined show() <basic format> (16:14)

'''

# importing all the helping modules 

from helper_mod_1 import max_lden,horz_pat

# importing inbuilt modules that can help

import pickle

# main body

def helps():
    print("<will display the help text>")

def create():
    nme = input("enter the name : ")
    num = int(input("enter the number : "))
    list=[nme,num]
    with open(".\\contact.ctb","+ab") as f:
        pickle.dump(list,f)

def search():
    print("<search text will go here>")

def show():
    with open(".\\contact.ctb","rb") as f:
        try:
            while True:
                k=pickle.load(f)
                print(k)
        except:
         print("file opened")

def update():
    print("will show all the details tp be updated")

def delete():
    print("will delete the message and show delete message")
