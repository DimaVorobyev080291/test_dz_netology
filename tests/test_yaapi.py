import requests
import pytest

tokens = []

with open("data/tokens.txt") as file :
    for row in file:
        red_row = row.strip()
        tokens.append(red_row)

class TestYD:
    def setup_method(self):
        self.headers = {
            'Authorization': tokens[0]
        }

    @pytest.mark.parametrize(
        'param,folder_name,status',
        (
                ['path', 'Image', 201],
                ['path', 'Image', 409],
                ['pat', 'Music', 400],
        )
    )
    def test_create_folder(self, param, folder_name, status):
        """Тест на проверку создание паки,неверные данные и повторного создание папки с темже именем."""
        params = {
            param: folder_name
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        if 200 <= response.status_code < 300:
            print(f'Папка успешно создана.Код ответа: {response.status_code}')
        elif response.status_code == 400:
            print(f'Некорректные данные.Код ответа: {response.status_code}')
        elif response.status_code == 409:
            print(f'Папка с таким именем уже существует!Код ответа: {response.status_code}')
        assert response.status_code == status


def test_create_folder_no_authorization():
    """Тест на проверку авторизации."""
    param = 'path'
    folder_name = 'Image'
    status = 401

    params = {
        param: folder_name
    }
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    payload = {}
    headers = {
        'Authorization': '47545837344054054'
    }

    response = requests.request('PUT', url, headers=headers, data=payload, params=params)
    print(f'Вы не авторизованы. Код ответа: {response.status_code}')
    assert response.status_code == status