# Мария Любавина, 11-я когорта — Финальный проект. Инженер по тестированию плюс

import sendor_stand_request

#Тест на проверку получения кода 200:
def test_get_order():
    track = sendor_stand_request.get_new_track()
    track = sendor_stand_request.get_order_body(track)
    assert track.status_code == 200