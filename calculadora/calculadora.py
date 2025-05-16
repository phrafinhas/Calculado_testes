class Calculadora:
    def _valido(self, x, y):
        if isinstance(x, bool) or isinstance(y, bool):
            return False
        return isinstance(x, (int, float)) and isinstance(y, (int, float))

    def somar(self, x, y):
        if not self._valido(x, y):
            return "Valores inválidos"
        return x + y

    def subtrair(self, x, y):
        if not self._valido(x, y):
            return "Valores inválidos"
        return x - y

    def multiplicar(self, x, y):
        if not self._valido(x, y):
            return "Valores inválidos"
        return x * y

    def dividir(self, x, y):
        if not self._valido(x, y):
            return "Valores inválidos"
        if y == 0:
            return "Não pode dividir por zero"
        return x / y

    def potencia(self, base, exp):
        if not self._valido(base, exp):
            return "Valores inválidos"
        return base ** exp

    def resto(self, x, y):
        if not self._valido(x, y):
            return "Valores inválidos"
        if y == 0:
            return "Não pode dividir por zero"
        return x % y
