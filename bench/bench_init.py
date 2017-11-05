import atexit
import sys
import os

from config import config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'integration_tests')))

import tmtc.tmtc
import tmtc.tc
import tmtc.tm.tm
from tools.loggers import *

from tools.tools import MainLog
MainLog("Starting session:", config['session_name'])

loggers = []
loggers_map = {'swo': JlinkSWOLogger, 'uart': UARTLogger, 'saleae': SaleaeLogger}

for i in config['LOGGERS']:
    name = i.split(' ')[0]
    args = i.split(' ')[1:]
    logger_type = loggers_map[name]
    loggers.append(logger_type(*args))

for logger in loggers:
    logger.start()


def cleanup():
    for log in loggers:
        log.stop()
    MainLog("Closing session:", config['session_name'])

atexit.register(cleanup)


class Bench(tmtc.tmtc.Tmtc, tmtc.tm.tm.Check):
    def __init__(self):
        tmtc.tmtc.Tmtc.__init__(self)
        tmtc.tm.tm.Check.__init__(self, self)

bench = Bench()

send = bench.send
check = bench.check

tm = tmtc.tm.TM
tc = tmtc.tc
