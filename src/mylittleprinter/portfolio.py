

class AbstractPortfolio(object):

    def __init__(self, cash: float):
        # TODO: use appropriate currencies representations?
        # TODO: let agent own multiple portfolios? Or run separate agent instances for each portfolio?
        self.cash = cash
        self.assets: dict = dict()

    def buy(self, ticker: str, qty: int, price: float) -> bool:
        return NotImplementedError
    
    def sell(self, ticker: str, qty: int, price: float) -> bool:
        return NotImplementedError
    

class SimulatedPortfolio(AbstractPortfolio):
    def __init__(self, cash: float):
        super().__init__(cash)
    
    def buy(self, ticker: str, qty: int, price: float) -> bool:
        """
        Buy if sufficient cash.
        """
        total_value = qty * price
        if total_value > self.cash or qty <= 0:
            # insufficient cash
            return False
        
        currently_owned = self.assets.get(ticker, 0)
        self.assets[ticker] = currently_owned + qty
        self.cash -= total_value
        return True
    
    def sell(self, ticker: str, qty: int, price: float) -> bool:
        """
        Sell if asset ticker and qty owned.
        """
        total_value = qty * price
        qty_owned = self.assets.get(ticker, 0)
        if qty > qty_owned:
            # invalid sell qty
            return False
        
        new_qty = qty_owned - qty
        self.assets[ticker] = new_qty
        self.cash += total_value
        if new_qty <= 0:
            del self.assets[ticker]
        return True
    
    
    