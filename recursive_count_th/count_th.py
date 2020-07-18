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
    rest_of_word = word[len('th')-1:]

    # First base case will be to check the length of the input/word
    # If the word is shorter than 2m then simply return counter
    # Because 'th' will not exist
    if len(word) < 2:
        return counter

    # Another base case to recruse back to in order to stop the function call.
    # meaning the stack will eventually end.
    # Our initial case should be to check if 'th' exists
    # If not, then simply return 0
    elif 'th' is not in word:
        return counter

    # Here is where we will do our recrusion.
    # We reach here if 'th' exists 
    # We add 1 to our counter and also continue to check by calling our function again.
    # So, we call count_th and pass in the remaining word
    else: 
        (counter += 1) + count_th(word, rest)
    
        return counter
