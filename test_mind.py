import unittest
from mindgame import MindGame

class TestMindGame(unittest.TestCase):
    # Unit tests to verify math logic and data integrity

    def setUp(self):
        # Set up a fresh game instance for every test
        self.game = MindGame()

    def test_master_list_integrity(self):
        # E$nsures the bank contains 50 even numbers and includes 100
        self.assertEqual(len(self.game.all_options), 50)
        self.assertIn(100, self.game.all_options)
        # Verify all numbers are even
        for num in self.game.all_options:
            self.assertEqual(num % 2, 0, f"{num} is not an even number!")

    def test_random_sample_size(self):
        # Ensures the UI only presents 4 options to the user
        sample = self.game.get_random_sample()
        self.assertEqual(len(sample), 4)
        # Ensure all sampled numbers are unique
        self.assertEqual(len(set(sample)), 4)

    def test_mathematical_proof(self):
        # Verifies the algebraic formula: ((2x + n) / 2) - x = n/2
        # We test across multiple secret numbers and modifiers
        test_cases = [
            {"secret": 5, "modifier": 10},
            {"secret": 100, "modifier": 50},
            {"secret": 1, "modifier": 2}
        ]
        
        for case in test_cases:
            x = case["secret"]
            n = case["modifier"]
            
            # Simulate the game steps
            step1 = x * 2
            step2 = step1 + n
            step3 = step2 / 2
            final = step3 - x
            
            self.assertEqual(final, n / 2)

if __name__ == "__main__":
    unittest.main()