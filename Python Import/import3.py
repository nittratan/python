# import own module

from new_folder.importExample import Person

class Man(Person): # inherit Person class from importExample.py
    pass


m = Man(1, "Ratan Sharma", 24)

print(m.display())