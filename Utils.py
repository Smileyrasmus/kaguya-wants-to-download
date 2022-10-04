class Utils:
    @staticmethod
    def format_number(number: str or int, length: int=3) -> str:
        while len(str(number)) < length:
            number = '0' + str(number)
        return str(number)