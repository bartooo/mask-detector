import datetime


class LoggingStructure:
    """Class keeps info about received frame from server - date of arrival, decision and delay."""

    def __init__(self, date: datetime.datetime, decision: str, delay: float) -> None:
        """Class LoggingStructure constructor.

        Args:
            date (datetime.datetime): time of arrival
            decision (str): decision which has been taken
            delay (float): delay on server
        """
        self._date = date
        self._decision = decision
        self._delay = delay

    @property
    def date(self) -> datetime.datetime:
        """Date getter.

        Returns:
            datetime.datetime: time of arrival
        """
        return self._date

    @property
    def decision(self) -> str:
        """Decision getter.

        Returns:
            str: decision taken
        """
        return self._decision

    @property
    def delay(self) -> float:
        """Delay getter.

        Returns:
            float: delay on server
        """
        return self._delay


class LoggingList:
    """List of logging structures."""

    def __init__(self, logging_folder: str = "logs/") -> None:
        """LoggingList constructor.

        Args:
            logging_folder (str, optional): path to logs folder, defaults to "logs/"
        """
        self._logging_folder = logging_folder
        self._list = []

    def add_element(self, element: LoggingStructure) -> None:
        """Function adds element to list.

        Args:
            element (LoggingStructure): element to add
        """
        if type(element.delay) == float:
            self._list.append(element)

    def clear_list(self) -> None:
        """Function clears list."""
        self._list.clear()

    def _get_avarage_delay(self) -> float:
        """Function returns avarage delay from all of the frames.

        Returns:
            float: avarage delay
        """
        if len(self._list) > 0:
            sum_del = 0
            for el in self._list:
                sum_del += el.delay
            return sum_del / len(self._list)

    def save_to_file(self) -> None:
        """Function writes to proper file logs."""
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
