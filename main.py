import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        HEADERS = {'Authorization': self.token}
        """Метод загруджает файл file_path на яндекс диск"""
        resp = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                            params={'path': f'/{file_path}', 'overwrite': 'true'},
                            headers=HEADERS)
        href = resp.json()['href']
        print(f'Href: {href}')

        with open(file_path, 'rb') as f:
            resp2 = requests.put(href, files={'file': f})
        return resp2.status_code


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('test.txt')
    print(result)
