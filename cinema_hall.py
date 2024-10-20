class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    @classmethod
    def view_show_list(cls):
        shows = []
        for hall in cls.__hall_list:
            shows.extend(hall.view_show_list())
        return shows


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self)

        self.seats[hall_no] = [['0' for _ in range(cols)] for _ in range(rows)]

    def entry_show(self, ID, movie_name, time):
        self.__show_list.append((movie_name, ID, time))

    def book_seats(self, hall_no, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Error: Seat is invalid.")
        elif self.seats[hall_no][row][col] == '1':
            print("Error: Seat is already booked.")
        else:
            self.seats[hall_no][row][col] = '1'
            print(f'Seat ({row + 1}, {col + 1}) booked successfully.')

    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self):
        seat_matrix = self.seats[self.hall_no]
        print("Available seats:")
        for r in range(self.rows):
            print(' '.join(seat_matrix[r]))

hall1 = Hall(5, 5, '201')
hall2 = Hall(5, 7, '202')

hall1.entry_show(101, 'Avengers: Endgame', '18:00')
hall1.entry_show(102, 'The Lion King', '19:00')
hall2.entry_show(103, 'Inception', '20:00')
hall2.entry_show(104, 'Toy Story 4', '21:00')

while True:
    print("\nMenu:")
    print("1. View Show List")
    print("2. View Available Seats")
    print("3. Book Seats")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        show_list = Star_Cinema.view_show_list()
        print("Show List:")
        for movie, ID, time in show_list:
            print(f'Movie Name: {movie}, ID: {ID}, Time: {time}')

    elif choice == '2':
        hall_id = input("Enter hall ID (e.g., 201): ")
        hall = next((h for h in Star_Cinema._Star_Cinema__hall_list if h.hall_no == hall_id), None)
        if hall:
            hall.view_available_seats()
        else:
            print("Error: Hall not found.")

    elif choice == '3':
        hall_id = input("Enter hall ID (e.g., 201): ")
        hall = next((h for h in Star_Cinema._Star_Cinema__hall_list if h.hall_no == hall_id), None)
        if hall:
            num_seats = int(input("How many seats do you want to book? "))
            for _ in range(num_seats):
                row = int(input("Row: ")) - 1
                col = int(input("Column: ")) - 1
                hall.book_seats(hall_id, row, col)
        else:
            print("Error: Hall not found.")

    else:
        print("Exiting...")
        break