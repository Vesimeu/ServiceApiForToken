import click
from client import create_note, get_note, update_note, delete_note, list_notes

@click.group()
def cli():
    """Консольный клиент для веб-сервиса заметок."""
    pass

@cli.command()
@click.argument("text")
def create(text):
    """Создать новую заметку."""
    try:
        note_id = create_note(text)
        click.echo(f"Заметка создана с ID: {note_id}")
    except Exception as e:
        click.echo(f"Ошибка при создании заметки: {e}")

@cli.command()
@click.argument("note_id", type=int)
def get(note_id):
    """Получить текст заметки по ID."""
    try:
        note = get_note(note_id)
        click.echo(f"Заметка ID: {note_id}:\nТекст: {note['text']}")
    except Exception as e:
        click.echo(f"Ошибка при получении заметки: {e}")

@cli.command()
@click.argument("note_id", type=int)
@click.argument("text")
def update(note_id, text):
    """Обновить текст заметки."""
    try:
        update_note(note_id, text)
        click.echo(f"Заметка {note_id} успешно обновлена.")
    except Exception as e:
        click.echo(f"Ошибка при обновлении заметки: {e}")

@cli.command()
@click.argument("note_id", type=int)
def delete(note_id):
    """Удалить заметку."""
    try:
        delete_note(note_id)
        click.echo(f"Заметка {note_id} успешно удалена.")
    except Exception as e:
        click.echo(f"Ошибка при удалении заметки: {e}")

@cli.command()
def list():
    """Получить список всех заметок."""
    try:
        notes = list_notes()
        click.echo("Список заметок:")
        for note in notes:
            click.echo(f"ID: {note['id']}, Текст: {note['text']}")
    except Exception as e:
        click.echo(f"Ошибка при получении списка заметок: {e}")

if __name__ == "__main__":
    cli()
