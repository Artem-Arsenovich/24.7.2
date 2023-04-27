from Pet.api import PetFriends
from settings import valid_email, valid_password, not_valid_email, not_valid_password
import os
pf = PetFriends()
def test_get_api_key_for_valid_user(
        email=valid_email,
        password=valid_password
):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_not_valid_email_and_password(
        email=not_valid_email,
        password=not_valid_password
):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(
        name='Батон',
        animal_type='кот',
        age='3',
        pet_photo='phote/kot-s.jpg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_empty_name(
        name='',
        animal_type='собака',
        age='47',
        pet_photo='phote/korgi.jpeg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result

def test_add_new_pet_with_empty_animal_type(
        name='Po',
        animal_type='',
        age='32',
        pet_photo='phote/pep.jpg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result

def test_add_new_pet_with_empty_age(
        name='Пчела',
        animal_type='кабан',
        age='',
        pet_photo='phote/kaban.jpg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result

def test_add_new_pet_with_empty_info(
        name='',
        animal_type='',
        age='',
        pet_photo='phote/oppf.jpg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result

def test_add_new_pet_with_negative_age(
        name='Глазки',
        animal_type='Бабочка',
        age='-3',
        pet_photo='phote/i.jpeg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result

def test_add_new_pet_with_incorrect_name(
        name='1234121!@#$!2%!@#)&*()_&^&&*^',
        animal_type='змея',
        age='3',
        pet_photo='phote/sneak.jpeg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result

def test_add_new_pet_with_incorrect_animal_type(
        name='Pepega',
        animal_type='!23&*',
        age='6',
        pet_photo='phote/pepega.jpg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result

def test_add_new_pet_with_incorrect_age(
        name='Рыжая',
        animal_type='Лиса',
        age='Не_культырный_вопрос',
        pet_photo='phote/lica.jpg'
):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result

def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Рыжая', "Лиса", "Не_культырный_вопрос", "phote/lica.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()