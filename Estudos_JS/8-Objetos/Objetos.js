// 8 - Objetos

// 8.1 - Referência de Objetos

// Em JavaScript, os objetos são tipos de dados complexos que armazenam coleções de dados e 
// funcionalidades. 
// Eles são muito usados para representar coisas do mundo real, como um carro, uma pessoa, etc.

// Objetos são compostos por pares de chave e valor, onde as chaves são sempre strings (ou símbolos) e os valores podem ser qualquer tipo de dado, incluindo outros objetos, funções, arrays, etc.

const pessoa = {
    nome: "João",
    idade: 30,
    cidade: "São Paulo"
};

// Acessando os valores de um objeto
console.log(pessoa.nome);      // "João"
console.log(pessoa["idade"]);  // 30

// Podemos também adicionar ou alterar propriedades de um objeto:
pessoa.idade = 31;                   // Alterando a idade
pessoa.profissao = "Desenvolvedor";  // Adicionando uma nova propriedade

console.log(pessoa); // { nome: 'João', idade: 31, cidade: 'São Paulo', profissao: 'Desenvolvedor' }

// 8.1.1 - Referência de Objetos

// Quando criamos um objeto e o atribuimos a uma variável, estamos trabalhando com **referências** a 
// esse objeto, e não com uma cópia do valor.

// Exemplo de criação de uma referência:
const pessoa2 = pessoa;  // A variável pessoa2 referencia o mesmo objeto que pessoa.

// Modificando a propriedade de pessoa2
pessoa2.idade = 35;

console.log(pessoa);  // { nome: 'João', 
//                         idade: 35, 
//                         cidade: 'São Paulo', 
//                         profissao: 'Desenvolvedor' }

console.log(pessoa2); // { nome: 'João', 
//                         idade: 35, 
//                         cidade: 'São Paulo', 
//                         profissao: 'Desenvolvedor' }

// Como as variáveis pessoa e pessoa2 referenciam o **mesmo objeto**, a mudança feita em uma delas afeta a outra também.

// 8.1.2 - Criando cópias de objetos

// Caso você queira criar uma cópia de um objeto e evitar que alterações afetem o objeto original, você pode usar métodos como o "spread operator" ou o "Object.assign".

// Usando spread operator:

const pessoa3 = { ...pessoa }; // Cria uma cópia rasa do objeto pessoa

pessoa3.idade = 40;

console.log(pessoa);  // { nome: 'João', idade: 35, cidade: 'São Paulo', profissao: 'Desenvolvedor' }
console.log(pessoa3); // { nome: 'João', idade: 40, cidade: 'São Paulo', profissao: 'Desenvolvedor' }

// Agora, pessoa3 é uma cópia independente de pessoa, então as alterações não afetam o objeto original.

// 8.1.3 - Cópias profundas de objetos

// Se o objeto contiver outros objetos dentro dele, o spread operator ou Object.assign criará apenas uma cópia rasa.
// Para fazer uma cópia profunda (onde até os objetos internos são copiados), você pode usar bibliotecas ou funções como JSON.parse(JSON.stringify()):
  
const pessoaComEndereco = {
    nome: "Carlos",
    idade: 28,
    endereco: {
        rua: "Rua das Flores",
        numero: 123
    }
};

// Criando uma cópia profunda
const pessoaComEnderecoCopia = JSON.parse(JSON.stringify(pessoaComEndereco));

pessoaComEnderecoCopia.endereco.rua = "Rua das Laranjeiras";

console.log(pessoaComEndereco);      // { nome: 'Carlos', idade: 28, endereco: { rua: 'Rua das Flores', numero: 123 } }
console.log(pessoaComEnderecoCopia); // { nome: 'Carlos', idade: 28, endereco: { rua: 'Rua das Laranjeiras', numero: 123 } }

// Como a cópia profunda foi feita, o objeto original permanece inalterado, mesmo que o endereço dentro de pessoaComEnderecoCopia tenha sido modificado.

// 8.1.4 - Comparando Objetos

// Objetos são comparados por referência, não por valor. Ou seja, mesmo que dois objetos tenham as mesmas propriedades e valores, eles são diferentes se estiverem em locais de memória diferentes.

const objeto1 = { nome: "Maria", idade: 25 };
const objeto2 = { nome: "Maria", idade: 25 };

console.log(objeto1 === objeto2);  // false, pois são dois objetos diferentes, mesmo que tenham os mesmos valores.

const objeto3 = objeto1;  // Referência ao mesmo objeto
console.log(objeto1 === objeto3);  // true, pois objeto3 é uma referência ao mesmo local de memória que objeto1.

// 8.1.5 - Funções dentro de Objetos (Métodos)
const pessoa4 = {
    nome: "Ana",
    idade: 22,
    saudacao: function() {
      return `Olá, meu nome é ${this.nome} e eu tenho ${this.idade} anos.`;
    }
};

console.log(pessoa4.saudacao()); // "Olá, meu nome é Ana e eu tenho 22 anos."

// 8.1.6 - Propriedades Computadas
// Em JavaScript, você também pode usar expressões para definir propriedades de objetos.
const propriedade = "cidade";
const pessoa5 = {
    nome: "Lucas",
    idade: 30,
    [propriedade]: "Rio de Janeiro"  // Propriedade dinâmica, o valor da variável 'propriedade' será usado como chave
};

console.log(pessoa5.cidade); // "Rio de Janeiro"

// 8.1.7 - Iterando sobre as propriedades de um objeto
// Você pode usar for...in para percorrer todas as chaves de um objeto.
for (let chave in pessoa) {
    console.log(`${chave}: ${pessoa[chave]}`);
}
// Isso exibirá:9
// nome: João
// idade: 35
// cidade: São Paulo
// profissao: Desenvolvedor
  
// 8.2 - Garbage Colletion -------------------------------------------------------------------------------------------------------------------------------------------------

// 8.3 - This -------------------------------------------------------------------------------------------------------------------------------------------------

// 8.4 - Construtores -------------------------------------------------------------------------------------------------------------------------------------------------

// 8.5 - Operador New -------------------------------------------------------------------------------------------------------------------------------------------------

// 8.6 - Operador Dates -------------------------------------------------------------------------------------------------------------------------------------------------

// 8.7 - Operador Math -------------------------------------------------------------------------------------------------------------------------------------------------
