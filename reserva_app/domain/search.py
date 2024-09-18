def search_by_id(array: list, target_id: int):
    low = 0
    high = len(array) - 1

    while (low < high):
        if low == high:
            return array[low]
    
        mid = (low + high) / 2 if len(array) % 2 == 0 else (low + high + 1) / 2
        mid = int(mid)

        print(low, high, mid)

        element = array[mid]

        print(element, target_id)

        if element.id == target_id:
            return element
        
        if target_id < element.id:
            high = mid - 1
            
        if target_id > element.id:
            low = mid + 1
        
    return None