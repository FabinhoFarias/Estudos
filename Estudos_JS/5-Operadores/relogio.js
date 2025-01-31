// Caso alguém leia este código, eu fiz para treinar a lógica de programação e com certeza nunca implementaria isto
// em um projeto real kkkkkkkkkkkkkkk 

let hora = document.getElementById("hora");
let agora = new Date(); // Obtém a hora atual
let horas =    Number(String(agora.getHours()).padStart(2, '0')  );
let minutos =  Number(String(agora.getMinutes()).padStart(2, '0'));
let segundos = Number(String(agora.getSeconds()).padStart(2, '0'));

setInterval(() => {
    segundos += 1

    // As próximas 3 condicionais servem para simular "Manualmnte" a lógica de um relógio   
    if (segundos === 60){
        minutos += 1;
        segundos = 0;
    }
    if (minutos === 60){
        horas += 1;
        minutos = 0;
        segundos = 0    
    }
    if (horas === 24){
        horas = 0;
        minutos = 0;
        segundos = 0;
    }
    
    // As próximas 3 condicionais servem para não colocar "3" no lugar de "03"
    if (segundos < 10){ 
        segundos = `0${segundos}`;
    }
    
    if (minutos < 10){
        minutos = `0${minutos}`;
    }

    if (horas < 10){
        horas = `0${horas}`;
    }

    hora.innerText = `${horas}:${minutos}:${segundos}`; // Printar

    horas = Number(horas)      // Transformar em inteiro novamente para realizar os cálculos
    minutos = Number(minutos)  // Transformar em inteiro novamente para realizar os cálculos
    segundos = Number(segundos)// Transformar em inteiro novamente para realizar os cálculos
    
}, 1000);
