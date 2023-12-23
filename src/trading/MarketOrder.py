from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

class MarketOrder:

    def __init__(self,
                 stock: str=None,
                 quantity: float=None,
                 buy_or_sell: OrderSide=None,
                 time_in_force: TimeInForce=None) -> None:
        
        self.stock = stock
        self.quantity = quantity
        self.buy_or_sell = buy_or_sell
        self.time_in_force = time_in_force

    def create_market_order(self) -> MarketOrderRequest:

        return MarketOrderRequest(
                    symbol=self.stock,
                    qty=self.quantity,
                    side=self.buy_or_sell,
                    time_in_force=self.time_in_force
                    )