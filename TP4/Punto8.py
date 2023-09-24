""" Dada una lista de temperaturas en grados celsius generar una nueva
lista con las temperaturas expresadas en grados fahrenheit,
la fórmula para convertir la temperatura es `°F=(°C*(9/5))+32`. """

#°F = (°C * 9/5) + 32

t_celsius = [15.5, 22.0, 30.3, 10.8, 5.2, 25.7]

fahrenheit = list(map(lambda c: "{:.1f}".format((c * 9/5) + 32), t_celsius))

print(fahrenheit)

""" 
temperaturas_fahrenheit = [(celsius * 9/5) + 32 for celsius in t_celsius]

print(temperaturas_fahrenheit) """