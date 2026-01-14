import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logging():
    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s | %(levelname)s | %(message)s"
                        )
    
    path = Path("./logs")
    path.mkdir(exist_ok=True)
    
    file_handler = RotatingFileHandler("./logs/bot.log",
                                       mode="a", 
                                       maxBytes=10_485_760,
                                       backupCount=5,
                                       encoding="utf-8"
                                       )
    file_handler.setLevel(logging.WARNING)
    logger = logging.getLogger()
    logger.addHandler(file_handler)

