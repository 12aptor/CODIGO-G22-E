import pytest
from rest_framework.test import APIClient
from rest_framework import status

@pytest.fixture
def client_with_token():
    client = APIClient()

    role_data = {
        'name': 'ADMIN'
    }
    role = client.post('/api/roles/create', role_data, format='json')
    assert role.status_code == status.HTTP_200_OK

    user_data = {
        'name': 'Test User',
        'email': 'test@test.com',
        'password': 'test123',
        'role': role.data['data']['id']
    }
    user = client.post('/api/auth/register', user_data, format='json')
    assert user.status_code == status.HTTP_200_OK

    creadentials = {
        'email': user_data['email'],
        'password': user_data['password']
    }
    auth = client.post('/api/auth/login', creadentials, format='json')
    assert auth.status_code == status.HTTP_200_OK

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {auth.data['access']}')

    return client

@pytest.mark.django_db
def test_services_list(client_with_token):
    response = client_with_token.get('/api/services/list')
    print(response)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['object'] == 'list_services'
    assert isinstance(response.data['data'], list)

@pytest.mark.django_db
def test_services_create(client_with_token):
    service_data = {
        'name': 'Test Service',
        'description': 'Test Description',
        'price': 100,
        'duration': 1,
    }
    response = client_with_token.post(
        '/api/services/create',
        service_data,
        format='json'
    )
    print(response)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['object'] == 'create_service'
    assert isinstance(response.data['data'], dict)
    assert isinstance(response.data['data']['id'], int)
    assert response.data['data']['name'] == service_data['name']
