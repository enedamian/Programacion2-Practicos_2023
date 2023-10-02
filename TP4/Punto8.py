"""8. Dada una lista de temperaturas en grados celsius generar una nueva lista 
con las temperaturas expresadas en grados fahrenheit, 
la fórmula para convertir la temperatura es `°F=(°C*(9/5))+32`.
"""
celsius = [0, 22.5, 40, 100]
fahrenheit = list(map(lambda temp: (temp * 9/5) + 32, celsius))
print (fahrenheit)