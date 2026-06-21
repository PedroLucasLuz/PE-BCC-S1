/*
====================================
EXERCÍCIO 1 - CONSUMO DE COMBUSTÍVEL
====================================

Peça a distância percorrida e a quantidade
de combustível consumida. Calcule o consumo médio.
*/

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("Digite a distância percorrida (km): ", (distanciaResp) => {
    readline.question("Digite os litros consumidos: ", (litrosResp) => {
        
        // double -> distância percorrida
        let distancia = parseFloat(distanciaResp);

        // double -> combustível consumido
        let litros = parseFloat(litrosResp);

        // double -> cálculo do consumo médio
        let consumo = distancia / litros;

        console.log("Consumo médio: " + consumo + " km/l");

        readline.close();
    });
});