function tratarErroElencar(erro) {
    throw new Error('deu ruim')
}

function imprimirNomeGritado(obj) {
    try  {
        console.log(obj.name.toUpperCase() + '!!!')
    }catch(e) {
        tratarErroElencar()
    }
}

const obj = {nome: 'Roberto'}
imprimirNomeGritado(obj)