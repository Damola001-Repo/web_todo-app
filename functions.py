def get_todos(filepath='todos.txt'):
    """Fetches to-do list from a text file"""
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos

def write_todo(todos_arg, filepath='todos.txt'):
    """Writes to-do items inside a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print(get_todos())