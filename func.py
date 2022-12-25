def disp(sh):
    print('disp function '+sh())

def show():
    return add()

def add():
    return  'add method'

disp(show)