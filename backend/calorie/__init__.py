#pylint:disable=invalid-name
"""
calorie
"""
import logging
import datetime
import pymysql
logger = logging.getLogger("calorie logger")
handler = logging.FileHandler(filename="%s calorie.log"%datetime.datetime.now().strftime("%Y-%m-%d"))
logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(pathname)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
pymysql.install_as_MySQLdb()

logger.addHandler(handler)
