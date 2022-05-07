chegadas = []
contAlunosNaAula = 0
minAlunos = int(input("Digite o mínimo de alunos para a aula."))

while True:
    aluno = input("Digite a chegada do aluno. Para finalizar o fornecimento de informações, "
                      "dê Enter.")
    if aluno is str:
        print("Digite um número, não uma letra.")
    elif aluno == "" or aluno == ' ':
        break
    else:
        chegadas.insert(0,int(aluno))


for i in range(0,len(chegadas)):
    if chegadas[i] <= 0:
        contAlunosNaAula += 1

if contAlunosNaAula >= minAlunos:
    print("Aula Normal.")
else:
    print("Aula Cancelada.")