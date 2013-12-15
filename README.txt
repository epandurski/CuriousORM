CuriousORM
==========

An extremely simple object-relational mapper for Python and PostgreSQL.

This ORM uses a very minimalistic approach. The general idea is
that the database schema is defined elsewhere (writing the SQL
directly, or using some specialized software), and all the
transactions are implemented either as methods in sub-classes of
"Database", or as stored procedures. 

This ORM allows you to very easily:

1. Implement complex database transactions
2. Call stored procedures
3. Do simple queries

For complex queries you should use database views and stored
procedures that return tables. (This is exactly what they were
invented for!)

Here is a quick example:

    >>> from curiousorm import *
    >>> class TestDatabase(Database):
    ...    def create_account(self, balance):
    ...        return self.insert_account(balance=balance, __return='id')
    ...
    ...    def increase_account_balance(self, account_id, amount):
    ...        with self.Transaction():
    ...            account = self.select_account_for_update(id=account_id)
    ...            if account == None:
    ...                raise Exception('wrong account id')
    ...            else:
    ...                account.balance += amount
    ...                account.update_row()
    ...
    ...    def delete_account(self, account_id):
    ...        with self.Transaction():
    ...            account = self.select_account_for_update(id=account_id)
    ...            if account == None:
    ...                raise Exception('wrong account id')
    ...            elif account.balance != 0:
    ...                raise Exception('nonzero account balance')
    ...            else:
    ...                account.delete_row()
    ...        
    >>> db = TestDatabase('dbname=curiousorm_test')
    >>> db.execute('CREATE TABLE account (id serial, balance int)')
    []
    >>> account_id = db.create_account(10)
    >>> db.increase_account_balance(account_id, 100)
    >>> db.select_account_list()
    [Record(id=1, balance=110)]
    >>> a = db.select_account(id=1)
    >>> a.balance
    110
    >>> db.delete_account(1)
    Traceback (most recent call last):
    ...
    Exception: nonzero account balance
    >>> db.callproc_current_database()  # calls a stored procedure
    u'curiousorm_test'
    >>> db.current_database()  # calls the same stored procedure
    u'curiousorm_test'
    >>> db.current_database_list()  # the same, but returns a list instead
    [Record(current_database=u'curiousorm_test')]
    
This ORM consists of less than 20KB of very clean, thread-safe
code, so that it can be reviewed and understood with minimum
effort. In fact, reading and understanding the code is the
recommended way of mastering it.

Run "python setup.py install" to install.
