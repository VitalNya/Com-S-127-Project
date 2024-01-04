# TODO: Student writes their name at the top of the file (delete this TODO line when completed) (0.5 pt.)
# Vital Nyabashi            <4/10/2023>
# <Assignment 5: ultimateTODO.py / 1 Lab/

# TODO: Ensure that the assignment is turned in by the due date AND Ensure that the file that gets submitted is called 'ultimateTODO.py' (1 pt.)

import sys
import pickle


def initList():
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList


def saveList(todoList):
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()


def loadList():
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()

    return todoList


def checkItem(item, todoList):
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    itemFound = False
    keyName = ""
    index = -1

    for key, lst in todoList.items():
        # If we item is present in the keys we iterate through set the variable itemFound to True
        if item in lst:
            itemFound = True
            # set the keyName variable to the key where the item was found, and the index in the list where the item was found.
            index = lst.index(item)
            # If the item is not found in any of lists in the dictionaries we iterate, break so we can keep the default values
            break

    # TODO: Iterate through all the keys in the dictionary and check each list of each key to see if an item is present.

    # Return the itemFound boolean, the keyName string, and the index integer (1 pt.)
    return itemFound, keyName, index


def addItem(item, toList, todoList):
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary of lists.

    if checkItem(item, todoList):
        # If the item already exists, find the list and index where it is located
        for key, value in todoList.items():
            if item in value:
                index = value.index(item)
                # Print an error message specifying the details requested in the prompt
                print(f"Error: {item} is already in {key} at index {index}")
                # Return the unmodified todoList
                return todoList
    else:
        # If the item doesn't exist, add it to the list specified by toList
        todoList[toList].append(item)
        # Return the modified todoList
    return todoList


def deleteItem(item, todoList):
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """
    # use the checkItem function to see if item already exists in the dictionary of the list
    itemFound=checkItem(item, todoList)
    # If item is in the dictionary of List, delete it
    if itemFound:
        for key, value in todoList.item():
            if item in value:
                value.remove(item)
    # in the Dictionary of Lists, print an error message specifying:
    # - the name of the item
    else:
        print(f"Error: {item} not found.")
    # Return the itemFound boolean and the todoList data structure after it has been modified (or not) (1 pt.)
    return itemFound, todoList

    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary




def moveItem(item, toList, todoList):
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    # Use the itemFound boolean it returns to determine if the item was found
    itemFound = deleteItem(item, todoList)
    if itemFound:
        #use the addItem function to add the item to the specified toList key
        addItem(item, toList, todoList)
    # TODO: Use the deleteItem function to search for/ delete the specified item. Use the itemFound boolean

    # Return the todoList data structure after it has been modified (or not) (1 pt.)
    return todoList


def printTODOList(todoList):
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """
    # TODO: Iterate through all the keys in the dictionary and print both the key and the list the dictionary
    # holds for that key on a single line on the screen.
    for key, value in todoList.items():
        print(f"{key}: {value}")
    # Return None (1 pt.)
    return None


def runApplication(todoList):
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """

    while True:
        print("-----------------------------------------------------------------")
        choice = input(
            "APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            item = input("Enter an item: ")
            # TODO: Prompt the user to enter an item, and take in that input as a string. Call the addItem function
            # to add the item to the 'backlog' key's corresponding list. Finally,
            todoList = addItem(item, "backlog", todoList)
            # use the printTODOList function to print the todoList data structure. (1 pt.)
            printTODOList(todoList)
            pass

        elif choice == "m":
            # check if any of the lists in the data structure in them
            if all(len(todoList[key]) == 0 for key in todoList):
                # If all th lists are empty , prunt an error message that states "No items t move"
                print("No item to move!")
            else:
                # Ask user to enter an item, and take in that input as a string
                item = input("Enter the item to move: ")
                # - Use the checkItem function to confirm if that item is in the data structure.
                while not checkItem(item, todoList):
                    # - While the item is not in the data structure, print an error message stating the item does not exist
                    #   and then prompt the user to enter a different item. Use the checkItem function again to confirm if
                    #   the new item is inside the data structure.
                    print(f"item '{item}' does not exist in the todo list!")
                    # - Prompt the user to enter an item, and take in that input as a string.
                    item = input("Enter the item to move: ")

                to_list = input("Enter the list to move the item to: ")
                # - While the dictionary key the user specifies is not a key that is in the dictionary, print an error
                #   message stating that the key does not exist. Then, prompt the user to enter a new dictionary key.
                while to_list not in todoList:
                    print(f"'{to_list}' is not a valid list name!")
                    to_list = input("Enter the list to move the item to: ")
                # - call the moveItem function, passing the item, dictionary key, and todoList as arguments.
                todoList = moveItem(item, to_list, todoList)
            # Finally, whether or not the data structure is totally empty or not, call the printTODOList function
            # and print out the data structure. (1 pt.)
            printTODOList(todoList)
            # TODO: #Check to see if any of the lists in the data structure have items in them. If all of the lists in
            # the dictionary are empty, print an error message that states 'No items to move!' or something similar.


            pass
        elif choice == "d":
            item = input("Enter the item to delete: ")

            item_deleted, todoList = deleteItem(item,todoList)
            # TODO: Prompt the user to enter an item, and take in that input as a string. Call the deleteItem function
            # to remove the item from the data structure if it is present. Finally, use the printTODOList function
            # to print the todoList data structure. (1 pt.)
            # HINT: the deleteItem function returns two (2) values - do you need to do things with both of them?
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList


def main():
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False

    print("The Ultimate TODO List")
    print()

    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: <Vital Nyabashi>")
    print("[COM S 127 <section A>]")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n":
            todoList = initList()

            printTODOList(todoList)

            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)

            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()


if __name__ == "__main__":
    main()