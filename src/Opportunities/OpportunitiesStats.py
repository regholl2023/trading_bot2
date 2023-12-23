import yfinance as yf
from src.Opportunities.Opportunities import Opportunities

# This class calculates stats for the days opportunities - individual methods which are called in a get_stats method
# Should I have an individual class that has the concept of an Opportunity, which can have stats calculated for it, then OpportunitiesStats calculates it for all of them?

class OpportunitiesStats:
    
    def __init__(self, opportunities:Opportunities=None) -> None:

        self.opportunities = opportunities
        self.tickers = list(opportunities["yf_ticker"])
    