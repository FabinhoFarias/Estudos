// 3 - Funções

// 3.1 - O que são funções -------------------------------------------------------------------------------------------------------------------------------------------------

/*Funções são blocos de código reutilizáveis que executam uma tarefa ou calculam um valor.
Elas ajudam a organizar e modularizar o código, tornando-o mais legível e eficiente.
*/

// 3.1.1 - Declaração de uma função simples
// A função abaixo não recebe argumentos e simplesmente imprime uma mensagem no console.
function saudacao() {
    console.log("Olá! Bem-vindo ao mundo das funções em JavaScript!");
}

// Chamando a função
saudacao(); // Saída: Olá! Bem-vindo ao mundo das funções em JavaScript!

// 3.1.2 - Funções com parâmetros

// Os parâmetros são variáveis que permitem passar informações para dentro da função.
 
function cumprimentar(nome) {
    console.log(`Olá, ${nome}! Como você está?`);
}

// Chamando a função com um argumento
cumprimentar("João"); // Saída: Olá, João! Como você está?

// 3.1.3 - Funções com retorno
// O "return" permite que uma função devolva um valor ao local onde foi chamada.

function soma(a, b) {
    return a + b;
}

// Armazenando o valor retornado em uma variável
const resultado = soma(5, 3);
console.log(`O resultado da soma é: ${resultado}`); // Saída: O resultado da soma é: 8

// 3.1.4 - Funções anônimas
// São funções que não possuem nome e geralmente são usadas como expressões.

const multiplicar = function(a, b) {
    return a * b;
};

console.log(`O resultado da multiplicação é: ${multiplicar(4, 7)}`); // Saída: O resultado da multiplicação é: 28

// 3.1.5 - Arrow functions

// Introduzidas no ES6, as arrow functions são uma sintaxe mais curta para escrever funções.

const dividir = (a, b) => {
    return a / b;
};

console.log(`O resultado da divisão é: ${dividir(10, 2)}`); // Saída: O resultado da divisão é: 5

// 3.1.6 - Funções autoexecutáveis (IIFE - Immediately Invoked Function Expressions)
// São funções que são executadas imediatamente após sua definição.

(function() {
    console.log("Esta função é executada imediatamente!");
})();


// 3.1.7 - Parâmetros padrão
// Você pode definir valores padrão para parâmetros que não forem fornecidos durante a chamada.

function apresentar(nome = "Visitante") {
    console.log(`Olá, ${nome}! Seja bem-vindo!`);
}

apresentar(); // Saída: Olá, Visitante! Seja bem-vindo!
apresentar("Ana"); // Saída: Olá, Ana! Seja bem-vindo!

// 3.1 - Binding de funções -------------------------------------------------------------------------------------------------------------------------------------------------

// Em JavaScript, o termo "binding" refere-se à associação de um contexto (“this”) a uma função.
// Isso é útil especialmente quando o contexto original da função é alterado por causa de como a função é chamada.

// Exemplo básico de como o contexto ("this") pode variar:
function mostrarNome() {
    console.log(this.nome);
}

const pessoa = {
    nome: 'Alice',
    mostrarNome
};

const outraPessoa = {
    nome: 'Bob'
};

// Chamada normal: o contexto é o objeto pessoa
pessoa.mostrarNome(); // Saída: 'Alice'

// Extraindo a função e chamando diretamente:
const funcaoIndependente = pessoa.mostrarNome;
funcaoIndependente(); // Saída: undefined, pois o contexto agora é o objeto global (ou undefined no modo estrito).

// Para corrigir isso, usamos o "binding" para fixar o contexto:
const funcaoComBind = pessoa.mostrarNome.bind(pessoa);
funcaoComBind(); // Saída: 'Alice'

// **Usando o método bind**
// O método `bind` cria uma nova função com o contexto ("this") definido explicitamente.
// Sintaxe: funcao.bind(contexto)

// Exemplo mais avançado: usando bind para passar funções como callbacks
function apresentar(separador = ',') {
    console.log(`Meu nome é ${this.nome}${separador} muito prazer!`);
}

const pessoa2 = { nome: 'Carlos' };
const apresentarCarlos = apresentar.bind(pessoa2);
apresentarCarlos(); // Saída: "Meu nome é Carlos, muito prazer!"

// **Diferença entre bind, call e apply**
// O método `bind` retorna uma nova função com o contexto associado, mas não a executa imediatamente.
// Já os métodos `call` e `apply` executam a função imediatamente com o contexto fornecido.

