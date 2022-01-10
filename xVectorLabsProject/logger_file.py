import logging

FORMAT = '%(process)10s %(threadName)10s %(levelno)5d %(levelname)10s %(funcName)10s %(asctime)10s\
         %(msecs)10s %(message)10s'

logging.basicConfig(level=logging.DEBUG,
                    filename='project_company_new.log',
                    filemode='a',
                    datefmt='%H:%M:%S',
                    format=FORMAT)
logger = logging.getLogger(__name__)
