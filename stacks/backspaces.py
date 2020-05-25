def remove_backspaces(string):
    """Given a string with '#', treat them as backspace and delete the char to the left.
    e.g., xya#b##c -> xc
    """
    backspace = '#'
    if not string:
        return ''
    stack = []
    top = -1
    i = len(string) - 1
    while i >= 0:
        if string[i] != backspace:
            if top == backspace:
                stack.pop()
            else:
                stack.append(string[i])
        else:
            stack.append(string[i])
        try:
            top = stack[-1]
        except IndexError:
            top = -1
        i -= 1
    result = ''.join(stack[::-1])
    if backspace in result:
        raise ValueError(f'{backspace} in resultant string')
    return result


if __name__ == '__main__':
    print(remove_backspaces(''))
