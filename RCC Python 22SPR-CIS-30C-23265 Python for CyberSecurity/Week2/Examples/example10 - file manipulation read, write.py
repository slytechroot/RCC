#Example 10: open, write string to file, test.txt, and close file.

def main():
    with open('test.txt', 'w') as file:
        file.write("this is a test file")

if __name__ == '__main__':
    main()

