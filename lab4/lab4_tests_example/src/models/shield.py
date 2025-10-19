from src.app.damage_modifiers import DamageModifier


class Shield(DamageModifier):
    def __init__(self, flat_reduction: int = 5):
        self.flat_reduction = int(flat_reduction)

    def modify(self, attacker, weapon, defender, damage: int) -> int:
        return damage

    def after_attack(
        self, attacker, weapon, target, critical: bool, damage: int
    ):
        if damage <= 0 or self.flat_reduction <= 0:
            return 0, None
        reduce_by = min(self.flat_reduction, damage)
        return -reduce_by, None
