def FindRoute(C):
    matriz = encontrar_ruta_aux(C, 0, 0)
    if matriz == []:
        return []
    else: 
        for i in range(0, len(matriz)):
            for j in range (0, len(matriz[0])):
                if matriz[i][j] == 't':
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0
    return matriz

def FindRoute_aux(C, i, j):
    if C[0][1] == 1 and C[1][0] == 1:
            return []
    else:
        if i==len(C)-1:
            if j==len(C)-1:
                return C
            elif C[i][j+1]==0:
                    C[i][j] = 't'
                    return encontrar_ruta_aux(C,i,j+1)
        elif j==len(C[i])-1:
            if C[i+1][j]==0:
                C[i][j] = 't'
                return encontrar_ruta_aux(C,i+1,j)
        elif C[i][j+1]==1 and C[i+1][j]==1:

            if C[i][j-1]=='t':
                C[i][j] = 1
                return encontrar_ruta_aux(C,i,j-1)

            elif C[i-1][j]=='t':
                C[i][j] = 1
                return encontrar_ruta_aux(C,i-1,j)

        else:
            if C[i][j+1]==0:
                C[i][j] = 't'
                return encontrar_ruta_aux(C,i,j+1)

            elif C[i+1][j]==0:
                C[i][j] = 't'
                return encontrar_ruta_aux(C,i+1,j)
