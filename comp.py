import pandas as pd
import matplotlib.pyplot as plt

# Função para converter o tempo no formato '0m0.002s' para milissegundos
def convert_to_milliseconds(time_str):
    minutes, seconds = time_str.split('m')
    seconds = seconds.replace('s', '')
    return (int(minutes) * 60 + float(seconds)) * 1000  # Convertendo para milissegundos

# Carregar os dados dos arquivos CSV
recursivo = pd.read_csv('recursivo.csv')
iterativo = pd.read_csv('iterativo.csv')

# Converter os tempos para milissegundos
recursivo['real_ms'] = recursivo['real'].apply(convert_to_milliseconds)
recursivo['user_ms'] = recursivo['user'].apply(convert_to_milliseconds)
recursivo['sys_ms'] = recursivo['sys'].apply(convert_to_milliseconds)

iterativo['real_ms'] = iterativo['real'].apply(convert_to_milliseconds)
iterativo['user_ms'] = iterativo['user'].apply(convert_to_milliseconds)
iterativo['sys_ms'] = iterativo['sys'].apply(convert_to_milliseconds)

# Calcular o speedup
speedup_real = recursivo['real_ms'] / iterativo['real_ms']
speedup_user = recursivo['user_ms'] / iterativo['user_ms']
speedup_sys = recursivo['sys_ms'] / iterativo['sys_ms']

# Gráfico de tempo de execução
plt.figure(figsize=(10,6))
plt.plot(recursivo['n'], recursivo['real_ms'], label='Recursivo - Real', marker='o', color='b')
plt.plot(iterativo['n'], iterativo['real_ms'], label='Iterativo - Real', marker='o', color='r')
plt.title('Tempo de Execução (em ms) - Recursivo vs Iterativo')
plt.xlabel('N')
plt.ylabel('Tempo (milissegundos)')
plt.legend()
plt.savefig('grafico_tempo_ms.png')  # Salvar o gráfico de tempo
plt.show()

# Gráfico de speedup
plt.figure(figsize=(10,6))
plt.plot(recursivo['n'], speedup_real, label='Speedup - Real', marker='x', color='g')
plt.title('Speedup (em ms) - Recursivo vs Iterativo')
plt.xlabel('N')
plt.ylabel('Speedup')
plt.legend()
plt.savefig('grafico_speedup_ms.png')  # Salvar o gráfico de speedup
plt.show()
