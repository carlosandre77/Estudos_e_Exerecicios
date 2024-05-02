function baseExpoente (number1,number2) {
    let resultado = 1
    for (let i = 0; i < number2; i++) {
        resultado *= number1
    }
    return resultado

}
console.log(baseExpoente(10,7))