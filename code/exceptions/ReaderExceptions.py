
class OpenException(Exception):
    def __init__(self):
        self.msg = 'Could not open file for reading.'
        super().__init__(self.msg)

class ReadException(Exception):
    def __init__(self):
        self.msg = 'Could not read file'
        super().__init__(self.msg)

class IniReaderException(Exception):
    def __init__(self):
        self.msg = 'Could not read the config file'
        super().__init__(self.msg)