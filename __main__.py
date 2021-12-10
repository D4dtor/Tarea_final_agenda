from contacto import Contacto
from agenda import Agenda

def crearAgendaPrueba():
    c1 = Contacto("Manuel", "622 233 658","ManeBetis@gmail.com")
    c2 = Contacto("Antonio", "681 639 470", "FuentesOnFire@gmail.com")
    c3 = Contacto("Estegen10", "622 465 458", "brawhallaenjoyer@gmail.com")
    a = Agenda()
    a.agregar_contacto(c1)
    a.agregar_contacto(c2)
    a.agregar_contacto(c3)
    return a

if __name__ == '__main__':
    a = crearAgendaPrueba()
    a.abrir_agenda()







    