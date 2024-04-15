import pytest
from indexerror import resultadoLista


def test_IndexError():
    assert resultadoLista(list) == IndexError
    # assert resultadoLista() == "Valores fuera de rango"


