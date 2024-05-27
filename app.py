import os

restaurantes = [
    {'nome': 'Bife sujo', 'categoria': 'prato-feito', 'ativo': True},
    {'nome': 'Saco de feijao', 'categoria': 'feijoada', 'ativo': False},
    {'nome': 'Pé de banha', 'categoria': 'pastelaria', 'ativo': True}
]

def finalizar_app():
    os.system("clear")
    os.system("cls")
    print("Finalizando o app\n")

def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")

def mostrar_subtitulo(texto):
   
    os.system("clear")
    linha = ''*(len(texto))
    print(linha)
    print(texto)
    print()

def escolher_opcoes():

    mostrar_subtitulo("""𝕽𝖊𝖘𝖙𝖆𝖚𝖗𝖆𝖓𝖙𝖊 𝕰𝖝𝖕𝖗𝖊𝖘𝖘𝖔\n""")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def opcao_invalida():
    
    mostrar_subtitulo("Opção inválida\n".ljust(20))
    voltar_menu_principal()

def listarRestaurantes():
    
    mostrar_subtitulo('Listando os Restaurantes'.ljust(20))
    print("Nome:".ljust(20), "Categoria:".ljust(22), "Status:".ljust(24))
  
 
    for restaurante in restaurantes:
        
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante["ativo"] else "Desativado"
        print(f' {nome_restaurante.ljust(20)}  {categoria.ljust(22)}  {ativo}')
        
def alternar_estado_restaurante():
     
     mostrar_subtitulo("Alterando o estado do restaurante".ljust(20))

     nome_restaurante = input("Digite o nome do Restaurante pata alterar")
     restaurante_encontrado = False
     for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'Restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo']else f"O restaurante {nome_restaurante} foi desativado"
            print(mensagem)

     if not restaurante_encontrado:
        print("Restaurante não encontrado")
            
def chamar_nome_do_app():
    print("""𝕽𝖊𝖘𝖙𝖆𝖚𝖗𝖆𝖓𝖙𝖊 𝕰𝖝𝖕𝖗𝖊𝖘𝖘𝖔""")

def cadastrar_novo_restaurante():
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    categoria = input(f'Digite a categoria do restaurante{nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"Você cadastrou o restaurante: {nome_do_restaurante}")

def main():
    
    while True:
        try:
            escolher_opcoes()
            opcaodigitada = int(input("Digite uma opção: "))
            if opcaodigitada == 1:
                print("Você vai cadastrar um restaurante\n" )
                cadastrar_novo_restaurante()
                main()
            elif opcaodigitada == 2:
                listarRestaurantes()
                voltar_menu_principal()
                main()
            elif opcaodigitada == 3:
                alternar_estado_restaurante()
                
            elif opcaodigitada == 4:
                print("Você saiu do aplicativo\n")
                finalizar_app()
                break
            else:
                opcao_invalida()
                main()
        except ValueError:
            print("Digite um número.")
            main()

if __name__ == "__main__":
    chamar_nome_do_app()
    main()