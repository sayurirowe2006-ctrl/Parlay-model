legs = [
    ParlayLeg("AAPL over 250", prob=0.58, american_odds=-110),
    ParlayLeg("TSLA over 430", prob=0.55, american_odds=+120),
    ParlayLeg("NFLX under 1250", prob=0.6, american_odds=-105),
]
best, all_results = best_parlay_subset(legs, max_size=3, objective="kelly")
print(best)
