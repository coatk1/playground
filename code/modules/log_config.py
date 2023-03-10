# Source: https://docs.python.org/3.8/howto/logging-cookbook.html
import os
import logging
import datetime

if not os.path.exists(os.path.join(os.path.abspath(os.getcwd()), "logs")):
    os.makedirs(os.path.join(os.path.abspath(os.getcwd()), "logs"))

# Config for logging to files.
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(os.path.abspath(os.getcwd()), "logs", "{}.log".format(datetime.date.today().strftime("%m_%d_%Y"))),
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    datefmt="I:%M:%S %p"
)

# Create handlers.
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers.
c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s", datefmt="I:%M:%S %p")
c_handler.setFormatter(c_format)

# Add handlers
logging.getLogger().addHandler(c_handler)

logger1 = logging.getLogger("main")
logger2 = logging.getLogger("secondary")

logger1.info("Test 1")
logger2.info("Test 2")
