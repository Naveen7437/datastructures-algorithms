# Write a function to generate all possible n pairs of balanced parentheses.

def generateParentheses(num):
    return _generateParentheses(['']*num, num, 0, 0, 0)


def _generateParentheses(string, num, opn, close, pos):

    if close == num/2:
        print(''.join(string))
        return    
    if opn < num/2:
        string[pos] = '{'
        _generateParentheses(string, num, opn+1, close, pos+1)
    
    if opn>close:
        string[pos] = '}'
        _generateParentheses(string, num, opn, close+1, pos+1)
    # return 


if __name__ == "__main__":
    generateParentheses(6)
