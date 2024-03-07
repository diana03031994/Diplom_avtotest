# Диана Щакарянц 14-я когорта - Дипломный проект Инженер по тестированию плюс
import sending_requests
def get_track_number_of_order():
    track_number = sending_requests.post_new_order() #сохраняем ответ при создании нового заказа
    return track_number.json()["track"] #сохраняем полученный трек

def test_create_and_track_order():
    track_number = get_track_number_of_order()
    get_response = sending_requests.get_order_info(track_number) #сохранить рузультат запроса на получение информации по треку
    assert get_response.status_code == 200 #Проверить,что код ответа 200