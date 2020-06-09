import sys

def read_file_content(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def size_sum(content):
    to_sum = [
        int(word[len(row.split()) - 1]) 
        for row in content.split('\n') 
        for word in [row.split()]
    ]
    return sum(to_sum)
    

def main():
    print(size_sum(read_file_content(sys.argv[1])[:-1]))
if __name__ == "__main__":
    main()