import pickle


class Pickler:
    def __init__(self, protocol=pickle.DEFAULT_PROTOCOL):
        if protocol < 0 or protocol > 5:
            self.protocol = pickle.DEFAULT_PROTOCOL
        elif protocol == 0:
            self.protocol = pickle.HIGHEST_PROTOCOL
        else:
            self.protocol = protocol

    def pickle_data(self, data):
        pickled_data = pickle.dumps(data, self.protocol)
        return pickled_data

    def pickle_data_to_file(self, filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file, protocol=self.protocol)
        print(f'Произведен пиклинг в файл {filename}')
        return True


class UnPickler:
    @classmethod
    def unpickle_data(cls, pickled_data):
        unpickle_data = pickle.loads(pickled_data)
        return unpickle_data

    @classmethod
    def unpickle_file(cls, pickled_filename):
        try:
            with open(pickled_filename, 'rb') as file:
                unpickle_data = pickle.load(file)
                return unpickle_data
        except FileNotFoundError:
            print(f'Файл не найден')
            return None
        except Exception as ex:
            print(ex)
            return None
