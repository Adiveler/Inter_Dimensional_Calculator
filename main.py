import convertor
from convertor import InterDimensionalConvertor as hac

if __name__ == '__main__':
    c = hac(45)
    c.set_human_num(109)
    print(c)
    c.set_alien_num('-6[42]')
    print(c)

    d = hac(6)
    convertor.alien_to_alien(c, d)
    print(d)
    print(convertor.alien_to_alien_number(d, 9))

    scan = int(input("Enter number for new number-base: "))
    t = hac(scan)
    h_number = int(input("Enter human number: "))
    t.set_human_num(h_number)
    print(t)
    a_number = input("Enter alien number from that base: ")
    t.set_alien_num(a_number)
    print(t)
