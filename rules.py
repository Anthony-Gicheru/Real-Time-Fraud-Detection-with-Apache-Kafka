def is_fraud(transaction):
    # Simple rule: flag if amount > 1000 and from high-risk country
    high_risk_countries = ["Nigeria",
    "India",
    "Russia",
    "China",
    "Philippines",
    "South Africa",
    "Brazil",
    "United States",
    "United Kingdom",
    "Canada"]
    return (
        transaction['amount'] > 1000 and
        transaction['location'] in high_risk_countries
    )
