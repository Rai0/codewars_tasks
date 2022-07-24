N = [[37, 68], [52, 74], [119, 146], [37, 65], [46, 74]]
right_N = [[37, 74], [119, 146]]
right_anser = 86
A = 15
B = 165

def get_N (N):
    i = 1
    while i < 10:
        if i < len (N):
            N = sorted (N)
            if N[i][0] <= N[i - 1][1]:
                N.append ([N[i - 1][0], N[i][1]])
                N.pop (i)
                N.pop (i - 1)
                i = 1
                continue
        else:
            return N
        i += 1

if __name__ == '__main__':
    corect_N = get_N (N)
    summ_N = 0
    if corect_N == right_N: 
        print ('True')
    for i in corect_N:
        summ_N += i[1] - i[0]
    print (B - A - summ_N)