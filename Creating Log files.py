import logging

"""
Log Levels:

Debug, Info, Warning, Error, Critical
"""

logging.basicConfig(filename=r'C:\Users\Akumar4\Desktop\test.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',  # Format of the message displayed time, levelname , message
                    datefmt='%m/%d/%Y %I:%M:%S %p',  # YOu can change Date Format also
                    level=logging.DEBUG)

logging.debug("This is a Debug Message")
logging.info("This is a Info Message")
logging.warning("This is a Warning Message")
logging.error("This is a Error Message")
logging.critical("This is a Critical Message")

"""
If you Run the above code logging.debug, logging.info.... in the Console window only Warning, Error, critical messages are printed. 
Debug & Info messages are not printed.
If you specify the path the log file will be stored in the respective path.
By setting the level=loggin.DEBUG then debug & info will be displayed in the Log file
"""

