# import słowników z pliku menu.py
from menu import MENU, zasoby


def wyswietl_stan():
    """Funkcja wyświetla stan zasobników ze składnikami oraz stan kasy"""
    pass


def sprawdz_stan(choice):
    """Funkcja sprawdza czy maszyna posiada wystarczająco półproduktów aby wykonać zamówienie, wyświetla stosowny komunikat jeśli nie"""
    pass


def zliczanie_monet():
    """funkcja zwraca wrzuconą w monetach kwotę"""
    pass


def obsluga_transankcji(choice):
    """funkcja sprawdza czy została wrzucona prawidłowa kwota, i wydaje resztę lub wyswietla komunikat że wrzucona kwota była za mała"""
    pass


def uzyj_skladniki(choice):
    """funkcja pomniejsza stan zasobów przy realizacji zamówienia"""
    pass


def obsluga_zamowienia(choice):
    """funkcja obsługująca zamówienie"""
    pass


def uzupelnij_skladniki():
    '''Funkcja pozwalająca na uzupełnienie zasobników ze składnikami
        do ich maksymalnych stanów'''
    pass


def pokaz_ceny():
    '''Funkcja wyświetlająca ceny dostępnych rodzajów kawy'''
    pass


stan = True
zasoby = zasoby.copy()

while stan:
    order = input('\nJaką ☕ chcesz zamówić? (espresso/latte/cappuccino): ')

    if order == 'off':
        stan = False
    elif order == 'raport':
        wyswietl_stan()
    elif order == 'reset':
        uzupelnij_skladniki()
    elif order == 'ceny':
        pokaz_ceny()
    else:
        obsluga_zamowienia(order)
