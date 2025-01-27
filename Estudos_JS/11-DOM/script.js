function BarraLateral() {
    const barraLateral = document.querySelector(".Lista-Itens"); // Seleciona o menu lateral
    const Menu = document.querySelector("#Menu"); // Seleciona o menu lateral

    if (barraLateral) {
        // Verifica se a barra lateral já está visível
        if (barraLateral.classList.contains("ativo")) {
            // Se estiver visível, torna-a oculta
            Menu.classList.remove("ativo");
            barraLateral.classList.remove("ativo");
            barraLateral.classList.add("oculto");
        } else {
            // Caso contrário, torna-a visível
            Menu.classList.add("ativo");
            barraLateral.classList.remove("oculto");
            barraLateral.classList.add("ativo");
        }
    }
}

function AlterarCorDivsQuadradas (){
    const divsQuadradas = document.querySelectorAll('#Lista-Quadrados > div'); // Seleciona as divs
    divsQuadradas.forEach(element => {
        // Aplicar múltiplas alterações
        element.style.backgroundColor = 'lightblue';
        element.style.border = '2px solid darkblue';
        element.textContent = 'Div alterada!';    
        }
    );
}


// const intervalId = setInterval(() => {AlterarCorDivsQuadradas()}, 2000);

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function AlterarCorComPausa() {
    const divsQuadradas = document.querySelectorAll('#Lista-Quadrados > div');

    for (const element of divsQuadradas) {
        // Alterar cor
        element.style.backgroundColor = 'lightblue';
        element.style.border = '2px solid darkblue';
        element.textContent = 'Div alterada!';
        
        // Pausar por 2 segundos
        await sleep(2000);
    }
}

// AlterarCorComPausa();


async function LoopQuadrados(listaDeDivs) {
    let contador = 0;
    // Usar setInterval para iterar continuamente
    const intervalId = setInterval(() => {
        // Redefinir estilos de todas as divs para remover bordas anteriores
        listaDeDivs.forEach(div => {
            div.style.borderRadius = '0px';
            div.style.backgroundColor = 'blue'; // Exemplo de uma segunda propriedade
        });
        
        // Aplicar a borda na div atual
        
        listaDeDivs[contador].style.borderRadius    = '50%';
        listaDeDivs[contador].style.backgroundColor = 'red';
        
        
        if (contador + 1 === listaDeDivs.length){ // Caso onde o contador é o último elemento
            listaDeDivs[0].style.borderRadius =     '40%';
        } else{
            listaDeDivs[contador + 1].style.borderRadius = '40%';
            listaDeDivs[contador + 1].style.backgroundColor = 'blue';
        }
        if (contador - 1 === -1){
            listaDeDivs[listaDeDivs.length - 1].style.borderRadius = '40%';
        } else {
            listaDeDivs[contador - 1].style.borderRadius = '40%';
            listaDeDivs[contador - 1].style.backgroundColor = 'blue';
        }
        // Incrementar o contador
        contador += 1;
        // Reiniciar o contador quando chegar ao final da lista
        if (contador === listaDeDivs.length) {
            contador = 0;
        }
    }, 500); // Alteração a cada 1 segundo

    // Para parar o loop, use clearInterval(intervalId);
}
LoopQuadrados(document.querySelectorAll('#Lista-Quadrados > div'));

/*

Loop infinito com settimeout

tamanho do objectCollection
contador
se contador = tamanho, reseta
*/