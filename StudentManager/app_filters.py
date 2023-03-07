import abc
import datetime, enum
from app_db import Transaction
from calendar import monthrange


class FilterFlags(enum.Enum):
    ALL = "ALL"
    FROM_TO = 'FROM_TO'

    @staticmethod
    def get_dict():
        return {
            "Все": FilterFlags.ALL,
            "Из отрезка": FilterFlags.FROM_TO,
        }


class AbstractFilter(abc.ABC):

    def __init__(self, flag, *args):
        self.flag = flag
        self.args = args

    @staticmethod
    def check_valid_type(value):
        return isinstance(value, Transaction)

    @abc.abstractmethod
    def check_transaction(self, transaction):
        pass


class TimeFilter(AbstractFilter):

    def __init__(self, flag: FilterFlags = FilterFlags.ALL, *args):
        super().__init__(flag, *args)

    def check_transaction(self, transaction):
        if self.check_valid_type(transaction):
            if self.flag == FilterFlags.ALL:
                return True
            elif self.flag == FilterFlags.FROM_TO:
                _from = self.args[0]
                _to = self.args[1]
                t = transaction.TIME
                result = self.is_more(t, _from) and self.is_more(_to, t)
                return result
            return False
        return False

    @staticmethod
    def this_year():
        now = datetime.datetime.now()
        _from = f"1.1.{now.year} 0:0:0"
        _to = f"31.12.{now.year} 23:59:59"
        return _from, _to

    @staticmethod
    def this_month():
        now = datetime.datetime.now()
        _from = f"1.{now.month}.{now.year} 0:0:0"
        _to = f"{monthrange(now.year, now.month)[1]}.{now.month}.{now.year} 23:59:59"
        return _from, _to

    @staticmethod
    def to_time(a: str):
        a = a.split(" ")
        day = [int(i) for i in a[0].split(".")]
        time = [int(i) for i in a[1].split(":")]

        return datetime.datetime(day[2], day[1], day[0],
                                 time[0], time[1], time[2], 0)

    @staticmethod
    def is_more(a, b):
        if a == b:
            return True
        a = TimeFilter.to_time(a)
        b = TimeFilter.to_time(b)
        return a > b

    def __str__(self) -> str:
        if self.flag != FilterFlags.ALL:
            return f'TimeFilter<flag={self.flag.value}, from={self.args[0]}, to={self.args[1]}>'
        return f'TimeFilter<flag={self.flag.value}>'

    def __repr__(self) -> str:
        return self.__str__()


class SummaryFilter(AbstractFilter):

    def __init__(self, flag: FilterFlags = FilterFlags.ALL, *args):
        super().__init__(flag, *args)

    def check_transaction(self, transaction):
        if self.check_valid_type(transaction):
            if self.flag == FilterFlags.ALL:
                return True
            elif self.flag == FilterFlags.FROM_TO:
                _from = self.args[0]
                _to = self.args[1]
                return float(_from) <= float(transaction.SUMMARY) <= float(_to)
            return False
        return False

    def __str__(self) -> str:
        if self.flag != FilterFlags.ALL:
            return f'SummaryFilter<flag={self.flag.value}, from={self.args[0]}, to={self.args[1]}>'
        return f'SummaryFilter<flag={self.flag.value}>'

    def __repr__(self) -> str:
        return self.__str__()


class TableFilter:

    def __init__(self, time_filter: TimeFilter,
                 summary_filter: SummaryFilter):
        self.time_filter = time_filter
        self.summary_filter = summary_filter

    def check_transactions(self, tranactions: list[Transaction]):
        """
        Filtering list of transactions
        :param tranactions: list of transaction
        :return: list of transaction, which valid for all sub-filters
        """
        filter_transaction = Transaction.create_transaction(0, 'Результаты фильтра')
        results = []
        for result in tranactions:
            if self.check_transaction(result):
                results.append(result)
                filter_transaction.SUMMARY += result.SUMMARY

        if len(results) > 0:
            filter_transaction.TIME = ""
            results.append(filter_transaction)
        return results

    def check_transaction(self, transaction) -> bool:
        """
        Check transaction by all filters
        :param transaction: object to checked
        :return: True if transaction is valid for sub-filter else False
        """
        return self.time_filter.check_transaction(transaction) and self.summary_filter.check_transaction(
            transaction)

    def __str__(self) -> str:
        return f'TableFilter<summary-filter={self.summary_filter}, ' \
               f'time-filter={self.time_filter}>'

    def __repr__(self) -> str:
        return self.__str__()
