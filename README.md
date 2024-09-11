# Resolução dos Problemas

1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA? 
R: 77

4) Descubra a lógica e complete o próximo elemento:
a) R: 9
b) R: 128
c) R: 49
d) R: 100
e) R: 13
f) R: 20


5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

R:  Ligue dois interruptores e deixe um desligado. Vá para uma das salas.
    Se uma lâmpada estiver acesa: O interruptor ligado que controla essa lâmpada, o desligado controla a lâmpada da outra sala. O interruptor restante controla a lâmpada da sala que você ainda não visitou.
    Se nenhuma lâmpada estiver acesa: O interruptor que você ligou por último controla a lâmpada da sala que você visitou.
    Segunda ida: Desligue o interruptor que você ligou por último. Vá para a outra sala com lâmpada. A lâmpada acesa nesta sala será controlada pelo interruptor que foi ligado e permaneceu ligado desde a primeira ida.