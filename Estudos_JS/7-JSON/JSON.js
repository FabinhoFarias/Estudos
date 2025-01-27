// 7 - JSON

// 7.1 - Conceito -------------------------------------------------------------------------------------------------------------------------------------------------

// JSON (JavaScript Object Notation) é um formato leve de intercâmbio de dados.
// Ele é usado para transmitir dados entre um servidor e um cliente de forma simples e legível.
// A estrutura do JSON é baseada em pares "chave: valor", semelhante a objetos literais em JavaScript.

// Exemplo de um JSON:
const exemploJSON = {
    "nome": "João",
    "idade": 30,
    "habilidades": ["JavaScript", "Python", "HTML"]
};

// 7.2 - Métodos JSON, toJSON -------------------------------------------------------------------------------------------------------------------------------------------------

// O objeto global JSON em JavaScript fornece métodos para trabalhar com dados JSON.
// Um desses métodos é o "toJSON", que pode ser definido em objetos para especificar como eles serão serializados.

const objetoComToJSON = {
    nome: "Maria",
    idade: 25,
    toJSON: function () {
        return { nomeCompleto: `${this.nome} da Silva` };
    }
};

// Quando o objeto é convertido em uma string JSON, o método "toJSON" é chamado:
const jsonString = JSON.stringify(objetoComToJSON);
console.log(jsonString); // Output: {"nomeCompleto":"Maria da Silva"}

/*
Sem toJSON: Todas as propriedades do objeto são incluídas no JSON gerado.
Com toJSON: Você pode especificar quais propriedades devem aparecer e como elas devem ser representadas.

o método toJSON é usado quando quiser personalizar o que será incluído no JSON.
*/

// 7.3 - stringify -------------------------------------------------------------------------------------------------------------------------------------------------

// O método JSON.stringify() é usado para converter um objeto ou array JavaScript em uma string JSON.
// É muito útil para enviar dados para um servidor ou armazenar em localStorage.

const objeto = {
    nome: "Pedro",
    idade: 22,
    habilidades: ["Node.js", "React"]
};

const jsonStringify = JSON.stringify(objeto);
console.log(jsonStringify);
// Output: {"nome":"Pedro","idade":22,"habilidades":["Node.js","React"]}

// JSON.stringify também pode receber argumentos adicionais para formatação:
const jsonFormatado = JSON.stringify(objeto, null, 4); // Indenta com 4 espaços
console.log(jsonFormatado);

// 7.4 - parse -------------------------------------------------------------------------------------------------------------------------------------------------

// O método JSON.parse() é usado para converter uma string JSON de volta em um objeto ou array JavaScript.
// Isso é útil para trabalhar com dados recebidos de um servidor.

const jsonStringRecebido = '{"nome":"Ana","idade":28,"habilidades":["Vue.js","CSS"]}';
const objetoParse = JSON.parse(jsonStringRecebido);

console.log(objetoParse);
// Output: { nome: 'Ana', idade: 28, habilidades: [ 'Vue.js', 'CSS' ] }

// JSON.parse também pode receber uma função reviver como segundo argumento para transformar os valores durante o parsing:
const objetoComReviver = JSON.parse(jsonStringRecebido, (chave, valor) => {
    if (chave === "idade") {
        return valor + 1; // Incrementa a idade em 1
    }
    return valor;
});

// a função reviver faz uma iteração sobre todas as chaves e valores, inclusive dentro de arrays.
// Use-a para transformar ou remover propriedades durante o processo de conversão.
// Ela oferece controle total sobre como o JSON é transformado em objeto.

console.log(objetoComReviver);
// Output: { nome: 'Ana', idade: 29, habilidades: [ 'Vue.js', 'CSS' ] }
