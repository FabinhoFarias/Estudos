// 1 - ESTRUTURA DA LINGUAGEM

// 1.1 - Expressões -------------------------------------------------------------------------------------------------------------------------------------------------
//    Em linguagens de programação, expressões são combinações de valores, variáveis, operadores e funções que são avaliadas para produzir um resultado. 
//    Uma expressão pode ser tão simples quanto um único valor ou variável, ou tão complexa quanto uma fórmula matemática ou lógica.


// 1.2 - Tipos de Dados
// 1.2.1 - Tipos Primitivos: Texto, Inteiro, Real e Lógico. Em JS:

// a) Number: Representa números, tanto inteiros quanto de ponto flutuante.

// // Exemplo:
// let inteiro = 42;        // Número inteiro
// let decimal = 3.14;      // Número decimal
// let negativo = -10;      // Número negativo
// let infinito = Infinity; // Resultado de operações como 1/0
// let naoNumero = NaN;     // Resultado de operações inválidas como ('texto' * 2), significa NotANumber

// b) String: Representa sequências de caracteres. As strings podem ser delimitadas por aspas simples (' '), aspas duplas (" ") ou crases (` `).

// // Exemplo:
// let texto = "Olá, Mundo!";                 // Tanto as aspas duplas quanto as aspas simples alternam o seu uso
// let saudacao = 'Bem-vindo ao JavaScript!'; //
// let mensagem = `Resultado: ${2 + 2}`;      // A crase é usada em template literals, semelhante ao f"{}" do Python
//                                            // ${Variável ou Expressão} == f"{Variável ou Expressão}"

// c) Boolean: Representa valores lógicos: true ou false.

// // Exemplo:
// let ligado = true;
// let desligado = false;

// d) Undefined: Indica que uma variável foi declarada, mas não recebeu um valor.

// // Exemplo:
// let naoDefinido;
// console.log(naoDefinido); // undefined

// e) Null: Representa a ausência proposital de valor.

// // Exemplo:
// let semValor = null;

// f) Symbol: Representa um identificador único.

// // Exemplo:
// let simbolo = Symbol("identificador");

// g) BigInt: Usado para representar números inteiros muito grandes.

// // Exemplo:
// let grandeNumero = 1234567890123456789012345678901234567890n; // Notação com 'n' no final para indicar o inteiro

// 1.2.2 - Tipos Não Primitivos (Objetos)

// a) Object: Um contêiner que armazena pares chave-valor.

// // Exemplo:
// let pessoa = {
//     nome: "João",
//     idade: 25,
//     ativo: true
// };
  
// b) Array: Representa uma coleção ordenada de valores.

// // Exemplo:
// let lista = [1, 2, 3, 4, 5];
  
// c) Function: Um bloco de código reutilizável.

// // Exemplo:
// function saudacao(nome) {
//     return `Olá, ${nome}!`;
// }
  
// d) Outros objetos: Incluem Date, RegExp, Map, Set, WeakMap, WeakSet, etc.

// // Exemplo:
// let dataAtual = new Date();
// let mapa = new Map();


// 1.3 - Variáveis -------------------------------------------------------------------------------------------------------------------------------------------------

// Variáveis são espaços na memória onde você armazena valores que podem ser usados e manipulados ao longo do programa.
// Existem três formas principais de declarar variáveis:
// 1. var
// 2. let
// 3. const

// A sintaxe básica para declarar uma variável no JavaScript é:
// let nome = "João"; // Declara uma variável chamada 'nome' e atribui o valor "João"

// 1.3.1 - Tipos de declaração de variáveis 
// Cada palavra-chave (var, let, const) possui características e usos diferentes.

// 1.3.1.1 - var

// - Introduzida nas versões iniciais do JavaScript.

// - Escopo:
//   * Tem escopo de função: está disponível dentro da função onde foi declarada.
//   * Ignora o escopo de bloco (pode ser acessada fora do bloco {}).
// - Problema de Hoisting:
//   * O hoisting move a declaração para o topo do escopo, mas não o valor inicial.
//   * Isso pode levar a comportamentos inesperados.

// // Exemplo:
// var a;          // Nenhum valor foi atribuido; espaço de memória vazio
// console.log(a); // undefined
// var a = 5;      // Inteiro 5 atribuído à variável a

// - Reatribuição e Redeclaração: Pode ser reatribuída e redeclarada sem erros.

// // Exemplo:
// var nome = "João";  
// var nome = "Maria"; // Reatribuição sem erros

// 1.3.1.1 - let

