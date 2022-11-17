# Lê o arquivo inteiro
def read_file():
    with open('readme.txt') as f:
        file = f.read()
    f.close()
    return file


# Lê somente uma linha
def read_line_file():
    with open('readme.txt') as file:
        line = file.readline()
    file.close()
    return line


# Lê o arquivo inteiro quebrando em uma tupla
def read_lines_file():
    with open('readme.txt') as file:
        lines = file.readlines()
    file.close()
    return lines


if __name__ == '__main__':
    print('### Read File ####')
    print(read_file())
    print('### Read Line ####')
    print(read_line_file())
    print('### Read Lines ####')
    print(read_lines_file())
