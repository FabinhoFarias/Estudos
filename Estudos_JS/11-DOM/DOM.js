// Seletores em JavaScript

// 1. Selecionando Elementos por ID
// Use quando o elemento tem um ID único no documento. É o mais rápido.
const listaQuadrados = document.getElementById("Lista-Quadrados");
console.log(listaQuadrados);

// 2. Selecionando Elementos por Classe
// Use para selecionar um ou mais elementos com a mesma classe.
const listaItens = document.getElementsByClassName("Lista-Itens");
console.log(listaItens[0]); // Retorna uma coleção HTML, acessível por índice

// 3. Selecionando Elementos por Tag
// Use para selecionar todos os elementos de uma tag específica.
const divs = document.getElementsByTagName("div");
console.log(divs);

// 4. Selecionando Elementos com querySelector
// Use para maior flexibilidade, selecionando o primeiro elemento que corresponder ao seletor CSS fornecido.
const primeiroQuadrado = document.querySelector("#Lista-Quadrados div");
console.log(primeiroQuadrado);

// 5. Selecionando Múltiplos Elementos com querySelectorAll
// Use para selecionar todos os elementos que correspondem ao seletor CSS.
const todosOsQuadrados = document.querySelectorAll("#Lista-Quadrados div");
todosOsQuadrados.forEach((quadrado, index) => {
    console.log(`Quadrado ${index + 1}:`, quadrado);
});

// 6. Selecionando Elementos pelo Atributo
// Use querySelector ou querySelectorAll para selecionar por atributos.
const itemComAtributo = document.querySelector("li[name='item-1']");
console.log(itemComAtributo);

// 7. Selecionando o Elemento Pai
// Use parentNode ou parentElement para acessar o pai de um elemento.
const paiDoQuadrado = primeiroQuadrado.parentNode;
console.log(paiDoQuadrado);

// 8. Selecionando Elementos Filhos
// Use children para acessar todos os filhos diretos de um elemento.
const filhosListaQuadrados = listaQuadrados.children;
console.log(filhosListaQuadrados);

// 9. Navegando pelos Irmãos
// Use nextElementSibling e previousElementSibling para acessar irmãos no DOM.
const segundoQuadrado = primeiroQuadrado.nextElementSibling;
console.log(segundoQuadrado);

// 10. Verificando a Presença de Classes
// Use classList para trabalhar com classes.
console.log(primeiroQuadrado.classList.contains("exemplo")); // Verifica se possui uma classe chamada "exemplo".

// Melhor uso para cada seletor: 
// - **ID**: Quando você sabe que o elemento é único.
// - **Classe**: Para grupos de elementos semelhantes.
// - **Tag**: Para elementos repetidos como "div", "li".
// - **querySelector**: Quando você precisa de seleções mais complexas.
// - **querySelectorAll**: Quando precisa de todos os elementos que correspondem ao seletor.
// - **Atributos**: Quando identifica elementos por atributos específicos.
// - **parentNode, children**: Para navegação e manipulação da hierarquia DOM.
// - **classList**: Útil para verificar, adicionar, ou remover classes dinamicamente.
