from abc import ABC, abstractmethod
from typing import List


class SearchAlgorithm(ABC):
    @abstractmethod
    def search(self, start: int, goal: int) -> List[int]:
        pass
