import unittest
from unittest.mock import MagicMock
from src.app.combat_system import CombatSystem
from src.models.character import Character
from src.models.sword import Sword
from src.models.shield import Shield
from src.models.vulnerability import Vulnerability


class TestDamageModifiers(unittest.TestCase):
    def test_shield_reduces_damage_but_not_below_zero(self):
        """Shield reduce daño plano y nunca deja daño negativo."""
        calc = MagicMock()
        calc.check_critical_hit.return_value = False  # no critic

        # Sword + 15; Shield - 5 = 10
        combat = CombatSystem(calc, modifiers=[Shield(flat_reduction=5)])
        attacker = Character("Hero")
        defender = Character("Tank")
        weapon = Sword()

        combat.perform_attack(attacker, weapon, defender)
        self.assertEqual(defender.health, 90)

        # extreme case, big dmg reduction
        combat = CombatSystem(calc, modifiers=[Shield(flat_reduction=999)])
        defender2 = Character("Tank2")
        combat.perform_attack(attacker, weapon, defender2)  # 15 - 999 = 0
        self.assertEqual(defender2.health, 100)

    def test_critical_then_vulnerability_multiplier(self):
        """Crítico (+10) se aplica ANTES y
        luego Vulnerability multiplica el daño final."""
        calc = MagicMock()
        calc.check_critical_hit.return_value = True

        # Sword 15 + crit 10 = 25; Vulnerability 1.5 = 37.5 = 38
        combat = CombatSystem(calc, modifiers=[Vulnerability(factor=1.5)])
        attacker = Character("Rogue")
        defender = Character("Ogre")
        weapon = Sword()

        combat.perform_attack(attacker, weapon, defender)
        self.assertEqual(defender.health, 62)  # 100 - 38 = 62


if __name__ == "__main__":
    unittest.main()
