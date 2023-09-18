lista_numerica = [1,2,3,4,5,6,7,8,9,10]
lista_par = [num for num in lista_numerica if num%2==0]
lista_impar = [num for num in lista_numerica if num%2!=0]

print(f"{lista_par}\n{lista_impar}")