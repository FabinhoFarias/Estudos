// 1 - CONCICIONAIS E LOOPS

// 2.1 - If -------------------------------------------------------------------------------------------------------------------------------------------------

/* O "if" é uma estrutura condicional que permite executar blocos de código
diferentes dependendo de uma condição especificada. 
Se a condição for verdadeira (true), o bloco de código dentro do "if" é executado.
Caso contrário, ele será ignorado.
*/

// Estrutura básica do if
if (condicao) {
    // Bloco de código a ser executado se a condição for verdadeira
}

// Exemplo simples
let idade = 18;
if (idade >= 18) {
    console.log("Você é maior de idade."); // Este código será executado
}

/**
 * Bloco else:
 * É usado para definir um bloco de código que será executado caso a condição
 * do "if" seja falsa.
 */

if (idade < 18) {
    console.log("Você é menor de idade.");
} else {
    console.log("Você é maior de idade."); // Este código será executado
}

/**
 * Bloco else if: Semelhante ao elif do python
 * É usado para verificar múltiplas condições em sequência. 
 * Assim que uma condição verdadeira é encontrada, seu bloco é executado, e as outras
 * condições são ignoradas.
 */

let nota = 85;
if (nota >= 90) {
    console.log("Parabéns! Você tirou A.");
} else if (nota >= 70) {
    console.log("Você tirou B."); // Este código será executado
} else if (nota >= 50) {
    console.log("Você tirou C.");
} else {
    console.log("Você precisa melhorar.");
}

/**
Importante:
- Sempre que possível, use chaves {} mesmo que o bloco de código tenha apenas
  uma linha. Isso ajuda a evitar erros.
- Condições podem usar operadores lógicos (&&, ||, !) para criar expressões complexas.
*/

// Exemplo com operadores lógicos
let temCarteira = true;
let temIdadeMinima = idade >= 18;

if (temCarteira && temIdadeMinima) {
    console.log("Você pode dirigir.");
} else {
    console.log("Você não pode dirigir.");
}

// 2.2 - While -------------------------------------------------------------------------------------------------------------------------------------------------

/*O laço "while" é usado para repetir um bloco de código enquanto uma condição especificada for verdadeira.
Ele verifica a condição antes de executar o bloco de código, ou seja, é um laço de controle baseado em condição.

Sintaxe Básica:

while (condicao) {
    // Código a ser executado enquanto a condição for verdadeira
}
*/

// Exemplo 1: Contando de 1 a 5
let contador = 1; // Inicialização
while (contador <= 5) { // Condição
    console.log(`Número: ${contador}`); // Ação
    contador++; // Incremento para evitar um loop infinito
}

/*
IMPORTANTE:
- Certifique-se de que a condição eventualmente se torne falsa, caso contrário, o "while" entrará em um loop infinito.
*/

// Exemplo 2: Parando um loop com uma condição específica
let numero = 0;
while (true) { // Loop infinito
    numero++;
    console.log(`Contando: ${numero}`);
    if (numero === 3) {
        console.log("Parando o loop.");
        break; // Interrompe o loop
    }
}

/*
Variação: "do...while"
- Diferentemente do "while", o "do...while" executa o bloco de código pelo menos uma vez, 
  mesmo que a condição inicial seja falsa.

Sintaxe Básica:
do {
    // Código a ser executado
} while (condicao);
*/

// Exemplo 3: Usando "do...while"
let tentativas = 0;
do {
    console.log(`Tentativa número: ${tentativas + 1}`);
    tentativas++;
} while (tentativas < 3);

// 1.3 - For -------------------------------------------------------------------------------------------------------------------------------------------------

/*
O loop "for" é usado para executar um bloco de código várias vezes. 
Ele é ideal para quando sabemos de antemão o número de iterações.

Sintaxe básica do "for":
for (inicialização; condição; incremento) {
    // Código a ser executado
}
- inicialização: Executado uma vez antes de o loop começar. Geralmente, inicializa uma variável de controle.
- condição: Avaliada antes de cada iteração. Se for verdadeira, o loop continua; se falsa, ele para.
- incremento: Executado ao final de cada iteração, geralmente para atualizar a variável de controle.
*/


// for i in range(5):
//     print("Número: "i)
// Exemplo 1: Loop simples que imprime números de 1 a 5
for (let i = 1; i <= 5; i++) { // Em Python =>  // for i in range(5):
    console.log("Número: ", i);                 //     print("Número: "i) 
}                              

/*
Saída:  1
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
*/

// Exemplo 2: Usando "for" para iterar em um array
const frutas = ["maçã", "banana", "laranja"];

