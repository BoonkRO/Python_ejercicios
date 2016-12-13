

def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):
    """
        Devuelve el conjunto de casos test en una matriz donde cada
        entrada es una matriz con todos los items modificados ese dia:
        matrizCasosTest = [casosTestDia1, casosTestDia2, ... ]

        Los casos test del dia forman una matriz donde cada fila es un item:
        casosTestDia = [item, item, ... ]

        item = ['Elixir of the Mongoose', ' 5', ' 7']

        Argumentos:
        matrizCasosTest = [
                            [item],
                            [item],
                             ... ]
                           ]
                          ]

        matrizCasosTest = [[
                            ['Elixir of the Mongoose', ' 5', ' 7'],
                            ['Elixir of the Mongoose', ' 5', ' 7'],
                             ... ]
                           ]
                          ]
    """

    fichero = open(rutaAccesoFichero, 'r')

    matrizCasosTest = []

    for linea in fichero:

        if linea.find("day") != -1:
            casosTestDia = []
        elif linea == "\n":
            matrizCasosTest.append(casosTestDia)
        elif linea.find("sellIn") != -1:
            pass
        else:
            item = linea.rstrip()
            if linea.find("Sulfuras") != -1:
                item = item.rsplit(',', maxsplit=2)
            else:
                item = item.split(',')
            casosTestDia.append(item)

    return matrizCasosTest


if __name__ == "__main__":

    rutaAccesoFichero = "stdout.gr"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)

    # Volcamos los casos test cargados en memoria
    # a un fichero stdout.txt para inspeccionarlos.

    stdout = open("stdout.txt", 'w')
    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
        for item in casosTestDia:
            stdout.write(','.join(item) + '\n')