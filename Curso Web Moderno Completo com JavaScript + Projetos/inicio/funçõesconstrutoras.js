function Carro(velocidadeMaxima = 200, delta =5) {
    //atributo privado
    let velocidadeAtual = 0

    // metodop publico
    this.acelarar = function () {
        if (velocidadeAtual + delta <= velocidadeMaxima) {
            velocidadeAtual += delta
        } else {
            velocidadeAtual = velocidadeMaxima        
        }
    }
}

//metodo publico
this.getVelocidadeAtual = function () {
    return velocidadeAtual
}