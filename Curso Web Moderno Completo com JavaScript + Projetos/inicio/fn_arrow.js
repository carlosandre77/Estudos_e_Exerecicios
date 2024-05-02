let dobro = function (a) {
    return 2 * a
}

dobro = (a) => {
    return 2 * a
}   
dobro = a => 2*a // return está implícito

let ola = function () {
    return 'Ola'
}
ola = () => 'Ola'
ola = _ => 'Olá' // possui um parametro
console.log(ola())