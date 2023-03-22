import pytest
from django.db import connections

# def test_db_connection(db):
#     cursor = db.cursor()
#     cursor.execute("SELECT COUNT(*) FROM my_table")
#     result = cursor.fetchone()
#     assert result[0] == 0

@pytest.mark.django_db
def test_db_connection():
    cursor = connections['default'].cursor()
    cursor.execute("SELECT COUNT(*) FROM my_table")
    result = cursor.fetchone()
    assert result[0] == 0
