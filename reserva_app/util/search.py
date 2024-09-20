from reserva_app.domain.model import Model

def search_by_id(array: list[Model], target_id: int) -> Model:
    
    mid = int((len(array) - 1) / 2)

    if array[mid].id == target_id:
        return array[mid]
    if target_id < array[mid].id:
        return search_by_id(array[0:mid - 1], target_id)
    if target_id > array[mid].id:
        return search_by_id(array[mid + 1:], target_id)
        
    return None