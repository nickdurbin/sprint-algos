'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # We need to create a variable that stores the count
    # going to call this counter
    # intial value will be 0
    counter = 0

    # First base case will be to check the length of the input/word
    # If the word is shorter than 2m then simply return counter
    # Because 'th' will not exist
    if len(word) < 2:
        return counter

    # Another base case to recruse back to in order to stop the function call.
    # meaning the stack will eventually end.
    # Our initial case should be to check if 'th' exists
    # If not, then simply return 0
    if 'th' not in word:
        return counter

    # Here is where we will do our recrusion.
    # We reach here if 'th' exists 
    # We add 1 to our counter and also continue to check by calling our function again.
    # So, we call count_th and pass in the remaining word
    else:
        # Here we take the counter and add the new number of 'th'
        # found in the word passed
        counter = counter + 1

        # Then we add the count and recursively run the function again
        # The function takes one argument, which we want to pass
        # The new string minus the 'th' we found
        # Going to try using the replace method to remove the 'th'
        # Found and set it to an empty string, then run 1 time
        # As the third parameter. 
        # Resource: https://www.geeksforgeeks.org/python-string-replace/?ref=lbp
        counter + count_th(word.replace('th',' ', 1))
    
        return counter
