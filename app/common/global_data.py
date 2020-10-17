from xy.stdlib_overwrite.dict import Dict
from xy.decorator.singleton import Singleton


@Singleton
class GlobalData(Dict):
    pass
