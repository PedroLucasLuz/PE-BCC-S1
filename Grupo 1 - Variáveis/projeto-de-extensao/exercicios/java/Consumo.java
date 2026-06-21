/*
====================================
EXERCÍCIO 1 - CONSUMO DE COMBUSTÍVEL
====================================

Peça a distância percorrida e a quantidade
de combustível consumida. Calcule o consumo médio.
*/

import java.util.Scanner;

public class Consumo {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite a distância percorrida (km): ");

        // double -> distância percorrida
        double distancia = entrada.nextDouble();

        System.out.print("Digite os litros consumidos: ");

        // double -> combustível consumido
        double litros = entrada.nextDouble();

        // double -> cálculo do consumo médio
        double consumo = distancia / litros;

        System.out.println("Consumo médio: " + consumo + " km/l");

        entrada.close();
    }
}