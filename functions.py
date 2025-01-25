FILEPATH = 'todos_store.txt'


def get_todos(filepath=FILEPATH):
    """
    Read the text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos( todos_arg, filepath=FILEPATH):    # This function modifies the text file
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:    # we created a 'file object' (to write/overwrite our todos there)
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())