import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.calculations import add, BankAccount

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

def test_add():
    print("testing add functions")
    # sum = add(5, 3)
    assert add(5,3) == 8


def test_bank_set_initial_amount():
    bank_account= BankAccount(50)
    print("testing bank account set initial amount")
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
     print("testing bank account default amount")
     assert zero_bank_account.balance == 0

def test_withdraw():
    bank_account= BankAccount(100)
    bank_account.withdraw(50)
    print("testing bank account withdraw")
    assert bank_account.balance == 50

def test_deposit():
    bank_account= BankAccount(100)
    bank_account.deposit(50)
    print("testing bank account deposit")

def test_collect_interest():
    bank_account= BankAccount(100)
    bank_account.collect_interest()
    print("testing bank account collect interest")
    assert round(bank_account.balance, 6) == 110


 