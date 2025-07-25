
MAX = 100


class ListaSequencial:
    def __init__(self):
        """Criação da lista vazia"""
        # Simula um vetor fixo de inteiros
        self.dados = [0] * MAX  # Array fixo de tamanho MAX
        self.tamanho_atual = 0  # Controla quantos elementos estão sendo usados

    def vazia(self):
        """Verificar se a lista está vazia"""
        return self.tamanho_atual == 0

    def cheia(self):
        """Verificar se a lista está cheia"""
        return self.tamanho_atual >= MAX

    def tamanho(self):
        """Obter o tamanho da lista"""
        return self.tamanho_atual

    def obter(self, pos):
        """Obter o valor do elemento de uma determinada posição"""
        if not (1 <= pos <= self.tamanho_atual):
            raise IndexError(f"Posição inválida: {pos}. Posições válidas: 1 a {self.tamanho_atual}")
        return self.dados[pos - 1]  # Converte posição 1-based para índice 0-based

    def modificar(self, pos, valor):
        """Modificar o valor do elemento de uma determinada posição"""
        if not isinstance(valor, int):
            raise TypeError("Apenas valores inteiros são permitidos")
        if not (1 <= pos <= self.tamanho_atual):
            raise IndexError(f"Posição inválida: {pos}. Posições válidas: 1 a {self.tamanho_atual}")
        self.dados[pos - 1] = valor

    def inserir(self, pos, valor):
        """Inserir um elemento em uma determinada posição"""
        if not isinstance(valor, int):
            raise TypeError("Apenas valores inteiros são permitidos")
        if self.cheia():
            raise OverflowError("Lista cheia - não é possível inserir mais elementos")
        if not (1 <= pos <= self.tamanho_atual + 1):
            raise IndexError(f"Posição inválida: {pos}. Posições válidas: 1 a {self.tamanho_atual + 1}")

        # Desloca elementos para a direita
        for i in range(self.tamanho_atual, pos - 1, -1):
            self.dados[i] = self.dados[i - 1]

        self.dados[pos - 1] = valor
        self.tamanho_atual += 1

    def remover(self, pos):
        """Retirar um elemento de uma determinada posição"""
        if self.vazia():
            raise ValueError("Lista vazia - não há elementos para remover")
        if not (1 <= pos <= self.tamanho_atual):
            raise IndexError(f"Posição inválida: {pos}. Posições válidas: 1 a {self.tamanho_atual}")

        valor_removido = self.dados[pos - 1]

        # Desloca elementos para a esquerda
        for i in range(pos - 1, self.tamanho_atual - 1):
            self.dados[i] = self.dados[i + 1]

        self.tamanho_atual -= 1
        return valor_removido

    def __str__(self):
        """Representação string da lista"""
        elementos = [str(self.dados[i]) for i in range(self.tamanho_atual)]
        return f"Lista[{', '.join(elementos)}]"
