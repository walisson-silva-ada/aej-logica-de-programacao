def principal():
    participantes = {}
    n_participantes = int(input('Digite o numero de participantes: '))
    for participante in range(1, n_participantes + 1):
        nome = input(f'Digite o nome do {participante} participante: ')
        participantes[nome] = [0, 'ativo']
    for chave, valor in participantes.items():
        jogada(chave, valor)
    verificacao(participantes)

def sorteio():
    from random import choice
    carta = choice(cria_baralho())
    print('Carta retirada', carta)
    if carta == 'Ás':
        return 1
    elif carta == 'Valete' or carta == 'Dama' or carta == 'Rei':
        return 10
    else:
        return carta

def cria_baralho():
    return ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei']

def jogada(participante, pontos):
    print(f'Rodada do {participante}')
    while True:
        if pontos[0] < 21 and pontos[1] == 'ativo':
            print(f'Você está com {pontos[0]}')
            resp = input('Deseja comprar mais uma carta? [s / n] ')
            if resp == 's':
                pontos[0] += sorteio()
        if resp == 'n' or pontos[0] >= 21:
            print(f'O {participante} parou com {pontos[0]}')
            pontos[1] = 'inativo'
            break

def verificacao(participantes):
    vencedores = []
    pontos_vencedores = 0
    for chave, valor in participantes.items():
        if pontos_vencedores == valor[0] and valor[0] <= 21:
            pontos_vencedores = valor[0]
            vencedores.append(chave)
        elif pontos_vencedores < valor[0] and valor[0] <= 21:
            vencedores.clear()
            pontos_vencedores = valor[0]
            vencedores.append(chave)
    if pontos_vencedores > 0:
        print(f'O(s) vencedor(es): {vencedores} com {pontos_vencedores} pontos.')
    else:
        print('Não tiveram vencedores')

principal()