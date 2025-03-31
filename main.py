from auth_system import register_user, verify_login

def main_menu():
    while True:
        print("\n===== Benutzerverwaltung =====")
        print("1. Registrieren")
        print("2. Login")
        print("3. Beenden")

        choice = input("Auswahl treffen (1-3): ").strip()

        if choice == "1":
            username = input("Benutzername: ").strip()
            password = input("Passwort: ").strip()
            try:
                register_user(username, password)
            except ValueError as e:
                print(f"⚠️ Fehler: {e}")
        elif choice == "2":
            username = input("Benutzername: ").strip()
            password = input("Passwort: ").strip()
            if verify_login(username, password):
                print("✅ Login erfolgreich!")
            else:
                print("❌ Login fehlgeschlagen!")
        elif choice == "3":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte 1, 2 oder 3 eingeben.")

if __name__ == "__main__":
    main_menu()
