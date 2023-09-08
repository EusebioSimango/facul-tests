#include <stdio.h>

int main()
{
    float saldo = 1000.0; // Saldo inicial
    int opcao;
    float valor;

    printf("Bem-vindo ao Sistema Bancário!\n");
    printf("1 - Consultar Saldo\n");
    printf("2 - Efetuar Levantamento\n");
    printf("3 - Efetuar Transferência\n");
    printf("0 - Sair\n");

    do
    {
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao)
        {
        case 1:
            printf("Saldo atual: %.2f\n", saldo);
            break;
        case 2:
            printf("Digite o valor para levantamento: ");
            scanf("%f", &valor);
            if (valor > saldo)
            {
                printf("Saldo insuficiente.\n");
            }
            else
            {
                saldo -= valor;
                printf("Levantamento efetuado com sucesso.\n");
            }
            break;
        case 3:
            printf("Digite o valor para transferência: ");
            scanf("%f", &valor);
            if (valor > saldo)
            {
                printf("Saldo insuficiente para a transferência.\n");
            }
            else
            {
                saldo -= valor;
                printf("Transferência efetuada com sucesso.\n");
            }
            break;
        case 0:
            printf("Obrigado por utilizar nosso sistema. Adeus!\n");
            break;
        default:
            printf("Opção inválida. Tente novamente.\n");
        }
    } while (opcao != 0);

    return 0;
}
