import sys
import re

def removeComments(file):
    """
    Removes all the comments in the file 
    """
    try:
        with open(file, 'r') as script:
            mess_file = script.read()

        clean_file = re.sub(re.compile("/\*.*?\*/"),"" ,mess_file)
        clean_file = re.sub(re.compile("//.*?\n"),"" ,clean_file) 
        clean_file = re.sub(re.compile("<!--.*?-->"),"", clean_file)
        
        with open(file, 'w') as script:
            script.write(clean_file)

    except IOError:
        print("Couldn't open file.")

    except Exception:
        print("Couldn't remove comments")            
    with open(file, 'r') as script:
        mess_file = script.read()
    clean_file = re.sub(re.compile("/\*.*?\*/"),"" ,mess_file) #removes comment with pattern /*...*/
    clean_file = re.sub(re.compile("//.*?\n"),"" ,clean_file) #removes comment with pattern //
    clean_file = re.sub(re.compile("<!--.*?-->"),"", clean_file) #removes comment with pattern <!-- ... -->
    
    with open(file, 'w') as script:
        script.write(clean_file)

def minifier(file):
    """
    Removes all white spaces in the file 
    """

    try:    
        minified =''
        with open(file,'r') as script_file:
            for line in script_file.read():
                for char in line.strip():
                    if not char == ' ':
                        minified += char    

        with open(file,'w') as script_file:
            script_file.write(minified)

    except IOError:
        print("Couldn't open file.")  

    except Exception:
        print("Couldn't minify the file.")                      
        
if __name__ == '__main__':
    try:
        removeComments(sys.argv[1])
        minifier(sys.argv[1])

    except Exception:
        print("Inappropriate arguments")    