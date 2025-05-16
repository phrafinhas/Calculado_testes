# 🧮 Calculadora em Python com Pytest

Este projeto consiste em uma **calculadora simples**, desenvolvida em Python, capaz de realizar operações matemáticas básicas. A aplicação foi criada como parte das atividades do estágio na **Compass UOL**, com o objetivo de praticar **programação orientada a objetos** e **testes automatizados com Pytest**.

---

## ✅ Funcionalidades

A calculadora permite as seguintes operações entre dois números:

- ➕ Adição  
- ➖ Subtração  
- ✖️ Multiplicação  
- ➗ Divisão  
- ⬆️ Potência  
- 🧩 Módulo (resto da divisão)

Todas as operações incluem **validação de tipos de dados**, rejeitando valores inválidos (como strings, booleanos, listas, etc.) e tratando casos especiais, como **divisão por zero**.

---

## 🧪 Testes Automatizados

A pasta `testes` contém os testes escritos com **Pytest**, que garantem:

- ✅ A precisão dos resultados das operações  
- ❗ O tratamento correto de erros  
- 🚫 A rejeição de tipos de dados inválidos  
- 🔁 A execução de múltiplos casos com `@pytest.mark.parametrize`

---

> Projeto desenvolvido como parte do estágio na Compass UOL.  
