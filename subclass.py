import threading
from typing import Dict


class Singleton:
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "_instance"):
            return cls._instance
        with cls._lock:
            if hasattr(cls, "_instance"):
                return cls._instance
            cls._instance = object.__new__(cls)
        return cls._instance


class BaseStrategyPublishHandler(Singleton):
    @property
    def target_type(self):
        return self._target_type

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, **kwargs):
        super().__init__()
        self._target_type = kwargs.get("target_type")


class StrategyPublishDispatcher(Singleton):
    @property
    def publisher_dict(self) -> Dict[int, BaseStrategyPublishHandler]:
        print(self._publisher_dict, end='**\n')
        return self._publisher_dict

    def __init__(self):
        super().__init__()
        self._publisher_dict = {
            clazz().target_type: clazz()
            for clazz in BaseStrategyPublishHandler.__subclasses__()
        }
        print(self._publisher_dict)
        print("StrategyPublishDispatcher 初始化成功")

    def get_publisher(self, target_type):
        print(">>>>>>>>>>")
        publisher = self.publisher_dict.get(target_type)
        print("<<<<<<<<<<")
        print(self.publisher_dict, end="%%\n")
        print("**********")
        return publisher


publish_dispatcher = StrategyPublishDispatcher()
aa = publish_dispatcher.get_publisher(1)
print(aa, end="&&\n")

# class AreaStrategyPublishHandler(BaseStrategyPublishHandler):
#     def __init__(self):
#         super().__init__(target_type=1)
#
#
# class HostStrategyPublishHandler(BaseStrategyPublishHandler):
#     def __init__(self):
#         super().__init__(target_type=3)


di = {None: "123456"}
if di.get(None):
    print(False)
else:
    print(True)


def is_None(publisher_dict):
    if publisher_dict.get(None) or not publisher_dict:
        import inspect
        import sys
        for name, sub in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(sub):  # 类别是class，并且父类是A
                print(sub.__name__, sub.__base__.__name__)
                if sub.__base__.__name__ == "BaseStrategyPublishHandler":
                    print(sub.__name__, end="$$$\n")
                    StrategyPublishDispatcher()._publisher_dict[sub().target_type] = sub
        print()


# is_None(publish_dispatcher.publisher_dict)

publish_dispatcher = StrategyPublishDispatcher()
bb = publish_dispatcher.get_publisher(3)
print(bb, end="&&\n")

import inspect
import sys
for name, sub in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(sub):  # 类别是class，并且父类是A
        print(sub.__name__, sub.__base__.__name__)
        if sub.__base__.__name__ == "BaseStrategyPublishHandler":
            print(sub.__name__, end="$$$\n")

class AreaStrategyPublishHandler(BaseStrategyPublishHandler):
    def __init__(self):
        super().__init__(target_type=1)


class HostStrategyPublishHandler(BaseStrategyPublishHandler):
    def __init__(self):
        super().__init__(target_type=3)
