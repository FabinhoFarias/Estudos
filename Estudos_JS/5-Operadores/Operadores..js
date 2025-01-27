// 5 - Operadores

// 5.1 - Matemáticos -------------------------------------------------------------------------------------------------------------------------------------------------

// Usados para realizar cálculos básicos operações.

let soma = 5 + 3;           // Soma: Adiciona dois valores (resultado: 8)
let subtracao = 10 - 4;     // Subtração: Subtrai o segundo valor do primeiro (resultado: 6)
let multiplicacao = 7 * 3;  // Multiplicação: Multiplica dois valores (resultado: 21)
let divisao = 20 / 4;       // Divisão: Divide o primeiro valor pelo segundo (resultado: 5)
let resto = 10 % 3;         // Módulo: Retorna o resto da divisão (resultado: 1)
let exponenciacao = 2 ** 3; // Exponenciação: Eleva o número à potência (resultado: 8)

// Operadores matemáticos podem ser combinados e usados com variáveis:
let resultado = (10 + 5) * 2; // Prioridade: Parênteses são avaliados primeiro (resultado: 30)

// 5.2 - Operadores de Comparação -------------------------------------------------------------------------------------------------------------------------------------------------

// Usados para comparar valores e retornam um booleano (true ou false).

let igual = 5 == '5';                  // Igualdade: Verifica valor, não tipo (resultado: true)
let estritamenteIgual = 5 === '5';     // Igualdade estrita: Verifica valor e tipo (resultado: false)
let diferente = 5 != '5';              // Diferença: Verifica valor, não tipo (resultado: false)
let estritamenteDiferente = 5 !== '5'; // Diferença estrita: Verifica valor e tipo (resultado: true)
let maior = 10 > 5;                    // Maior que (resultado: true)
let menor = 10 < 5;                    // Menor que (resultado: false)
let maiorOuIgual = 10 >= 10;           // Maior ou igual (resultado: true)
let menorOuIgual = 10 <= 5;            // Menor ou igual (resultado: false)

// 5.3 - Operadores Lógicos -------------------------------------------------------------------------------------------------------------------------------------------------

// Usados para combinar expressões booleanas.

let e = true && false;  // AND (&&): Retorna true se ambos os valores forem true (resultado: false)
let ou = true || false; // OR (||): Retorna true se pelo menos um valor for true (resultado: true)
let nao = !true;        // NOT (!): Inverte o valor booleano (resultado: false)

// Os operadores lógicos são frequentemente usados com condições:
let condicao = (5 > 3) && (10 < 20); // Verifica se ambas as condições são verdadeiras (resultado: true)

// 5.4 - Operadores de Atribuição -------------------------------------------------------------------------------------------------------------------------------------------------

// Usados para atribuir valores a variáveis.

let x = 10; // Atribuição simples
x += 5; // Atribuição com soma: x = x + 5 (resultado: 15)
x -= 3; // Atribuição com subtração: x = x - 3 (resultado: 12)
x *= 2; // Atribuição com multiplicação: x = x * 2 (resultado: 24)
x /= 4; // Atribuição com divisão: x = x / 4 (resultado: 6)
x %= 3; // Atribuição com módulo: x = x % 3 (resultado: 0)
x **= 2; // Atribuição com exponenciação: x = x ** 2 (resultado: 0 porque x era 0)

// 5.5 - Operadores Relacionais -------------------------------------------------------------------------------------------------------------------------------------------------

// Parecidos com os operadores de comparação, mas usados para determinar relação entre valores.

let maiorRelacional = 15 > 10; // Retorna true porque 15 é maior que 10
let menorRelacional = 10 < 20; // Retorna true porque 10 é menor que 20
let igualRelacional = 15 == '15'; // Retorna true porque os valores são iguais (ignora tipo)

