
class CtdException(BaseException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self._message = message

    @property
    def message(self):
        return self._message

    @property
    def cause(self) -> BaseException|None:
        try:
            out = self.__cause__
            if isinstance(out, BaseException):
                return out
            return None
        except:
            return None
        

class CtdInvalidParameterException(CtdException):
    def __init__(self, parameter: str, validation: str) -> None:
        super().__init__(f"Parameter '{parameter}' is invalid - {validation}")
        self._parameter = parameter

    @property
    def parameter(self):
        return self._parameter