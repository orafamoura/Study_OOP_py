from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title() # .title para manter a primeira letra maiuscula
        self._categoria = categoria
        self._ativo = False # O _ na frente do ativo indica que ele e protected para a pessoa que for programar
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod #É uma boa prática indicar que se trata de um método da classe
    def listar_restaurantes(cls):
        print(f'{'Nome Restaurante'.ljust(18)} | {'Categoria'.
        ljust(12)} |{'Avaliacao'.ljust(10)}| {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(18)} | {restaurante._categoria.
            ljust(12)} |{str(restaurante.media_avaliacoes).ljust(10)}| {restaurante.ativo}')

    @property #modifica a forma que o atributo esta sendo lido
    def ativo(self):
        return 'true' if self._ativo else 'false'
        
    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1) # round serve para a quantidade de casas decimais
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): # isinstance compara A e B
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'): #hasattr = se tiver tal atributo
                mensagem_prato = f'{i}. Nome:{item._nome} | Preco: R${item.
                _preco} | Descricao: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preco: R${item.
                _preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)


