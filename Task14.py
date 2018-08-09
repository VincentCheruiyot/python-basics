#Shopping list app as per video no. 23

#run the script
#put new things into the list
#enter the word done in all caps to quit the program
#on quiting, let the app show all the items in the list
#have the HELP command
#have the SHOW command
#clean code up in general


#make a list to hold onto our items
shopping_list=[]

def show_help():
    print("what should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def show_list():
    #print out the list
    print("Here's your list: ")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))
show_help()

while True:
    # ask for new items
    new_item = input("> ")

    if new_item=='DONE':
        break
    elif new_item=='HELP':
        show_help()
        continue
    elif new_item=='SHOW':
        show_list()
        continue
    add_to_list(new_item)


show_list()
#be able to quit the app


