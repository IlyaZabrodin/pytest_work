from src.database.operations import select


def test_db_operation_select(mocker):
    mock_response = [
        {"item_id": 1, "price": 300, "name": "Item 1"},
        {"item_id": 2, "price": 300, "name": "Item 2"},
        {"item_id": 3, "price": 300, "name": "Item 3"},
    ]
    mock_object = mocker.patch(
        "src.database.operations.create_db_response", return_value=mock_response
    )
    db_config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "root",
        "db": "test_db",
    }
    sql_query = "select * from items"
    db_result = select(db_config, sql_query)

    assert len(db_result) > 0

    item_case = db_result[0].keys()
    assert "item_id" in item_case
    assert "price" in item_case
    assert "name" in item_case

    assert mock_object.call_count == 1
    assert mock_object.call_args_list[0][0][0] == db_config
    assert mock_object.call_args_list[0][0][1] == sql_query
