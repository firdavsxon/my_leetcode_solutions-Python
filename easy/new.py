def commonPrefix(inputs):
    inputs_list = [i for i in inputs]
    inputs_list = inputs_list[::-1]
    leave_suffix = []
    length = 0
    length += len(inputs)
    for i in range(len(inputs)):
        leave_suffix.append(inputs_list.pop())
        comparing_length = len(leave_suffix)
        if inputs_list[-comparing_length:] == leave_suffix[::-1]:
            length += comparing_length
    return length


print(commonPrefix('abcabcd'))
""" 
''    'ababaa'   6
'a'   'babaa'    0
'ab'   'abaa'    2
'aba'   'baa'    0
'abab'   'aa'    0
'ababa'   'a'    0
'ababaa'   ''    0
8
"""

""" 
''    'abcabcd'   7
'a'   'bcabcd'    0
'ab'   'cabcd'    0
'abc'   'abcd'    3
'abca'   'bcd'    0
'abcab'   'cd'    0
'abcabcd'  'd'    0
'abcabcd'   ''    0
10
"""