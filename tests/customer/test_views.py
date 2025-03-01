from fastapi.testclient import TestClient
from http import HTTPStatus
from src.main import app
import unittest


class TestCustomerViews(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_001_successfully_retrieve_customer(self):
        response = self.client.get("/customers/")
        self.assertEqual(200, response.status_code)

    def test_002_successfully_insert_customer(self):
        payload = {"name": "Test", "email": "test@test.com", "person_id": "000.000.000-00"}
        response = self.client.post("/customers/", json=payload)
        self.assertEqual(200, response.status_code)

    def test_003_successfully_update_customer(self):
        record_id = self.client.get("/customers/?name=Test").json()[0].get("id")
        payload = {"name": "Test2", "email": "test2@test.com", "person_id": "111.111.111-11"}
        response = self.client.put(f"/customers/{record_id}/", json=payload)
        self.assertEqual(200, response.status_code)

    def test_004_successfully_delete_customer(self):
        record_id = self.client.get("/customers/?name=Test").json()[0].get("id")
        response = self.client.delete(f"/customers/{record_id}/")
        self.assertEqual(200, response.status_code)

    def test_005_respond_with_404_when_no_customers_found(self):
        response = self.client.delete("/customers/0/")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_006_respond_with_error_if_payload_not_correct(self):
        payload = {"nam": "Test", "email": "test@test.com"}
        assert self.client.post("/customers", json=payload).status_code == HTTPStatus.UNPROCESSABLE_ENTITY