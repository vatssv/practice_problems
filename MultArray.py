def main():
    A = [12, 3, 5, 7, 13, 12]
    R_even, R_odd = A[0], A[1]
    for i in range(2, len(A), 2):
        if i % 4 == 0:
            R_even += A[i]
            # print('Adding ', A[i])
        elif i % 2 == 0:
            R_even *= A[i]
            # print('Mult ', A[i])
        else:
            continue
    R_even = R_even % 2

    for i in range(3, len(A), 4):
        if (i-1) % 4 == 0:
            R_odd += A[i]
            # print('Adding ', A[i])
        elif (i-1) % 2 == 0:
            R_odd *= A[i]
            # print('Mult ', A[i])
        else:
            continue
    R_odd = R_odd % 2
    if R_odd > R_even:
        print('ODD')
    elif R_even > R_odd:
        print('EVEN')
    else:
        print('NEUTRAL')

if __name__=="__main__":
    main()