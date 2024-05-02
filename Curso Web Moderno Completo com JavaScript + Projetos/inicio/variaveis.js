// {
//     {
//         {
//             {
//                 var sera = 'será'
//                 console.log(sera)
            
//             }
//         }
//     }
// }


// console.log(sera)

// function test() {
//     var local =134
//     console.log(local)

// }

// console.log(local)

// AULA VARiavel 2

// var numero =1
// {
//     var numero = 2
//     console.log('dentro =',numero)
// }
// console.log('fora =', numero)


// AULA variavel 3

// let numero =1
// {
//     let numero = 2
//     console.log('dentro =',numero)
// }
// console.log('fora =', numero)

// aula var em loop

// for( var i = 0; i < 10; i++) {
//     console.log(i)
// }

// console.log('i é igual a = ', i)


/////// var em loop 2 ///////////

const funcs = []

for(let i = 0; i <  10 ;i++) {
    funcs.push(function() {
        console.log(i)
        })
}
funcs[2]()
funcs[8]()
