from time import localtime, strftime
from model.Note import Note


class ConsoleUI:
    @staticmethod
    def sort_by_id(note: Note):
        return note.get_id()

    @staticmethod
    def sort_by_create_date(note: Note):
        return note.get_created_timestamp()

    @staticmethod
    def sort_by_last_change_timestamp(note: Note):
        return note.get_last_change_timestamp()

    __DATE_FORMAT: str = "%d.%m.%Y %H:%M"

    __SORTS: dict[str, callable] = {"1": sort_by_id,
                                    "2": sort_by_create_date,
                                    "3": sort_by_last_change_timestamp}

    def wellcome(self) -> None:
        print("Приложение Заметки запущено\n",
              "Введите команду help для просмотра справки\n",
              sep="")

    def show_menu(self) -> None:
        print("all - Показать все заметки\n",
              "find - Поиск заметки по содержимому\n",
              "add - Добавить новую заметку\n",
              "edit - Редактировать заметку\n",
              "del - Удалить заметку\n",
              "help - Показать меню\n",
              "exit - Выйти из приложения",
              sep="")

    def show_bad_command_msg(self) -> None:
        print("Неверная команда\n",
              "Введите команду help для просмотра справки",
              sep="")

    def show_changing_menu(self):
        print("Что бы вы хотели изменить?:\n",
              "1 - Заголовок\n",
              "2 - Текст заметки",
              sep="")

    def show_sort_menu(self):
        print("Как бы вы хотели отсортировать вывод?:\n",
              "1 - по id\n",
              "2 - по дате создания\n",
              "3 - по дате изменения",
              sep="")

    def check_sort_param(self, sort_param: str) -> bool:
        if sort_param in ConsoleUI.__SORTS:
            return True
        return False

    def show_note(self, note: Note) -> None:
        id: int = note.get_id()
        created_timestamp: int = note.get_created_timestamp()
        head: str = note.get_head()
        text: str = note.get_text()
        last_change_timestamp: int = note.get_last_change_timestamp()

        created_timestamp: str = strftime(self.__DATE_FORMAT, localtime(created_timestamp))

        if not (last_change_timestamp is None):
            last_change_timestamp: str = strftime(self.__DATE_FORMAT, localtime(last_change_timestamp))

        print(f"id={id} created:{created_timestamp} edited:{last_change_timestamp}\n",
              f"{head}\n",
              f"{text}\n",
              sep="")

    def show_notes(self, data: dict[int, Note], sort_param: str) -> None:
        if data:
            notes: list[Note] = list(data.values())
            notes.sort(key=ConsoleUI.__SORTS[sort_param])
            for note in notes:
                self.show_note(note)
        else:
            print("Заметок нет")

    def show_has_id(self, has_id: bool) -> None:
        if not has_id:
            print("Такого id нет")

    def show_is_changeable_field(self, is_changeable_field: bool) -> None:
        if not is_changeable_field:
            print("Неверно указано поле")

    def show_is_sort_param(self, is_sort_param: bool) -> None:
        if not is_sort_param:
            print("Некорректный параметр для сортировки")

    def show_adding_status(self, code: int) -> None:
        if code == 0:
            print("Заметка добавлена! code: 0")
        else:
            print(f"Что-то пошло не так! code: {code}")

    def show_changing_status(self, code: int) -> None:
        if code == 0:
            print("Заметка изменена! code: 0")
        else:
            print(f"Что-то пошло не так! code: {code}")

    def show_del_status(self, code: int) -> None:
        if code == 0:
            print("Заметка удалена! code: 0")
        else:
            print(f"Что-то пошло не так! code: {code}")