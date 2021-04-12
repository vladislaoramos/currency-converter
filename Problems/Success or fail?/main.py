import requests


def check_success(url):
    return "Success" if requests.get(url).status_code < 400 \
        else "Fail"
