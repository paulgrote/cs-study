# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # base case: if the input is a single character
    if len(sequence) == 1:
        return [sequence]
    else:
        # split the string into two variables: the first character, then the rest
        first_char = sequence[0] # <--this line might be unnecessary. recursion on subsequence might provide this value.
        print(first_char)
        subsequence = sequence[1:]
        print(subsequence)
        # return subsequence + reversed subsequence
        # permutations = permutate(subsequence) # <--might not be necessary
        subsequence = get_permutations(subsequence) + [first_char]
        print(subsequence)

        for i in range[len(subsequence)]:
            subsequence[i] = subsequence[i] + first_char

        return [subsequence]
    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    print('Input:', 'a')
    print('Expected Output:',['a'])
    print('Actual Output:', get_permutations('a'),'\n')

    print('Input:', 'ab')
    print('Expected Output:',['ab','ba'])
    print('Actual Output:', get_permutations('ab'),'\n')

    print('Input:', 'abc')
    print('Expected Output:',['abc','bac','bca','acb','cab','cba'])
    print('Actual Output:', get_permutations('abc'))