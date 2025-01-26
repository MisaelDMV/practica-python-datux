class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []

    def asignar_horario(self, hora):
        if hora in self.horarios:
            return False
        self.horarios.append(hora)
        return True


class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []
        self.conductor_asignado = None

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, hora):
        if hora in self.horarios:
            return False
        self.horarios.append(hora)
        return True

    def asignar_conductor(self, conductor):
        self.conductor_asignado = conductor


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, placa):
        nuevo_bus = Bus(placa)
        self.buses.append(nuevo_bus)

    def agregar_conductor(self, nombre):
        nuevo_conductor = Conductor(nombre)
        self.conductores.append(nuevo_conductor)

    def asignar_ruta_a_bus(self, placa, ruta):
        for bus in self.buses:
            if bus.placa == placa:
                bus.asignar_ruta(ruta)
                return True
        return False

    def registrar_horario_a_bus(self, placa, hora):
        for bus in self.buses:
            if bus.placa == placa:
                return bus.registrar_horario(hora)
        return False

    def asignar_horario_a_conductor(self, nombre, hora):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor.asignar_horario(hora)
        return False

    def asignar_bus_a_conductor(self, placa, nombre, hora):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                if hora in conductor.horarios:
                    return False

                for bus in self.buses:
                    if bus.placa == placa and hora in bus.horarios:
                        conductor.asignar_horario(hora)
                        bus.asignar_conductor(conductor)
                        return True
        return False

    def menu(self):
        while True:
            print("------BIENVENIDO AL MENÚ-------")
            print("1.Agregar bus")
            print("2.Agregar ruta a bus")
            print("3.Registrar horario a bus")
            print("4.Agregar conductor")
            print("5.Agregar horario a conductor")
            print("6.Asignar bus a conductor")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa = input("Ingrese la placa del bus: ")
                self.agregar_bus(placa)
                print("Bus agregado.")

            elif opcion == "2":
                placa = input("Ingrese la placa del bus: ")
                ruta = input("Ingrese la ruta del bus: ")
                if self.asignar_ruta_a_bus(placa, ruta):
                    print("Ruta asignada.")
                else:
                    print("Bus no encontrado.")

            elif opcion == "3":
                placa = input("Ingrese la placa del bus: ")
                hora = input("Ingrese el horario (hora:minuto): ")
                if self.registrar_horario_a_bus(placa, hora):
                    print("Horario registrado.")
                else:
                    print("Horario ya registrado o bus no encontrado.")

            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                self.agregar_conductor(nombre)
                print("Conductor agregado.")

            elif opcion == "5":
                nombre = input("Ingrese el nombre del conductor: ")
                hora = input("Ingrese el horario (hora:minuto): ")
                if self.asignar_horario_a_conductor(nombre, hora):
                    print("Horario asignado.")
                else:
                    print("Conductor no encontrado u horario ya asignado.")

            elif opcion == "6":
                placa = input("Ingrese la placa del bus: ")
                nombre = input("Ingrese el nombre del conductor: ")
                hora = input("Ingrese el horario (hora:minuto): ")
                if self.asignar_bus_a_conductor(placa, nombre, hora):
                    print("Bus asignado al conductor exitosamente.")
                else:
                    print("Conductor ocupado, bus no encontrado u horario inválido.")

            else:
                print("Esta opción no extiste, intentelo de nuevo.")


if __name__ == "__main__":
    admin = Admin()
    admin.menu()
