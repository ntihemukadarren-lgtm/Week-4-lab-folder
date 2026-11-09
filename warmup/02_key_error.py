# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}
percent = (record["value"]/record["limit"])*100
record["status"] = "OVER_LIMIT" if percent >= 100 else "OK"
print(record["status"])
