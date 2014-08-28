from main import init_collection

from users import init_users
from coverages import init_coverages
from core_config import init_core_config
from report_statuses import init_report_statuses

if __name__ == '__main__':
    for init in [
            init_users,
            init_coverages,
            init_core_config,
            init_report_statuses
    ]:
        init_collection(init)
