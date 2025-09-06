# Bus Routes
## O problema
Você tem várias rotas de ônibus e precisa ir de uma parada origem até uma parada destino usando o menor número de ônibus possível. 

As entradas esperadas são:
- routes: lista de rotas, onde cada rota é uma lista de paradas que se repete sempre.
- source: parada de origem
- target: parada de destino

A saída é o menor número de ônibus ou -1 se é impossível. 

## A resolução
Pra resolver esse problema, usei uma fila junto com hash. Primeiro criei um dicionário que mapeia cada parada pros ônibus que passam nela, e transformei todas as rotas em sets pra deixar as buscas mais rápidas.

Começo da parada origem e vou explorando. Para cada parada, vejo quais ônibus posso pegar. Se um ônibus já vai direto pro destino, acabou então retorno o número de ônibus + 1. Se não, adiciono todas as paradas desse ônibus na fila pra explorar depois.

## Conclusões
O algoritmo que usei foi uma busca sequencial otimizada com hashing. A busca sequencial básica seria testar parada por parada até achar o destino, mas isso seria muito lento.
Em vez de procurar linearmente em listas, uso hash (sets e dicionários) que fazem as consultas em tempo constante. Isso transformou as operações que seriam O(n) em O(1).