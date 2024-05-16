nome = input ("Digite o nome: ")
idade= int(input("Digite a idade: "))
doencaInfectocontagiosa = input("Suspeita de doença infectocontagiosa? "). upper()
if idade >= 65: #utilizar bem as identações principalmente por não utilizar parenteses e representar a hierarquia do programa
    print ("O paciente " + nome + " possui atendimento prioritário!")
elif doencaInfectocontagiosa == "SIM": 
    print("O paciente " + nome + " deve ser direcionado para a sala de espera reservada")
else: 
    print("O paciente " + nome + "NÃO possui atendimento prioritário")

#hierarquia do mesmo nivel que if e else o que faz aparece na impressão em ambos os casos
print("FIM")