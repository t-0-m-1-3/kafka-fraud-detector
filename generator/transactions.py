"""Utilities to model money transactions."""

from random import choices, randint
from string import ascii_letters, digits

account_chars: str = digits + ascii_letters


def _random_account_id():
    """Return a random account number made of 12 characters."""
    return str(''.join(choices(account_chars, k=12)))


def _random_amount():
    """Return a random amount between 1.00 and 1000.00."""
    return float(randint(100, 100000) / 100)


def create_random_transaction():
    """Create a fake, randomised transaction."""
    return dict({
        'source': _random_account_id(),
        'target': _random_account_id(),
        'amount': _random_amount(),
        # Keep it simple: it's all euros
        'currency': 'EUR',
    })
