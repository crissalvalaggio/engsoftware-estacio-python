class Lista:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append({"tarefa": tarefa, "marcada": False})
        print("Tarefa adicionada com sucesso!")

    def marcar(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["marcada"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Índice de tarefa inválido.")

    def remover(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa_removida = self.tarefas.pop(indice)
            print(f"Tarefa removida: {tarefa_removida['tarefa']}")
        else:
            print("Índice de tarefa inválido.")

    def exibir(self):
        if self.tarefas:
            print("Lista de Tarefas:")
            for i, tarefa in enumerate(self.tarefas, start=1):
                marcada = "X" if tarefa["marcada"] else " "
                print(f"{i}. [{marcada}] {tarefa['tarefa']}")
        else:
            print("Nenhuma tarefa na lista.")

# Função principal
def main():
    lista_tarefas = Lista()

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Marcar Tarefa como Concluída")
        print("3. Remover Tarefa")
        print("4. Exibir Lista de Tarefas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefa = input("Digite a nova tarefa: ")
            lista_tarefas.adicionar(tarefa)
        elif opcao == '2':
            indice = int(input("Digite o índice da tarefa a marcar como concluída: "))
            lista_tarefas.marcar(indice - 1)  # Subtrai 1 porque a lista começa em 0
        elif opcao == '3':
            indice = int(input("Digite o índice da tarefa a remover: "))
            lista_tarefas.remover(indice - 1)  # Subtrai 1 porque a lista começa em 0
        elif opcao == '4':
            lista_tarefas.exibir()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
