import pytest # type: ignore
from app.models.user_model import User, UserRole
from sqlalchemy.exc import IntegrityError # type: ignore
from datetime import datetime
import uuid

def test_create_user(db_session):
    """Test user creation with valid data."""
    user = User(
        id=uuid.uuid4(),
        nickname="test_user",
        email="test@example.com",
        hashed_password="hashed_pw",
        role=UserRole.AUTHENTICATED
    )
    db_session.add(user)
    db_session.commit()
    assert user.id is not None
    assert user.email == "test@example.com"

def test_missing_required_fields(db_session):
    """Test user creation with missing required fields."""
    with pytest.raises(IntegrityError):
        user = User(
            nickname=None,  # Required field
            email="missing@example.com",
            hashed_password="hashed_pw",
            role=UserRole.AUTHENTICATED
        )
        db_session.add(user)
        db_session.commit()

def test_email_verification(db_session):
    """Test verifying email."""
    user = User(
        id=uuid.uuid4(),
        nickname="email_verify_user",
        email="verify@example.com",
        hashed_password="hashed_pw",
        email_verified=False,
        role=UserRole.AUTHENTICATED
    )
    user.verify_email()
    assert user.email_verified is True

def test_lock_unlock_account(db_session):
    """Test locking and unlocking a user account."""
    user = User(
        id=uuid.uuid4(),
        nickname="lock_user",
        email="lock@example.com",
        hashed_password="hashed_pw",
        is_locked=False,
        role=UserRole.AUTHENTICATED
    )
    user.lock_account()
    assert user.is_locked is True

    user.unlock_account()
    assert user.is_locked is False

def test_professional_status_update(db_session):
    """Test updating professional status."""
    user = User(
        id=uuid.uuid4(),
        nickname="pro_status_user",
        email="pro@example.com",
        hashed_password="hashed_pw",
        is_professional=False,
        role=UserRole.AUTHENTICATED
    )
    user.update_professional_status(True)
    assert user.is_professional is True
    assert user.professional_status_updated_at is not None
