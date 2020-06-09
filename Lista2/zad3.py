import os
import sys

def rename_files(my_dir):
    files_list = os.listdir(my_dir)

    for f in files_list:
        my_path = os.path.join(my_dir, f)

        if os.path.isdir(my_path):
            rename_files(my_path)
            os.rename(my_path, os.path.join(my_dir, f.lower()))
        else:
            os.rename(my_path, os.path.join(my_dir, f.lower()))



def main():
    try:
        rename_files(sys.argv[1])
    except:
        print('Wrong path.')

if __name__ == '__main__':
    main()