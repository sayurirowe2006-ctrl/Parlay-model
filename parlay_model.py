from dataclasses import dataclass
import math

@dataclass
class ParlayLeg:
    name: str
    prob: float       # your model win probability (0–1)
    odds: float       # decimal odds (example: 1.91 for -110)

def parlay_ev(legs):
    total_prob = math.prod([leg.prob for leg in legs])
    total_odds = math.prod([leg.odds for leg in legs])
    ev = total_prob * (total_odds - 1) - (1 - total_prob)
    return {
        "legs": [leg.name for leg in legs],
        "probability": round(total_prob, 4),
        "decimal_odds": round(total_odds, 3),
        "ev_per_$1": round(ev, 4)
    }

# Example test
legs = [
    ParlayLeg("AAPL > 247", prob=0.58, odds=1.91),
    ParlayLeg("TSLA > 430", prob=0.55, odds=2.20),
    ParlayLeg("NFLX < 1250", prob=0.60, odds=1.95)
]

print(parlay_ev(legs))
