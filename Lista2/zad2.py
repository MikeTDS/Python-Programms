import sys


def encode_file(file_name):
    tablica = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base_64 = list(tablica)
    iterator = 0
    code = ''
    with open(file_name, 'rb') as file:
        cur_byte = 1
        while cur_byte:
            if iterator % 4 == 0:
                cur_byte = file.read(1)
                if not cur_byte:
                    break
                handler = (int.from_bytes(cur_byte, 'big') & 0b11111100) >> 2
                code += base_64[handler]
            
            elif iterator % 4 == 1:
                handler = (int.from_bytes(cur_byte, 'big') & 0b00000011) << 4
                cur_byte = file.read(1)
                if not cur_byte:
                    break
                handler += (int.from_bytes(cur_byte, 'big') & 0b11110000) >> 4
                code += base_64[handler]

            elif iterator % 4 == 2:
                handler = (int.from_bytes(cur_byte, 'big') & 0b00001111) << 2
                cur_byte = file.read(1)
                if not cur_byte:
                    break
                handler += (int.from_bytes(cur_byte, 'big') & 0b11000000) >> 6
                code += base_64[handler]

            elif iterator % 4 == 3:
                handler = (int.from_bytes(cur_byte, 'big') & 0b00111111)
                code += base_64[handler]

            iterator += 1

        # if iterator % 4 != 0:
        #     code += base_64[handler]
    return code
def find_id(cur_byte):
    to_find = cur_byte.decode('ascii')
    tablica = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base_64 = list(tablica)
    for i in range(len(base_64)):
        if base_64[i] == to_find:
            return i

def decode_file(file_name):
    iterator = 0
    message = ''
    with open(file_name, 'rb') as file:
        cur_byte = 1
        while cur_byte:
            if iterator % 3 == 0:
                cur_byte = file.read(1)
                index = find_id(cur_byte)
                if not cur_byte:
                    break
                handler = (index & 0b00111111) << 2
                
                cur_byte = file.read(1)
                index = find_id(cur_byte)
                if not cur_byte:
                    break
                handler += (index & 0b00110000) >> 4
                message += chr(handler)

            elif iterator % 3 == 1:
                handler = (index & 0b00001111) << 4
                cur_byte = file.read(1)
                index = find_id(cur_byte)
                if not cur_byte:
                    break
                handler += (index & 0b00111100) >> 2
                message += chr(handler)

            elif iterator % 3 == 2:
                handler = (index & 0b00000011) << 6
                cur_byte = file.read(1)
                index = find_id(cur_byte)
                if not cur_byte:
                    break
                handler += (index & 0b00111111)
                message += chr(handler)
            iterator += 1

    return message

def save_to_file(filename, message):
    with open(filename, 'w+') as file:
        file.write(message)

def read_input():
    if sys.argv[1] == '--encode':
        code = encode_file(sys.argv[2])
        print(code)
        save_to_file(sys.argv[3], code)
    elif sys.argv[1] == '--decode':
        message = decode_file(sys.argv[2])
        print(message)
        save_to_file(sys.argv[3], message)
def main():
    read_input()

if __name__ == '__main__':
    main()