import os
import sys
import hashlib


def prepare_files(my_dir):
    data_list = []
    for root, dirs, files in os.walk(my_dir):
        for f in files:
            content = ''
            f_path = os.path.join(root, f)
            #with open(f_path, 'rb') as my_f:
            #    content = my_f.read()
            f_size = os.stat(f_path).st_size
            f_hash = hash_content(f_path)
            # f_hash = hashlib.md5(content.encode()).hexdigest()
            data_list.append(tuple((f_path, f_size, f_hash)))
    return data_list

def hash_content(path):
    f_hash = hashlib.md5()
    size = 65536

    with open(path, 'rb') as file:
        content = file.read(size)
        while len(content) > 0:
            f_hash.update(content)
            content = file.read(size)
    
    return f_hash.hexdigest()

def compare(data):
    copy_list = []
    for path1, size1, file_hash1 in data:
        for path2, size2, file_hash2 in data:
            if(path1 != path2):
                if(size1 == size2 and file_hash1 == file_hash2):
                    if(path1 not in copy_list or path2 not in copy_list):
                        print(path1)
                        print(path2)
                        print('------------------')
                        copy_list.append(path1)
                        copy_list.append(path2)
    return copy_list

def main():
    to_comapre = prepare_files(sys.argv[1])
    compare(to_comapre)
    
if __name__ == '__main__':
    main()