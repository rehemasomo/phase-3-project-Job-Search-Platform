from create_tables import Database
from cli import main_menu

def main():
    db = Database('database.db')
    db.create_tables()
    main_menu()

if __name__ == '__main__':
    main()