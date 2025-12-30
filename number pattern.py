
def number_pattern(n):
    if (isinstance(n, int) != True):
        return "Argument must be an integer value."
    elif (n < 1):
        return "Argument must be an integer greater than 0."
    numbers = [str(i) for i in range(1,1+n)]
    return " ".join(numbers)

print(number_pattern(4))
print(number_pattern(12))

