from alerts import crypto_prices

def test_crypto_prices_sube():
    resultado = crypto_prices(100, 50, 2, "Bitcoin")
    assert "subió" in resultado

def test_crypto_prices_baja():
    resultado = crypto_prices(50, 100, 2, "Bitcoin")
    assert "bajó" in resultado

def test_crypto_prices_none():
    resultado = crypto_prices(50, 50, 2, "Bitcoin")
    assert resultado is None

