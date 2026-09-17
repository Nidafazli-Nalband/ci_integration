import csv
from pathlib import Path


def load_shipments(file_path):
    with Path(file_path).open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def delivery_rate(shipments):
    if not shipments:
        return 0.0
    delivered = sum(row["status"].strip().lower() == "delivered" for row in shipments)
    return delivered / len(shipments) * 100


def average_delivery_days(shipments):
    if not shipments:
        return 0.0
    total = sum(float(row["delivery_days"]) for row in shipments)
    return total / len(shipments)


def delayed_shipments(shipments, threshold=5):
    return [
        row for row in shipments
        if float(row["delivery_days"]) > threshold
    ]


def summarize(shipments):
    return {
        "total_shipments": len(shipments),
        "delivery_rate": delivery_rate(shipments),
        "average_delivery_days": average_delivery_days(shipments),
        "delayed_shipments": len(delayed_shipments(shipments)),
    }
