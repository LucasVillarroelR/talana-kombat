class Peleador:
    def __init__(self, nombre, vida, id):
        self.nombre = nombre
        self.vida = vida
        self.id = "player" + str(id)
        self.golpes = []

    def anadir_golpe(self, nombre, combinacion, energia, mensaje):
        self.golpes.append(Golpe(nombre, combinacion, energia, mensaje))


class Golpe:
    def __init__(self, nombre, combinacion, energia, mensaje):
        self.nombre = nombre
        self.combinacion = combinacion
        self.energia = energia
        self.mensaje = mensaje


class Pelea:
    def __init__(self, peleador1, peleador2):
        self.peleador1 = peleador1
        self.peleador2 = peleador2

    def simular_pelea(self, pelea):
        primero, segundo = self.definir_turnos(pelea)
        longitud_maxima = max(
            len(pelea[self.peleador1.id]["movimientos"]),
            len(pelea[self.peleador2.id]["movimientos"]),
        )

        for i in range(longitud_maxima):
            if i < len(pelea[primero.id]["movimientos"]):
                energia = self.golpes(
                    primero,
                    segundo,
                    pelea[primero.id]["golpes"][i],
                    pelea[primero.id]["movimientos"][i],
                )
                self.golpear(segundo, energia)
                if segundo.vida <= 0:
                    print(
                        f"{primero.nombre} gana la pelea y aun le queda {primero.vida} de energía"
                    )
                    break
            if i < len(pelea[segundo.id]["movimientos"]):
                energia = self.golpes(
                    segundo,
                    primero,
                    pelea[segundo.id]["golpes"][i],
                    pelea[segundo.id]["movimientos"][i],
                )
                self.golpear(primero, energia)
                if primero.vida <= 0:
                    print(
                        f"{segundo.nombre} gana la pelea y aun le queda {segundo.vida} de energía"
                    )
                    break

    def golpes(self, atacante, defensor, golpe, movimiento):
        for g in atacante.golpes:
            if movimiento + golpe == g.combinacion and movimiento:
                mensaje = g.mensaje + " " + g.nombre if g.nombre else g.mensaje
                print(f"{atacante.nombre} {mensaje}")
                return g.energia
            elif golpe and golpe.endswith(g.combinacion):
                mensaje = g.mensaje + " " + defensor.nombre
                print(f"{atacante.nombre} {mensaje}")
                return g.energia
        if movimiento:
            print(f"{atacante.nombre} se mueve")
        return 0

    def golpear(self, defensor, golpe):
        defensor.vida -= golpe

    def definir_turnos(self, pelea):
        p1_movimientos = len(pelea[self.peleador1.id]["movimientos"][0])
        p1_golpes = len(pelea[self.peleador1.id]["golpes"][0])
        p2_movimientos = len(pelea[self.peleador2.id]["movimientos"][0])
        p2_golpes = len(pelea[self.peleador2.id]["golpes"][0])

        p1_total = p1_movimientos + p1_golpes
        p2_total = p2_movimientos + p2_golpes

        if p1_total < p2_total:
            return self.peleador1, self.peleador2
        elif p1_total > p2_total:
            return self.peleador2, self.peleador1
        elif p1_movimientos > p2_movimientos:
            return self.peleador2, self.peleador1
        else:
            return self.peleador1, self.peleador2


def setear_pelea():
    peleador1 = Peleador("Tony", 6, 1)
    peleador2 = Peleador("Arnold", 6, 2)
    peleador1.anadir_golpe("Taladoken", "DSDP", 3, "usa un")
    peleador1.anadir_golpe("Remuyuken", "SDK", 2, "conecta un")
    peleador1.anadir_golpe("Puño", "P", 1, "le da un puñetazo al pobre")
    peleador1.anadir_golpe("Patada", "K", 1, "da una patada a")

    peleador2.anadir_golpe("Remuyuken", "SAK", 3, "conecta un")
    peleador2.anadir_golpe("Taladoken", "ASAP", 2, "usa un")
    peleador2.anadir_golpe("Puño", "P", 1, "le da un puñetazo al pobre")
    peleador2.anadir_golpe("Patada", "K", 1, "da una patada a")

    pelea = Pelea(peleador1, peleador2)

    return pelea


def main():
    pelea = setear_pelea()
    pelea.simular_pelea(
        {
            "player1": {
                "movimientos": ["D", "DSD", "S", "DSD", "SD"],
                "golpes": ["K", "P", "P", "K", "P"],
            },
            "player2": {
                "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
                "golpes": ["K", "", "K", "P", "P"],
            },
        }
    )
    pelea = setear_pelea()
    pelea.simular_pelea(
        {
            "player1": {
                "movimientos": ["SDD", "DSD", "SA", "DSD"],
                "golpes": ["K", "P", "K", "P"],
            },
            "player2": {
                "movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"],
                "golpes": ["P", "K", "K", "K", "P", "K"],
            },
        }
    )
    pelea = setear_pelea()
    pelea.simular_pelea(
        {
            "player1": {"movimientos": ["DSD", "S"], "golpes": ["P", ""]},
            "player2": {
                "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
                "golpes": ["P", "", "P", "K", "K", "K"],
            },
        }
    )


if __name__ == "__main__":
    main()
