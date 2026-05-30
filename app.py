from timetrack import calculate_hours


def main():
    print("TimeTrack Pro")
    print("-" * 20)

    employee = input("Employee name: ")

    start = float(input("Start hour: "))
    end = float(input("End hour: "))

    hours = calculate_hours(start, end)

    print()
    print(f"Employee: {employee}")
    print(f"Hours worked: {hours}")


if __name__ == "__main__":
    main()