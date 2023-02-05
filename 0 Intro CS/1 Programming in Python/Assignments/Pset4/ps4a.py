# vscode my beloved
try:
    import os
    os.system("cls")
    os.chdir("0 Intro CS/1 Programming in Python/Assignments/Pset4")
except:
    pass


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

    # https://github.com/andyshen55/MITx6.0001/blob/c8e17bbd6ae3113cff135557efd9054eb674e586/ps4/ps4a.py

    seqlen = len(sequence)

    # base case
    if seqlen == 1:
        return sequence

    # recursive case
    res = []
    for letter in sequence:
        permutations = get_permutations(sequence.replace(letter, ""))
        for perm in permutations:
            res += [letter + perm]

    return res
    # understand this shit before doing ps4b


if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    seq = 'abc'
    print('Input:', seq)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    permutations = get_permutations(seq)
    print(f" Actual Output : {permutations}\n")

    seq = '123'
    print('Input:', seq)
    print('Expected Output:', ['123', '132', '213', '231', '312', '321'])
    permutations = get_permutations(seq)
    print(f" Actual Output : {permutations}\n")

    seq = 'def'
    print('Input:', seq)
    print('Expected Output:', ['def', 'dfe', 'edf', 'efd', 'fde', 'fed'])
    permutations = get_permutations(seq)
    print(f" Actual Output : {permutations}\n")
