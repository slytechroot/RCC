#file I/O
def MainRead():
    f = open('myfiles.txt', 'r')
    for line in f:
        #strip the characters \n \r
        print(line.strip('\n\r'))
    f.close()

def MainWrite():
    f = open('myfiles.txt', 'w')
    for word in range(4):
        f.write(input('Enter a word: ') + '\n')
    f.close()

if __name__ == "__main__":
    #MainRead()
    MainWrite()


