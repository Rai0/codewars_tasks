
# this programme mast do:
# dog == dgo -> true
# dog == dfo -> false
# doog == ddog -> false

n1 = ['dog', 'dgo']
n2 = ['dog', 'dfo']
n3 = ['doog', 'ddog']

def is_it_same (one, two) -> bool:
    one = sorted (one)
    two = sorted (two) 
    return one == two

if __name__ == '__main__':
    print (is_it_same (n1[0], n1[1]))
    print (is_it_same (n2[0], n2[1]))
    print (is_it_same (n3[0], n3[1]))