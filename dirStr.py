import os
import sys
import re

def main():
    dirFile = sys.argv[1] # path/file with dir structure
     # root path, default is current directory
    path_stack = ["."]
    if len(sys.argv) > 1:
        path_stack = ["./" + sys.argv[2]]

    lines = open(dirFile, 'r').readlines()

    for line in lines:
        # remove all whitesapce characters after the name
        # line = re.sub(r"[^\w\s]", " ", line).rstrip() 
        
        line = line.rstrip() # remove all whitesapce characters after the name
    
        # for root dir, with a name and no extra whitespace
        if len(line) == len(line.strip()):
            if len(line) < 1:
                continue
            path_stack = path_stack[:1] # reset the stack to the root dir
            path_stack.append(line.strip())     
        else: # for child dir, with potential whitespace
            depth_level = (len(line) - len(line.strip())) // 4
            if depth_level < len(path_stack) - 1:
                path_stack = path_stack[:depth_level + 1]
            path_stack.append(line.strip())
           
        if "." not in line:
            os.makedirs("/".join(path_stack), exist_ok=True)
        else:
            open("/".join(path_stack), 'w').close()
            
if __name__ == '__main__':
    main()
