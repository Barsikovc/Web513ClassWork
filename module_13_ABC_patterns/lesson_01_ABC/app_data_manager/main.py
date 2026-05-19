from classes import DatabaseDataManager, FileDataManager

if __name__ == '__main__':
    file_manager = FileDataManager()
    file_manager.save('Пример записи данных')
    print(file_manager.load())
    print()

    db_manager = DatabaseDataManager()
    db_manager.save('Пример данных в БД')
    print(db_manager.load())
