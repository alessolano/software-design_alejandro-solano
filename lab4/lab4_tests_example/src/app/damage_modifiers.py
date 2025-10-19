from abc import ABC, abstractmethod


class DamageModifier(ABC):
    @abstractmethod
    def modify(self, attacker, weapon, defender, damage: int) -> int:
        """Devuelve el daño final tras aplicar la modificación."""
        ...
