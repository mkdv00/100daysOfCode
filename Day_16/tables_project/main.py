from prettytable import PrettyTable


if __name__ == "__main__":
    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electic", "Water", "Fire"])
    print(table)
