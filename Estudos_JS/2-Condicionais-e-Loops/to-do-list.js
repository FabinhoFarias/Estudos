const prompt = require('prompt-sync')(); // Importa o módulo
"use strict";
/**
Funcionalidades do Projeto: Sistema de Gerenciamento de Tarefas (To-Do List)

Adicionar Tarefa: Permitir que o usuário insira uma nova tarefa. OK
                  A tarefa será armazenada em uma lista (array). OK

Listar Tarefas: Exibir todas as tarefas cadastradas. OK
                Indicar se uma tarefa está concluída ou pendente. Ok

Marcar Tarefa como Concluída: Permitir ao usuário marcar uma tarefa específica como concluída. OK
                              Atualizar o status da tarefa na lista. OK

Editar Tarefa: Permitir ao usuário editar o nome ou descrição de uma tarefa existente. OK

Remover Tarefa: Permitir ao usuário excluir uma tarefa da lista. OK

*/

const ToDo = {
    Tarefa: [],
    adicionarTarefa: function(){
        if (ToDo.Tarefa.length === 0){
            console.log("A lista de tarefas está vazia. Cadastre uma tarefa: ")
        } 

        var NomeTarefa       = prompt("Digite o NOME da tarefa que você deseja inserir: ")
        while(NomeTarefa === ""){ // O nome não pode ser vazio
            console.log("O campo NOME não pode estar vazio. Por favor, insira um NOME para a sua tarefa")
            var NomeTarefa = prompt("Digite o NOME da tarefa que você deseja inserir: ")
        }
        let DescricaoTarefa  = prompt("Digite a DESCRIÇÃO da tarefa que você deseja inserir: ")
        if (DescricaoTarefa === ""){
            DescricaoTarefa = "Sem descrição"
        }
        let PrioridadeTarefa = prompt("Digite a PRIORIDADE da tarefa que você deseja inserir: ")
        if (this.Prioridade === ""){
            this.Prioridade = "Sem prioridade"
        }

        ToDo.Tarefa[ToDo.Tarefa.length]                   = NomeTarefa
        ToDo.DescricaoTarefa[ToDo.DescricaoTarefa.length] = DescricaoTarefa
        ToDo.Prioridade[ToDo.Tarefa.length]               = PrioridadeTarefa
        ToDo.Status[ToDo.Status.length]                   = "Pendente" // Toda tarefa cadastrada ainda não foi concluída
        },
    listarTarefas: function (){
        if (ToDo.Tarefa.length === 0){
            console.log("A lista de tarefas está vazia.")
        } else {
            console.log("\n------------ Lista de tarefas ------------\n")
            for (var i = 0; i < ToDo.Tarefa.length; i++) {
                console.log(`Tarefa ${i}: ${ToDo.Tarefa[i]}\n`)
            }
        }
    },
    DescricaoTarefa: [],  
    Prioridade: [],
    Status: [],
    editarTarefa: function() { 
        if (ToDo.Tarefa.length === 0){
            console.log("Não é possível fazer a edição de nenhuma tarefa pois a lisa de tarefas está vazia!");
        } else {
            console.log("1: Tarefa\n2: Descrição\n3: Prioridade\n4: Status")
            var Acao = prompt("Digite o número do que você deseja editar: ")
            console.log(typeof(Acao))
            if (Acao === "1"){
                ToDo.listarTarefas()
                let Acao = prompt("Qual tarefa você deseja editar? ")
                const NumeroTarefa = prompt("Digite o número ao lado da tarefa que você deseja editar: ")
                const Numero = prompt(`Digite o novo nome da tarefa ${NumeroTarefa}`)
                ToDo.Tarefa[NumeroTarefa] = Numero
            }
            else if (Acao === "2"){
                ToDo.listarTarefas()
                let Acao = prompt("Qual descrição você deseja editar? ")
                const NumeroTarefa = prompt("Digite o número ao lado da descrição que você deseja editar: ")
                const Numero = prompt(`Digite a nova descrição ${NumeroTarefa}`)
                ToDo.DescricaoTarefa[NumeroTarefa] = Numero
            }
            else if (Acao === "3"){
                ToDo.listarTarefas()
                let Acao = prompt("Qual prioridade você deseja editar? ")
                const NumeroTarefa = prompt("Digite o número ao lado da prioridade que você deseja editar: ")
                const Numero = prompt(`Digite o novo nome da prioridade ${NumeroTarefa}`)
                ToDo.PrioridadeTarefa[NumeroTarefa] = Numero
            }
            else if (Acao === "4"){
                ToDo.listarTarefas()
                let Acao = prompt("Qual status você deseja editar? ")
                const NumeroTarefa = prompt("Digite o número ao lado do ststus de tarefa que você deseja editar: ")
                ToDo.Status[NumeroTarefa] = "Concluido"
            } else {
                console.log("Ação inválida!")
                ToDo.editarTarefa()
            }
        }
    },
    statusTarefa: function(){
        if (ToDo.Tarefa.length === 0){
            console.log("Não é possível consultar o status de nenhuma tarefa pois nenhuma tarefa foi cadastrada")
        } else {

            for (var i = 0; i < ToDo.Tarefa.length; i++) {
                console.log(`Tarefa ${i}: ${ToDo.Tarefa[i]} - Status: ${ToDo.Status[i]}\n`)
            }
        }
    },
    alterarStatusTarefa: function(){
        if (ToDo.Tarefa.length === 0){
            console.log("Não é possível alterar o status de nenhuma tarefa pois a lista de tarefas está vazia")
        } else {
            console.log("\n------------ Lista de tarefas ------------")
            for (var i = 0; i < ToDo.Tarefa.length; i++) {
                console.log(`Tarefa ${i}: ${ToDo.Tarefa[i]} - Status: ${ToDo.Status[i]}`)
            }
            const Numero = prompt("Digite o número ao lado da tarefa que você deseja marcar como concluída: ")
            ToDo.Status[Numero] = "Concluído"
            console.log(`Tarefa ${Numero} foi concluída !\n`)
        }
    },
    excluirTarefa: function(){
        if (ToDo.Tarefa.length === 0){
            console.log("Não é possível excluir nenhuma tarefa pois a lista de tarefas está vazia")
        } else {
            ToDo.listarTarefas()
            const Numero = prompt("Digite o número ao lado da tarefa que você deseja excluir: ")
            ToDo.Tarefa.splice(parseFloat(Numero))
            ToDo.listarTarefas()
        }
    }
};
ToDo.adicionarTarefa()
ToDo.alterarStatusTarefa()
ToDo.excluirTarefa()
