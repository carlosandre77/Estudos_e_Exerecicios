function criarProduto(nome,preco) {
    return {
        nome,
        preco,
        desconto: 0.15
    }
}
console.log(criarProduto('NoteBook', 2119.56))
console.log(criarProduto('ipad',1999.38))