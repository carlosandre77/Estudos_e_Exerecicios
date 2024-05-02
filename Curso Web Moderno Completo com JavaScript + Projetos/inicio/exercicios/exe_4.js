/*
04) Crie uma função que irá receber dois valores, o dividendo e o divisor. A função deverá imprimir o resultado
e o resto da divisão destes dois valores.
*/

function div (dividendo,divisor) {
    return {resultado: dividendo / divisor,
        resto: dividendo%divisor
}
}

console.log(div(20,5))