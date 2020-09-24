
import requests


def handler_request(fn):
    def wrapper(*args, **kwargs):
        try:
            response = fn(*args, **kwargs)
            response.raise_for_status()

        except requests.exceptions.HTTPError as err:
            print(err)
            return response.text

        except Exception as err:
            print(f"Erro inexperado - {err} ")
            return response.text
        else:
            return response.json()
    return wrapper

@handler_request
def get_desafio(url):
    return requests.get(url)

@handler_request
def post_desafio(url, data):
    return requests.post(url, json=data)

def grito_de_torcida(func):
    def wrapper(*args, **kwargs):
        print('da-lhe!', end=' ')
        func(*args, **kwargs)
        return func
    return wrapper

@grito_de_torcida
def grito_do_guarani():
    print('bugreeee!')


@grito_de_torcida
def grito_da_lusa():
    print('lusa!')



