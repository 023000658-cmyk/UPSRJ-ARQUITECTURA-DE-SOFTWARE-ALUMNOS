from abc import ABC, abstractmethod
from typing import Optional

# Interfaz del repositorio (bajo acoplamiento)
class EntityRepository(ABC):
    
    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def find_by_id(self, entity_id: int) -> Optional[dict]:
        pass

    @abstractmethod
    def find_by_keyword(self, keyword: str) -> Optional[dict]:
        pass
