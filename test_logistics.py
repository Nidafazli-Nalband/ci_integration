from src.logistics import (
    average_delivery_days,
    delayed_shipments,
    delivery_rate,
    summarize,
)


SAMPLE = [
    {"id": "1", "status": "Delivered", "delivery_days": "3"},
    {"id": "2", "status": "Delivered", "delivery_days": "5"},
    {"id": "3", "status": "Delayed", "delivery_days": "8"},
    {"id": "4", "status": "Delivered", "delivery_days": "4"},
]


def test_delivery_rate():
    assert delivery_rate(SAMPLE) == 75.0


def test_average_delivery_days():
    assert average_delivery_days(SAMPLE) == 5.0


def test_delayed_shipments():
    assert len(delayed_shipments(SAMPLE)) == 1


def test_empty_delivery_rate():
    assert delivery_rate([]) == 0.0


def test_summary():
    result = summarize(SAMPLE)
    assert result["total_shipments"] == 4
    assert result["delayed_shipments"] == 1
