import os
import pickle
import random

FILE_NAME = "ticket.dat"

def calculate_price(mode: str, distance: int) -> tuple[int, tuple[int, int]]:
    """Return (price, ticket‑id‑range) based on travel *mode* and *distance*."""
    mode = mode.lower()

    if mode == "car":
        if distance <= 300:
            return 2450, (100, 160)
        elif distance <= 600:
            return 4750, (100, 160)
        elif distance <= 1000:
            return 6150, (100, 160)
        else:
            return 8050, (100, 160)

    elif mode == "bus":
        if distance <= 300:
            return 1750, (210, 320)
        elif distance <= 600:
            return 3250, (210, 320)
        elif distance <= 1000:
            return 5150, (210, 320)
        else:
            return 6350, (210, 320)

    elif mode == "train":
        if distance <= 300:
            return 1950, (410, 655)
        elif distance <= 600:
            return 3450, (410, 655)
        elif distance <= 1000:
            return 5250, (410, 655)
        else:
            return 7150, (410, 655)

    elif mode == "aeroplane":
        if distance <= 300:
            return 5450, (1000, 2000)
        elif distance <= 600:
            return 8750, (1000, 2000)
        elif distance <= 1000:
            return 14_150, (1000, 2000)
        else:
            return 21_050, (1000, 2000)

    else:
        raise ValueError("Invalid mode of travel.")

def book_tickets() -> None:
    try:
        n = int(input("Enter number of passengers: "))
    except ValueError:
        print(" Not a number; cancelling.")
        return

    with open(FILE_NAME, "ab") as fw: 
        for _ in range(n):
            nm   = input("Passenger name: ")
            des  = input("Destination: ")
            try:
                dis = int(input("Distance (km): "))
            except ValueError:
                print(" Distance must be a number; skipping this passenger.")
                continue
            date = input("Date (DD/MM/YYYY): ")
            mt   = input("Mode (car / bus / train / aeroplane): ")

            try:
                price, tid_range = calculate_price(mt, dis)
            except ValueError as err:
                print(err)
                continue

            tid = random.randint(*tid_range)
            record = [tid, nm, des, dis, date, mt.lower(), price]
            pickle.dump(record, fw)
            print(f" Booking confirmed!  Ticket ID: {tid}")


def view_details() -> None:
    try:
        with open(FILE_NAME, "rb") as fr:
            print("\n--- All Bookings ---")
            any_record = False
            while True:
                try:
                    print(pickle.load(fr))
                    any_record = True
                except EOFError:
                    break
            if not any_record:
                print("No bookings yet.")
    except FileNotFoundError:
        print("No bookings yet.")


def update_details() -> None:
    try:
        tid = int(input("Ticket ID to update: "))
    except ValueError:
        print(" Ticket ID must be an integer.")
        return

    updated = False
    try:
        with open(FILE_NAME, "rb") as fr, open("temp.dat", "wb") as fw:
            while True:
                try:
                    rec = pickle.load(fr)
                except EOFError:
                    break

                if rec[0] == tid:
                    print("Enter NEW details:")
                    nm  = input("Passenger name: ")
                    des = input("Destination: ")
                    dis = int(input("Distance (km): "))
                    date= input("Date (DD/MM/YYYY): ")
                    mt  = input("Mode (car / bus / train / aeroplane): ")

                    try:
                        price, _ = calculate_price(mt, dis)
                    except ValueError as err:
                        print(err, "Keeping old record.")
                        pickle.dump(rec, fw)
                        continue

                    new_rec = [tid, nm, des, dis, date, mt.lower(), price]
                    pickle.dump(new_rec, fw)
                    updated = True
                    print(" Booking updated.")
                else:
                    pickle.dump(rec, fw)
    except FileNotFoundError:
        print("No bookings file found.")
        return

    if updated:
        os.remove(FILE_NAME)
        os.rename("temp.dat", FILE_NAME)
    else:
        os.remove("temp.dat")
        print("Ticket ID not found.")


def search_details() -> None:
    try:
        tid = int(input("Ticket ID to search: "))
    except ValueError:
        print(" Ticket ID must be an integer.")
        return

    found = False
    try:
        with open(FILE_NAME, "rb") as fr:
            while True:
                try:
                    rec = pickle.load(fr)
                    if rec[0] == tid:
                        print(" Ticket found:", rec)
                        found = True
                        break
                except EOFError:
                    break
    except FileNotFoundError:
        pass

    if not found:
        print("Ticket ID not present.")


def cancel_booking() -> None:
    try:
        tid = int(input("Ticket ID to cancel: "))
    except ValueError:
        print(" Ticket ID must be an integer.")
        return

    cancelled = False
    try:
        with open(FILE_NAME, "rb") as fr, open("temp.dat", "wb") as fw:
            while True:
                try:
                    rec = pickle.load(fr)
                except EOFError:
                    break

                if rec[0] == tid:
                    cancelled = True  
                else:
                    pickle.dump(rec, fw)
    except FileNotFoundError:
        print("No bookings file found.")
        return

    if cancelled:
        os.remove(FILE_NAME)
        os.rename("temp.dat", FILE_NAME)
        print(" Booking cancelled.")
    else:
        os.remove("temp.dat")
        print("Ticket ID not present.")


def main() -> None:
    while True:
        print(
            "\nTRAVEL AGENCY MENU"
            "\n1. Book Tickets"
            "\n2. View All Bookings"
            "\n3. Update Booking"
            "\n4. Search Booking"
            "\n5. Cancel Booking"
            "\n6. Exit"
        )
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print(" Enter a number between 1‑6.")
            continue

        if   choice == 1: book_tickets()
        elif choice == 2: view_details()
        elif choice == 3: update_details()
        elif choice == 4: search_details()
        elif choice == 5: cancel_booking()
        elif choice == 6:
            print("Good‑bye!")
            break
        else:
            print(" Enter a number between 1‑6.")


if __name__ == "__main__":
    main()