// - Introduzida no ES6 (ECMAScript 2015).
// - Escopo: Tem escopo de bloco, só está acessível dentro do bloco {} onde foi declarada.

// // Exemplo:
// {
//     let b = 10;
//     console.log(b); // Funciona
// }
// console.log(b); // Erro: b não está definida pois está dentro de um bloco

// - Sem Hoisting:
//   * Não é acessível antes de ser declarada.
// console.log(c); // Erro: c não está definida
// let c = 5;

// - Reatribuição:
//   * Pode ser reatribuída, mas não pode ser redeclarada no mesmo escopo.

// // Exemplo:
// let idade = 20;
// idade = 25; // Ok
// let idade = 30; // Erro, pois foi redeclarada

// 1.3.1.3 - const 

// - Também introduzida no ES6.
// - Escopo:
//   * Tem escopo de bloco, como let.
// - Imutabilidade:
//   * Não pode ser reatribuída, mas o conteúdo interno de objetos e arrays pode ser alterado.

// // Exemplo: Redeclaração
// const nomePessoa = "João";
// nomePessoa = "Maria"; // Erro: não pode reatribuir

// // Exemplo: Conteúdo dos objetos
// const pessoa = { 
//     idade: 25 
// }; // Objetos são imutáveis, mas o conteúdo interno pode ser alterado
// pessoa.idade = 30; // Ok
// console.log(pessoa.idade); // 30

// - Deve ser inicializada na declaração:

// // Exemplo:
// const valor;      // Erro
// const valor = 10; // Ok

// *** Diferenças Resumidas ***
// | Característica     | var                 | let                 | const               |
// |--------------------|---------------------|---------------------|---------------------|
// | Escopo             | Função              | Bloco               | Bloco               |
// | Reatribuição       | Sim                 | Sim                 | Não                 |
// | Redeclaração       | Sim                 | Não                 | Não                 |
// | Hoisting           | Sim, com undefined  | Não acessível antes | Não acessível antes |

// *** Boas Práticas ***
// 1. Prefira const sempre que possível.
// const PI = 3.14159;

// 2. Use let para variáveis que mudam de valor.
// let contador = 0;
// contador++;

// 3. Evite var em código moderno.

// // Exemplo:
// function exemplo() {
//     if (true) {
//         var a = "var: visível fora do bloco";
//         let b = "let: só dentro do bloco";
//         const c = "const: só dentro do bloco";

//         console.log(a); // Funciona
//         console.log(b); // Funciona
//         console.log(c); // Funciona
//     }
//     console.log(a); // Funciona
//     // console.log(b); // Erro
//     // console.log(c); // Erro
// }
// exemplo();

// 1.4 - Comentários -------------------------------------------------------------------------------------------------------------------------------------------------

// 1.4.1 - Linha única 

// Este é um comentário de linha única

// 1.4.2 - Multiplas linhas 

/*
Este é um comentário de multiplas linhas
Este é um comentário de multiplas linhas
Este é um comentário de multiplas linhas
Este é um comentário de multiplas linhas
Este é um comentário de multiplas linhas
*/

// 1.5 - Interações -------------------------------------------------------------------------------------------------------------------------------------------------

// Interações em JavaScript podem ser realizadas através de eventos e manipulações no DOM.
// Abaixo estão alguns exemplos práticos e comentados.

// Selecionar um botão pelo seu ID.
const botao = document.getElementById('meuBotao');

// Adicionar um evento de clique ao botão.
// 'addEventListener' permite associar eventos ao elemento.
botao.addEventListener('click', function () {
    alert('Você clicou no botão!'); // Exibe uma mensagem quando o botão é clicado.
});

// Alterar o conteúdo de um elemento ao passar o mouse por cima.
// Selecionamos um parágrafo pelo seu ID.
const paragrafo = document.getElementById('meuParagrafo');

// Adiciona um evento de mouseover (quando o mouse passa por cima do elemento).
paragrafo.addEventListener('mouseover', function () {
    paragrafo.textContent = 'Você passou o mouse aqui!'; // Altera o texto do parágrafo.
});

// Restaurar o conteúdo do parágrafo quando o mouse sair do elemento.
paragrafo.addEventListener('mouseout', function () {
    paragrafo.textContent = 'Passe o mouse aqui!'; // Restaura o texto original.
});

// Alterar o estilo de um elemento ao interagir.
// Selecionamos um campo de entrada (input) pelo ID.
const campoTexto = document.getElementById('meuInput');

