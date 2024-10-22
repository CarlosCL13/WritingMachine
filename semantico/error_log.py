class SingletonMeta(type):
    instances = {}  # Contiene todas las clases que utilizan a la meta clase SinletonMeta, y estas solo se pueden instanciar una vez

    def __call__(clase, *args, **kwargs):
        if clase not in clase.instances:
            instance = super().__call__(*args, **kwargs)
            clase.instances[clase] = instance
        return clase.instances[clase]


class ErrorLog(metaclass=SingletonMeta):
    def __init__(self):
        self.log = ""

    def log_error(self, message):
        self.log += message + "\n"

    def get_message(self):
        return self.log