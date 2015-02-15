#!/usr/bin/python

# http://en.wikipedia.org/wiki/Permutation

def generate_permutation(listOfAlphabets):
    # create a lowest permutation
    l = sorted(listOfAlphabets)
    output = []

    output.append("".join(l))

    while True:

        # find largest k such that l[k]<l[k+1], is no k, terminate
        k = -1
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                k = i
        if k == -1:
            return  output
            return
        # find largest i such that l[k] < l[i]
        for i in range(k + 1, len(l)):
            if l[k] < l[i]:
                j = i

        # print(k,j,l[k],l[j])
        # swap l[k] and l[i]
        temp = l[k]
        l[k] = l[j]
        l[j] = temp

        # revert l[k+1:]
        i = k + 1
        j = len(l) - 1
        while i < j:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1
            j -= 1
        output.append("".join(l))

    return output


if __name__ == "__main__":
    print(generate_permutation(['foo', 'bar', 'hhh', 'aaa']))

