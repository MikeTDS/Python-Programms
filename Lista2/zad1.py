import sys
import os

def read_file(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
    except:
        print('Could not load file stats.')
        exit(1)
    return content

def display_stats(content):
    size = words = lines = max_line = 0
    
    try:
        size = os.stat(sys.argv[1]).st_size
    except:
        print('Could not load size.')

    lines = content.count('\n') + 1
    words = len(content.split())
    temp_lines = content.split('\n')
    sorted_lines = sorted(temp_lines, key=len)
    print('Size: ' + str(size) + ' bytes')    
    print('Lines: ' + str(lines))
    print('Words: ' + str(words))
    print('Longest line: ' + str(len(sorted_lines[-1])))

def main():
    try:
        file = read_file(sys.argv[1])
    except:
        print('No file was found.')
        exit(1)
    display_stats(file)

if __name__ == '__main__':
    main()