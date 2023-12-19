
import sched
import time
from mylittleprinter.activity import Activity
from mylittleprinter.portfolio import AbstractPortfolio, SimulatedPortfolio

RUN_TASK_DELAY = 5
RUN_TASK_PRIORITY = 1

class Agent(object):
    def __init__(self, cash: int) -> None:
        self.portfolio: AbstractPortfolio = SimulatedPortfolio(cash)
        self.activity: Activity = Activity()
        self.scheduler = sched.scheduler(time.monotonic, time.sleep)

        self._init_task_scheduler()

    def run_task(self) -> None:
        """
        Run periodic task.
        """
        print("Running periodic task...")
        # add next task call to the queue
        self.scheduler.enter(RUN_TASK_DELAY, RUN_TASK_PRIORITY, self.run_task)

    def _init_task_scheduler(self):
        self.scheduler.enter(RUN_TASK_DELAY, RUN_TASK_PRIORITY, self.run_task)

    def run(self) -> None:
        """
        Run periodic task scheduler.
        """
        print("Starting task scheduler...")
        self.scheduler.run()
        
        

