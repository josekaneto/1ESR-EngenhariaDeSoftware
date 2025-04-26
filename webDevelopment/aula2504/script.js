// const tarefas = ["Estudar JS", 'Criar Projeto', "Preparar Apresentação", 'Revisar código']

// console.table(tarefas)

// const categorias  = new Array("Trabalho", "Estudo", "Pessoal", "Projetos")

// console.table(categorias)

// const prioridades = Array.of("Baixa", "Media", "Alta")

// console.table(prioridades)

// const letras = Array.from('José')

// console.table(letras) 



// const tarefas = ["Estudar JS", 'Criar Projeto', "Preparar Apresentação", 'Revisar código']

// console.log(tarefas[0])

// tarefas[1] = "Criar projeto novo"

// console.table(tarefas)

// tarefas.push('Realizar testes')

// console.table(tarefas)

// tarefas.unshift("Revisar documentação")

// console.table(tarefas)

// tarefas.shift()

// console.table(tarefas)

// tarefas.pop()

// console.table(tarefas)

// tarefas.splice(1, 1, "AAAAAAAAAAAAAAAAAA")

// console.table(tarefas)



// const tarefas = ["Estudar JS", 'Criar Projeto', "Preparar Apresentação", 'Revisar código']

// const executarForeach = (elemento, i) => {
//     console.log(`${i + 1}. ${elemento}`)
// }

// tarefas.forEach(executarForeach)

// const arrayNovo =  tarefas.map((elemento, indice) => {
//     return elemento + " - concluído"
// })

// console.table(arrayNovo)

// const tarefasComA = tarefas.filter(elemento => elemento.toLowerCase().includes("p"))

// console.table(tarefasComA)

// const tarefaEncontrada = tarefas.find(elemento => elemento.toLowerCase().includes("código"))

// console.table(tarefaEncontrada)

// const indiceTarefaEncontrada = tarefas.findIndex(elemento => elemento.toLowerCase().includes("js"))

// console.table(indiceTarefaEncontrada)

// const valorFinal = tarefas.reduce((total, t) => 
//     total + t.length, 0
// )

// console.log(valorFinal)



// const tarefa = {
//     id: 1,
//     titulo: "Aprender sobre projetos",
//     descricao: "Estudar propriedades e metódos",
//     concluida: false,
//     prioridade: "alta",
//     dataCriacao: new Date()
// }

// console.log(tarefa)
// console.log(tarefa?.titulo)
// console.log(tarefa["titulo"])

// const tarefasEspeciais = {
//     "data-criacao": new Date(),
//     "nome da tarefa": "AAAAAAAAAAAAAAAAA"
// }

// console.log(tarefasEspeciais["data-criacao"])



// const projetoTaskMaster = {
//     nome: "TaskMaster",
//     version: "1.0",
//     autor: "Curso JavaScript",
//     tarefas: [],
    // adicionarTarefa(titulo, prioridade = "média") {
    //   const novaTarefa = {
    //     id: this.tarefas.length + 1,
    //     titulo,
    //     prioridade,
    //     concluida: false,
    //     criada: new Date()
    //   };
    //   this.tarefas.push(novaTarefa);
    //   console.log(`Tarefa "${titulo}" adicionada.`);
    //   return novaTarefa;
    // },
    // listarTarefas() {
    //   console.log(`Projeto ${this.nome} - Lista de Tarefas:`);
    //   this.tarefas.forEach(t => console.log(`- ${t.id}: ${t.titulo} (${t.prioridade})`));
    // }
//   };
  
//   projetoTaskMaster.adicionarTarefa("Estudar Objetos", "alta");
//   projetoTaskMaster.adicionarTarefa("Criar interface");
//   projetoTaskMaster.listarTarefas();

// console.log(Object.keys(projetoTaskMaster))

// console.log(Object.values(projetoTaskMaster))


// const prioridades = ["baixa", "média", "alta"];

// const [baixa, media, alta] = prioridades;
// console.log("Baixa:", baixa);
// console.log("Média:", media);
// console.log("Alta:", alta);

// const [primeiraCat, ...outrasCats] = ["Trabalho", "Estudo", "Pessoal", "Saúde"];
// console.log("Categoria principal:", primeiraCat);
// console.log("Outras categorias:", outrasCats);



const projetoTaskMaster = {
    nome: "TaskMaster",
    version: "1.0",
    autor: "Curso JavaScript",
    tarefas: []
}

const {nome, version, ...outrasProps} = projetoTaskMaster

console.log(nome)
console.log(version)
console.log(outrasProps)


