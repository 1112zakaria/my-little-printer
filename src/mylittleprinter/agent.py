
from mylittleprinter.activity import Activity
from mylittleprinter.portfolio import AbstractPortfolio, SimulatedPortfolio

class Agent(object):
    def __init__(self, cash: int) -> None:
        self.portfolio: AbstractPortfolio = SimulatedPortfolio(cash)
        self.activity: Activity = Activity()

    def run_task(self) -> None:
        """
        Run periodic task.
        """
        return NotImplementedError

    def run(self) -> None:
        """
        Run periodic task scheduler.
        """
        return NotImplementedError

