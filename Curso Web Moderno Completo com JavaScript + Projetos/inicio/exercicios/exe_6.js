/* Elabore duas funções que recebem três parâmetros: capital inicial, taxa de juros e tempo de aplicação. A
primeira função retornará o montante da aplicação financeira sob o regime de juros simples e a segunda
retornará o valor da aplicação sob o regime de juros compostos 
*/

function taxacaoJuros(capital_inicial, taxa_juros, tempo_aplicado) {
    juros_simp = 0
    juros_comp = capital_inicial
    for (i = 0;  i < tempo_aplicado;i++) {
        juros_simp = capital_inicial + taxa_juros
        juros_comp += taxa_juros
    }
    return {juros_simp, juros_comp}
}

console.log(taxacaoJuros(1000,0.05,2))



function jurosSimples(capital, taxa, tempo) {
    /**
     * Calcula o montante da aplicação financeira sob o regime de juros simples.
     *
     * @param {number} capital - O capital inicial investido.
     * @param {number} taxa - A taxa de juros (em decimal).
     * @param {number} tempo - O tempo de aplicação (em anos).
     * @returns {number} O montante da aplicação financeira.
     */
    let juros = capital * taxa * tempo;
    let montante = capital + juros;
    return montante;
}

function jurosCompostos(capital, taxa, tempo) {
    /**
     * Calcula o montante da aplicação financeira sob o regime de juros compostos.
     *
     * @param {number} capital - O capital inicial investido.
     * @param {number} taxa - A taxa de juros (em decimal).
     * @param {number} tempo - O tempo de aplicação (em anos).
     * @returns {number} O montante da aplicação financeira.
     */
    let montante = capital * Math.pow((1 + taxa), tempo);
    return montante;
}

// Exemplo de uso:
let capital = 1000;
let taxa = 0.05;
let tempo = 2;

let montanteJurosSimples = jurosSimples(capital, taxa, tempo);
let montanteJurosCompostos = jurosCompostos(capital, taxa, tempo);

console.log("Montante sob juros simples:", montanteJurosSimples);
console.log("Montante sob juros compostos:", montanteJurosCompostos);
