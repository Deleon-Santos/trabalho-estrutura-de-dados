"""Sistema de tabela Hash"""


class NodoEstado:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None


class TabelaHash:
    def __init__(self):
        self.tabela = [None, None, None, None,
                       None, None, None, None, None, None]

    def funcao_hash(self, sigla):
        if sigla.upper() == "DF":
            return 7
        a = ord(sigla[0])
        b = ord(sigla[1])

        return ((a * 100 + b) % 10)

    def inserir(self, sigla, nome_estado):
        indice = self.funcao_hash(sigla)
        novo_nodo = NodoEstado(sigla, nome_estado)
        novo_nodo.proximo = self.tabela[indice]
        self.tabela[indice] = novo_nodo

    def imprimir(self):
        for i in range(10):
            atual = self.tabela[i]
            elementos = []
            while atual:
                elementos.append(atual.sigla)
                atual = atual.proximo
            print(
                f"Posição {i}: {' -> '.join(elementos) + ' -> None' if elementos else 'None'}")


estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF",
                                       "Distrito Federal"), ("ES", "Espírito Santo"),
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT",
                                          "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ",
                                            "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR",
                                                      "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
]

# Inicio do sistema de tabela Hash
tabela = TabelaHash()
print("\nImpressão da Tabela Hash")
tabela.imprimir()
for sigla, nome in estados:
    tabela.inserir(sigla, nome)
print("\nImpressão da Tabela Hash Após Inserção dos 27 Estados")
tabela.imprimir()
tabela.inserir("DS", "Deleon Santos-ru:4565949")
print("\nImpressão da Tabela Hash Após Inserção do Estado Fictício")
tabela.imprimir()
