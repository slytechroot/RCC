#file I/O 2
def Main():
    words = ['cat','sat','bat','map']
    
    with open('myfiles.txt','w') as f:
        for word in words:
            f.write(word + '\n')
            
if __name__ == "__main__":
    Main()
    


