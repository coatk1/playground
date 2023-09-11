# Source: https://docs.python.org/3.8/howto/logging-cookbook.html

# Standard Libraries
import os
import logging
import datetime

LOGGING_PATH = "logs"
# LOGGING_PATH = os.path.join(os.path.abspath(os.getcwd()), "logs")

# if not os.path.exists(LOGGING_PATH):
#     os.makedirs(LOGGING_PATH)

# Creating an importable logger to be used in any Python module.
logger = logging

# Config for logging to files.
logging.basicConfig(
    level=logging.INFO,
    # filename=os.path.join(os.path.abspath(os.getcwd()), "logs", "{}.log".format(datetime.date.today().strftime("%m_%d_%Y"))),
    filename=os.path.join(LOGGING_PATH, "{}.log".format(datetime.date.today().strftime("%m_%d_%Y"))),
    filemode="a",
    # format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    format="%(asctime)s: - %(filename)s:%(lineno)s: %(levelname)s - %(message)s",
    datefmt="I:%M:%S %p",
)

# Note: Commenting out the below for jupyter notebook purposes.

# # Create handlers.
# c_handler = logging.StreamHandler()
# c_handler.setLevel(logging.INFO)

# # Create formatters and add it to handlers.
# c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s", datefmt="I:%M:%S %p")
# c_handler.setFormatter(c_format)

# # Add handlers
# logging.getLogger().addHandler(c_handler)

# # logger1 = logging.getLogger("main")
# # logger2 = logging.getLogger("secondary")

# # logger1.info("Test 1")
# # logger2.info("Test 2")
