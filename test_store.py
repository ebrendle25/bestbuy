import pytest
from products import Product
from store import Store


def test_order_is_atomic_when_second_product_fails():
    # 1. Arrange (Vorbereitung): Store mit zwei Produkten anlegen
    macbook = Product("MacBook Air M2", price=1450, quantity=5)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=2)
    best_buy = Store([macbook, bose])

    # 2. Act & Assert (Ausführen & Fehler prüfen):
    # 1 MacBook ist da (5 >= 1), aber 10 Kopfhörer sind zu viel (2 < 10)
    with pytest.raises(ValueError):
        best_buy.order([(macbook, 1), (bose, 10)])

    # 3. Assert (Zustand nach dem Fehler prüfen):
    # Weder beim MacBook noch bei den Kopfhörern darf Bestand abgezogen worden sein!
    assert macbook.get_quantity() == 5
    assert bose.get_quantity() == 2


def test_order_fails_if_same_product_exceeds_stock_combined():
    # Testet den Spezialfall, dass dasselbe Produkt zweimal im Warenkorb liegt
    # (z. B. 3 + 3 = 6 Stück angefragt, aber nur 5 auf Lager)
    macbook = Product("MacBook Air M2", price=1450, quantity=5)
    best_buy = Store([macbook])

    with pytest.raises(ValueError):
        best_buy.order([(macbook, 3), (macbook, 3)])

    assert macbook.get_quantity() == 5
