# replace string pi with value 3.14
def replace_pi(n):
    if len(n) == 0 or len(n) == 1:
        return n
    # base case done
    if n[0] == 'p' and n[1] == 'i':
        output = replace_pi(n[2:])
        return ' 3.14 ' + output
    else:
        output = replace_pi(n[1:])
        return n[0] + output


print(replace_pi("abcpidefpipippi"))
