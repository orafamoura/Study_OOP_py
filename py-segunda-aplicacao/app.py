from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca','gourmet')
bebida_suco = Bebida('Suco pera', 5.0, 'G')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pao', 2.00, 'pao bom')
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == "__main__":
    main()


