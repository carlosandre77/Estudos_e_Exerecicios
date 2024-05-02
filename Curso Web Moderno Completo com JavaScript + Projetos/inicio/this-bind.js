// const pessoa = {
//     saudacao: 'Bom dia!',
//     falar() {
//         console.log(this.saudacao)
//     }
// }

// pessoa.falar()
// const falar = pessoa.falar()
// //  falar() // conflito entre paradigmas: funcional e OO

//  const falarDePessoa = pessoa.falar.bind(pessoa)
//  falarDePessoa()

 function Pessoa() {
    this.idade = 0
    setInterval(() => {
        this.idade++
        console.log(this.idade)
    }, 1000)

 }

new Pessoa
