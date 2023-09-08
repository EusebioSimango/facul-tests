#include <stdio.h>

int main()
{
    int numero;

    printf("Digite um número de 1 a 7: ");
    scanf("%d", &numero);

    if (numero == 1)
    {
        printf("Domingo\n");
    }
    else if (numero == 2)
    {
        printf("Segunda-feira\n");
    }
    else if (numero == 3)
    {
        printf("Terça-feira\n");
    }
    else if (numero == 4)
    {
        printf("Quarta-feira\n");
    }
    else if (numero == 5)
    {
        printf("Quinta-feira\n");
    }
    else if (numero == 6)
    {
        printf("Sexta-feira\n");
    }
    else if (numero == 7)
    {
        printf("Sábado\n");
    }
    else
    {
        printf("Número inválido. Por favor, digite um número de 1 a 7.\n");
    }

    return 0;
}