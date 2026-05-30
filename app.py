from timetrack import calculate_hours


def main():
    print("TimeTrack Pro")
    print("=" * 25)

    employee = input("Employee name: ")

    start = float(input("Start hour (24h format): "))
    end = float(input("End hour (24h format): "))

    hours = calculate_hours(start, end)

    print("\nWork Summary")
    print("-" * 25)
    print(f"Employee: {employee}")
    print(f"Start time: {start}")
    print(f"End time: {end}")
    print(f"Hours worked: {hours}")


if __name__ == "__main__":
    main()