import re
import json

# Abre o arquivo e lê as linhas
with open('processos.txt', 'r') as f:
    lines = f.readlines()

# Lista para armazenar os dados dos 20 primeiros registos
data = []
linha = 0

# Loop através das linhas do arquivo
for line in lines:
    if '::' in line:
        # Extrai as informações do registro usando regex
        match = re.match(r'^(\d+)::(\d{4}-\d{2}-\d{2})::(.+?)::(.+?)::(.+?)::(.+?)$', line)
        if match:
            # Verifica se já lemos 20 registros
            if linha >= 20:
                break

            # Adiciona os dados do registro na lista
            registo = {
                'pasta': match.group(1),
                'data': match.group(2),
                'nome': match.group(3),
                'pai': match.group(4),
                'mae': match.group(5),
                'observacoes': match.group(6),
            }
            data.append(registo)
            linha += 1

# Cria um novo arquivo JSON e grava os dados
with open('processos.json', 'w') as f:
    json.dump(data, f, indent=4)