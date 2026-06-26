#Save the sentence: "The!quick!brown!fox!jumps!over!the!lazy!dog." as a single string.
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
#Reprint this sentence as "The quick brown fox jumps over the lazy dog." using the replace()function to replace every "!" exclamation mark with a blank space.
sentence_replace = sentence.replace("!", " ")
print(sentence_replace)

#Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZYDOG.” using the upper() function.
sentence_upper = sentence_replace.upper()
print(sentence_upper)

#Print the sentence in reverse order using slicing.
sentence_reverse = sentence_replace[::-1]
print(sentence_reverse)