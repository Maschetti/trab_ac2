#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

void fatorial_iterativo(mpz_t resultado, int n) {
    mpz_set_ui(resultado, 1);  // Inicializa o resultado com 1
    for (int i = 1; i <= n; i++) {
        mpz_mul_ui(resultado, resultado, i);  // Multiplica o resultado por i
    }
}

int main(int argc, char *argv[]) {
    int numero = atoi(argv[1]);
    mpz_t resultado;

    mpz_init(resultado);  // Inicializa o resultado

    fatorial_iterativo(resultado, numero);

    // Verifica se o resultado é 0
    if (mpz_cmp_ui(resultado, 0) == 0) {
        printf("Fatorial iterativo de %d é 0 (erro de memória)\n", numero);
    } else {
        gmp_printf("%Zd\n", resultado);
    }

    mpz_clear(resultado);  // Libera a memória usada pelo resultado
    return 0;
}
