from auth import hash_password, verify_password, create_access_token

def test_hash_password():
    hash = hash_password("password123")
    assert isinstance(hash,str)
    assert hash != "password123"

def test_verify_password():
    hash = hash_password("password123")
    assert verify_password("password123",hash) is True

def test_verify_password():
    hash = hash_password("password123")
    assert verify_password("password",hash) is False  