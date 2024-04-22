from models import db
import pytest

testing_db_contents = {
    "items": [
        {
            "date": "2024-04-14",
            "name": "ball",
            "cost": 4
        },
        {
            "date": "2024-03-10",
            "name": "phone",
            "cost": 300
        }
    ]
}

def test_get_data():
    assert db.get_data("./models/testing_db.json") == testing_db_contents


def test_get_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        db.get_data("./models/doesnotexist.json")

def test_get_data_validation():
    with pytest.raises(ValueError):
        db.get_data("./models/testing_db_not_valid.json")
        