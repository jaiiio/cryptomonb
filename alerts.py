def crypto_prices(precio_actual, precio_anterior, umbral, moneda):
    cambio = ((precio_actual - precio_anterior) / precio_anterior) * 100
    if cambio < -umbral:
        return f"ALERTA: {moneda} bajó {cambio:.2f}%"
    elif cambio > umbral:
        return f"ALERTA: {moneda} subió {cambio:.2f}%"
    else:
        return None
