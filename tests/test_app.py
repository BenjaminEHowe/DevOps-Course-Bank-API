"""Integration tests for app.py"""
import pytest

from bank_api.app import app
from flask import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client):
    ACCOUNT_NAME = 'Bob'
    initialRequest = client.get(f'accounts/{ACCOUNT_NAME}')
    assert initialRequest.status_code == 404
    createRequest = client.post(f'accounts/{ACCOUNT_NAME}')
    assert createRequest.status_code == 200
    subsequentRequest = client.get(f'accounts/{ACCOUNT_NAME}')
    assert subsequentRequest.status_code == 200
    data = json.loads(subsequentRequest.data)
    assert data['name'] == ACCOUNT_NAME
