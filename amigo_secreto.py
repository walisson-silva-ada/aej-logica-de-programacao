numero_pessoas = int(input("Numero de pessoas a serem cadastradas"))
cadastro_amigo_oculto = {}
for i in range(numero_pessoas):
    nome_presentes = input('Digite o nome da pessoa e os tres presentes que ela quer: ').split(' ')
    nome = nome_presentes.pop(0)
    presentes = nome_presentes
    del nome_presentes
    cadastro_amigo_oculto[nome] = presentes

while True:
    n_p = input('Digite o nome da pessoae o presente: \n').split(' ')
    n, p = n_p[0], n_p[1]
    del n_p
    if n in cadastro_amigo_oculto.keys() and p in cadastro_amigo_oculto[n]:
        print('Uhul" Seu amigo secreto vai adorar o/')
    else:
        print('Tente Novamente!')
    continuar = input('Quer continuar? (s/n)')
    if continuar == 's':
        continue
    else:
        break