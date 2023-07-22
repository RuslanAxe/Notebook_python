from model.Model import Model, Note
from views.ConsoleUI import ConsoleUI


class Controller:
    def __init__(self,
                 model: Model,
                 view: ConsoleUI):
        self.model = model
        self.view = view

    def start_app(self):
        self.view.wellcome()
        while True:
            command: str = input("Введите команду: ")
            if command == "all":
                self.view.show_sort_menu()
                sort_param: str = input("Введите параметр для сортировки: ")
                is_sort_param: bool = self.view.check_sort_param(sort_param)
                if not is_sort_param:
                    self.view.show_is_sort_param(is_sort_param)
                    continue
                data: dict[int, Note] = self.model.get_all_notes()
                self.view.show_notes(data, sort_param)

            elif command == "find":
                self.view.show_sort_menu()
                sort_param: str = input("Введите параметр для сортировки: ")
                is_sort_param: bool = self.view.check_sort_param(sort_param)
                if not is_sort_param:
                    self.view.show_is_sort_param(is_sort_param)
                    continue
                find_text: str = input("Введите текст для поиска: ")
                data: dict[int, Note] = self.model.find_note(find_text)
                self.view.show_notes(data, sort_param)

            elif command == "add":
                head: str = input("Введите заголовок: ")
                text: str = input("Введите текст: ")
                status: int = self.model.add_new_note(head, text)
                self.view.show_adding_status(status)

            elif command == "edit":
                id: int = int(input("Введите id заметки: "))
                has_id: bool = self.model.check_id(id)
                if not has_id:
                    self.view.show_has_id(has_id)
                    continue
                self.view.show_note(self.model.get_note_by_id(id))
                self.view.show_changing_menu()
                field: str = input("Введите цифру: ")
                is_changing_field: bool = self.model.check_field(field)
                if not is_changing_field:
                    self.view.show_is_changeable_field(is_changing_field)
                    continue
                change: str = input("Введите новое значение: ")
                status: int = self.model.edit_note_by_id(id, field, change)
                self.view.show_changing_status(status)

            elif command == "del":
                id: int = int(input("Введите id заметки: "))
                has_id: bool = self.model.check_id(id)
                if not has_id:
                    self.view.show_has_id(has_id)
                    continue
                self.view.show_note(self.model.get_note_by_id(id))
                sure: str = input("Вы уверены, что хотите удалить эту заметку? (y/n): ")
                if sure == "y":
                    status: int = self.model.del_note_by_id(id)
                    self.view.show_del_status(status)

            elif command == "help":
                self.view.show_menu()

            elif command == "exit":
                break

            else:
                self.view.show_bad_command_msg()