def is_paired(input_string):
    pairs = []
    for c in input_string:
        if not is_valid(c):
            continue
        print(c)            
        if is_match(pairs, c):
            pairs.pop(-1)
        else:
            pairs.append(c)
    return len(pairs) == 0
                
        
def is_valid(char):
    return char in '([{}])'
def is_match(string, char):
    if len(string) == 0:
        return False
    if (string[-1] == '(' and char == ')') or \
       (string[-1] == '{' and char == '}') or \
       (string[-1] == '[' and char == ']'):
        return True
    return False
