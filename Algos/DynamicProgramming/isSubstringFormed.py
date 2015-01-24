#!/usr/bin/python

#http://www.geeksforgeeks.org/find-given-string-can-represented-substring-iterating-substring-n-times/




def is_substr_formed(string):
	dpTable = [None] * len(string)
	
	subStringLen = 1
	subStringCursor = 0
	for currCursor in range(1, len(string)):
		if string[currCursor] == string[subStringCursor]:
			subStringCursor += 1
		else:
			subStringLen += 1
			subStringCursor = 0
	
		if subStringCursor == subStringLen:
			subStringCursor = 0
	
	if subStringCursor == 0:
		print(string+" ,Found substring: "+string[0:subStringLen])
	else:
		print("No substring found")




if __name__ == "__main__":
	is_substr_formed("abcabcabc")
	is_substr_formed("abadabad")
	is_substr_formed("aabaabaabaab")
	is_substr_formed("abcdabc")

		

