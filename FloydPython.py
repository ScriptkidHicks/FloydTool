"""
This program is so that I don't have to manually do
a floyd warshal demonstration on every bloody step
of the mat.
"""
INF = None

def one_stop_gas(mat, n):
    tank = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                temp = max(mat[i][k], mat[k][j])
                if temp > tank:
                    tank = temp
    return tank


def printmat(mat: list):
    for sublist in mat:
        for element in sublist:
            if element is INF:
                print(f"{'INF': ^4}", end='')
            else:
                print(f"{element: ^4}", end='')
        print("")
    print("\n")


def floyd_warsh(mat: list, n: int):

    printmat(mat)
    tank = 0

    for a in range(n):
        for b in range(n):
            for c in range(n):
                if (mat[b][a] is INF) or (mat[a][c] is INF):
                    pass
                elif mat[b][c] is INF:
                    mat[b][c] = mat[b][a] + mat[a][c]
                    temp = max(mat[b][a], mat[a][c])
                    if temp > tank:
                        tank = temp
                elif mat[b][c] > mat[b][a] + mat[a][c]:
                    mat[b][c] = mat[b][a] + mat[a][c]
                    temp = max(mat[b][a], mat[a][c])
                    if temp > tank:
                        tank = temp
        print(f" ({a+1})")
        print("D")
        printmat(mat)

    print(f"The necessary tank size is {tank}")


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
