import re
# применение паттерна Стратегия. Об этом в приложенной документации к этому файлу

class ExpressionEvaluator:
    def evaluate(self, expression):
        raise NotImplementedError

class RegexEvaluator(ExpressionEvaluator):
    def evaluate(self, expression):
        # Функция замены для re.sub
        def replace(match):
            # Получаем строку совпадения и передаем в evaluate_expression
            return self.evaluate_expression(match.group(0))

        return re.sub(r'([\d\s()\-+*/.]+)', replace, expression)

    def evaluate_expression(self, expression):
        expression = expression.strip()
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            print(f"Ошибка при вычислении выражения '{expression}': {e}")
            return expression


class ParsingEvaluator(ExpressionEvaluator):
    def __init__(self):
        self.parser = ExpressionParser
        # создания атрибута экземпляра класса, который ссылается на класс ExpressionParser

    def evaluate(self, expression):
        try:
            parser = self.parser(expression)
            result = parser.parse()  # Запускаем парсинг
            return str(result)
        except Exception as e:
            print(f"Ошибка при парсинге выражения '{expression}': {e}")
            return expression


class EvalEvaluator(ExpressionEvaluator):
    def evaluate(self, expression):
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            print(f"Ошибка при вычислении выражения '{expression}': {e}")
            return expression


class ExpressionParser:
    """Конструктор, который принимает строку expression, токенизирует её и
    инициализирует текущий токен и позицию."""

    def __init__(self, expression):
        self.tokens = self.tokenize(expression)
        # принимается строка expression, которая сразу разбивается на токены (числа и операторы)
        self.current_token = None #инициализация текущего токена
        self.position = -1 # текущая позиция в списке токенов

    def tokenize(self, expression):
        """Разбивает выражение на токены."""
        expression = expression.replace(" ", "")
        tokens = []
        number = ''
        for char in expression:     # для типа float
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(float(number))
                    number = ''
                tokens.append(char) # тут добавление операторов
        if number:
            tokens.append(float(number))
        return tokens

    def parse(self):
        """Запускает парсинг и вычисление выражения."""
        self.position = -1
        self.next_token()
        return self.expr()

    def next_token(self):
        """Получает следующий токен."""
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def expr(self):
        """Обрабатывает выражения: term (('+' | '-') term)*"""
        result = self.term()
        while self.current_token in ('+', '-'):
            operator = self.current_token
            self.next_token()
            if operator == '+':
                result += self.term()
            elif operator == '-':
                result -= self.term()
        return result

    def term(self):
        """Обрабатывает термы: factor (('*' | '/') factor)*"""
        result = self.factor()
        while self.current_token in ('*', '/'):
            operator = self.current_token
            self.next_token()
            if operator == '*':
                result *= self.factor()
            elif operator == '/':
                divisor = self.factor()
                if divisor == 0:
                    raise ValueError("Деление на ноль")
                result /= divisor
        return result

    def factor(self):
        """Обрабатывает факторы: NUMBER | '(' expr ')'"""
        if isinstance(self.current_token, float):
            number = self.current_token
            self.next_token()
            return number
        elif self.current_token == '(':
            self.next_token()
            result = self.expr()
            self.next_token()  # Пропустить ')'
            return result
        raise ValueError("Некорректный токен")