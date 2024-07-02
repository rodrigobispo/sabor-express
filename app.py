print('''
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
''')

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

if opcao_escolhida == 1:
    print(f'Você escolheu a opção {opcao_escolhida} Cadastrar restaurante')
elif opcao_escolhida == 2:
    print(f'Você escolheu a opção {opcao_escolhida} Listar restaurantes')
elif opcao_escolhida == 3:
    print(f'Você escolheu a opção {opcao_escolhida} Ativar restaurantes')
else:
    print('Encerrando o programa')