'''
this application has command-line interface because its a console-based application, thus
it might not be user freindly but i'll try to change it and make it more interactive !

version syntax : (form right) first 2 digits represents numbers of bugs fixed or day-wise
logs made or the test version (if there is no ready version). The next two digits represents
new features added and last two digits represnt the ready and executable version of project!

current version : 00.00.01

contact book (v00.00.01) - 09-04-2024 TUE 12:23 logs

-> "main" module created
-> "commands" module created
-> command processing added (via conditons)

contact book (v00.00.01) - 10-04-2024 WED 13:23 logs

-> no changes made till 13:34
-> tested 2 fuctions to read query 16:36

'''

# commands module contains all the available commands that can be used in this application

import commands

print("CONTACT BOOK v00.00.01 | type \"help\" for help ")

# to keep our application alive.

while True:

    # main functions of application
    # 1) taking command input
    # 2) closing the application

    cmd = input("> ")

    if cmd.strip() == "":
        continue

    elif cmd.lower() in ["quit","exit","close"]:
        break

    # reading commands from user

    # for help prompt

    elif cmd.lower() == "help":
        commands.helps()

    # for creating contact details
    
    elif cmd.lower() == "create":
        commands.create()

    # for displaying all details
    
    elif cmd.lower() == "show":
        commands.show()
    
    # for searching a contact
    
    elif cmd.lower() == "search":
        commands.search()

    # for updating an existing contact
        
    elif cmd.lower() == "update":
        commands.update()
    
    # for deleting an existing contact
        
    elif cmd.lower() == "delete":
        commands.delete()

    # end of processing
       
    else:
        print("no commands found | please check your syntaax or type \"help\" for help !")
