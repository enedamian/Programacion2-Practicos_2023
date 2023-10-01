""" Dada una lista de temperaturas en grados celsius generar una nueva
lista con las temperaturas expresadas en grados fahrenheit,
la fórmula para convertir la temperatura es `°F=(°C*(9/5))+32`. """
grados_celsius = [37.5 , 23.4 , 12.6 , 100.0 , 18.3]

grados_F= list(map(lambda x: "{:.1f}".format((x * 9/5) + 32), grados_celsius))
print(grados_F)