// Exemplo:
apresentar.call(pessoa2, ';'); // Executa imediatamente com contexto definido. Saída: "Meu nome é Carlos; muito prazer!"
apresentar.apply(pessoa2, [';']); // Igual ao `call`, mas aceita argumentos como array.

// **Arrow Functions e Binding**
// Arrow functions não possuem seu próprio contexto ("this"). Elas herdam o contexto do local onde foram definidas.
const objeto = {
    nome: 'Diana',
    mostrarArrow: () => {
        console.log(this.nome);
    },
    mostrarRegular: function() {
        console.log(this.nome);
    }
};

objeto.mostrarArrow(); // Saída: undefined ("this" é o contexto externo, não o objeto).
objeto.mostrarRegular(); // Saída: 'Diana' ("this" aponta para o objeto).

function saudar(saudacao) {
    console.log(`${saudacao}, meu nome é ${this.nome}`);
}

const pessoa3 = { nome: 'Alice' };

// Usando bind para criar uma nova função com contexto fixo
const saudarAlice = saudar.bind(pessoa3);

saudarAlice('Olá'); // Saída: "Olá, meu nome é Alice"

// Função original continua funcionando normalmente
saudar('Oi'); // Saída: "Oi, meu nome é undefined" (this aponta para o escopo global)


// Em resumo, o binding de funções é fundamental para controlar o contexto ("this") e garantir que o comportamento seja consistente,
// especialmente em callbacks e em ambientes com mudanças frequentes de contexto.

// 3.1 - Funções Arrow-------------------------------------------------------------------------------------------------------------------------------------------------

{
// Uma função arrow é uma forma concisa de escrever funções introduzida no ES6.
// Ela usa a sintaxe => para definir o corpo da função.

// Exemplo básico de uma função tradicional:
function soma(a, b) {
    return a + b;
}

// O mesmo exemplo usando uma função arrow:
const somaArrow = (a, b) => a + b;

// Observação:
// - Se o corpo da função tiver apenas uma expressão, você pode omitir as chaves {}
//   e o "return" é implícito.

// Exemplo de funções arrow com diferentes tipos de argumentos:

// 1. Sem argumentos:
const dizerOla = () => "Olá!";

// 2. Com um único argumento (os parênteses podem ser omitidos):
const quadrado = x => x * x;

// 3. Com múltiplos argumentos (os parênteses são necessários):
const multiplicar = (x, y) => x * y;

// Exemplos de uso:
console.log(soma(2, 3)); // Saída: 5
console.log(somaArrow(2, 3)); // Saída: 5
console.log(dizerOla()); // Saída: "Olá!"
console.log(quadrado(4)); // Saída: 16
console.log(multiplicar(3, 5)); // Saída: 15

// Diferenças principais entre funções arrow e funções tradicionais:

// 1. Escopo do "this":
// Funções arrow não possuem seu próprio "this". Elas herdão o "this" do contexto
// onde foram definidas. Isso é útil em situações como callbacks.

const objeto = {
    nome: "Objeto Teste",
    metodoTradicional: function() {
        console.log("this no metodoTradicional:", this);
    },
    metodoArrow: () => {
        console.log("this no metodoArrow:", this);
    }
};

objeto.metodoTradicional(); // "this" refere-se ao objeto
objeto.metodoArrow();       // "this" é herdado do contexto externo (provavelmente o escopo global ou undefined no modo estrito)

// 2. Uso em funções como callbacks:

// Funções tradicionais:
setTimeout(function() {
    console.log("Função tradicional no setTimeout.");
}, 1000);

// Funções arrow:
setTimeout(() => {
    console.log("Função arrow no setTimeout.");
}, 1000);

// Restrições das funções arrow:
// - Não podem ser usadas como construtores (não é possível usar "new" com elas).
// - Não possuem "arguments", mas podem usar o operador rest (...args) para acessar argumentos.

// Exemplo de operador rest em uma função arrow: O operador ... transforma os argumentos em um array [1, 2, 3, 4].
const somarTudo = (...numeros) => numeros.reduce((total, numero) => total + numero, 0);
console.log(somarTudo(1, 2, 3, 4)); // Saída: 10

// As funções arrow são muito úteis para escrever código mais limpo e conciso,
// especialmente em funções curtas ou callbacks.
}