// Adiciona um evento que detecta quando o usuário digita no campo.
campoTexto.addEventListener('input', function () {
    // Atualiza a cor de fundo do campo com base no comprimento do texto digitado.
    if (campoTexto.value.length > 5) {
        campoTexto.style.backgroundColor = 'lightgreen';
    } else {
        campoTexto.style.backgroundColor = 'lightcoral';
    }
});

// Eventos de teclado.
// Detecta quando uma tecla é pressionada.
document.addEventListener('keydown', function (event) {
    console.log(`Tecla pressionada: ${event.key}`); // Mostra no console qual tecla foi pressionada.
});

// Eventos de formulário.
// Prevenção do envio padrão de um formulário ao clicar no botão de envio.
const formulario = document.getElementById('meuFormulario');

formulario.addEventListener('submit', function (event) {
    event.preventDefault(); // Impede que a página seja recarregada.
    alert('Formulário enviado com sucesso (simulado)!'); // Mensagem simulando envio bem-sucedido.
});

// 1.6 - Arrays -------------------------------------------------------------------------------------------------------------------------------------------------
// Arrays são listas ordenadas de valores. 
// Eles podem conter qualquer tipo de dado, como números, strings, objetos, ou até outros arrays.

const meuArray = [1, 2, 3, 4, 5]; // Array simples com números.
console.log(meuArray);            // [1, 2, 3, 4, 5]

// Podemos acessar os elementos de um array usando seu índice (começa em 0).
console.log(meuArray[0]); // 1 (primeiro elemento)
console.log(meuArray[4]); // 5 (último elemento)

// Alterar o valor de um elemento específico.
meuArray[1] = 10;
console.log(meuArray); // [1, 10, 3, 4, 5]

// Adicionar elementos ao final do array com push().
meuArray.push(6); 
console.log(meuArray); // [1, 10, 3, 4, 5, 6]

// Remover o último elemento do array com pop().
const ultimoElemento = meuArray.pop(); 
console.log(ultimoElemento); // 6
console.log(meuArray); // [1, 10, 3, 4, 5]

// Adicionar elementos no início do array com unshift().
meuArray.unshift(0); 
console.log(meuArray); // [0, 1, 10, 3, 4, 5]

// Remover o primeiro elemento do array com shift().
const primeiroElemento = meuArray.shift();
console.log(primeiroElemento); // 0
console.log(meuArray); // [1, 10, 3, 4, 5]

// Encontrar o índice de um elemento com indexOf().
const indice = meuArray.indexOf(10);
console.log(indice); // 1

// Verificar se um elemento está no array com includes().
console.log(meuArray.includes(4)); // true
console.log(meuArray.includes(7)); // false

// Criar uma cópia do array com slice().
const copiaArray = meuArray.slice();
console.log(copiaArray); // [1, 10, 3, 4, 5]

// Remover ou substituir elementos com splice().
meuArray.splice(2, 1, 99); // Remove 1 elemento na posição 2 e adiciona 99.
console.log(meuArray);     // [1, 10, 99, 4, 5]

// Ordenar os elementos do array com sort().
const nomes = ['Carlos', 'Ana', 'João', 'Beatriz'];
nomes.sort();       // Ordena alfabeticamente.
console.log(nomes); // ['Ana', 'Beatriz', 'Carlos', 'João']

// Reverter a ordem dos elementos com reverse().
nomes.reverse();
console.log(nomes); // ['João', 'Carlos', 'Beatriz', 'Ana']

// Iterar sobre os elementos com forEach().
meuArray.forEach(function (item, indice) {
    console.log(`Índice: ${indice}, Valor: ${item}`);
});

// Criar um novo array com map().
const novoArray = meuArray.map(function (item) {
    return item * 2; // Multiplica cada elemento por 2.
});
console.log(novoArray); // [2, 20, 198, 8, 10]

// Filtrar elementos com filter().
const numerosPares = meuArray.filter(function (item) {
    return item % 2 === 0; // Retorna apenas os números pares.
});
console.log(numerosPares); // [10, 4]

// Reduzir o array a um único valor com reduce().
const soma = meuArray.reduce(function (acumulador, item) {
    return acumulador + item; // Soma todos os elementos.
}, 0);             // O valor inicial do acumulador é 0.
console.log(soma); // 119

// Obter o tamanho do array com length.
console.log(meuArray.length); // 5

// Concatenar dois arrays com concat().
const outroArray = [6, 7, 8];
const arrayConcatenado = meuArray.concat(outroArray);
console.log(arrayConcatenado); // [1, 10, 99, 4, 5, 6, 7, 8]

