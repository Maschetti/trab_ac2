#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

void fatorial_recursivo(mpz_t resultado, int n) {
    if (n == 0 || n == 1) {
        mpz_set_ui(resultado, 1);  // Base case: fatorial de 0 ou 1 é 1
    } else {
        mpz_t temp;
        mpz_init(temp);  // Inicializa a variável temp
        fatorial_recursivo(temp, n - 1);  // Chama recursivamente
        mpz_mul_ui(resultado, temp, n);  // Multiplica o resultado por n
        mpz_clear(temp);  // Limpa a variável temp após o uso
    }
}

int main(int argc, char *argv[]) {
    int numero = atoi(argv[1]);
    mpz_t resultado;

    mpz_init(resultado);  // Inicializa o resultado

    fatorial_recursivo(resultado, numero);

    // Verifica se o resultado é 0
    if (mpz_cmp_ui(resultado, 0) == 0) {
        printf("Fatorial recursivo de %d é 0 (erro de memória)\n", numero);
    } else {
        gmp_printf("%Zd\n", resultado);
    }

    mpz_clear(resultado);  // Libera a memória usada pelo resultado
    return 0;
}
