// const titulo = document.querySelector('h1')
// titulo.textContent ="Novo titulo"

// const div = document.querySelector('#container')
// div.innerHTML = '<p>Novo parágrafo <b>HTML</b></p>'

// const imagem = document.querySelector('img')
// imagem.setAttribute('src', 'images/vecteezy_cheerful-3d-avatar-with-glasses-for-digital-marketing_57357660.png')
// imagem.setAttribute('width', '200px')
// imagem.alt = 'Avatar profile'

// const caixa = document.querySelector('.box')

// const botao = document.getElementById('meuBotao')
// botao.addEventListener('click', () =>{
//     caixa.classList.toggle('oculta')
// } )

// const item = document.createElement('li')
// item.textContent = 'Novo Item'

// const item2 = document.createElement('li')
// item2.textContent = 'Novo Item 2'

// document.querySelector('ul').appendChild(item)
// document.querySelector('ul').appendChild(item2)

// sessionStorage.setItem('nome', 'José')
// localStorage.setItem('nome2', 'Underson')

// const nome = sessionStorage.getItem('nome')
// console.log(nome)

// const nome2 = localStorage.removeItem('nome2')

// localStorage.clear()

// const usuario = {nome: 'José', idade: 18}
// localStorage.setItem('usuario', JSON.stringify(usuario))

// const usuarioRecuperado = JSON.parse(localStorage.getItem('usuario'))
// console.log(usuarioRecuperado)


let tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];

function renderizarTarefas() {
    const lista = document.getElementById("lista-tarefas");
    lista.innerHTML = "";
    tarefas.forEach((t, i) => {
      const li = document.createElement("li");
      li.textContent = t;
      lista.appendChild(li);
    });
}

renderizarTarefas()

document.getElementById("form-tarefa").onsubmit = (e) => {
    e.preventDefault();
    const input = document.getElementById("input-tarefa");
    tarefas.push(input.value);
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
    input.value = "";
    renderizarTarefas();
  };

document.getElementById("btn-limpar").onclick = () => {
    tarefas = [];
    localStorage.removeItem("tarefas");
    renderizarTarefas();
};