from globals import  file_path

def get_list_form_file(path = file_path):
    """"
    Read a file
    Return the todos list form file
    """
    with open(path, "r") as file:
        list_todos = file.readlines()

    return list_todos


def update_file(list_todos, path = file_path):
    """" Write the to-do items list in the text file """
    with open(path, "w") as file:
        file.writelines(list_todos)

# this block runs only if I run the functions.py file
if __name__ == "__main__":
    print(get_list_form_file())
