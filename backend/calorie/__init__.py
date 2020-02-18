#pylint:disable=invalid-name
"""
calorie
"""
import logging
logger = logging.getLogger("calorie logger")
handler = logging.FileHandler(filename="calorie.log")
logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(pathname)s %(levelname)s %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
