#ask the user to enter a sentence using the input() method.
str_manip = input("Please enter a sentence: ")

#Using this string value, write the code to do the following:
# Calculate and display the length of str_manip.
length = len(str_manip)
print("The length of the entered sentence is:", length)

#Find the last letter in str_manip sentence. Replace every occurrence
#of this letter in str_manip with ‘@’
last_letter = str_manip[-1]
str_manip = str_manip.replace(last_letter, '@')
print("The sentence after replacing the last letter is:", str_manip)
