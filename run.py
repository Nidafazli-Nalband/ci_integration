from src.logistics import load_shipments, summarize


if __name__ == "__main__":
    shipments = load_shipments("data/shipments.csv")
    result = summarize(shipments)

    print("Logistics Analytics Summary")
    print("---------------------------")
    print(f"Total shipments: {result['total_shipments']}")
    print(f"Delivery rate: {result['delivery_rate']:.2f}%")
    print(f"Average delivery days: {result['average_delivery_days']:.2f}")
    print(f"Delayed shipments: {result['delayed_shipments']}")
