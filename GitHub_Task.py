# 3 UŽDUOTIS

import pickle

failo_vardas = 'Biudzetas.pkl'

try:
    with open(failo_vardas, 'rb') as failas:
        duomenys = pickle.load(failas)
except:
    duomenys = {"Pajamos": [], "Išlaidos": []}

# Kuriamas kontekstinis meniu.
while True:
    print("\nPasirinkite pageidaujamą veiksmą iš kontekstinio meniu.")
    veiksmo_meniu = input(
        "\n1.Pridėti pajamas arba išlaidas"
        "\n2.Parodyti duomenis"
        "\n3.Parodyti balansą"
        "\n4.Išeiti"
        "\nJūsų pasirinkimas:"
    )

    # Pridedamos pajamos arba išlaidos.
    if veiksmo_meniu == '1':
        try:
            suma = float(input("Iveskite pajamas, išlaidos įvedamos su '-' ženklu: "))
            duomenys['Išlaidos' if suma < 0 else 'Pajamos'].append(suma)
            with open(failo_vardas, 'wb') as failas:
                pickle.dump(duomenys, failas)
        except:
            print("Klaida: neteisinga įvestis, naudokite tik teigiamus ir neigiamus skaičius.")

    # Terminale parodo įvestus ir išsaugotus duomenis.
    elif veiksmo_meniu == '2':
        print(f"Pajamos: {duomenys[f'Pajamos']}\nIšlaidos: {duomenys['Išlaidos']}")

    # Skaičiuojamas balansas.
    elif veiksmo_meniu == '3':
        print(f"Balansas: {sum(duomenys['Pajamos']) + sum(duomenys['Išlaidos'])} EUR")

    # Programa uždaroma.
    elif veiksmo_meniu == '4':
        print("Programa uždaryta.")
        break

