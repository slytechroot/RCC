# Correcting mistake values in a list
odd = [2, 4, 6, 8]
print(odd)

# change the 1st item    
odd[0] = 1            
print(odd)


# change 2nd item in index to 4th items
#formula = index[1] -> index[4]
#the index starts at 0, that's why 1 in result (or index[0])
#in the index remains unchanged, and change happens at index[1]
#or second element/item. 
odd[1:4] = [3, 5, 7]  

print(odd)
