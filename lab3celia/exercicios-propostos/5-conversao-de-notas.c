#include <stdio.h>

int main()
{
    int nota;

    printf("Digite a nota (0-100): ");
    scanf("%d", &nota);

    if (nota < 0 || nota > 100)
    {
        printf("Nota inválida. A nota deve estar na faixa de 0 a 100.\n");
    }
    else
    {
        if (nota >= 90)
        {
            printf("A\n");
        }
        else if (nota >= 80)
        {
            printf("B\n");
        }
        else if (nota >= 70)
        {
            printf("C\n");
        }
        else if (nota >= 60)
        {
            printf("D\n");
        }
        else
        {
            printf("F\n");
        }
    }

    return 0;
}