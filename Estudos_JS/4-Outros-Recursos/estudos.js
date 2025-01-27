// 4 - Outros Recursos

// 4.1 - Recursividade -------------------------------------------------------------------------------------------------------------------------------------------------

/*
Recursividade ocorre quando uma função chama a si mesma, direta ou indiretamente, 
para resolver um problema maior dividindo-o em subproblemas menores.
É útil em situações como cálculos matemáticos, processamento de árvores, 
problemas de busca, e muito mais.

IMPORTANTE:
1. Sempre defina uma condicao de parada para evitar loops infinitos.
2. Certifique-se de que cada chamada recursiva se aproxima da condicao de parada.
*/

// Exemplo 1: Fatorial de um número
// O fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n.
// Por exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

function fatorial(n) {
    // Condição de parada: fatorial de 0 ou 1 é 1
    if (n === 0 || n === 1) {
      return 1;
    }
    
    // Chamada recursiva: n * fatorial(n - 1)
    return n * fatorial(n - 1);
}

console.log("Fatorial de 5:", fatorial(5)); // Saída: 120

/*
Passos da execução:
1. fatorial(5) = 5 * fatorial(4)
2. fatorial(4) = 4 * fatorial(3)
3. fatorial(3) = 3 * fatorial(2)
4. fatorial(2) = 2 * fatorial(1)
5. fatorial(1) = 1 (condição de parada)
Assim, 5 * 4 * 3 * 2 * 1 = 120.
*/

// Exemplo 2: Soma de uma sequência de números até n
// Soma de 1 até n: soma(3) = 1 + 2 + 3 = 6

function somaSequencia(n) {
// Condição de parada: se n for 0, a soma é 0
if (n === 0) {
    return 0;
}

// Chamada recursiva: n + somaSequencia(n - 1)
return n + somaSequencia(n - 1);
}

console.log("Soma de 1 a 3:", somaSequencia(3)); // Saída: 6

/*
Passos da execução:
1. somaSequencia(3) = 3 + somaSequencia(2)
2. somaSequencia(2) = 2 + somaSequencia(1)
3. somaSequencia(1) = 1 + somaSequencia(0)
4. somaSequencia(0) = 0 (condição de parada)
Assim, 3 + 2 + 1 + 0 = 6.
*/

// Nota importante:
// Embora a recursividade seja poderosa, em alguns casos ela pode ser menos eficiente 
// do que soluções iterativas devido ao uso da pilha de chamadas (stack).
// Para problemas muito grandes, considere o uso de loops ou técnicas como tail-call optimization 
// (se disponível no seu ambiente JavaScript).

// 4.2 - Rest e operador spread -------------------------------------------------------------------------------------------------------------------------------------------------

// O operador Rest é representado por '...' (três pontos) e é usado para coletar vários argumentos
// ou elementos em um único array ou objeto. Ele é útil para lidar com um número variável de argumentos
// em funções ou para fazer cópias e manipulações em arrays e objetos.

// Exemplo 1: Usando o operador Rest em uma função
function somarNumeros(...numeros) {
    // Aqui, o operador Rest coleta todos os argumentos passados para a função
    // e os transforma em um array chamado 'numeros'.
  
    // Retornando a soma dos números usando o método reduce
    return numeros.reduce((total, num) => total + num, 0);
}

console.log(somarNumeros(1, 2, 3, 4, 5)); // Saída: 15

// Exemplo 2: Desestruturando um array com o operador Rest
const [primeiro, segundo, ...resto] = [10, 20, 30, 40, 50];

console.log(primeiro); // Saída: 10
console.log(segundo); // Saída: 20
console.log(resto);   // Saída: [30, 40, 50]

// Exemplo 3: Usando o operador Rest para copiar e adicionar elementos a um objeto
const pessoa = {
    nome: "João",
    idade: 25,
    cidade: "São Paulo"
};
  
  const novaPessoa = {
    ...pessoa, // Copiando todas as propriedades do objeto 'pessoa'
    profissao: "Desenvolvedor" // Adicionando uma nova propriedade
};
  
console.log(novaPessoa);
// Saída: {
//   nome: 'João',
//   idade: 25,
//   cidade: 'São Paulo',
//   profissao: 'Desenvolvedor'
// }

// Resumo:
// O operador Rest é extremamente versátil e pode ser usado em vários contextos, como:
// - Manipular argumentos em funções
// - Desestruturar arrays e objetos
// - Copiar e estender objetos

