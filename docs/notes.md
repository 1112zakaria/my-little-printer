# Some random jot notes

Potential data feeds:
- tickers
- technicals
- market sentiment
- fundamentals
- Q: is there a way to subscribe to live market feed, like a websocket connection?

This info above seems to be retrievable via openBB api, I'd have to check how fast/slow it is...

Other thing to consider would be testing/backtesting of the system
- I would probably have to test fo ra good while before going live
- It's probably important that you do not test in a way that overfits on past historical data
- Is there a way to build a system that, while not knowing what prices changes will happen in the future, predicts what
changes will happen and makes trading decisions to optimize for a balance between profit and risk
- Is there a way to automatically identify stocks which are currently undervalued for a long term strategy?
- What would the control feedback loop look like? How will it handle world updates?
- What platform can I use to simulate current time for backtesting?

What about training?

Deployment and updates?
- How do you make a system that is reentrant and safe to stop and startup again?
- Can I deploy on the cloud? Would be nice to not have my computer running all the time
- Should be reliable during trading hours and able to self-start itself up in the event of a crash/failure
- How do I implement graceful shutdown and startup?

Financial background research todo:
- I need some financial knowledge in order to understand somewhat what I am doing...
- Can you implement adequate risk management into your learned/fixed algorithm?
- For initial prototypes, perhaps use basic indicators to buy when oversold and sell with overbought
- How do I know how much is ok to buy at a time?
- How do I know when to close out of a losing position?
- At what percent profit should I close out at?

Software components:
- Agent
- Portfolio
- Activity
- Feed
- How do I make the system configurable to work for both paper trading simulations and real deployments?

Milestone iteration goals:
- 1. Build a basic agent that buys and sells a specific stock based on some criteria in real-time (i.e RSI)
    - Single-asset trading problem
- 2. Improve agent to buy and sell a stock out of a set universe of stocks (i.e S&P 100)
    - Calculate a rating for each stock
- 3. Improve agent to buy/sell multiple stocks concurrently
    - It should know when to sell a position early to take advantage of a better potential financial opportunity, within a threshold of course
    - Portfolio selection problem
- 4. Improve agent to tune its buy/sell timing using AI techniques (reinforcement learning, LSTM)
- 5. Integrate other non-technical analysis criteria into the decision making scoring
    - Fundamentals, news, sentiment, insider trading, sharpe/sortino?
- 6. Implement interface that lets you easily update scoring criteria via configuration