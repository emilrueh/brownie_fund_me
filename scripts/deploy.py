from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from time import sleep

from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy


if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
    gas_price(gas_strategy)


def deploy_fund_me():

    account = get_account()
    print("")
    print(f"Active network: {network.show_active()}")

    # checking API
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    print(f"Price feed: {price_feed_address}")

    # deploying contract
    print(f"Deploying from: {account}")
    print("")
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    sleep(1)

    print(f"Deployed to: {fund_me.address}")
    print("")

    return fund_me


def main():
    sleep(1)
    deploy_fund_me()
