import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook
# import csv


def main():
    strona = 1
    # IMPUT UZYTKOWNIKA
    co_szukać = str(input("Co chcesz wyszukac: "))
    cena = int(input("Podaj maksymalna cene: "))
    strony = int(input("Podaj ilosc stron: "))
    tak = []
    while strony > 0:
        # print(f"Strony {strony}")
        # print(f"Strona {strona}")

        URL = f"https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-{co_szukać.replace(" ", "-")}/?page={strona}&search%5Bfilter_float_price%3Ato%5D={cena}"
        page = requests.get(URL)
        # print(URL)
        # print("\n")

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="hydrate-root")


        ogloszenia = results.find_all("div", class_="css-1sw7q4x")

        for ogloszenie in ogloszenia:
        # Nazwa ogłoszenia
            nazwa_element = ogloszenie.find("h6", class_="css-16v5mdi er34gjf0")
            nazwa = nazwa_element.text if nazwa_element else ""
            
            # Id ogłoszenia
            id_ogloszenia = ogloszenie.get("id", "")

            # Stan
            stan_element = ogloszenie.find("span", class_="css-3lkihg")
            stan = stan_element.text if stan_element else ""

            # Cena
            cena_element = ogloszenie.find("p", class_="css-tyui9s er34gjf0")
            cena = cena_element.text if cena_element else ""
            
            # Link do ogłoszenia
            link_element = ogloszenie.find("a", class_="css-z3gu2d")
            link = f"https://olx.pl{link_element['href']}" if link_element else ""

            tak.append({
                "nazwa": nazwa,
                "id": id_ogloszenia,
                "stan": stan,
                "cena": cena,
                "link": link
            })
        strony -=1
        strona +=1

    # print("TEST")
    keys = tak[0].keys()
    with open('ogloszenia.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = keys
        dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(tak)

    print("Koniec wyszukiwania")

    csv_to_xlsx()
    # print(tak)


    # print(keys)

    # with open('ogloszenia.csv', 'w', encoding='utf-8', newline='') as output_file:
    #     dict_writer = csv.DictWriter(output_file, keys)
    #     dict_writer.writeheader()
    #     dict_writer.writerows(tak)



        # print(ogloszenie.prettify())
    # print(results)

def csv_to_xlsx():
    wb = Workbook()
    ws = wb.active
    with open('ogloszenia.csv', 'r', encoding='utf-8') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save('ogloszenia.xlsx')
    print("Zapisano do pliku ogloszenia.xlsx")

main()