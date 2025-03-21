console.log("Hello World")
console.info("info")
console.warn("warning")
console.error("Error")

console.table([
    {id : 1, tarefa: "Estudar JS"},
    {id : 2, tarefa: "Praticar Código"}
])

console.group("Grupo de Logs")
console.log("log 1")
console.log("log 2")
console.groupEnd()

console.time("Timer")
if(1 == 2){
    console.log("nao")
}

console.timeEnd("Timer")

// comentário de 1 linha

/*
    Comentário de 
    várias linhas
*/

var antigo = "valor"
console.log(antigo)

let variavelMutavel = "Valor que pode ser alterado"
const variavelImutavel = "Valor que não pode ser alterado diretamente"

variavelMutavel = 1
console.log(variavelMutavel)

let texto = "texto"
console.log(typeof texto)

let numero = 1
console.log(typeof numero)

let isCompleted = true
console.log(typeof isCompleted)

let semValor
console.log(typeof semValor)

let nulo = null
console.log(typeof nulo)

let uniqueID = Symbol("id")
console.log(typeof uniqueID)

let bigNumero = 99999999999999n
console.log(typeof bigNumero)

let objeto =  {id : 1, tarefa: "Estudar JS"}
console.log(objeto)
console.log(objeto.id)
console.log(objeto.tarefa)

let tasks = [
    {id : 2, tarefa: "Estudar CSS"},
    {id : 3, tarefa: "Praticar Código"}
]

console.log(tasks)
console.log(tasks[0])
console.log(tasks[0]["id"])

let hoje =  new Date()

console.log(hoje)

let pattern = /^[a-z]+$/i
console.log(pattern )