// Converter um array em string com join().
const arrayComoString = meuArray.join(' - ');
console.log(arrayComoString); // "1 - 10 - 99 - 4 - 5"

// Dividir uma string em um array com split().
const string = 'A,B,C,D';
const arrayDeString = string.split(',');
console.log(arrayDeString); // ['A', 'B', 'C', 'D']

// Trabalhar com arrays multidimensionais (arrays dentro de arrays).
const matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
console.log(matriz[1][2]); // 6 (linha 2, coluna 3)

// 1.7 - Template de Literais -------------------------------------------------------------------------------------------------------------------------------------------------
// Template Literals são uma forma aprimorada de trabalhar com strings no JavaScript. 
// Introduzidas no ECMAScript 6 (ES6), elas oferecem recursos avançados, como interpolação 
// de variáveis e criação de strings em múltiplas linhas, de maneira mais simples e legível.

// 1.7.1 - Interpolação de Variáveis
// Você pode incluir variáveis ou expressões dentro de uma string, usando a sintaxe ${expressão}.

const nome = "Maria";
const idade = 25;

// Sem template literals:
const mensagem1 = "Meu nome é " + nome + " e eu tenho " + idade + " anos.";
console.log(mensagem1); // Meu nome é Maria e eu tenho 25 anos.

// Com template literals:
const mensagem2 = `Meu nome é ${nome} e eu tenho ${idade} anos.`;
console.log(mensagem2); // Meu nome é Maria e eu tenho 25 anos.

// 1.7.2 - Strings em múltiplas linhas
// Template Literals permitem criar strings que ocupam várias linhas sem a necessidade de caracteres especiais.

// Sem template literals:
const texto1 = "Linha 1\n" +
               "Linha 2\n" +
               "Linha 3";
console.log(texto1);

// Com template literals:
const texto2 = `Linha 1
Linha 2
Linha 3`;
console.log(texto2);

// 1.8 - Strict Mode -------------------------------------------------------------------------------------------------------------------------------------------------

/* Strict Mode em JavaScript
* O "strict mode" (modo estrito) é uma funcionalidade do JavaScript que foi introduzida no ECMAScript 5 (ES5).
* Ele serve para impor uma versão mais rigorosa da linguagem, ajudando a identificar erros que podem ser difíceis de detectar.
* 
* Para ativar o strict mode, basta usar a diretiva "use strict" no início de um arquivo ou função.
*/

// Ativando o strict mode globalmente
"use strict";

// Exemplo 1: Erro ao usar variáveis sem declarar
try {
    x = 10; // Isso gera um erro porque 'x' não foi declarada.
} catch (e) {
    console.error("Erro: Variáveis precisam ser declaradas com var, let ou const.");
}

// Exemplo 2: Prevenção de duplicação de parâmetros
function soma(a, a) { // Sem strict mode, isso é permitido (mas confuso).
    return a + a;
}
// Com strict mode, uma tentativa de usar parâmetros duplicados gera um erro.
try {
    function somaEstrita(a, a) {
        "use strict";
        return a + a;
    }
} catch (e) {
    console.error("Erro: Parâmetros duplicados não são permitidos no modo estrito.");
}

// Exemplo 3: Prevenção de escrita em propriedades somente leitura
const obj = Object.freeze({
    nome: "João"
});
try {
    obj.nome = "Maria"; // Gera um erro no strict mode
} catch (e) {
    console.error("Erro: Não é possível modificar propriedades de objetos congelados.");
}

// Exemplo 4: Prevenção de palavras reservadas futuras
try {
    const public = "Isso não pode ser usado como nome de variável no modo estrito.";
} catch (e) {
    console.error("Erro: 'public' é uma palavra reservada no strict mode.");
}

/* Por que usar o strict mode?
 * 1. Segurança: Evita práticas de codificação inseguras.
 * 2. Melhor desempenho: Permite otimizações do motor JavaScript.
 * 3. Depuração: Ajuda a identificar e corrigir erros mais cedo.
 */

// Exemplo 5: Aplicando strict mode em funções específicas
function exemploEstrito() {
    "use strict";
    // Código dentro dessa função segue o modo estrito.
    try {
        y = 20; // Gera erro porque 'y' não foi declarada.
    } catch (e) {
        console.error("Erro: Variáveis precisam ser declaradas no strict mode dentro da função.");
    }
}

exemploEstrito(); // Executa a função com strict mode ativo

/* Observação:
* O strict mode pode ser desativado removendo a diretiva "use strict", mas é uma boa prática mantê-lo sempre ativo.
* Isso ajuda a garantir a qualidade e segurança do código.
*/