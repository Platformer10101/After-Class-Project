x = int(input("Enter the number of terms"))

def recur_sequence(n):
    if n in {0,1}:
        return n
    return recur_sequence(n-1) + recur_sequence(n-2)


print([recur_sequence(n) for n in range(x)])