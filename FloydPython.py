"""
This program is so that I don't have to manually do
a floyd warshal demonstration on every bloody step
of the mat.
"""
INF = 1000000

def printmat(mat: list):
    for sublist in mat:
        print(sublist)
    print("\n\n")


def floyd_warsh(mat: list, n: int):

    printmat(mat)

    for a in range(n):
        for b in range(n):
            for c in range(n):
                if (mat[b][a] == INF) or (mat[a][c] is INF):
                    pass
                elif mat[b][c] > mat[b][a] + mat[a][c]:
                    mat[b][c] = mat[b][a] + mat[a][c]
        printmat(mat)

if __name__ == '__main__':
    val = None
    while not val:
        try:
            val = int(input("Please enter the size of the mat: "))
        except:
            print("Oops, that's not a number!")

    mat = []
    for a in range(val):
        mat.append([])
        for b in range(val):
            mat[a].append(None)


    print("Fill the mat by row now.")
    for a in range(val):
        for b in range(val):
            inval = 'oops'
            while inval == 'oops':
                try:
                    inval = input("Please enter a number or INF: ").lower()
                    if inval == 'inf':
                        inval = INF
                    else:
                        inval = int(inval)
                    mat[a][b] = inval

                except:
                    print("oops, that's not a number or None")
    floyd_warsh(mat, val)