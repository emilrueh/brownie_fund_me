from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entrance fee is: {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})

    print("")
    print("------")
    print(f"Entrance fee: {entrance_fee}")
    print(f"Contract balance: {fund_me.addressToAmountFunded(account.address)}")
    print("------")
    print("")


def withdraw():

    fund_me = FundMe[-1]
    account = get_account()

    print("Withdrawing...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
