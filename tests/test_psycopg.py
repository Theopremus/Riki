import psycopg


def test_can_make_db_cursor():
    dbconn = psycopg.connect("dbname=Riki user=postgres")
    cursor = dbconn.cursor()
