from enum import Enum
from reserva_app.util.constants import PASSWORD_MIN_LENGHT

class Error(Enum):
    BlankFields = "Por favor, preencha todos os campos obrigatórios."
    BadCredentials = "E-mail ou senha incorretos."
    InvalidEmail = "Insira um e-mail válido."
    UnavailableEmail = "E-mail indisponível"
    NameSpecialCharacters = "O nome não pode ter caracteres especiais."
    PasswordMinimumLength = f"A senha deve ter, no mínimo, {PASSWORD_MIN_LENGHT} caracteres."
    InvalidSalaType = "Selecione um tipo válido."
    ZeroCapacity = "A capacidade deve ser maior que 0."
    InvalidReservaStartDate = "Data de início inválida."
    InvalidReservaEndDate = "Data de fim inválida."
    ReservaEndBeforeStart = "Reservas só podem acabar após o horário de início."
    ReservaTooLong = "Reservas não podem durar mais de um dia."
    SalaAlreadyInUse = "Horário indisponível."

    def __str__(self):
        return self.value