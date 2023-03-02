import re
with open('processos.txt', 'r') as f:
    lines = f.readlines()
    relacoes = {}
    for line in lines:
        if '::' in line:
            # Extrai as relações usando regex",
            match = re.search(r',([^,.]+).', line)
            if match:
                relacao = match.group(1).strip()

                # Incrementa a contagem da relação encontrada"
                if relacao in relacoes:
                    relacoes[relacao] += 1
                else:
                    relacoes[relacao] = 1
    
# Ordena as relações por frequência e imprime as mais comuns"
for relacao, freq in sorted(relacoes.items(), key=lambda item: item[1], reverse=True)[:5]:
    print(f'{relacao}: {freq}')