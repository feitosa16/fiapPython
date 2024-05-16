#inventário
inventario=[]
resposta="S"
while resposta == "S":
    inventario.append(input("Equipamento: ")) #append insere o dado dentro da lista
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Numero serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()
    
for elemento in inventario:
    print(elemento)