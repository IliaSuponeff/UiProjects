import datetime
import sqlite3
import time
import enum
import os.path
from jinja2 import Template
from os import PathLike
from typing import Union, Optional


def get_time_now() -> str:
    _time = datetime.datetime.now()
    return f'{_time.day}.{_time.month}.{_time.year} {_time.hour}:{_time.minute}:{_time.second}'


class Account:

    def __init__(self, _id, name, balance, currency, table_name):
        self.BALANCE = float(balance)
        self.NAME = name
        self.TABLE_NAME = table_name
        self.CURRENCY = currency

    def __str__(self) -> str:
        return f"Account<name='{self.NAME}'," \
               f"balance={self.BALANCE}, currency='{self.CURRENCY}'" \
               f"table_name='{self.TABLE_NAME}'>"

    def __repr__(self) -> str:
        return self.__str__()

    def set_transaction(self, transaction):
        self.BALANCE += float(transaction.SUMMARY)

    def unset_transaction(self, transaction):
        self.BALANCE -= float(transaction.SUMMARY)


class Transaction:

    def __init__(self, id, _time, summary, information):
        self.ID = id
        self.TIME: int = _time
        self.SUMMARY: float = summary
        self.INFORMATION: str = information

    def get_summary(self):
        return self.SUMMARY

    @staticmethod
    def create_transaction(summary, information):
        _time = get_time_now()
        return Transaction(0, _time, summary, information)

    def get_time(self):
        if self.TIME:
            a = self.TIME.split(" ")
            day = [i for i in a[0].split(".")]
            _time = [i for i in a[1].split(":")]
            if int(day[1]) in range(1, 10):
                day[1] = '0' + str(day[1])
            return f'{".".join(day)} {":".join(_time)}'
        return ''

    def __str__(self) -> str:
        return f"Transaction<time={self.TIME}, summary={self.SUMMARY}," \
               f"info='{self.INFORMATION}'>"

    def __repr__(self) -> str:
        return self.__str__()


