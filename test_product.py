import pytest
from products import Product


def test_create_valid_product():
    # Prüft, ob ein normales Produkt korrekt erstellt wird und aktiv ist
    macbook = Product("MacBook Air M2", price=1450, quantity=10)
    assert macbook.name == "MacBook Air M2"
    assert macbook.price == 1450
    assert macbook.get_quantity() == 10
    assert macbook.is_active() is True


def test_product_deactivates_when_quantity_reaches_zero():
    # Wenn der gesamte Bestand gekauft wird, muss is_active() auf False wechseln
    bose = Product("Bose Earbuds", price=250, quantity=3)
    
    total_price = bose.buy(3)
    
    assert total_price == 750
    assert bose.get_quantity() == 0
    assert bose.is_active() is False


def test_buy_inactive_product_raises_error():
    # Ein bereits deaktiviertes Produkt darf nicht mehr gekauft werden können
    pixel = Product("Google Pixel 7", price=500, quantity=5)
    pixel.deactivate()
    
    with pytest.raises(Exception):
        pixel.buy(1)


@pytest.mark.parametrize("invalid_price", [-10, -0.01])
def test_create_product_with_negative_price_raises_error(invalid_price):
    # Negative Preise müssen beim Erstellen abgefangen werden
    with pytest.raises(ValueError):
        Product("Fehlerhaftes Produkt", price=invalid_price, quantity=5)


@pytest.mark.parametrize("invalid_quantity", [-1, -100])
def test_create_product_with_negative_quantity_raises_error(invalid_quantity):
    # Negative Stückzahlen müssen beim Erstellen abgefangen werden
    with pytest.raises(ValueError):
        Product("Fehlerhaftes Produkt", price=100, quantity=invalid_quantity)


def test_create_product_with_empty_name_raises_error():
    # Leere Namen (oder nur Leerzeichen) sollten nicht erlaubt sein
    with pytest.raises(ValueError):
        Product("", price=100, quantity=5)
