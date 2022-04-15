from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:

    print('=====================================')
    print('============= SHOP-TEC ==============')
    print('=====================================')

    print('\nSelecione Uma Opção\n')
    print('1 - Cadastro de Produto')
    print('2 - Listar Todos os Produtos')
    print('3 - Comprar')
    print('4 - Ver Carrinho')
    print('5 - Finalizar Pedido')
    print('6 - Sair')
    opcao = input('\n>>> ')

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produto()
    elif opcao == '3':
        comprar_produto()
    elif opcao == '4':
        visualizar_carrinho()
    elif opcao == '5':
        fechar_pedido()
    elif opcao == '6':
        print('\nVolte Sempre!')
        sleep(2)
        exit()
    else:
        print('\nOpção Inválida Digite apenas valores de 1 a 6\n')
        sleep(3)
        menu()


def cadastrar_produto() -> None:
    print('\n-------------------')
    print('Cadastro de Produto')
    print('-------------------\n')

    nome: str = input('Informe o nome do produto: \n')
    preco: float = float(input('Informe o Valor do produto: \n'))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'\nO produto {produto.nome} foi cadastrado com Sucesso!')
    sleep(2)
    menu()


def listar_produto() -> None:

    if len(produtos) > 0:
        print('\n-----------------')
        print('Lista de Produtos')
        print('-----------------\n')
        for produto in produtos:
            print(produto)
            print('-----------------')
            sleep(2)
    else:
        print('\nNão há Produtos Cadastrados no Sistema! ')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto: ')
        print('------------------------------\n')
        print('*****Produtos Disponíveis*****\n')
        for produto in produtos:
            print(produto)
            print('----------------------------\n')
            sleep(2)
        codigo: int = int(input('>>> '))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho!')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome}, foi adicionado ao carrinho!\n')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo}, não foi encontrado!')
            sleep(2)
    else:
        print('Não há Produtos cadastrados! ')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no Carrinho\n')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}\n')
                sleep(3)
    else:
        print('Carrinho Vazio')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho\n')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('---------------------------')
                sleep(3)
        print(f'Custo Total {formata_float_str_moeda(valor_total)}')
        print('Compra Efetuada Com Sucesso')
        carrinho.clear()
        sleep(5)
    else:
        print('Carrinho Vazio')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
