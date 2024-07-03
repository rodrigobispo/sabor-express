from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida = Bebida('Suco de Melancia', 8.0, 'Grande')
bebida.aplicar_desconto()
prato = Prato('Pão', 1.00, 'Pão francês')
prato.aplicar_desconto()

# restaurante_praca.adicionar_bebida_no_cardapio(bebida)
# restaurante_praca.adicionar_prato_no_cardapio(prato)

restaurante_praca.adicionar_no_cardapio(bebida)
restaurante_praca.adicionar_no_cardapio(prato)

# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

# restaurante_mexicano.alternar_estado()

# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 4)
# restaurante_praca.receber_avaliacao('Emy', 3)

def main():
    print(bebida)
    print(prato, '\n')
    restaurante_praca.exibir_cardapio
    # Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()