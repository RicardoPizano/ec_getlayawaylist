from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

token = '7642e4b94ef5cda555323ea2f16662780b543c7369fe0992a5a4b0c009671ddc'


def test_get_layaway_list():
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.get("getLayawayList", headers=headers)
    response_json = response.json()
    assert len(response_json) > 0
