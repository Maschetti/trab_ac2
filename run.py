import pandas as pd
import matplotlib.pyplot as plt

# Função para converter o tempo no formato "XmYs" para milissegundos
def time_to_milliseconds(time_str):
    minutes, seconds = time_str.split('m')
    seconds = seconds.replace('s', '')
    total_seconds = int(minutes) * 60 + float(seconds)
    return total_seconds * 1000  # Converte para milissegundos

# Carregar os arquivos CSV
recursivo_df = pd.read_csv('recursivo.csv')
iterativo_df = pd.read_csv('iterativo.csv')

# Converter os tempos para milissegundos
for df in [recursivo_df, iterativo_df]:
    df['real_ms'] = df['real'].apply(time_to_milliseconds)
    df['user_ms'] = df['user'].apply(time_to_milliseconds)
    df['sys_ms'] = df['sys'].apply(time_to_milliseconds)

# Função para gerar e salvar gráficos
def salvar_grafico(df, coluna, metodo, titulo, cor, arquivo):
    plt.figure(figsize=(8, 6))
    plt.plot(df['n'], df[coluna], label=metodo, color=cor)
    plt.xlabel('Entrada (n)')
    plt.ylabel('Tempo (ms)')
    plt.title(titulo)
    plt.grid(True)
    plt.ylim(0)
    plt.legend()
    plt.savefig(arquivo, format='png')
    plt.close()  # Fecha a figura para liberar memória

# Salvar gráficos iterativo
salvar_grafico(iterativo_df, 'real_ms', 'Iterativo', 'Tempo Real (Iterativo)', 'orange', 'tempo_real_iterativo.png')
salvar_grafico(iterativo_df, 'user_ms', 'Iterativo', 'Tempo User (Iterativo)', 'orange', 'tempo_user_iterativo.png')
salvar_grafico(iterativo_df, 'sys_ms', 'Iterativo', 'Tempo Sys (Iterativo)', 'orange', 'tempo_sys_iterativo.png')

# Salvar gráficos recursivo
salvar_grafico(recursivo_df, 'real_ms', 'Recursivo', 'Tempo Real (Recursivo)', 'blue', 'tempo_real_recursivo.png')
salvar_grafico(recursivo_df, 'user_ms', 'Recursivo', 'Tempo User (Recursivo)', 'blue', 'tempo_user_recursivo.png')
salvar_grafico(recursivo_df, 'sys_ms', 'Recursivo', 'Tempo Sys (Recursivo)', 'blue', 'tempo_sys_recursivo.png')