// Ele é uma ferramenta fundamental para escrever código mais limpo, flexível e reutilizável em JavaScript.
  
// Operador Spread em JavaScript

// O operador spread ("...") permite que você expanda elementos de arrays, objetos ou outros iteráveis.
// Ele é amplamente usado para criar cópias, combinar dados ou passar argumentos para funções de forma flexível.

// Oerador spread

// Exemplo 1: Usando o spread para copiar um array
const arrayOriginal = [1, 2, 3];
const copiaArray = [...arrayOriginal]; // Expande os elementos do arrayOriginal no novo array

console.log("Array Original: ", arrayOriginal); // [1, 2, 3]
console.log("Cópia do Array: ", copiaArray);   // [1, 2, 3]

// Exemplo 2: Combinar dois arrays
const arrayA = [1, 2, 3];
const arrayB = [4, 5, 6];
const arrayCombinado = [...arrayA, ...arrayB]; // Combina elementos de ambos os arrays

console.log("Array Combinado:", arrayCombinado); // [1, 2, 3, 4, 5, 6]

// Exemplo 3: Passar argumentos para funções
function soma(a, b, c) {
    return a + b + c;
}

const numeros = [1, 2, 3];
const resultado = soma(...numeros); // Expande os valores do array como argumentos da função

console.log("Soma dos Números:", resultado); // 6

// Exemplo 4: Copiar e adicionar propriedades a objetos
const objetoOriginal = { a: 1, b: 2 };
const copiaObjeto = { ...objetoOriginal, c: 3 }; // Cria uma cópia do objeto e adiciona a propriedade 'c'

console.log("Objeto Original: ", objetoOriginal); // { a: 1, b: 2 }
console.log("Cópia do Objeto com Modificação: ", copiaObjeto); // { a: 1, b: 2, c: 3 }

// Exemplo 5: Evitar mutação acidental
const estadoInicial = { nome: "Alice", idade: 25 };
const novoEstado = { ...estadoInicial, idade: 26 }; // Cria um novo objeto com uma alteração

console.log("Estado Inicial:", estadoInicial); // { nome: "Alice", idade: 25 }
console.log("Novo Estado:", novoEstado);       // { nome: "Alice", idade: 26 }

// Benefícios do operador spread:
// 1. Sintaxe concisa e legível.
// 2. Reduz a necessidade de métodos como concat() e Object.assign().
// 3. Facilita a manipulação de estruturas de dados imutáveis.

// 4.3 - setTimeout -------------------------------------------------------------------------------------------------------------------------------------------------

// O método setTimeout executa uma função após um intervalo de tempo específico.
// Sintaxe: setTimeout(função, tempoEmMilissegundos);

// Exemplo: Exibir uma mensagem após 3 segundos
setTimeout(() => {
    console.log('Esta mensagem aparece depois de 3 segundos!');
}, 3000);

/*
Detalhes:
1. O setTimeout aceita dois parâmetros principais:
- Uma função callback que será executada.
- O tempo de atraso em milissegundos (3000 ms = 3 segundos).
2. É uma execução única; a função será executada apenas uma vez.
*/

// 4.4 - setInteval -------------------------------------------------------------------------------------------------------------------------------------------------

// O método setInterval executa uma função repetidamente em um intervalo de tempo especificado.
// Sintaxe: setInterval(função, intervaloEmMilissegundos);

// Exemplo: Exibir uma mensagem a cada 2 segundos
const intervalId = setInterval(() => {
    console.log('Esta mensagem aparece a cada 2 segundos!');
}, 2000);

/*
Detalhes:
1. O setInterval aceita dois parâmetros principais:
   - Uma função callback que será executada.
   - O intervalo de repetição em milissegundos (2000 ms = 2 segundos).
2. Continua executando até que seja explicitamente interrompido com clearInterval().
*/

// Parar a execução do setInterval após 10 segundos
setTimeout(() => {
    clearInterval(intervalId); // Interrompe o setInterval
    console.log('O setInterval foi parado após 10 segundos.');
}, 10000);

/*
Diferenças entre setTimeout e setInterval:
1. O setTimeout executa a função uma única vez após um atraso.
2. O setInterval executa a função repetidamente com base no intervalo definido.

Ambos podem ser cancelados:
- clearTimeout(id) para setTimeout.
- clearInterval(id) para setInterval.
*/

