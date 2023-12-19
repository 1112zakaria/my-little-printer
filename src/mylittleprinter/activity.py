
class TradeAction(object):
    def __init__(self, ticker: str, qty: int, price: float):
        self.ticker: str = ticker
        self.qty: int = qty
        self.price: float = price
        self.trade_value: float = None
    
class BuyAction(TradeAction):
    def __init__(self, ticker: str, qty: int, price: float):
        super().__init__(ticker, qty, price)
        self.trade_value = -1 * self.qty * self.price
    
class SellAction(TradeAction):
    def __init__(self, ticker: str, qty: int, price: float):
        super().__init__(ticker, qty, price)
        self.trade_value = self.qty * self.price

class Activity(object):
    def __init__(self):
        # TODO: implement loading activity from file or db?
        self.actions: list[TradeAction] = []
        self.total_profit = 0

    def addTrade(self, action: TradeAction) -> None:
        self.actions += [action]
        self.total_profit += action.trade_value
    
    def getTotalProfit(self) -> float:
        return self.total_profit
