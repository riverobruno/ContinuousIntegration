from elarchivo import defensa

def test_cantidad():
    assert len(defensa) == 4
def test_fabra():
    for jugador in defensa:
        assert "fabra" not in jugador.lower()