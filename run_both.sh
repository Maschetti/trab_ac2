#!/bin/bash

# Compilar os códigos C
gcc -o recursivo recursivo.c -lgmp
gcc -o iterativo iterativo.c -lgmp

# Verificar se a compilação foi bem-sucedida
if [[ ! -f recursivo ]] || [[ ! -f iterativo ]]; then
    echo "Erro na compilação. Verifique os códigos C."
    exit 1
fi

# Limpar ou apagar arquivos CSV existentes
> recursivo.csv
> iterativo.csv

# Arquivos CSV para salvar os resultados
echo "n,real,user,sys,output" > recursivo.csv
echo "n,real,user,sys,output" > iterativo.csv

# Loop para valores de n de 1 a 20
for n in {1..100}
do
    # Executando o código recursivo e capturando a saída
    output_rec=$(./recursivo $n)
    time_rec=$( (time ./recursivo $n) 2>&1)
    real_rec=$(echo "$time_rec" | grep real | awk '{print $2}')
    user_rec=$(echo "$time_rec" | grep user | awk '{print $2}')
    sys_rec=$(echo "$time_rec" | grep sys | awk '{print $2}')
    
    # Salvando os tempos e a saída no arquivo CSV
    echo "$n,$real_rec,$user_rec,$sys_rec,$output_rec" >> recursivo.csv

    # Executando o código iterativo e capturando a saída
    output_iter=$(./iterativo $n)
    time_iter=$( (time ./iterativo $n) 2>&1)
    real_iter=$(echo "$time_iter" | grep real | awk '{print $2}')
    user_iter=$(echo "$time_iter" | grep user | awk '{print $2}')
    sys_iter=$(echo "$time_iter" | grep sys | awk '{print $2}')
    
    # Salvando os tempos e a saída no arquivo CSV
    echo "$n,$real_iter,$user_iter,$sys_iter,$output_iter" >> iterativo.csv
done

echo "Resultados salvos em recursivo.csv e iterativo.csv"
