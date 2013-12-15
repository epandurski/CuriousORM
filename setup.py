from distutils.core import setup

long_description = """
This ORM uses a very minimalistic approach. The general idea is that
the database schema is defined elsewhere (writing the SQL directly, or
using some specialized software), and all the transactions are
implemented either as methods in sub-classes of "Database", or as
stored procedures.

This ORM allows you to very easily: (1) implement complex database
transactions, (2) call stored procedures, (3) do simple queries. For
complex queries you should use database views and stored procedures
that return tables.
"""

setup(name='CuriousORM',
      version='1.2.0',
      description='Simple object-relational mapper for Python and PostgreSQL',
      maintainer="Evgeni Pandurski",
      maintainer_email="epandurski@gmail.com",
      author='Evgeni Pandurski',
      author_email='epandurski@gmail.com',
      url='https://github.com/epandurski/CuriousORM',
      long_description=long_description,
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      platforms=['any'],
      license='Public Domain',
      py_modules=['curiousorm'],
      )
