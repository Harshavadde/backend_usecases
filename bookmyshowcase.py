import threading
import time

class Database:
    def __init__(self):
        self.db={1:'Available',2:'Available',3:'Available',
                 4:'Available',5:'Available',6:'Available' }

        self.stack = []
        self.lock = threading.Lock()

    def show_all_seats(self):
        print("\nCurrent seat status:")
        for seat, status in self.db.items():
            print(f"Seat {seat}: {status}")
        print()

    def show_seat(self, seat):
        if seat not in self.db:
            print("Seat does not exist\n")
            return
        print(f"Seat {seat}: {self.db[seat]}\n")

    def add(self,seat):
        with lock:
            if seat not in self.db:
                print("Seat does not exist\n")
                return
            if self.db[seat] != 'Available':
                print("Seat is already booked, cannot add to stack")
                return
            if seat in self.stack:
                print("Seat is already added to the stack")
                return
            self.stack.append(seat)
            print("Seat successfully added to the stack")

    def book_seat(self, user_name, seat):
        with self.lock:
            print(f"{user_name} is trying to book Seat {seat}...")

            if seat not in self.db:
                print("Seat does not exist\n")
                return

            if self.db[seat] != "Available":
                print(f"{user_name}: Seat {seat} is NOT available ({self.db[seat]})\n")
                return

            print(f"{user_name} got the lock. Processing booking...")
            time.sleep(2)

            self.db[seat] = f"Booked by {user_name}"
            self.stack.append(seat)
            print(f"{user_name} successfully booked Seat {seat}\n")

    def cancel_seat(self, user_name, seat):
        with self.lock:
            print(f"{user_name} is trying to cancel Seat {seat}...")

            if seat not in self.db:
                print("Seat does not exist\n")
                return

            if not str(self.db[seat]).startswith("Booked"):
                print(f"{user_name}: Seat {seat} is not currently booked. Cannot cancel.\n")
                return

            print(f"{user_name} cancelled Seat {seat}. It will become AVAILABLE again in 15 seconds.")
            self.db[seat] = "Cancelling..."

            if seat in self.stack:
                self.stack.remove(seat)
            t = threading.Thread(target=self.afterdelay, args=(seat,))
            t.start()
            print()

    def afterdelay(self, seat):
        time.sleep(15)
        with self.lock:
            self.db[seat] = "Available"
            print(f"Seat {seat} is now AVAILABLE book again now.\n")

def user_flow(db, user, seat):
    db.book_seat(user, seat)
    time.sleep(5)
    db.cancel_seat(user, seat)

obj = Database()
obj.show_all_seats()
t1 = threading.Thread(target=user_flow, args=(obj, "User-1", 5))
t2 = threading.Thread(target=user_flow, args=(obj, "User-2", 6))
t1.start()
t2.start()
t1.join()
t2.join()
obj.show_all_seats()



