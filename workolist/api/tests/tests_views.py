def test_api_health_check(client):
    response = client.get('/api/v1/health-check/')
    assert response.status_code == 200
