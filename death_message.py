#print a random message everytime you die

import random  # for fun
import gd

messages = ["Get good.", "RIP", "F", "bruh", "hm..."]  # some messages to pick from

# initialize memory object by acquiring process handle and base addresses
memory = gd.memory.get_memory()
do_print = True

while True:
    if memory.is_dead():  # if player is dead
        if do_print:
            print(f"{random.choice(messages)} ({memory.get_percent()}%)")
        do_print = False
    else:
        do_print = True