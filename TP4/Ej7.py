# 8. Dada una lista de temperaturas en grados celsius generar una nueva lista con las temperaturas expresadas en grados fahrenheit, la fórmula para convertir la temperatura es `°F=(°C*(9/5))+32`.

listaDegree=[15,3,45,25,12,13,16,14,24,25,26,29,28,30]

def transformar (numero):
    return (numero*(9/5))+32

listaFahreinheit=list(map(transformar,listaDegree))

print(listaFahreinheit)