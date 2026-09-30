def process_premium_payment(amount, callback):

    print("Processing premium payment:", amount)
    print("Payment successful!")
    callback(amount)


def payment_confirmation(amount):
    print("Premium payment confirmed:", amount)


process_premium_payment(25000, payment_confirmation)