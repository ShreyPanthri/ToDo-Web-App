def get_todos(filename):
    file = open(filename, "r")
    todos_local = file.readlines()
    file.close()
    return todos_local
def write_todos(filename, todos_arg):
    file = open(filename, "w")
    file.writelines(todos_arg)
    file.close()

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
