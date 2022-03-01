a = int(input('inserisci un intero: '))
b = int(input('inserisci un intero: '))
c = int(input('inserisci un intero: '))

if (a and b and c) > 0:
    if a < (b + c) and b < (c + a) and c < (b + a):
        if a == b == c:
            print('ok, hai inserito un triangolo equilatero')

        elif (a == b != c) or (b == c != a) or (c == a != b):
            print('ok, hai inserito un triangolo isoscele')

        elif a != b != c:
            print('ok, hai inserito un triangolo scaleno')

    else:
        print('i dati inseriti non sono validi') #se uno non è minore della somma degli altri
else:
    print('i dati inseriti non sono validi') #se non sono maggiori di 0




