
from pprint import pprint

def make_block(filename, dirname, size):
    return {"fname": filename, "dname": dirname, "size": size}


RESULT = {}

def get_folder_dict(cwd: list):
    return "/".join(cwd)

def get_file_sizes(files, dire):
    if not dire in RESULT:
        RESULT[dire] = 0
    # print(dire)
    for f in files[dire]:
        if f["fname"]:
            RESULT[dire] += f["size"]
        else:
            get_file_sizes(files, f["dname"])
            RESULT[dire] += RESULT[f["dname"]]


with open("data/7", 'r') as file:
# with open("data/wdwd", 'r') as file:
    files = {}
    cwd = []
    datacode = file.read().split('\n')
    i = 0
    while i < len(datacode):
        line = datacode[i]
        b = line.split()
        if b[0] == "$":
            # print(line)
            if b[1] == "ls":
                # list out directory until no longer number first
                i += 1
                # output all files in directory
                dirn = get_folder_dict(cwd)
                files[dirn] = []
                cwdl = files[dirn]
                print(cwdl)
                while i < len(datacode) and ((ll:=datacode[i].split())[0] != "$"):
                    if ll[0] == 'dir':
                        # dir
                        cwdl.append(make_block(None, dirn+"/"+ll[1], 0))
                    elif ll[0].isdigit():
                        # file
                        cwdl.append(make_block(dirn+"/"+ll[1], 0, int(ll[0])))
                    i += 1
                i -= 1
                # print(files)
            elif b[1] == "cd":
                # print(b)
                if b[2] == "..":
                    cwd.pop()
                elif b[2] == "/":
                    cwd = ["/"]
                else:
                    cwd.append(b[2])
                # print(cwd)
        i += 1
    # print(i, len(datacode))

    get_file_sizes(files, '/')
    pprint(RESULT)
    # directories = [(xi, xj) for xi, xj in RESULT.items()]
    directories = list(RESULT.values())
    print(directories)

HAVE = 70000000 - RESULT["/"]
NEED = 30000000 - HAVE
directories.sort()

print(NEED, directories)

for i in directories:
    if i >= NEED:
        print(i)
        break
