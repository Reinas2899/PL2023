import re

# Estados da máquina de estados
estado_inicial = 'INICIAL'
estado_levantado = 'LEVANTADO'
estado_moeda = 'MOEDA'
estado_chamada = 'CHAMADA'
estado_pousado = 'POUSADO'

# Dicionário de transições
transicoes = {
    estado_inicial: {
        'LEVANTAR': estado_levantado,
    },
    estado_levantado: {
         'MOEDA': estado_moeda,
    },
    estado_moeda: {
        'MOEDA': estado_moeda,
        'T': estado_chamada,
        'ABORTAR': estado_inicial,
    },
    estado_chamada: {
        'T': estado_chamada,
        'POUSAR': estado_pousado,
        'ABORTAR': estado_inicial,
    },
    estado_pousado: {
        'LEVANTAR': estado_levantado,
    }
}

# Dicionário de valores de moedas
valores_moedas = {
    '1c': 0.01,
    '2c': 0.02,
    '5c': 0.05,
    '10c': 0.10,
    '20c': 0.20,
    '50c': 0.50,
    '1e': 1.00,
    '2e': 2.00,
}

# Estado atual da máquina de estados
estado_atual = estado_inicial

# Variáveis de estado da máquina de estados
saldo = 0
chamada = ''

# Loop principal da máquina de estados
while True:
    # Obter input do utilizador
    comando = input()

    # Obter o comando e o argumento
    partes = re.match(r'(\w+)(?:\s+(.*))?$', comando)
    partes2 = re.match(r'(\w+)=(\d+)?$', comando)
    if partes:
        comando, argumento = partes.groups()
    elif partes2:
        comando, argumento = partes2.groups()
    else:    
        continue
    
    # Verificar se o comando é válido para o estado atual
    if comando not in transicoes[estado_atual]:
        print('maq: Comando inválido para o estado atual.')
        continue
     # Transitar para o novo estado
    estado_atual = transicoes[estado_atual][comando]
    

    # Executar ações específicas para cada comando
    if comando == 'LEVANTAR':
        estado_atual = estado_levantado
        print("maq: Introduza moedas.")
        saldo = 0
        
    elif comando == 'MOEDA':
        estado_atual = estado_moeda
        # Adicionar o valor de cada moeda ao saldo
        moedas = re.split(",",argumento)
        for moeda in moedas:
            if moeda not in valores_moedas:
                print('maq: {0} - moeda inválida; saldo = {1:.2f}'.format(moeda, saldo))
            else:
                saldo += valores_moedas[moeda]
        print('maq: saldo = {1:.2f}'.format(moeda, saldo))        
    elif comando == 'T':
        estado_atual = estado_chamada
        # Verificar se o número de telefone é válido
        if re.match(r'601\d{6}', argumento) or re.match(r'641\d{6}', argumento):
            print('maq: Esse número não é permitido neste telefone. Queira inserir um novo número!')
            estado_atual = estado_moeda
        elif re.match(r'00\d{9}', argumento):
            if saldo<= 1.50:
                print('maq: Saldo insuficiente para efetuar uma chamada para este número. Valor minimo 1.50')
                estado_atual = estado_moeda
            else:
                saldo-=1.50
                chamada=argumento
        elif re.match(r'2\d{8}', argumento):
            if saldo<= 0.25:
                print('maq: Saldo insuficiente para efetuar uma chamada para este número. Valor minimo 0.25')
                estado_atual = estado_moeda
            else:
                saldo-=0.25
                chamada=argumento
        elif re.match(r'808\d{6}', argumento):
            if saldo<= 0.10:
                print('maq: Saldo insuficiente para efetuar uma chamada para este número. Valor minimo 0.10')
                estado_atual = estado_moeda
            else:
                saldo-=0.10
                chamada=argumento        
        else:
            chamada = argumento
        print('maq: saldo = {1:.2f}'.format(moeda, saldo))     
    elif comando == 'POUSAR':
        estado_atual = estado_pousado
        # Calcular o troco
        valor_troco = saldo
        troco = {}
        for moeda, valor in sorted(valores_moedas.items(), key=lambda x: -x[1]):
            quantidade_moedas = int(valor_troco // valor)
            if quantidade_moedas > 0:
                troco[moeda] = quantidade_moedas
                valor_troco -= quantidade_moedas * valor
                
        saldo = 0
        # Imprimir mensagem de saída
        if troco:
            mensagem = 'troco = ' + ', '.join([f'{v}x{k}' for k, v in troco.items()]) + f'; Volte sempre!'
        else:
            mensagem = 'troco = 0; Volte sempre!'
        print(f'maq: {mensagem}')

        # Resetar a máquina de estados
        estado_atual = estado_inicial
        continue

    elif comando == 'ABORTAR':
        print('maq: Retornando moedas.')
        saldo = 0
        estado_atual = estado_inicial
        continue
        print('maq: Encerrando programa.')