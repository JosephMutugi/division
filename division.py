# where a is the divisor
# where b is the divider



def divide(a, b):
    # initialice the quotient to zero
    quotient = 0
    #the logical arguments
    if b == 0:
        return("cannot divide by zero")
    elif a == b:
        return(1, 0)
    elif b > a:
        return(0, a)

    else:
        quotient = (quotient + 1)
        a = (a-b)
    return(quotient, a)




