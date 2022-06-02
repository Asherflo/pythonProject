import unittest
import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account("samson", "1234", "09098702304")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        account1 = account.Account("samson", "1234", "09098702304")
        name = account1.name
        self.assertEqual("samson", name)

    def test_to_add_phone_number(self):
        account1 = account.Account("samson", "1234", "09098702304")
        phone_number = account1.phone_number
        self.assertEqual("09098702304", phone_number)

    def test_that_account_cam_deposit(self):
        """

        GIVEN:
        WHEN:
        THEN:


        :return:
        """
        account1 = account.Account("samson", "1234", "09098702304")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        """

        GIVEN:
        WHEN:
        THEN:


        :return:
        """
        account1 = account.Account("samson", "1234", "09098702304")
        account1.deposit(500)
        # account1.deposit(-1000)

        self.assertRaises(ValueError, account1.deposit, -1000)
        self.assertEqual(500, account1.balance)

    def test_has_password(self):
        account1 = account.Account("samson", "1234", "09098702304")
        password = account1.password
        self.assertEqual("1234", password)

    def test_that_account_can_withdraw(self):
        account1 = account.Account("samson", "1234", "09098702304")
        account1.deposit(5000)
        self.assertEqual(5000, account1.balance)
        account1.withdraw(3000, "1234")
        self.assertEqual(2000, account1.balance)

    def test_that_account_cannot_withdraw_negative_amount(self):
        account1 = account.Account("samson", "1234", "09098702304")
        account1.deposit(5000)
        self.assertEqual(5000, account1.balance)
        self.assertRaises(ValueError, account1.withdraw, -3000, "1234")
        self.assertEqual(5000, account1.balance)

    def test_that_account_can_withdraw_above_the_balance(self):
        account1 = account.Account("samson", "1234", "09098702304")
        account1.deposit(5000)
        self.assertEqual(5000, account1.balance)
        self.assertRaises(ValueError, account1.withdraw, 10000, "1234")
        self.assertEqual(5000, account1.balance)

    def test_to_load_airtime(self):
        account1 = account.Account("samson", "1234", "09098702304")
        account1.deposit(5000)
        self.assertEqual(5000, account1.balance)
        account1.load_airtime(500, "09098702304")
        self.assertEqual(4500, account1.balance)

    def test_that_account2_can_be_created(self):
        account2 = account.Account("tolani", "6757", "08131108763")
        self.assertIsNotNone(account2)
        self.assertIsInstance(account2, account.Account)

    def test_that_the_two_account_can_deposit(self):
        account1 = account.Account("samson", "1234", "09098702304")
        account1.deposit(5000)
        account2 = account.Account("tolani", "6757", "08131108763")
        account2.deposit(2000)
        self.assertEqual(5000,account1.balance)
        self.assertEqual(2000,account2.balance)

    def test_that_the_two_account_can_transfer(self):
        account1 = account.Account("samson", "1234", "09098702304")
        account1.deposit(5000)
        account2 = account.Account("tolani", "6757", "08131108763")
        account1.transfer(2000,account2,"1234")
        self.assertEqual(3000,account1.balance)
        self.assertEqual(2000,account2.balance)





if __name__ == '__main__':
    unittest.main()
# test load airtime
# test account number can be wrong
