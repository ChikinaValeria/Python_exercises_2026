import requests

def download_tampere_rss(url, filename):
    try:
        print(f"Downloading data from {url}...")
        response = requests.get(url)

        # Проверяем, успешно ли прошел запрос
        response.raise_for_status()

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"File successfully saved as: {filename}")

        # Вывод атрибуции согласно лицензии CC BY 4.0
        print("\n--- Attribution ---")
        print("Source: Latest bulletins from the City of Tampere.")
        print("Maintainer: Viestintäyksikkö.")
        print("License: Creative Commons Attribution 4.0")

    except requests.exceptions.RequestException as e:
        print(f"Error while loading: {e}")
    except IOError as e:
        print(f"Error while writing file: {e}")


rss_url = "https://www.tampere.fi/tampereen-kaupunki/ajankohtaista/tiedotteet/rss.xml.stx"
output_file = "tampere_bulletins.xml"

if __name__ == "__main__":
    download_tampere_rss(rss_url, output_file)