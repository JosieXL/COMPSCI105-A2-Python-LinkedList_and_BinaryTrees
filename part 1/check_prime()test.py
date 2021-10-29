##def is_prime(num):
##    if num >= 2:
##        for y in range(2, num):
##            if num % y == 0:
##                return False
##    
##
##    return True
##
##def largest(num):
##    for i in range(2*num,num,-1):
##        if is_prime(i) == True:
##            print(i)
##            break



#output:
    #19
    #17
    #13
#加了break - output: 19


def largest(num):
    a_list = []
    for i in range(2*num,num,-1):
        for y in range(2, i):
            if not i % y:
                a_list += [i]
                break
    print(a_list)
    p_list = []
    for j in range(2,num):
        if j not in a_list:
            p_list += [j]
    print(p_list)
def main():
    largest(11)

main()
