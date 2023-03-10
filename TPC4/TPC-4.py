import csv
import json
import re

# abrir o arquivo CSV e ler o cabeçalho
def csv_to_json(csvfile_name,jsonfile_name):
    with open(csvfile_name) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        # criar uma lista para os dados dos alunos
        alunos = []

        # percorrer as linhas do arquivo
        for row in reader:
            # criar um dicionário para o aluno
            aluno = {}

            # percorrer os campos do cabeçalho e adicionar os valores ao dicionário
            i = 0
            k = 0
            while i+1 < len(header):
                # usar a biblioteca re para extrair o número de colunas que o campo abrange
                
                match = re.match(r'(\w+)\{(\d+)\}$', header[i])
                match2 = re.match(r'(\w+)\{(\d+),(\d+)\}$', header[i]+','+header[i+1])
                match3 = re.match(r'(\w+)\{(\d+),(\d+)\}::(\w+)$', header[i]+','+header[i+1])
                print(match3)
                if match:
                    field_name = match.group(1)
                    field_size = int(match.group(2))
                    field_value = row[i:i+field_size]
                    i += field_size
                elif match2:
                    field_name = match2.group(1)
                    field_size = int(match2.group(3))
                    field_value = row[int(match2.group(2)):int(match2.group(3))]
                    i += field_size
                elif match3:
                    field_name = match3.group(4)
                    field_size = int(match3.group(3))
                    lista = row[i:i+field_size]
                    lista = [int(item) for item in lista if item != '']
                    print(lista)
                    if field_name == 'sum':
                        field_value = sum(lista)
                    elif field_name == 'media':
                        field_value = sum(lista)/len(lista)
                    i += field_size
                    
                while k < len(header):
                    clean = re.match(r'(\w+)$',header[k])
                    if clean:
                        field_name = header[k]
                        if k < len(row):
                            field_value = row[k]
                        else:
                            field_value = None
                        
                        aluno[field_name] = field_value
                    k += 1
                i+=1
                aluno[field_name] = field_value
            # adicionar o dicionário do aluno à lista
            alunos.append(aluno)

    # converter a lista de alunos em JSON e salvar em um arquivo
    with open(jsonfile_name, 'w') as jsonfile:
        json.dump(alunos, jsonfile, ensure_ascii=False, indent=2)

        
csv_to_json('alunos4.csv','alunos4.json')
