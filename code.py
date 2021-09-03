lowercase = input("Enter a word in all lowercase: ")
uppercase = ""


'''
at this point in the code, it is essential to find the end result of subtracting the uppercase from the lowecase value - use B and b as an example.
'''

difference = ord('B') - ord('b')

for i in range(0, len(lowercase)):
  letter = lowercase[i]
  uppercase += chr(ord(letter) + difference)
  

print("The word in all uppercase is: " + uppercase)
