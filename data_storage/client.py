import argparse
import requests


def upload_file(url, file_path):
    with open(file_path, 'rb') as f:
        response = requests.post(url + '/files/', files={'file': f})
        print(response.json())


def download_file(url, filename):
    response = requests.get(url + f'/files/{filename}/')
    with open(filename, 'wb') as f:
        f.write(response.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default='http://127.0.0.1:8000/', help="URL of the server")
    args = parser.parse_args()

    while True:
        command = input("Upload or Download?\n").lower().strip()
        if command == 'q':
            break
        elif command == 'u':
            file_path = input("Enter file path: ")
            upload_file(args.url, file_path)
        elif command == 'd':
            filename = input("Enter file name: ")
            download_file(args.url, filename)
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()