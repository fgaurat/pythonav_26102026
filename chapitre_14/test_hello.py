from hello import bonjour


def test_bonjour_par_defaut():

    # Arrange
    expected = "Bonjour"

    # Act
    r = bonjour()

    # asser
    assert r == expected


def test_bonjour_avec_nom():

    # Arrange
    name = "Fred"
    expected = "Bonjour Fred"

    # Act
    r = bonjour(name)

    # asser
    assert r == expected