class DataBase:

    def __init__(self):
        self._db = sqlite3.connect('./sql/database.db')
        self._cursor = self._db.cursor()
        self._execute_file_sql_script('./sql/scripts/initial_db.sql', need_save=True)
        self.accounts = [Account(*account) for account in
                         self._execute_simple_script('SELECT * FROM accounts', -1)]

    def get_transactions(self, account: Account) -> list[Transaction]:
        if account is None:
            return []
        if account not in self.accounts:
            return []
        results = []
        r = self._execute_simple_script(f'SELECT * FROM {account.TABLE_NAME}', -1)
        for t in r:
            results.append(Transaction(*t))
        return results

    def add_account(self, name: str, balance: int = 0, currency: str = 'BYN') -> None:
        """
        Adding account to database.
        :raise FileNotFoundError: if sql scripts files not found.
        :raise AssertionError: if account by name==f'name' in database now.
        :param name: str, name of account
        :param balance: int, start balance on account
        :param currency: str, currency of balance
        :return: None
        """
        if not os.path.exists('./sql/scripts/add_account.sql'):
            raise FileNotFoundError("Файл './sql/scripts/add_account.sql' не найден в корневой директории приложения.\n"
                                    "Невозможно выполнить запрос.")

        if not os.path.exists('./sql/scripts/create_transaction_table.sql'):
            raise FileNotFoundError(
                "Файл './sql/scripts/create_transaction_table.sql' не найден в корневой директории приложения.\n"
                "Невозможно выполнить запрос.")

        for account in self.accounts:
            if account.NAME == name:
                raise AssertionError(f"Счёт с именем '{name}' уже существует.")

        table = f'table_{hash(name)}'.replace('-', '_')
        self.accounts.append(Account(0, name, balance, currency, table))
        with open('./sql/scripts/add_account.sql') as f:
            tmp = Template(f.read())
            script = tmp.render(name=str(name), balance=int(balance), currency=str(currency), table=str(table))
            self._execute_simple_script(script)

        with open('./sql/scripts/create_transaction_table.sql') as f:
            tmp = Template(f.read())
            script = tmp.render(table_name=str(table))
            self._execute_simple_script(script)
        self._saving()

    def delete_account(self, account_name: str) -> None:
        """
        Deleting account to database.
        :raise FileNotFoundError: if sql scripts files not found.
        :param account_name: name of account to deleting
        :return: None
        """
        if not os.path.exists('./sql/scripts/delete_account.sql'):
            raise FileNotFoundError(
                "Файл './sql/scripts/delete_account.sql' не найден в корневой директории приложения.\n"
                "Невозможно выполнить запрос.")

        if not os.path.exists('./sql/scripts/delete_account_table.sql'):
            raise FileNotFoundError(
                "Файл './sql/scripts/delete_account_table.sql' не найден в корневой директории приложения.\n"
                "Невозможно выполнить запрос.")

        account: Account = None
        for a in self.accounts.copy():
            if a.NAME == account_name:
                account = a
                self.accounts.remove(account)
                break

        with open('./sql/scripts/delete_account.sql') as f:
            tmp = Template(f.read())
            script = tmp.render(account_name=account.NAME)
            self._execute_simple_script(script)

        with open('./sql/scripts/delete_account_table.sql') as f:
            tmp = Template(f.read())
            script = tmp.render(table_name=account.TABLE_NAME)
            self._execute_simple_script(script)
        self._saving()

    def save_accounts(self):
        for account in self.accounts:
            script = f"UPDATE accounts SET balance={account.BALANCE} WHERE name='{account.NAME}'"
            self._execute_simple_script(script)
        self._saving()

    def add_transactions(self, account: Account, summary: int, information: str, date) -> Transaction:
        """
        :raise FileNotFoundError: if sql script file not found.
        :param account: account, which needs to add new transaction
        :param summary: summary of transaction
        :param information: more info about transaction
        :return: Transaction object, which adding to database
        """
        if not os.path.exists('./sql/scripts/add_transaction.sql'):
            raise FileNotFoundError(
                "Файл './sql/scripts/add_transaction.sql' не найден в корневой директории приложения.\n"
                "Невозможно выполнить запрос.")

        t = Transaction(0, date, float(summary), information)
        with open('./sql/scripts/add_transaction.sql', 'r', encoding='utf-8') as f:
            tmp = Template(f.read())
            script = tmp.render(table_name=account.TABLE_NAME, _time=str(t.TIME),
                                summary=t.SUMMARY, info=t.INFORMATION)
            self._execute_simple_script(script, need_save=True)
        account.set_transaction(t)
        return t

    def delete_transaction(self, account: Account, transaction: Transaction) -> None:
        """
        Delete transaction by its ID
        :raise FileNotFoundError: if sql script file not found.
        :param account: current account, which contain this transaction
        :param transaction: Transaction object, which need delete
        :return: None
        """
        if not os.path.exists('./sql/scripts/delete_transaction.sql'):
            raise FileNotFoundError(
                "Файл './sql/scripts/delete_transaction.sql' не найден в корневой директории приложения.\n"
                "Невозможно выполнить запрос.")

        with open('./sql/scripts/delete_transaction.sql', 'r', encoding='utf-8') as f:
            tmp = Template(f.read())
            script = tmp.render(table_name=account.TABLE_NAME, _time=transaction.TIME)
            self._execute_simple_script(script, True)
        self._saving()
        account.unset_transaction(transaction)

    def update_transaction(self, account: Account, _id, _time, summary: int,
                           information: str) -> Transaction:
        """

        :raise FileNotFoundError: if sql script file not found.
        :param account: account, which needs to add new transaction
        :param _time: time of transaction
        :param summary: summary of transaction
        :param information: more info about transaction
        :return: Transaction object, which adding to database
        """
        if not os.path.exists('./sql/scripts/update_transaction.sql'):
            raise FileNotFoundError(
                "Файл './sql/scripts/update_transaction.sql' не найден в корневой директории приложения.\n"
                "Невозможно выполнить запрос.")

        t = Transaction(_id, _time, summary, information)
        account.set_transaction(t)
        with open('./sql/scripts/update_transaction.sql', 'r', encoding='utf-8') as f:
            tmp = Template(f.read())
            script = tmp.render(table_name=account.TABLE_NAME, _id=t.ID, _time=str(t.TIME),
                                summary=t.SUMMARY, info=t.INFORMATION)
            self._execute_simple_script(script, need_save=True)
        self._saving()
        return t

    def _saving(self) -> None:
        """
        Saving all changes in db
        :return: None
        """
        self._db.commit()

    def close(self) -> None:
        """
        closed db and closed cursor
        :return:
        """
        self._cursor.close()
        self._db.close()

    def _execute_file_sql_script(self, file: str | PathLike, result_count: int = 0, need_save: bool = False) -> \
            list[tuple]:
        """
        Execution sql script from file, and return sample results
        :raise FileNotFoundError: if sql script file not found.
        :param file: file to reading SQL script
        :param result_count:
        :param need_save: flag to saving sql request result(s)
        :return: None(if file not exists), [](if result_count==0), [()...()](if result_count==0)
        """
        if not os.path.exists(file):
            raise FileNotFoundError(
                f"Файл '{file}' не найден в корневой директории приложения.\n"
                "Невозможно выполнить запрос.")
        with open(file, 'r', encoding='utf-8') as f:
            self._cursor.executescript(f.read())
        if need_save:
            self._saving()
        return self._get_results(result_count)

    def _execute_simple_script(self, script: str, result_count: int = 0, need_save: bool = False) -> list[tuple]:
        """
        Execution sql script, and return sample results
        :param script: sql script to executing
        :param result_count:
        :param need_save: flag to saving sql request result(s)
        :return: None(if file not exists), [](if result_count==0), [()...()](if result_count==0)
        """
        self._cursor.execute(script)
        if need_save:
            self._saving()
        return self._get_results(result_count)

    def _get_results(self, result_count: int) -> list[tuple]:
        """
        return sample results by count from params
        :param result_count:
        :return: None(if file not exists), [](if result_count==0), [()...()](if result_count==0)
        """
        if result_count == 0:
            return []
        if result_count == -1:
            return self._cursor.fetchall()
        res = self._cursor.fetchall()
        if len(res) <= result_count:
            return res
        return res[:result_count]
