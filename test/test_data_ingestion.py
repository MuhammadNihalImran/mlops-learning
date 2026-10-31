from src.data_ingestion import load_data

def test_load_data(tmp_path):
    file_path = tmp_path / "student.csv"

    file_path.write_text(
        "name,age,marks\nAli,20,85\n"
    )

    result = load_data(file_path)

    assert len(result) == 1
    assert result.iloc[0]["name"] == "Ali"