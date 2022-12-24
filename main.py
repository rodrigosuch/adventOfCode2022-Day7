from dir import Directory
import re
import bisect


INPUT_FILE = "input.txt"

root = Directory("/")
folder = root
current_folder = "/"
size_list = []

def get_total_size(directory):
    total_size = 0
    total_size += directory.files_size
    for dir in directory.dir:
        total_size += get_total_size(dir)
        bisect.insort(size_list, get_total_size(dir))

    return total_size


def process_cmd(line):
    global folder
    split = re.split(" |\n", line)
    if split[1] == "cd" and split[2] == "..":
        folder = folder.go_back()
    elif split[1] == "cd":
        current_folder = split[2]
        new = folder.goto_dir(current_folder)
        if new != None:
            folder = new

def process_ls(line):
    split = re.split(" |\n", line)
    if split[0].isnumeric():
        folder.add_file(int(split[0]))
    elif split[0] == "dir":
        folder.add_dir(split[1])

with open(INPUT_FILE) as file:
    line = file.readline()
    line = file.readline()
    while line != "":
        if line[0] == "$":
            process_cmd(line)
        else:
            process_ls(line)
        #print(root.print_dirs())
        line = file.readline()

num = 0
print(f"Need to release {30000000- (70000000-root.get_total_size())} bytes")

print(root.total_result)
get_total_size(root)
print(size_list)

for item in size_list:
    if item >= 30000000 - (70000000-root.get_total_size()):
        print(f"Will remove item: {item}")
        break