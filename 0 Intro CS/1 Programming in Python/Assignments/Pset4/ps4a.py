# Problem Set 4A
# Name: kyaruwo
# Collaborators: me
# Time Spent: 2023/02/03 - 2023/??/??

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
    seqlen = len(sequence)

    # pain


if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    from os import system as sys
    sys("cls")

    seq = 'abc'
    print('Input:', seq)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    permutations = get_permutations(seq)
    print(f" Actual Output : {permutations}\n")

    seq = 'xyz'
    print('Input:', seq)
    print('Expected Output:', ['xyz', 'xzy', 'yxz', 'zxy', 'yzx', 'zxy'])
    permutations = get_permutations(seq)
    print(f" Actual Output : {permutations}\n")

    seq = 'def'
    print('Input:', seq)
    print('Expected Output:', ['def', 'dfe', 'edf', 'fde', 'efd', 'fed'])
    permutations = get_permutations(seq)
    print(f" Actual Output : {permutations}\n")
