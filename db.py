import os
from os import environ, getenv
import logging
import traceback
from typing import Tuple
import pymysql
import pymysql.cursors
import pymysql.connections

class Db:
  db_connection = pymysql.connect(
    host=os.getenv('MYSQL_HOST', "127.0.0.1"),
    user=os.getenv('MYSQL_USER', "root"),
    password=os.getenv('MYSQL_PASS', ""),
    db=os.getenv('MYSQL_DB_NAME', "classicmodels"),
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
  )

  def __init__(self) -> None:
    pass

  def __run(self, queryList) -> dict:
    try:
      with self.db_connection.cursor() as cursor: 
        for query in queryList:
          cursor.execute(query)
        self.db_connection.commit()
        fetch = cursor.fetchone()
        return fetch
    except Exception:
      logging.error(traceback.format_exc())
    finally:
      self.db_connection.close()

  def __sql_get_creditLimit(self, customorNumber) -> str:
    return f"SELECT `creditLimit` FROM `customers` WHERE customerNumber={customorNumber}"

  def __sql_get_office_address(self, officeCode) -> str:
    return f"SELECT `addressLine1` FROM `offices` WHERE officeCode={officeCode}"

  def runCreditLimitWithGetAddress(self, param) -> dict:
    return self.__run([self.__sql_get_creditLimit(customorNumber=param), self.__sql_get_office_address(officeCode=1)])