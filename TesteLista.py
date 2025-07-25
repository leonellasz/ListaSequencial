

import sys
import traceback
from lista import ListaSequencial


def test_criacao_lista_vazia():
    """Teste 1: Criação da lista vazia"""
    print("Teste 1: Criação da lista vazia")
    lista = ListaSequencial()
    assert lista.vazia() == True
    assert lista.cheia() == False
    assert lista.tamanho() == 0
    print("Passou")


def test_inserir_elementos():
    """Teste 2: Inserir elementos"""
    print("Teste 2: Inserir elementos")
    lista = ListaSequencial()

    # Inserir na posição 1 (lista vazia)
    lista.inserir(1, 10)
    assert lista.tamanho() == 1
    assert lista.obter(1) == 10
    assert not lista.vazia()

    # Inserir na posição 2
    lista.inserir(2, 20)
    assert lista.tamanho() == 2
    assert lista.obter(2) == 20

    # Inserir na posição 1 (deslocando elementos)
    lista.inserir(1, 5)
    assert lista.tamanho() == 3
    assert lista.obter(1) == 5
    assert lista.obter(2) == 10
    assert lista.obter(3) == 20

    print(" Passou")


def test_obter_modificar():
    """Teste 3: Obter e modificar elementos"""
    print("Teste 3: Obter e modificar elementos")
    lista = ListaSequencial()
    lista.inserir(1, 100)
    lista.inserir(2, 200)

    # Obter valores
    assert lista.obter(1) == 100
    assert lista.obter(2) == 200

    # Modificar valores
    lista.modificar(1, 150)
    lista.modificar(2, 250)
    assert lista.obter(1) == 150
    assert lista.obter(2) == 250

    print(" Passou")


def test_remover_elementos():
    """Teste 4: Remover elementos"""
    print("Teste 4: Remover elementos")
    lista = ListaSequencial()
    lista.inserir(1, 10)
    lista.inserir(2, 20)
    lista.inserir(3, 30)

    # Remover do meio
    valor = lista.remover(2)
    assert valor == 20
    assert lista.tamanho() == 2
    assert lista.obter(1) == 10
    assert lista.obter(2) == 30

    # Remover do início
    valor = lista.remover(1)
    assert valor == 10
    assert lista.tamanho() == 1
    assert lista.obter(1) == 30

    print(" Passou")


def test_tratamento_erros():
    """Teste 5: Tratamento de erros"""
    print("Teste 5: Tratamento de erros")
    lista = ListaSequencial()

    # Erro: posição inválida em lista vazia
    try:
        lista.obter(1)
        assert False, "Deveria lançar IndexError"
    except IndexError:
        pass

    # Erro: remover de lista vazia
    try:
        lista.remover(1)
        assert False, "Deveria lançar ValueError"
    except ValueError:
        pass

    # Erro: tipo não inteiro
    try:
        lista.inserir(1, "texto")
        assert False, "Deveria lançar TypeError"
    except TypeError:
        pass

    print("Passou")


def test_lista_cheia():
    """Teste 6: Lista cheia"""
    print("Teste 6: Lista cheia (teste parcial - só alguns elementos)")
    lista = ListaSequencial()

    # Inserir alguns elementos para testar
    for i in range(1, 6):
        lista.inserir(i, i * 10)

    assert lista.tamanho() == 5
    assert not lista.cheia()  # Ainda não está cheia

    print(" Passou")


def executar_todos_testes():
    """Executa todos os casos de teste"""
    testes = [
        test_criacao_lista_vazia,
        test_inserir_elementos,
        test_obter_modificar,
        test_remover_elementos,
        test_tratamento_erros,
        test_lista_cheia
    ]

    print("=" * 50)
    print("EXECUTANDO TESTES DA LISTA SEQUENCIAL")
    print("=" * 50)

    sucessos = 0
    falhas = 0

    for teste in testes:
        try:
            teste()
            sucessos += 1
        except Exception as e:
            print(f" Falhou: {e}")
            traceback.print_exc()
            falhas += 1
        print()

    print("=" * 50)
    print(f"RESULTADOS: {sucessos} sucessos, {falhas} falhas")
    print("=" * 50)

    return falhas == 0


if __name__ == "__main__":
    sucesso = executar_todos_testes()
    sys.exit(0 if sucesso else 1)
