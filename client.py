import requests
import os
from dotenv import load_dotenv

# Загрузить переменные окружения из .env файла
load_dotenv()

# Получить токен из переменных окружения
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = "http://127.0.0.1:8000"  # Адрес вашего API

#print(API_TOKEN)

# Проверка наличия токена
if not API_TOKEN:
    print("API_TOKEN не найден в переменных окружения!")
    exit(1)

# Функция для добавления токена в заголовки
def get_headers():
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

# Функция для создания заметки
def create_note(text: str) -> int:
    """
    Создаёт новую заметку и возвращает её ID.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/notes/",
            headers=get_headers(),
            json={"text": text},
        )
        response.raise_for_status()  # Проверяем, нет ли HTTP ошибок
        note_data = response.json()  # Получаем тело ответа в формате JSON
        print("Прошёл запрос:", note_data)
        return note_data["id"]  # Извлекаем и возвращаем ID заметки
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при создании заметки: {response.status_code} - {response.text}")
        raise e

# Функция для получения заметки по ID
def get_note(note_id):
    url = f"{BASE_URL}/notes/{note_id}"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        print("Заметка найдена:")
        print(response.json())
    else:
        print(f"Ошибка при получении заметки: {response.status_code} - {response.text}")

# Функция для обновления заметки
def update_note(note_id, text):
    url = f"{BASE_URL}/notes/{note_id}"
    data = {"text": text}
    response = requests.patch(url, json=data, headers=get_headers())

    if response.status_code == 200:
        print("Заметка обновлена успешно!")
        print(response.json())
    else:
        print(f"Ошибка при обновлении заметки: {response.status_code} - {response.text}")

# Функция для удаления заметки
def delete_note(note_id):
    url = f"{BASE_URL}/notes/{note_id}"
    response = requests.delete(url, headers=get_headers())

    if response.status_code == 204:
        print("Заметка удалена успешно!")
    else:
        print(f"Ошибка при удалении заметки: {response.status_code} - {response.text}")

# Функция для получения всех заметок
def list_notes():
    url = f"{BASE_URL}/notes"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        print("Список заметок:")
        print(response.json())
    else:
        print(f"Ошибка при получении списка заметок: {response.status_code} - {response.text}")

# Пример использования:
if __name__ == "__main__":
    # Создание заметки
    get_note(create_note("Это моя первая заметка через API."))



