from enum import Enum
from datetime import datetime

NUM_DAYS_TO_COMPUTE = 365
AVG_MONTHLY_PROFIT_PERC = 9.2

class WithdrawalType(Enum):
    ON_BREAKEVEN_ONE_WITHDRAWAL = 1
    NO_WITHDRAWALS = 2
    EVERY_BREAKEVEN = 3
    PROFIT_PERC_MONTHLY = 4

match WithdrawalType:
    case WithdrawalType.ON_BREAKEVEN_ONE_WITHDRAWAL:
        ComputeBreakeven()
    case _:
        print("Nope")

datetime.today().replace(day=1)

