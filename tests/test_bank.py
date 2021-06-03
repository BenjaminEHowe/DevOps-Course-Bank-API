"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank, Account


@pytest.fixture
def bank() -> Bank:
    return Bank()


def test_accounts_are_immutable():
    account = Account('Immutable')
    with pytest.raises(Exception):
        # This operation should raise an exception
        account.name = 'Mutable'


def test_bank_creates_empty(bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0


def test_can_create_and_get_account(bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'


def test_cannot_duplicate_accounts(bank):
    bank.create_account('duplicate')
    bank.create_account('duplicate')

    assert len(bank.accounts) == 1


def test_cannot_modify_accounts_set(bank):
    accounts = bank.accounts
    accounts.append(Account('New Account'))

    assert len(bank.accounts) == 0

def test_can_add_transaction(bank):
    assert len(bank.transactions) == 0
    ACCOUNT_NAME = 'Test'
    bank.create_account(ACCOUNT_NAME)
    TRANSACTION_AMOUNT = 1
    bank.add_funds(ACCOUNT_NAME, TRANSACTION_AMOUNT)
    assert len(bank.transactions) == 1
    assert bank.transactions[0].account.name == ACCOUNT_NAME
    assert bank.transactions[0].amount == TRANSACTION_AMOUNT

def test_can_add_negative_transaction(bank):
    assert len(bank.transactions) == 0
    ACCOUNT_NAME = 'Test'
    bank.create_account(ACCOUNT_NAME)
    TRANSACTION_AMOUNT = -1
    bank.add_funds(ACCOUNT_NAME, TRANSACTION_AMOUNT)
    assert len(bank.transactions) == 1
    assert bank.transactions[0].account.name == ACCOUNT_NAME
    assert bank.transactions[0].amount == TRANSACTION_AMOUNT

def test_cannot_transact_non_existant_account(bank):
    ACCOUNT_NAME = 'Test'
    TRANSACTION_AMOUNT = -1
    with pytest.raises(ValueError):
        bank.add_funds(ACCOUNT_NAME, TRANSACTION_AMOUNT)
