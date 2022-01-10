def replace(s, target, repl):
    n = len(target)
    if len(s) < n or n == 0:
        return s
    elif s[0:n] == target:
        return 	repl + replace(s[n:], '', repl)
    else:
        return s[0] + replace(s[1:], target, repl)

s = 'CISC 121, CISC 124, CISC 235'
t = replace(s, 'CISC', 'MATH')        # t is 'MATH 121, CISC 124, CISC 235'
print(t)