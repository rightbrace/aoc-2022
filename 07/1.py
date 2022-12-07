import re

# Define a stack-based language with four functions:
# PUSH(dirname) -- move one level deeper in the hierarchy
# POP()         -- move one level higher, adding the current directory size to the parent
# GROW(size)    -- increase the size of the current directory
# FINISH()      -- POP out back to root

scanned_directories = {}
current_directory = ""

def PUSH(dirname):
    global scanned_directories
    global current_directory 
    current_directory += "/" + dirname
    scanned_directories[current_directory] = 0


def GROW(size):
    global scanned_directories
    global current_directory
    scanned_directories[current_directory] += size

def POP():
    global scanned_directories
    global current_directory
    parent = "/".join(current_directory.split("/")[:-1])
    scanned_directories[parent] += scanned_directories[current_directory]
    current_directory = parent

def FINISH():
    while current_directory != "//":
        POP()

# Now take the puzzle input and convert it into that language
with open("input.txt") as f:
    control = f.read()

# Lines starting in dir aren't needed - they will be CDed into anyway
control = re.sub(r"dir .*\n", "", control)
# Same for ls
control = re.sub(r"\$ ls\n", "", control)

# cd .. becomes POP()
control = re.sub(r"\$ cd ..\n", "POP()\n", control)
# cd x becomes PUSH("x")
control = re.sub(r"\$ cd ([/a-zA-Z\.]+)\n", "PUSH(\"\g<1>\")\n", control)
# ### name becomes GROW(###)
control = re.sub(r"(\d+) ([/a-zA-Z\.]+)", "GROW(\g<1>)", control)

# when done, cd .. all the way up to root
control += "\nFINISH()"

exec(control, {"GROW": GROW, "POP": POP, "PUSH": PUSH, "FINISH": FINISH})
print(sum([value for value in scanned_directories.values() if value <= 100000]))
