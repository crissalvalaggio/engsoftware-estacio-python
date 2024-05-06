#coloquei algumas coisas a mais no código como por ex: não aceita caracteres vazios nos campos, impede que seja informado valores altos na idade e colocando um limite de idade para ser informado, etc..  =D

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = self.calcular_media()
        return "Aprovado" if media >= 7 else "Reprovado"

class SistemaCadastroAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self):
        while True:
            nome = input("Digite o nome do aluno: ").strip()
            if nome.replace(" ", "").isalpha():
                break
            print("Nome não pode estar vazio ou usar números.")
        
        while True:
            try:
                idade = int(input("Digite a idade do aluno: "))
                if 1<= idade <= 90:
                    break
                else:
                    print("Idade deve estar entre 1 e 90 anos.")
            except ValueError:
                print("Idade deve ser um número inteiro")
    

        notas = []
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i + 1}: "))
                    notas.append(nota)
                    break
                except ValueError:
                    print("Nota deve ser um número.")
        
        aluno = Aluno(nome, idade, notas)
        self.alunos.append(aluno)
        print("Aluno adicionado com sucesso!")

    def listar_alunos(self):
        for aluno in self.alunos:
            media = aluno.calcular_media()
            situacao = aluno.verificar_situacao()
            print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Média: {media}, Situação: {situacao}")

    def buscar_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                return aluno
        return None

    def remover_aluno(self, nome):
        aluno = self.buscar_aluno(nome)
        if aluno:
            self.alunos.remove(aluno)
            print(f"Aluno {nome} removido com sucesso!")
        else:
            print(f"Aluno {nome} não encontrado.")

# Exemplo de uso:
sistema = SistemaCadastroAlunos()

while True:
    opcao = input("Escolha uma opção:\n1. Adicionar aluno\n2. Listar alunos\n3. Remover aluno\n4. Finalizar\n")
    
    if opcao == "1":
        sistema.adicionar_aluno()
    elif opcao == "2":
        print("\nLista de Alunos:")
        sistema.listar_alunos()
    elif opcao == "3":
        nome_aluno = input("Digite o nome do aluno que deseja remover: ").strip()
        if nome_aluno:
            sistema.remover_aluno(nome_aluno)
        else:
            print("Nome não pode estar vazio.")
    elif opcao == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
