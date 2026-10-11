from main import add_vitamins

def test_add_vitamins():
    result = add_vitamins("D3, , Mg")
    assert result == ["d3", "mg"]