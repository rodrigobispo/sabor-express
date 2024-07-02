import os

def exibir_nome_do_programa():
    print('''
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('clear')
    print('Encerrando o programa\n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal.')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print(f'Você escolheu a opção {opcao_escolhida} Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print(f'Você escolheu a opção {opcao_escolhida} Listar restaurantes')
        elif opcao_escolhida == 3:
            print(f'Você escolheu a opção {opcao_escolhida} Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()