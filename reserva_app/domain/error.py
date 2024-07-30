from enum import Enum
from reserva_app.domain.constants import PASSWORD_MIN_LENGHT

class Error(Enum):
    BlankCredentials = "Por favor, preencha todos os campos obrigatórios."
    BadCredentials = "E-mail ou senha incorretos."
    InvalidEmail = "Insira um e-mail válido."
    UnavailableEmail = "E-mail indisponível"
    NameSpecialCharacters = "O nome não pode ter caracteres especiais."
    PasswordMinimumLength = f"A senha deve ter, no mínimo, {PASSWORD_MIN_LENGHT} caracteres."
    InvalidSalaType = "Selecione um tipo válido."
    ZeroCapacity = "A capacidade deve ser maior que 0."

    def __str__(self):
        return self.value