import re

# Abre o arquivo e lê as linhas
with open('processos.txt', 'r') as file:
    lines = file.readlines()

# Cria dicionários para cada século
nomes_por_seculo = {'XVI': {}, 'XVII': {}, 'XVIII': {}, 'XIX': {}, 'XX': {}, 'XXI': {}}
apelidos_por_seculo = {'XVI': {}, 'XVII': {}, 'XVIII': {}, 'XIX': {}, 'XX': {}, 'XXI': {}}

# Percorre o arquivo e adiciona as ocorrências de nomes e apelidos aos dicionários correspondentes
for line in lines:
    if '::' in line:
        campos = line.strip().split('::')
        ano = int(re.search(r'\d{4}', campos[1]).group())
        nome_completo = campos[2]
        partes_nome = nome_completo.split()
        nome = partes_nome[0]
        apelido = partes_nome[-1]
        seculo = ''

    if ano >= 1501 and ano <= 1600:
        seculo = 'XVI'
    elif ano >= 1601 and ano <= 1700:
        seculo = 'XVII'
    elif ano >= 1701 and ano <= 1800:
        seculo = 'XVIII'
    elif ano >= 1801 and ano <= 1900:
        seculo = 'XIX'
    elif ano >= 1901 and ano <= 2000:
        seculo = 'XX'
    elif ano >= 2001 and ano <= 2100:
        seculo = 'XXI'

    nomes_por_seculo[seculo][nome] = nomes_por_seculo[seculo].get(nome, 0) + 1
    apelidos_por_seculo[seculo][apelido] = apelidos_por_seculo[seculo].get(apelido, 0) + 1

# Seleciona os 5 nomes e apelidos mais frequentes em cada século
for seculo in nomes_por_seculo:
    nomes = nomes_por_seculo[seculo]
    apelidos = apelidos_por_seculo[seculo]
    nomes_ordenados = sorted(nomes.items(), key=lambda x: x[1], reverse=True)[:5]
    apelidos_ordenados = sorted(apelidos.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f'Século {seculo}:')
    print(f'Nomes: {", ".join([f"{nome} ({frequencia}x)" for nome, frequencia in nomes_ordenados])}')
    print(f'Apelidos: {", ".join([f"{apelido} ({frequencia}x)" for apelido, frequencia in apelidos_ordenados])}')