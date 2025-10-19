from src.app.i_combat_system import ICombatSystem


class CombatSystem(ICombatSystem):
    def __init__(self, damage_calculator, modifiers=None):
        self.damage_calculator = damage_calculator
        self.modifiers = list(modifiers) if modifiers else []

    def perform_attack(self, attacker, weapon, target):
        if not target.is_alive:
            return f"{target.name} ya está derrotado"

        _hp_before = getattr(target, "health", None)

        result = weapon.attack(attacker, target)
        critical = self.damage_calculator.check_critical_hit()

        if critical:
            bonus_damage = 10
            target.take_damage(bonus_damage)
            result += f" ¡GOLPE CRÍTICO! +{bonus_damage} daño extra"

        inflicted = 0
        if isinstance(_hp_before, (int, float)) and hasattr(target, "health"):
            inflicted = max(0, int(_hp_before - target.health))

        # apply modifiers
        for modifier in getattr(self, "modifiers", []):
            hook = getattr(modifier, "after_attack", None)
            if callable(hook):
                delta, note = hook(
                    attacker, weapon, target, critical, inflicted
                )
                if isinstance(delta, (int, float)) and delta != 0:
                    delta = int(delta)
                    if delta > 0:
                        target.take_damage(delta)
                        inflicted += delta
                    else:
                        heal = min(-delta, inflicted)
                        if heal > 0:
                            target.health = min(100, target.health + heal)
                            inflicted -= heal
                if note:
                    result += f" {note}"

        return result
