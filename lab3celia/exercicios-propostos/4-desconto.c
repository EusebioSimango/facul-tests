#include <stdio.h>

int main()
{
  float preco, precoComDesconto;

  printf("Digite o preço do produto: ");
  scanf("%f", &preco);

  if (preco >= 1000)
  {
    precoComDesconto = preco - (preco * 0.10);
    printf("Preço com desconto:  %.2f mzn\n", precoComDesconto);
  }
  else
  {
    printf("Preço sem desconto: %.2f mzn\n", preco);
  }

  return 0;
}