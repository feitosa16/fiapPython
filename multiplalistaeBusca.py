equipamentos = []
valores = []
seriais = []
departamentos = []
resposta="S"
while resposta == "S":
    equipamentos.append(input("Equipamento: ")) #append insere o dado dentro da lista
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for indice in range(0,len(equipamentos)): #len realiza leitura dos valores presentes nos equipanemtneos
    if busca == equipamentos[indice]: #compara se o que foi digitado na busca é equivalente ao equipamento 
        print(" Valor.........: ", valores[indice])
        print(" Serial........: ", seriais[indice])
   