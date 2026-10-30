#Estrutura de decisão - Escreva um algoritmo que tenha a entrada de um nome e de 3 provas (prova1, prova2 e prova3).
#Esse algoritmo deve calcular a média entre as provas e verificar a situação do aluno quando:
#média >= 7 aprovado média >= 5 recuperação média < 5 reprovado
print("Escola Senac\n")
nome = input("Digite seu nome: ").title()
prova1 = float(input("Digite a nota da prova 1: ").replace(",","."))
prova2 = float(input("Digite a nota da prova 2: ").replace(",","."))
prova3 = float(input("Digite a nota da prova 3: ").replace(",","."))
media = (prova1 + prova2 + prova3)/3
if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperação"
else:
    situacao = "reprovado"
print("\nResutado:\n")  
print(f"Nome: {nome}")
print(f"Prova 1: {prova1:.1f}".replace(".",","))
print(f"Prova 2: {prova2:.1f}".replace(".",","))
print(f"Prova 3: {prova3:.1f}".replace(".",","))
print(f"Média: {media:.1f}".replace(".",","))
print(f"Situação: {situacao.upper()}")
