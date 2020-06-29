import os
import re
from xy.decorator.singleton import Singleton
from xy.common.global_data import GlobalData
from xy.common.logger import Logger


global_data = GlobalData()


@Singleton
class LoggerRun(Logger):
    def __init__(self):
        super().__init__(
            name="运行日志",
            log_name="run",
            log_path=os.path.join(global_data["log_path"], "run"),
            use_console=False,
            use_timed_rotating=True,
            timed_rotating_params={"when": "d", "suffix": "%Y-%m-%d.log", "extMatch": re.compile("^\d{4}-\d{2}-\d{2}"), "backupCount": 30}
        )

