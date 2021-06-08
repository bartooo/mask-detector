import datetime


class LoggingStructure:
    def __init__(self, date: datetime.datetime, decision: str, delay: float) -> None:
        self._date = date
        self._decision = decision
        self._delay = delay

    @property
    def date(self) -> datetime.datetime:
        return self._date

    @property
    def decision(self) -> str:
        return self._decision

    @property
    def delay(self) -> float:
        return self._delay


class LoggingList:
    def __init__(self, logging_folder: str = "logs/") -> None:
        self._logging_folder = logging_folder
        self._list = []

    def add_element(self, element: LoggingStructure) -> None:
        if type(element.delay) == float:
            self._list.append(element)

    def clear_list(self) -> None:
        self._list.clear()

    def _get_avarage_delay(self) -> float:
        if len(self._list) > 0:
            sum_del = 0
            for el in self._list:
                sum_del += el.delay
            return sum_del / len(self._list)

    def save_to_file(self) -> None:
        file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S.log")
        with open(self._logging_folder + file_name, "w+") as file:
            for element in self._list:
                file.write(
                    "{}||DECISION: {}||DELAY: {:.3f}MS\n".format(
                        element.date.strftime("%Y/%m/%d||%H:%M:%S"),
                        element.decision,
                        element.delay,
                    )
                )
            file.write("~" * 15 + "\n")
            file.write("SUMMARY DELAY: {}MS".format(self._get_avarage_delay()))
