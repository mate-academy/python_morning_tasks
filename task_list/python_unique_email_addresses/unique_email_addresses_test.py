from unique_email_addresses import Solution


def test_emails_with_dot_and_plus():
    solution = Solution()
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]
    assert solution.numUniqueEmails(emails) == 2


def test_different_simple_emails():
    solution = Solution()
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    assert solution.numUniqueEmails(emails) == 3


def test_emails_with_only_dots():
    solution = Solution()
    emails = [
        "test.email@leetcode.com",
        "test.email@leetcode.com",
        "testemail@leetcode.com",
    ]
    assert solution.numUniqueEmails(emails) == 1


def test_emails_with_only_plus():
    solution = Solution()
    emails = [
        "test+email@leetcode.com",
        "test+hello@leetcode.com",
        "test+world@leetcode.com",
    ]
    assert solution.numUniqueEmails(emails) == 1


def test_emails_with_both_dot_and_plus_mixed():
    solution = Solution()
    emails = [
        "test.email+alex@leetcode.com",
        "testemail+alex@leetcode.com",
        "test.email.leet+code@leetcode.com",
    ]
    assert solution.numUniqueEmails(emails) == 1


def test_emails_with_different_domains():
    solution = Solution()
    emails = [
        "test.email@leetcode.com",
        "test.email@leet.code.com",
        "test.email@lee.tcode.com",
    ]
    assert solution.numUniqueEmails(emails) == 3


def test_no_emails():
    solution = Solution()
    emails = []
    assert solution.numUniqueEmails(emails) == 0


def test_all_identical_emails():
    solution = Solution()
    emails = ["user@example.com", "user@example.com", "user@example.com"]
    assert solution.numUniqueEmails(emails) == 1


def test_complex_emails():
    solution = Solution()
    emails = [
        "user.name+tag+sorting@example.com",
        "user.name+tag@example.com",
        "user.name@example.com",
    ]
    assert solution.numUniqueEmails(emails) == 1


def test_emails_with_plus_at_end():
    solution = Solution()
    emails = ["test.email+@leetcode.com", "test.email@leetcode.com"]
    assert solution.numUniqueEmails(emails) == 1


def test_emails_with_dot_at_start():
    solution = Solution()
    emails = [".test.email@leetcode.com", "test.email@leetcode.com"]
    assert solution.numUniqueEmails(emails) == 1
