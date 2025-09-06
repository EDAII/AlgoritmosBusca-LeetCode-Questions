# BST Reorder Ways

## O problema
Você tem um array e quer saber de quantas formas pode reordenar ele mantendo a mesma árvore binária de busca.

As entradas são:
- nums: array de números de 1 a n

A saída é quantas formas diferentes existem de reordenar, ou 0 se não tem.

## A resolução
Usei recursão com combinatória. Pego o primeiro elemento como raiz e separo o resto: menores vão pra esquerda, maiores pra direita.

Calculei os fatoriais antes pra não ficar refazendo conta. Pra cada subárvore, chamo a função de novo e multiplico pelas formas de misturar esquerda com direita.

A conta é: formas_esquerda × formas_direita × combinação(total, esquerda). A combinação me diz quantos jeitos tem de encaixar os elementos mantendo as ordens.

## Conclusões  
Usei busca em árvore pela recursão, cada vez que chamo a função exploro uma parte menor da árvore. Não é busca de um elemento específico, é busca de todas as possibilidades.

A combinatória foi o melhor caminho porque senão teria que testar todas as permutações uma por uma, o que seria muito demorado. Calculando os fatoriais antes, as contas ficaram bem mais rápidas.