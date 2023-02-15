import csv
import matplotlib.pyplot as plt




#    Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória;
#    Pense num modelo para guardar uma distribuição; ---> Guarda num dicionario com cada chave sendo uma coluna do ficheiro, tendo os seus respetivos valores associados
def csv_to_dic():
  data = {}
  with open(r'C:\Users\Renato Gomes\OneDrive\Documentos\GitHub\PL2023\TPC1\myheart.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        for key, value in row.items():
            if key not in data:
               data[key] = []
            data[key].append(value)
  return data



#   Crie uma função que calcula a distribuição da doença por sexo;
def calcula_distribucao_sexo(data):

    doente = {'M': 0, 'F': 0}
    total = {'M': 0, 'F': 0}
    
    for i, sex in enumerate(data['sexo']):
        if data['temDoenÃ§a'][i] == '1':
            doente[sex] += 1
        total[sex] += 1
    
    media = {}
    for sex in doente:
        media[sex] = round((doente[sex] / total[sex]) * 100, 2)
    
    return media

#print(calcula_distribucao_sexo(csv_to_dic()))    



#   Crie uma função que calcula a distribuição da doença por escalões etários. Considere os seguintes escalões: [30-34], [35-39], [40-44], ...
def calcula_distribucao_idade(data):

    grupos = {'[30-34]': 0, '[35-39]': 0, '[40-44]': 0, '[45-49]': 0, '[50-54]': 0,
                  '[55-59]': 0, '[60-64]': 0, '[65-69]': 0, '[70-74]': 0, '[75-79]': 0, '>=80': 0}
    total = 0

    for i, idade in enumerate(data['idade']):
        if data['temDoenÃ§a'][i] == '1':
            total += 1
            if int(idade) >= 30 and int(idade) <= 34:
                grupos['[30-34]'] += 1
            elif int(idade) >= 35 and int(idade) <= 39:
                grupos['[35-39]'] += 1
            elif int(idade) >= 40 and int(idade) <= 44:
                grupos['[40-44]'] += 1
            elif int(idade) >= 45 and int(idade) <= 49:
                grupos['[45-49]'] += 1
            elif int(idade) >= 50 and int(idade) <= 54:
                grupos['[50-54]'] += 1
            elif int(idade) >= 55 and int(idade) <= 59:
                grupos['[55-59]'] += 1
            elif int(idade) >= 60 and int(idade) <= 64:
                grupos['[60-64]'] += 1
            elif int(idade) >= 65 and int(idade) <= 69:
                grupos['[65-69]'] += 1
            elif int(idade) >= 70 and int(idade) <= 74:
                grupos['[70-74]'] += 1
            elif int(idade) >= 75 and int(idade) <= 79:
                grupos['[75-79]'] += 1
            else:
                grupos['>=80'] += 1
    
    distribucao = {}
    for group, count in grupos.items():
        distribucao[group] = round((count / total) * 100, 2)
    
    return distribucao

#print(calcula_distribucao_idade(csv_to_dic()))    




#   Crie uma função que calcula a distribuição da doença por níveis de colesterol. Considere um nível igual a um intervalo de 10 unidades, comece no limite inferior e crie os níveis necessários até abranger o limite superior;
def calcula_distribucao_colesterol(data):

    niveis_colesterol =[]
    total = 0
    for i, colesterol in enumerate(data['colesterol']):
        if data['temDoenÃ§a'][i] == '1':
            niveis_colesterol.append(int(colesterol))
            total += 1

    min_colesterol = int(min(niveis_colesterol))
    max_colesterol = int(max(niveis_colesterol))
    num_levels = (max_colesterol - min_colesterol) // 10 + 1
    colesterol_levels = {str(min_colesterol + i*10) + '-' + str(min_colesterol + (i+1)*10 - 1): 0 for i in range(num_levels)}

    for i, colesterol in enumerate(data['colesterol']):
        if data['temDoenÃ§a'][i] == '1':
            total += 1
            colesterol = int(colesterol)
            for level, count in colesterol_levels.items():
                lower, upper = map(int, level.split('-'))
                if lower <= colesterol <= upper:
                    colesterol_levels[level] += 1
                    break
    
    distribuicao = {}
    for level, count in colesterol_levels.items():
        distribuicao[level] = round((count / total) * 100, 2)
    
    return distribuicao


#print(calcula_distribucao_colesterol(csv_to_dic()))   

#   Crie uma função que imprime na forma de uma tabela uma distribuição;
def print_distribuicao(distribuicao, titulo):

    print(f'{titulo}\n')
    print(f'{"Categoria":<15}{"Percentagem":<15}')
    print('-' * 30)
    for categoria, percentagem in distribuicao.items():
        print(f'{categoria:<15}{percentagem:<15}')


#print_distribuicao(calcula_distribucao_idade(csv_to_dic()), 'Idade')

#   Especifique um programa que ao executar apresenta as tabelas correspondentes às distribuições pedidas;


def cria_tabelas():

  data = csv_to_dic()

  while(True):
    menu_options = {
    1: 'Distribuição por Sexo',
    2: 'Distribuição por Idade',
    3: 'Distribuição por Colesterol',
    4: 'Sair',
    }
  
    print('TPC1: Análise de dados: doença cardíaca: ')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

    option = int(input('Selecione uma opção: ')) 
    if option == 1:
      print_distribuicao(calcula_distribucao_sexo(data),'Sexo')
      print('\n')
    elif option == 2:
      print_distribuicao(calcula_distribucao_idade(data),'Idade')
      print('\n')
    elif option == 3:
      print_distribuicao(calcula_distribucao_colesterol(data),'Colesterol')
      print('\n')
    elif option == 4:
      exit()
    else:
      print('Opção invalida. Insira um numero entre 1 e 4.')



#cria_tabelas()



    
#   Extra: explore o módulo matplotlib e crie gráficos para as suas distribuições.

def cria_grafs_sexo():

  # Dados
  data = csv_to_dic()
  disease_by_sex = calcula_distribucao_sexo(data)

  # Gráfico
  fig, ax = plt.subplots()
  ax.bar(disease_by_sex.keys(), disease_by_sex.values())

  # Títulos e rótulos
  ax.set_title('Distribuição da doença por sexo')
  ax.set_xlabel('Sexo')
  ax.set_ylabel('Número de casos')

  # Exibir gráfico
  plt.show()

#cria_grafs_sexo()


def cria_grafs_idade():
  # Dados
  data = csv_to_dic()
  disease_by_age = calcula_distribucao_idade(data)

  # Gráfico
  fig, ax = plt.subplots()
  ax.bar(disease_by_age.keys(), disease_by_age.values())

  # Títulos e rótulos
  ax.set_title('Distribuição da doença por faixa etária')
  ax.set_xlabel('Faixa etária')
  ax.set_ylabel('Número de casos')

  # Exibir gráfico
  plt.show()


#cria_grafs_idade()



def cria_grafs_colesterol():
  data = csv_to_dic()
  disease_by_cholesterol = calcula_distribucao_colesterol(data)

  # Gráfico
  fig, ax = plt.subplots()
  ax.bar(disease_by_cholesterol.keys(), disease_by_cholesterol.values())

  # Títulos e rótulos
  ax.set_title('Distribuição da doença por níveis de colesterol')
  ax.set_xlabel('Nível de colesterol')
  ax.set_ylabel('Número de casos')

  # Exibir gráfico
  plt.show()

#cria_grafs_colesterol()