for (let i = 0; i < frutas.length; i++) {
    console.log("Fruta:", frutas[i]);
}

/*
Saída:
Fruta: maçã
Fruta: banana
Fruta: laranja
*/

// Exemplo 3: Loop aninhado para criar uma tabela
for (let linha = 1; linha <= 3; linha++) {
    for (let coluna = 1; coluna <= 3; coluna++) {
        console.log(`Posição: (${linha}, ${coluna})`);
    }
}

/*
Saída:
Posição: (1, 1)
Posição: (1, 2)
Posição: (1, 3)
Posição: (2, 1)
Posição: (2, 2)
Posição: (2, 3)
Posição: (3, 1)
Posição: (3, 2)
Posição: (3, 3)
*/

/*
Observações importantes:
1. O "for" é muito flexível e pode ser usado com diversas estruturas de dados.
2. Sempre tome cuidado com a condição para evitar loops infinitos.
3. É possível usar "break" para sair de um loop antecipadamente e "continue" para pular para a próxima iteração.
*/

// 2.4 - Switch -------------------------------------------------------------------------------------------------------------------------------------------------

/**
 * O switch é uma estrutura de controle condicional usada para comparar um valor
 * contra diferentes casos (case) e executar um bloco de código correspondente.
 * Ele é útil quando você precisa lidar com várias condições para um único valor.
 */

// Sintaxe básica do switch:
const cor = "vermelho";

switch (cor) {
  case "vermelho":
    console.log("A cor é vermelho.");
    break; // Interrompe o switch após encontrar o caso correspondente
  case "azul":
    console.log("A cor é azul.");
    break;
  case "verde":
    console.log("A cor é verde.");
    break;
  default:
    // Caso nenhuma das condições seja atendida
    console.log("A cor não foi reconhecida.");
}

/**
 * Explicação:
 * - O switch avalia o valor da variável e o compara com os casos (case).
 * - O bloco de código do case correspondente é executado.
 * - A instrução break impede que os casos seguintes sejam executados.
 * - O default é opcional e é executado se nenhum caso corresponder.
 */

// Exemplo sem o uso de break:
const dia = "segunda";

switch (dia) {
  case "segunda":
    console.log("Hoje é segunda.");
  case "terça":
    console.log("Hoje é terça.");
  default:
    console.log("Dia não especificado.");
}
// Neste caso, todos os blocos após o caso correspondente serão executados,
// pois falta o break para interromper o fluxo.

// Dica prática: Quando usar switch?
// - Quando há várias condições baseadas em um único valor.
// - Pode ser mais legível do que várias instruções if/else.

// Comparação com if/else:
const fruta = "maçã";

// Com if/else:
if (fruta === "banana") {
  console.log("Fruta é banana.");
} else if (fruta === "maçã") {
  console.log("Fruta é maçã.");
} else {
  console.log("Fruta não reconhecida.");
}

// Com switch (mais compacto):
switch (fruta) {
  case "banana":
    console.log("Fruta é banana.");
    break;
  case "maçã":
    console.log("Fruta é maçã.");
    break;
  default:
    console.log("Fruta não reconhecida.");
}


// 2.5 - Do While -------------------------------------------------------------------------------------------------------------------------------------------------

/* 
O laço "do...while" é uma estrutura de repetição em JavaScript. 
Ele executa um bloco de código pelo menos uma vez, independentemente da condição, 
pois a verificação ocorre após a execução do bloco. 
*/

// Sintaxe Básica:
// do {
//     // Código a ser executado
// } while (condição);

/* 
Características principais:
1. O código dentro do bloco "do" é executado pelo menos uma vez.
2. A condição é avaliada após a execução do bloco.
3. Se a condição for verdadeira, o laço continua a executar; caso contrário, ele é encerrado.
*/

// Exemplo 1: Contagem simples
if (true){
let contador = 1;
do {
    console.log(`Contador: ${contador}`); // Executa o código
    contador++; // Incrementa o contador
} while (contador <= 5); // Verifica a condição após executar
}

// Exemplo 2: Condição inicial falsa
if(true){
let numero = 10;
do {
    console.log(`Número atual: ${numero}`); // Executa o bloco pelo menos uma vez
} while (numero < 5); // Mesmo com a condição falsa, o código acima será executado uma vez
}

/* 
Vantagens do "do...while":
- Útil quando você precisa garantir que o bloco de código execute pelo menos uma vez.
- Boa escolha para processos que requerem uma ação inicial antes da verificação da condição.
*/
