import unittest
from bank_system import BankSystem


class TestBankSystem(unittest.TestCase):

    def setUp(self):
        self.bank = BankSystem()
        self.bank.create_account("Alice", 100)
        self.bank.create_account("Bob", 50)

    def test_create_account(self):
        self.assertFalse(self.bank.create_account("Alice", 100))  # Account already exists
        self.assertTrue(self.bank.create_account("Charlie", 200))

    def test_deposit(self):
        alice_account = self.bank.get_account("Alice")
        self.assertTrue(alice_account.deposit(50))
        self.assertEqual(alice_account.balance, 150)

    def test_withdraw(self):
        alice_account = self.bank.get_account("Alice")
        self.assertTrue(alice_account.withdraw(50))
        self.assertEqual(alice_account.balance, 50)
        self.assertFalse(alice_account.withdraw(100))  # Insufficient balance

    def test_transfer(self):
        alice_account = self.bank.get_account("Alice")
        bob_account = self.bank.get_account("Bob")
        self.assertTrue(alice_account.transfer(50, bob_account))
        self.assertEqual(alice_account.balance, 50)
        self.assertEqual(bob_account.balance, 100)
        self.assertFalse(alice_account.transfer(100, bob_account))  # Insufficient balance

    def test_save_and_load(self):
        self.bank.save_to_csv("test_bank_data.csv")
        new_bank = BankSystem()
        new_bank.load_from_csv("test_bank_data.csv")
        self.assertEqual(new_bank.get_account("Alice").balance, 100)
        self.assertEqual(new_bank.get_account("Bob").balance, 50)

if __name__ == "__main__":
    unittest.main()
