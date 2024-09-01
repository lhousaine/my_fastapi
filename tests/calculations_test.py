import pytest
from app.calculations import add, substruct, multiply, devide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected",[
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16),
])
def test_add(num1,num2,expected):
    print('testing add function')
    sum = add(num1, num2)
    
    assert sum== expected
    
def test_substruct():
    print('testing add function')
    res = substruct(5, 3)
    
    assert res == 2
    
    
def test_multiply():
    print('testing add function')
    res = multiply(4, 3)
    
    assert res==12
    
def test_devide():
    print('testing add function')
    res = devide(18, 3)
    
    assert res==6
    
def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance==50
    
def test_bank_default_initial_amount(zero_bank_account):
    assert zero_bank_account.balance==0
    
def test_bank_withdraw_amount(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance==30
    
def test_bank_deposit_amount(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance==70
    
def test_bank_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6)==55
    

@pytest.mark.parametrize("deposited, withdraw, expected",[
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transaction(zero_bank_account,deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance==expected
    
def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
    