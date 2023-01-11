from os.path import dirname, join, basename
import re
import traceback

def process_base64(f, line):
    if line == "\n":
        f.write(line)
        return
    length = len(line) - 1 # ignore '\n'
    if length < 4:
        line = line.rstrip("\n") + "a"*(4-length) + "\n"
        f.write(line)
    elif length <= 76:
        if length % 4 != 0:
            line = line.rstrip("\n") + "a"*(length//4+1)*4 + "\n"
        f.write(line)
    else:
        f.write(line[-77:])
        process_base64(f, line[:-77] + "\n")

def modify_file(file_path):
    try:
        f = open(file=file_path, mode="r")
        backup_f = open(file=join(dirname(file_path), basename(file_path) + ".bak"), mode="a+")
        rule1 = re.compile("boundary=\"(.*)\"")
        rule2 = re.compile("--(.*)")
        rule3 = re.compile("--(.*)--")
        boundary_set = set()
        stack = []
        in_base64 = False
        for line in f:
            match1 = rule1.search(line)
            if match1:
                backup_f.write(line)
                boundary = match1.group(1)
                boundary_set.add(boundary)
            elif rule2.search(line):
                backup_f.write(line)
                match2 = rule2.search(line)
                if match2.group(1) in boundary_set:
                    in_base64 = False
                    boundary = match2.group(1)
                    if not stack or stack[-1] != boundary:
                        stack.append(boundary)
            elif rule3.search(line):
                backup_f.write(line)
                match3 = rule3.search(line)
                if match3.group(1) in boundary_set:
                    if not stack and stack[-1] == boundary:
                        boundary = match3.group(1)
                        boundary_set.remove(boundary)
                        stack.pop()
                else:
                    raise SystemExit("boudary end error")
            elif line == "Content-Transfer-Encoding: base64\n":
                in_base64 = True
                backup_f.write(line)
            elif in_base64:
                process_base64(backup_f, line)
            else:
                backup_f.write(line)
    except Exception as e:
        traceback.print_exc()
    finally:
        f.close()
        backup_f.close()


if __name__ == "__main__":
    modify_file(r"C:\Users\mengchen\src\pydemo\yzy\test1.txt")