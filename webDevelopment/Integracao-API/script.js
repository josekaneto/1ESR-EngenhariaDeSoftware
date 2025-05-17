const  listarProdutos = async () => {
   const res = await fetch('https://66429d3a3d66a67b3437cdb2.mockapi.io/products');
   const produtos = await res.json();

    const ul = document.getElementById("lista-produtos");
      ul.innerHTML = "";

      produtos.forEach((p) => {
        const li = document.createElement("li");
        li.innerHTML = `
        <img src="${p.image}" width="50">
        <strong>${p.name}</strong> - R$ ${p.price} <em>(${p.seller})</em>
        <button id='excluir-produto' onclick='excluirProduto(${p.id})'>Excluir</button>
      `;
        ul.appendChild(li);
      });
}

listarProdutos();


document.getElementById("salvar-produto").onclick = async (e) => {
  e.preventDefault()
  const name = document.getElementById("name").value.trim()
  const price = document.getElementById("price").value.trim()
  const seller = document.getElementById("seller").value.trim()

  try {
    const res = await fetch('https://66429d3a3d66a67b3437cdb2.mockapi.io/products', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        "createdAt": new Date(),
        name,
        price,
        image:'',
        seller
      })
    })
    if (res.status === 201){
      alert("Produto cadastrado com sucesso!")
      name.value = ''
      price.value = 0
      seller.value = ''
      listarProdutos();
    }
    else{
      alert('Houve erros ')
    }
    
  } catch (error) {
    console.error(error)
  }


}

const excluirProduto = async (produto) => {
  try {
    const resposta = confirm('Você realmente quer excluir essse produto ?')
    if(resposta){
      const res = await fetch(`https://66429d3a3d66a67b3437cdb2.mockapi.io/products/${produto}`, {
        method: 'DELETE',
      })
      if (res.status === 200){
        alert('Produto exlcluido com sucesso!')
        listarProdutos()
      }
    }
  } catch (error) {
    console.error(error)
  }
}