import pytest
import uuid
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user_model import User, UserRole, Base

# Setup a test database
DATABASE_URL = "sqlite:///:memory:"  # Use in-memory SQLite for tests
engine = create_engine(DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture
def db_session():
    """Fixture to initialize and teardown the test database."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_user(db_session):
    """Test creating a new User with valid fields."""
    user = User(
        id=uuid.uuid4(),
        nickname="johndoe",
        email="john.doe@example.com",
        hashed_password="fake_hashed_password",
        role=UserRole.AUTHENTICATED,
        email_verified=False,
    )
    db_session.add(user)
    db_session.commit()

    saved_user = db_session.query(User).filter_by(email="john.doe@example.com").first()
    assert saved_user is not None
    assert saved_user.nickname == "johndoe"
    assert saved_user.role == UserRole.AUTHENTICATED

def test_lock_unlock_user(db_session):
    """Test locking and unlocking a User account."""
    user = User(
        id=uuid.uuid4(),
        nickname="locked_user",
        email="locked@example.com",
        hashed_password="hashed_password",
        role=UserRole.MANAGER,
    )
    db_session.add(user)
    db_session.commit()

    # Lock the account
    user.lock_account()
    db_session.commit()

    locked_user = db_session.query(User).filter_by(email="locked@example.com").first()
    assert locked_user.is_locked is True

    # Unlock the account
    user.unlock_account()
    db_session.commit()

    unlocked_user = db_session.query(User).filter_by(email="locked@example.com").first()
    assert unlocked_user.is_locked is False

def test_update_professional_status(db_session):
    """Test updating the professional status of a User."""
    user = User(
        id=uuid.uuid4(),
        nickname="pro_user",
        email="pro@example.com",
        hashed_password="hashed_password",
        role=UserRole.MANAGER,
        is_professional=False,
    )
    db_session.add(user)
    db_session.commit()

    # Update professional status
    user.update_professional_status(True)
    db_session.commit()

    updated_user = db_session.query(User).filter_by(email="pro@example.com").first()
    assert updated_user.is_professional is True
    assert updated_user.professional_status_updated_at is not None

def test_invalid_user_missing_required_fields(db_session):
    """Test creating a User with missing required fields."""
    with pytest.raises(Exception):  # IntegrityError should be raised
        user = User(
            id=uuid.uuid4(),
            nickname=None,  # Required field
            email="invalid@example.com",
            hashed_password="password",
            role=UserRole.AUTHENTICATED,
        )
        db_session.add(user)
        db_session.commit()
