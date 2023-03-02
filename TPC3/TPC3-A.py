import re

# Abrir o arquivo e ler as linhas
with open('processos.txt', 'r') as f:
    lines = f.readlines()

# Criar um dicionário para armazenar o número de processos por ano
processos_por_ano = {}

# Loop através das linhas do arquivo
for line in lines:
    # Usar regex para encontrar a data no formato "yyyy-mm-dd"
    match = re.search(r'\d{4}-\d{2}-\d{2}', line)
    if match:
        # Extrair o ano a partir da data
        ano = match.group(0)[:4]

        # Incrementar o contador correspondente ao ano atual
        if ano in processos_por_ano:
            processos_por_ano[ano] += 1
        else:
            processos_por_ano[ano] = 1

# Calcular a soma total de processos
total_processos = sum(processos_por_ano.values())

# Criar uma lista de tuplas contendo ano, número de processos e percentagem
tabela = []
for ano, num_processos in processos_por_ano.items():
    percentagem = (num_processos / total_processos) * 100
    tabela.append((ano, num_processos, percentagem))

# Ordenar a tabela por percentagem (em ordem decrescente)
tabela = sorted(tabela, key=lambda x: x[2], reverse=True)

# Imprimir a tabela
print('{:<10}{:<15}{:<15}'.format('Ano', 'Nº Processos', 'Percentagem'))
for linha in tabela:
    print('{:<10}{:<15}{:<15.2f}'.format(linha[0], linha[1], linha[2]))