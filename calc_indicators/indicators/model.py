# Class to represent an indicator with
from abc import ABC, abstractmethod
class Indicator(ABC):
    @abstractmethod
    def calc_indicator(self, data_frame):
        pass

    @abstractmethod
    def __eq__(self, obj):
        pass

    def __ne__(self, obj):
        pass
