def MultiplicarEntreSi(A, B):
    C = [A[i]*B[i] for i in range(len(A))]
    return C

listaA = [1, 2, 3, 4, 5]
listaB = [1, 2, 3, 4, 5]

print(MultiplicarEntreSi(listaA, listaB))
