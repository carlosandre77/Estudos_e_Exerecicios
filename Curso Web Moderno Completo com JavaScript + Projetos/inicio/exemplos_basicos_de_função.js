// // função sem retorno
// function imprimirSoma(a, b )  {
//     console.log(a + b);
// }

// // imprimirSoma(2, 3);
// // imprimirSoma(2);
// // imprimirSoma(2,10,2,4,5,);
// // imprimirSoma();

// // Função com retorno
// function soma(a, b = 0) {
//     return a + b
// }

// console.log(soma(2, 3));
// console.log(soma(2));

//        aula função 2

// armazenando um afunção dentro de uma variável

const imprimirSoma = function(a, b) {
    console.log(a + b);
}

imprimirSoma(2, 7);

// armazenando uma função arrow em uma variável

const soma = (a, b) => {
    return a + b
}

console.log(soma(2,3));

// retorno implicito

const subtracao = (a, b) => a - b

console.log(subtracao(2, 3));


const imprimir2 = a => console.log(a)

imprimir2('Legal!!!')
