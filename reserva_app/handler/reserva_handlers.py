from reserva_app.repository.repository import reservaRepository

def get_reservas():
    return reservaRepository.find_all()