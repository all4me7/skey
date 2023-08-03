from jsonpath_ng import jsonpath, parse
from art import tprint
from colorama import Fore
import json
import requests
import os


def main():
    os.system('cls')
    tprint('Search-Key')

    url = input('API Endpoint: ')

    while True:
        target_key = input('Search Key: ')
        response = requests.get(url)
        json_str = response.json()
        data = json.loads(json.dumps(json_str, ensure_ascii=False))

        if target_key:
            try:
                jsonpath_expression = parse(f'$..{target_key}')
                matches = [
                    match.value for match in jsonpath_expression.find(data)
                ]

                if matches:
                    print(
                        Fore.GREEN + '\n',
                        json.dumps(matches, indent=4, ensure_ascii=False)
                        + Fore.RESET,
                    )
                else:
                    print(
                        Fore.RED + '\n',
                        f'Key not found "{target_key}".' + Fore.RESET,
                    )
            except Exception:
                print(
                    Fore.RED + '\n',
                    f'Incorrect key "{target_key}".' + Fore.RESET,
                )
        else:
            print(
                Fore.GREEN + '\n',
                json.dumps(json_str, indent=4, ensure_ascii=False) + Fore.RESET,
            )

        print('\n', ('-' * 50), '\n')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nApp closed.\n')
        os._exit(1)
