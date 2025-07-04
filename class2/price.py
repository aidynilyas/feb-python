discount = 0


def calculate_tax(price):
    tax = price *0.08
    return tax

def apply_discount(price, discount):
    subtotal = price - (price * discount)
    return subtotal

