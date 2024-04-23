def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')

if opcao_escolhida == 1: 
    print('Cadastrar restaurante')
elif opcao_escolhida == 2: 
    print('Listar restaurantes')
elif opcao_escolhida == 3: 
    print('Ativar restaurante')
elif opcao_escolhida == 4: 
    finalizar_app()
else:
    opcao_invalida()

    #usando try except 

try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)
    
    if opcao_escolhida == 1: 
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2: 
        print('Listar restaurantes')
    elif opcao_escolhida == 3: 
        print('Ativar restaurante')
    elif opcao_escolhida == 4: 
        finalizar_app()
    else:
        opcao_invalida()
except: 
    opcao_invalida()

# código omitido
