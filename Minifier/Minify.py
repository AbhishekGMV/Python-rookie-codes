import sys
def minifier():
    minified =''
    with open(sys.argv[1],'r') as script_file:
        for line in script_file.read():
            for char in line.strip():
                if char == ' ':
                    continue
                minified += char    

    with open(sys.argv[1],'w') as script_file:
        script_file.write(minified)            
        
if __name__ == '__main__':
    minifier()