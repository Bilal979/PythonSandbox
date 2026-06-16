
def countPairs(list_str):

    length = len(list_str)
    count = 0
    if(length == 1):
        return count

    for i in range(length):
        x = i+1
        while(x < length):
            a = check(list_str, i, x)
            if(a):
                count += 1

            x += 1

    print(count)


def check(list_str, i, x):
    if (len(list_str[i]) > len(list_str[x])):
        one = list_str[i]
        two = list_str[x]
    else:
        one = list_str[x]
        two = list_str[i]

    if (len(one) == len(two)):
        if (one == two):
            return True
        else:
            return False

    check1 = True
    for j in range(len(two)):
        print(f'{two[j]} in {one} is {two[j] in one}')
        if (two[j] in one):
            continue
        else:
            check1 = False
            break

    if (check1):
        return True
    else:
        return False


list_str = ['ac', 'b', 'aa', 'c', 'bc']
# list_str = ['ac', 'aa']
countPairs(list_str)
