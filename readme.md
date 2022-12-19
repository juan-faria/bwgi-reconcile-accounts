# BWGI - Reconcile Accounts

Esta é uma função para realizar a conciliação (batimento) entre dois grupos de transações financeiras

## Conceito

Para viabilizar o desenvolvimento dessa solução fez-se necessário utilizar alguns conceitos de ordenação, o que se somou na complexidade. A complexidade da ordenação em python é O(n log n) pois utiliza o algoritmo TimSort.

## Usando a função reconcile_accounts

Para utilizar a função reconcile_accounts basta importá-la e chamá-la passando como parâmetros duas listas de transações. No exemplo estas listas foram importadas dos arquivos _transactions1.csv_ e _transactions2.csv_.

O arquivo _example.py_ contém um exemplo de implementação utilizando a função. 