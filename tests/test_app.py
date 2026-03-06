from app import create_app
from app.extensions import db


def test_index_page_loads():
    app = create_app()
    app.config.update(TESTING=True, SQLALCHEMY_DATABASE_URI="sqlite:///:memory:")

    with app.app_context():
        db.drop_all()
        db.create_all()

    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Fragrance Ledger" in response.data
