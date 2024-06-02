def knapsack(tamanioMochila, volumenObjetos, beneficiosObjetos):
    tabla = [[0] * (tamanioMochila + 1) for _ in range(len(volumenObjetos) + 1)]
    # for i in range(tamanioMochila + 1):
    #     for j in range(volumenObjetos + 1):
    #         tabla[i][j] = 0

    for i in range(1, tamanioMochila + 1):
        for j in range(1, len(volumenObjetos) + 1):
            if volumenObjetos[i - 1] <= j:
                tabla[i][j] = max(tabla[i-1][j], beneficiosObjetos[i - 1] + tabla[i-1][j - volumenObjetos[i - 1]])
            else:
                tabla[i][j] = max(tabla[i-1][j], tabla[i][j-1])

    for i in range(tamanioMochila + 1):
        print(tabla[i])

tamanioMochila = 8
volumenObjetos = [1, 2, 3, 4, 5, 6, 7, 8]
beneficiosObjetos = [2, 5, 10, 15, 20, 25, 30, 35]
knapsack(tamanioMochila, volumenObjetos, beneficiosObjetos)





