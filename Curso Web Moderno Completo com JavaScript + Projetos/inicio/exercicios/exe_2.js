function classificarTriangulo (comp1, comp2, comp3) {
    let tipo_do_triangulo = ''
    if (comp1 === comp2 && comp1 === comp3) {
        tipo_do_triangulo = 'Isóseles'
    } else if (comp1 === comp2 || comp2===comp3) {
        tipo_do_triangulo = 'Equilátero'
    } else if (comp1 != comp2 && comp1 != comp3) {
        tipo_do_triangulo = 'Escaleno'
    }
    return(`o triângulo é: ${tipo_do_triangulo}`)

}

console.log(classificarTriangulo(2, 2, 2)); // Equilátero
console.log(classificarTriangulo(2, 5, 5)); // Isósceles
console.log(classificarTriangulo(3, 4, 5)); // Escaleno