import csv

DEFAULT_PRICES = {
    "X-Wing": 10.0,
    "Falcon": 50.80,
    "Tie Fighter": 15.0,
    "Destroyer": 300.59,
    "Light Cruiser": 200.00,
    "Command Cruiser": 300.00
}

class ParkingStation:
    def __init__(self, price_sheet: dict[str, float] | None = None, capacity: int = 10, csv_file_name: str = "parking_lot.csv"):       
        # If price_sheet is None, initialize it as an the DEFAULT_PRICES dictionary
        self.price_sheet = price_sheet if price_sheet is not None else DEFAULT_PRICES.copy() 
        
        # If capacity is None, initialize it as 0
        self.capacity = capacity if capacity is not None else 0       
        self.csv_file_name = csv_file_name   

        # Dictionary to store the parked ships, where the key is the ship name and the value is the ship model                                
        self.parking_lot: dict[str, str] = {}                             

        self.load_from_csv()

    def load_from_csv(self) -> None:
        """
        Load the parking lot data from the csv for reading. If the file does not exist, create it when saving. 
        """
        try:
            with open(self.csv_file_name, "r") as read_file:
                reader = csv.reader(read_file)
                for row in reader:
                    if row:
                        ship_name, ship_model = row
                        self.parking_lot[ship_name] = ship_model
        except FileNotFoundError:
            pass

    def save_to_csv(self) -> None:
        """
        Save the parking lot data to the csv. If the file does not exist, create it.
        """
        with open(self.csv_file_name, "w", newline="") as write_file:
            writer = csv.writer(write_file)
            for ship_name, ship_model in self.parking_lot.items():
                writer.writerow([ship_name, ship_model])


    def park_ship(self, ship_name: str, ship_model: str) -> None:
        """
        Park a ship in the parking lot. If the parking lot is full, print an error message.
        """
        if len(self.parking_lot) >= self.capacity:
            print("ERRO: O pátio está cheio. Não é possível estacionar mais naves.")
            return

        try:
            # Checks if the ship model exists in the price sheet.
            self.price_sheet[ship_model]

            # Add the ship name and model to the parking lot dictionary.
            self.parking_lot[ship_name] = ship_model
            self.save_to_csv()

            print(f'Nave {ship_name} adicionada ao pátio com sucesso!')

        except KeyError:
            # If the ship model does not exist, print an error message.
            print(f'ERRO: O modelo de nave {ship_model} não é aceito.')

        self.save_to_csv()


    def release_ship(self, ship_name: str) -> float:
        """
        Release a ship from the parking lot and calculate the price based on the time it stayied in
        """
        price = 0
        time = get_valid_hours()

        try:
            release_ship_model = self.parking_lot[ship_name]
            price = time * self.price_sheet[release_ship_model]
            release_ship_model = self.parking_lot.pop(ship_name)
            self.save_to_csv()

            return f"O preço a ser pago pela nave {ship_name} é: $${price:,.2f}"
        
        except KeyError:
            print('ERRO: Nave não se encontra no sistema.')
        except ValueError:
            print('ERRO: Valor inválido.')

        

    def display_parking_lot(self) -> None:
        """Display the ships currently in the parking lot"""
        if not self.parking_lot:
            print('O pátio está vazio.')
            return

        print("="*12,"NAVES NO PÁTIO","="*12)
        for ship_name, ship_model in self.parking_lot.items():
            print(f'Nave: {ship_name} | Modelo: {ship_model}')
        print("="*40)

def get_valid_hours() -> float:
    """
    Get a valid number of hours from the user. Don't accept numbers less than or equal to zero.
    If the number is greater than zero but less than one, covert it to minutes.
    Return the number of hoours as a float.
    """
    while True:
        try:
            time = float(input("Quanto tempo (em horas) ficou no pátio? ").strip())
            if time <= 0:
                print('ERRO: O tempo deve ser maior que zero.')
                continue
            return time
        
        except ValueError:
            print("ERRO: Por favor, digite um número inteiro válido.")
