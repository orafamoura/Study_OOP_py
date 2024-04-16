import os

restaurantes = [{'nome':'resta1', 'categoria': 'japa', 'ativo': True}, 
                {'nome':'resta2', 'categoria': 'italiana', 'ativo': False},
                {'nome':'resta3', 'categoria': 'brasileira', 'ativo': False}]

def exibir_nome_do_programa():
  '''Funcao que exibi o nome do programa no terminal
  '''
  print('Sabor Express\n')

def exibir_opcoes():
  '''Funcao que exibi as opcoes disponiveis no menu principal'''
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Alternar estado do restaurante' )
  print('4. Sair\n')

def finalizar_app():
  '''Funcao que finaliza o aplicativo
  - exibir subtitulo'''
  exibir_subtitulo('Saindo...')

def voltar_ao_menu_principal():
  '''funcao que ao digitar qualquer tecla volta para o menu principal

  Output:
  - retorna ao menu principal
  '''
  input('Digite uma tecla para voltar ao menu principal: ')
  main()

def opcao_invalida():
  '''Funcao que mostra que a opcao selecionada foi invalida

  Output:
  - voltar ao menu principal'''
  print('Opcao invalida\n')
  voltar_ao_menu_principal()

def exibir_subtitulo(texto):
  '''Funcao que exibi o subtitulo de cada opcao selecionada no menu

  Output:
  - texto: str - O texto do subtitulo
  '''
  os.system('cls')
  linha = '*' * (len(texto) + 4)
  print(linha)
  print(texto)
  print(linha)
  print()

def cadastrar_novo_restaurante():
  '''Funcao responsavel por cadastrar novo restaurante
    - nome do restaurante
    - categoria

    Output: 
    - Adiciona um novo restaurante a lista de restaurante
  '''
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
  dados_do_restaurante = {'nome': nome_do_restaurante,
                          'categoria': categoria, 'ativo': False}
  restaurantes.append(dados_do_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
  voltar_ao_menu_principal()

def listar_restaurantes():
  '''Funcao que lista todos os restaurantes ativos em uma tabela

   Outputs:
   - Exibe a lista de restaurantes na tela
   '''
  exibir_subtitulo('Listando de restaurantes')

  print(f'{'nome do restaurante'.ljust(20)} | {'categoria'.ljust(12)} | Status')
  for restaurante in restaurantes:
    if restaurante['ativo'] == True:
      nome_restaurante = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = 'ativado' if restaurante['ativo'] else 'desativado'
      print(f'- {nome_restaurante.ljust(18)} | {categoria.ljust(12)} | {ativo}')
  voltar_ao_menu_principal()

def alternar_restaurante():
  '''Funcao que ativa ou desativa um restaurante cadastrado
  Output: 
  - exibe mensagem indicando o sucesso da operacao
  '''
  exibir_subtitulo('Alternando estado do restaurante')
  
  for restaurante in restaurantes:
    if restaurante['ativo'] == False:
      nome_restaurante = restaurante['nome']
      print(f'{nome_restaurante}')

  nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo']
      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)
  if not restaurante_encontrado:
    print(f'O restaurante {nome_restaurante} nao foi encontrado')
  voltar_ao_menu_principal()

def escolher_opcao():
  '''solicita e executa a opcao dada pelo usuario
  Output: 
  - Executa a opcao escolhida pelo usuario
  '''
  try:
    opcao_escolhida = int (input('Escolha uma opcao: '))

    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      alternar_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  '''Funcao principal que inicia o programa'''
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
    main()