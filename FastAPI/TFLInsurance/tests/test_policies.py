import pytest  #It discovers functions whose names start with test_, executes them, and reports the results.
from fastapi.testclient import TestClient #TestClient lets you send HTTP-style requests to your FastAPI application without launching a separate server.
from main import app, policies

# Creates a test client for the FastAPI application
client = TestClient(app)


# Restore the original policies before and after every test
@pytest.fixture(autouse=True)
def reset_policies():
    original_policies = [policy.copy() for policy in policies]

    yield

    policies.clear()
    policies.extend(original_policies)


# 1. Test the home endpoint
def test_home():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "TFLInsurance"
    assert data["docs"] == "/docs"


# 2. Test retrieving all policies
def test_get_all_policies():
    response = client.get("/api/policies")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Policies retrieved successfully"
    assert data["count"] == 3
    assert len(data["data"]) == 3


# 3. Test retrieving a policy by ID
def test_get_policy_by_id():
    response = client.get("/api/policies/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Jeevan Labh"
    assert data["premium"] == 15000.0


# 4. Test retrieving a nonexistent policy
def test_get_policy_not_found():
    response = client.get("/api/policies/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Policy not found"


# 5. Test creating a new policy
def test_create_policy():
    new_policy = {
        "name": "Jeevan Anand",
        "description": "Life insurance protection plan",
        "maturity": "20 years",
        "premium": 18000.0
    }

    response = client.post(
        "/api/policies",
        json=new_policy
    )

    assert response.status_code == 201

    data = response.json()

    assert data["message"] == "Policy created successfully"
    assert data["data"]["id"] == 4
    assert data["data"]["name"] == "Jeevan Anand"
    assert data["data"]["premium"] == 18000.0


# 6. Test creating a policy with invalid data
def test_create_policy_invalid_data():
    invalid_policy = {
        "name": "Jeevan Anand",
        "description": "Life insurance protection plan",
        "maturity": "20 years"
        # premium is missing
    }

    response = client.post(
        "/api/policies",
        json=invalid_policy
    )

    assert response.status_code == 422


# 7. Test updating an existing policy
def test_update_policy():
    updated_policy = {
        "name": "Jeevan Labh Updated",
        "description": "Updated life insurance plan",
        "maturity": "12 years",
        "premium": 17000.0
    }

    response = client.put(
        "/api/policies/1",
        json=updated_policy
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Policy updated successfully"
    assert data["data"]["id"] == 1
    assert data["data"]["name"] == "Jeevan Labh Updated"
    assert data["data"]["premium"] == 17000.0


# 8. Test updating a nonexistent policy
def test_update_policy_not_found():
    updated_policy = {
        "name": "Unknown Policy",
        "description": "Test description",
        "maturity": "5 years",
        "premium": 10000.0
    }

    response = client.put(
        "/api/policies/999",
        json=updated_policy
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Policy not found"


# 9. Test deleting an existing policy
def test_delete_policy():
    response = client.delete("/api/policies/1")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Policy deleted successfully"
    assert data["deleted_policy"]["id"] == 1

    # Verify that the policy was actually removed
    get_response = client.get("/api/policies/1")

    assert get_response.status_code == 404


# 10. Test deleting a nonexistent policy
def test_delete_policy_not_found():
    response = client.delete("/api/policies/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Policy not found"


# 11. Test an invalid policy ID format
def test_invalid_policy_id():
    response = client.get("/api/policies/abc")

    assert response.status_code == 422
