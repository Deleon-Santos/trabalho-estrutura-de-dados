"""Lista de Espera para Atendimento Médico com Cartões de Cores"""


class Nodo:
    def __init__(self, numeroDeChamada, corPrioridade):
        self.numeroDeChamada = numeroDeChamada
        self.corPrioridade = corPrioridade
        self.seguinte = None


class ListaEspera:
    def __init__(self):
        self.head = None
        self.contador_v = 1
        self.contador_a = 201

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
            return
        paciente = self.head
        while paciente.seguinte:
            paciente = paciente.seguinte
        paciente.seguinte = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.corPrioridade == "V":
            nodo.seguinte = self.head
            self.head = nodo
            return
        paciente = self.head
        while paciente.seguinte and paciente.seguinte.corPrioridade == "A":
            paciente = paciente.seguinte
        nodo.seguinte = paciente.seguinte
        paciente.seguinte = nodo

    def inserir(self):
        while True:
            corPrioridade = input(
                "Informe o nivel de prioridade: A- para Amarelo, V- para Verde ou S- Sair: ").strip().upper()
            if corPrioridade == "V":
                numeroDeChamada = self.contador_v
                self.contador_v += 1
                print(f">>Cartão Verde Senha: {numeroDeChamada} adicionado à fila.")
            elif corPrioridade == "A":
                numeroDeChamada = self.contador_a
                self.contador_a += 1
                print(f">>Cartão Amarelo Senha: {numeroDeChamada} adicionado à fila.")
            elif corPrioridade == "S":
                return
            else:
                print("Cor invalida.")
                continue
            nodo = Nodo(numeroDeChamada, corPrioridade)
            if not self.head:
                self.head = nodo
            elif corPrioridade == "V":
                self.inserirSemPrioridade(nodo)
            elif corPrioridade == "A":
                self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        paciente = self.head
        listaMostrar = []
        
        if not paciente:
            print("A fila esta vazia.")
            return
        print("\nLista de Espera:")
        while paciente:
            print(
                f"Cartão: {paciente.corPrioridade} Senha: {paciente.numeroDeChamada}")
            listaMostrar.append(f'{paciente.corPrioridade}-{paciente.numeroDeChamada}')
            
            paciente = paciente.seguinte
            
        print(listaMostrar) 
           
    def atenderPaciente(self):
        while True:
            if not self.head:
                print("Nenhum paciente na fila.")
                return
            atendido = self.head
            self.head = self.head.seguinte
            print(
                f">>Chamando paciente com cartão: {atendido.corPrioridade} Senha: {atendido.numeroDeChamada} para atendimento.")
            acao = input(
                "Para continuar atendendo digite 'S' ").strip().upper()
            if acao == "S":
                continue
            else:
                print("Pausa no atendimento.")
            return

    def menu(self):
        print("\nSistema de inclusão em lista de espera para atendimento médico")
        while True:
            opcao = input(
                "\n1 – Adicionar novo paciente a fila\n"
                "2 – Mostrar todos os pacientes na fila\n"
                "3 – Chamar paciente da fila\n"
                "4 – Sair\n"
                "Escolha uma opção do menu: ")
            match opcao:
                case "1": self.inserir()
                case "2": self.imprimirListaEspera()
                case "3": self.atenderPaciente()
                case "4": print("Encerrando programa.");break    
                case _: print("Opcao invalida. Tente novamente.")


ListaEspera().menu()