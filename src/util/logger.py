import datetime


class Logger:
    def __init__(self, save_path: str = "./logs.log") -> None:
        self.save_path = save_path

    def info(self, unit: str, msg: str, silent: bool = False):
        now = datetime.datetime.now()
        line = f"{now.strftime('%d/%m/%Y %H:%M:%S')}-[{unit}/INFO]:\t{msg}" # noqa
        with open(self.save_path, "a") as file:
            file.write(line + "\n")
        if not silent:
            print(line)

    def warn(self, unit: str, msg: str, silent: bool = False):
        now = datetime.datetime.now()
        line = f"{now.strftime('%d/%m/%Y %H:%M:%S')}-[{unit}/WARN]:\t{msg}" # noqa
        with open(self.save_path, "a") as file:
            file.write(line + "\n")
        if not silent:
            print(line)

    def error(self, unit: str, msg: str, silent: bool = False):
        now = datetime.datetime.now()
        line = f"{now.strftime('%d/%m/%Y %H:%M:%S')}-[{unit}/ERROR]:\t{msg}" # noqa
        with open(self.save_path, "a") as file:
            file.write(line + "\n")
        if not silent:
            print(line)


logger = Logger()
