import pytest
import requests

host = "http://localhost:8000"

@pytest.mark.sanity
def test_getmain_api():
    res = requests.get(host)
    assert res.status_code == 200
    js = res.json()
    assert js['Hello'] == 'World123!'


@pytest.mark.regression
@pytest.mark.parametrize("id", (1, 2))
def test_getitem_api(id: int):
    res = requests.get(f"{host}/items/{id}")
    assert res.status_code == 200
    js = res.json()
    assert js["item_id"] == id
    assert js['q'] is None