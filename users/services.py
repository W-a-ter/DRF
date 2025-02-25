import stripe

import config.settings

stripe.api_key = config.settings.STRIPE_API_KEY


def strip_create_product(obj):
    """Создает продукт в стрипе."""
    return stripe.Product.create(name=obj.title)


def strip_create_price(obj, amount):
    """Создание цены на продукт в стрипе."""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": obj.get("name")},
    )


def strip_create_sessions(price):
    """Создание сессии оплаты в стрипе."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
