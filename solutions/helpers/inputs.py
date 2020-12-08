import os.path

def import_input(day):
    path = os.path.abspath(os.path.dirname(__file__))
    file = open(os.path.join(path,'../../inputs/'+str(day)+'.txt'), 'r')
    return file.read()