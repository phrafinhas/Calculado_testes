import pytest
from calculadora.calculadora import Calculadora

def test_somar():
    c = Calculadora()
    assert c.somar(5, 3) == 8
    assert c.somar(-2, 2) == 0
    assert c.somar(2.5, 3.5) == 6.0

def test_subtrair():
    c = Calculadora()
    assert c.subtrair(10, 3) == 7
    assert c.subtrair(5, 10) == -5
    assert c.subtrair(5.5, 2.5) == 3.0

def test_multiplicar():
    c = Calculadora()
    assert c.multiplicar(3, 4) == 12
    assert c.multiplicar(-2, 5) == -10
    assert c.multiplicar(2.5, 4) == 10.0

def test_dividir():
    c = Calculadora()
    assert c.dividir(10, 2) == 5.0
    assert c.dividir(15, 3) == 5.0
    assert c.dividir(7, 2) == 3.5

def test_divisao_zero():
    c = Calculadora()
    assert c.dividir(10, 0) == "Não pode dividir por zero"
    assert c.dividir(0, 0) == "Não pode dividir por zero"

def test_potencia():
    c = Calculadora()
    assert c.potencia(2, 3) == 8
    assert c.potencia(5, 0) == 1
    assert c.potencia(3, 2) == 9
    assert c.potencia(2.5, 2) == 6.25

def test_resto():
    c = Calculadora()
    eps = 1e-9
    assert c.resto(10, 3) == 1
    assert c.resto(15, 4) == 3
    assert abs(c.resto(15.7, 4) - 3.7) < eps

def test_valores_invalidos():
    c = Calculadora()
    assert c.somar("2", 3) == "Valores inválidos"
    assert c.subtrair(5, {}) == "Valores inválidos"
    assert c.multiplicar(None, 4) == "Valores inválidos"
    assert c.dividir(10, [2]) == "Valores inválidos"
    assert c.potencia("3", 2) == "Valores inválidos"
    assert c.resto(10, True) == "Valores inválidos"

def test_booleanos():
    c = Calculadora()
    assert c.somar(True, 5) == "Valores inválidos"
    assert c.resto(10, False) == "Valores inválidos"

@pytest.mark.parametrize("x, y, res", [
    (2, 3, 5),
    (-5, -3, -8),
    (0, 0, 0),
    (2.5, 3.5, 6.0),
    (-2, 5, 3),
])
def test_somar_param(x, y, res):
    c = Calculadora()
    assert c.somar(x, y) == res

@pytest.mark.parametrize("x, y, res", [
    (10, 2, 5.0),
    (15, 3, 5.0),
    (7, 2, 3.5),
    (0, 5, 0.0),
    (5, 0, "Não pode dividir por zero"),
])
def test_dividir_param(x, y, res):
    c = Calculadora()
    assert c.dividir(x, y) == res