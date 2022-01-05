composicao = input('Digite todas as notas e compassos: \n')
compassos = composicao.strip('/').split('/')
notas_duracao = {'W':1,'H':1/2,'Q':1/4,'E':1/8,'S':1/16,'T':1/32,'X':1/64}
incorretos = []
qtd_corretos = 0
for compasso in compassos:
    tempo = 0
    for nota in compasso:
        tempo += notas_duracao[nota]
    if tempo == 1:
        qtd_corretos +=1
    else:
        incorretos.append(compasso)
print(f'''
Qtd. de Corretos: {qtd_corretos}
''')
if len(incorretos) == 1:
    print(f'''Incorretos: {incorretos[0]}''')
elif len(incorretos) > 1:
    print(f'''Incorretos: {incorretos}''')