from os import mkdir


class ServiceID:
    __SYSTEM_ID_DIR: str = "MyNotes\\.systemID"
    __FREE_IDS: str = "MyNotes\\.systemID\\free_ids"
    __LAST_ID: str = "MyNotes\\.systemID\\last_id"

    def __init__(self):
        try:
            mkdir(self.__SYSTEM_ID_DIR)
        except FileExistsError:
            pass

    def get_new_id(self) -> int:
        id: int = self.__get_last_free_id()
        if not id:
            id = self.__get_last_id()
            self.__set_last_id(id + 1)
        return id

    def __get_last_id(self) -> int:
        try:
            with open(self.__LAST_ID) as last_id_file:
                last_id: str = last_id_file.read()
            if last_id:
                return int(last_id)
            return 1
        except FileNotFoundError:
            return 1

    def __set_last_id(self, id: int) -> None:
        with open(self.__LAST_ID, 'w') as last_id_file:
            last_id_file.write(str(id))

    def __get_free_ids(self) -> list[str]:
        try:
            with open(self.__FREE_IDS) as free_ids_file:
                free_ids_list: list[str] = free_ids_file.read().split()
            return free_ids_list
        except FileNotFoundError:
            with open(self.__FREE_IDS, 'w') as free_ids_file:
                pass
            return []

    def __get_last_free_id(self) -> int:
        free_ids: list[str] = self.__get_free_ids()
        if free_ids:
            last_free_id: int = int(free_ids.pop())
            with open(self.__FREE_IDS, 'w') as free_ids_file:
                free_ids_file.write(" ".join(free_ids))
        else:
            last_free_id = 0
        return last_free_id

    def add_free_id(self, id: int) -> None:
        with open(self.__FREE_IDS, 'a') as free_ids_file:
            free_ids_file.write(f"{str(id)} ")