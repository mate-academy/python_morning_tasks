from unique_email_addresses import num_unique_emails


def test_emails_with_dot_and_plus():
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]
    assert num_unique_emails(emails) == 2, "Function should identify 2 unique emails."


def test_different_simple_emails():
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    assert (
        num_unique_emails(emails) == 3
    ), "Function should count each simple email as unique."


def test_emails_with_only_dots():
    emails = [
        "test.email@leetcode.com",
        "test.email@leetcode.com",
        "testemail@leetcode.com",
    ]
    assert (
        num_unique_emails(emails) == 1
    ), "Dots in the local part should not affect uniqueness."


def test_emails_with_only_plus():
    emails = [
        "test+email@leetcode.com",
        "test+hello@leetcode.com",
        "test+world@leetcode.com",
    ]
    assert (
        num_unique_emails(emails) == 1
    ), "Plus signs in the local part should not affect uniqueness."


def test_emails_with_both_dot_and_plus_mixed():
    emails = [
        "test.email+alex@leetcode.com",
        "testemail+alex@leetcode.com",
        "test.email.leet+code@leetcode.com",
    ]
    assert (
        num_unique_emails(emails) == 1
    ), "Mixing dots and plus signs should result in 1 unique email."


def test_emails_with_different_domains():
    emails = [
        "test.email@leetcode.com",
        "test.email@leet.code.com",
        "test.email@lee.tcode.com",
    ]
    assert (
        num_unique_emails(emails) == 3
    ), "Different domains should result in different emails."


def test_no_emails():
    emails = []
    assert num_unique_emails(emails) == 0, "No emails should result in 0 unique emails."


def test_all_identical_emails():
    emails = ["user@example.com", "user@example.com", "user@example.com"]
    assert num_unique_emails(emails) == 1, "Identical emails should be counted as one."


def test_complex_emails():
    emails = [
        "user.name+tag+sorting@example.com",
        "user.name+tag@example.com",
        "user.name@example.com",
    ]
    assert (
        num_unique_emails(emails) == 1
    ), "Complex emails with tags and sorting should count as one."


def test_emails_with_plus_at_end():
    emails = ["test.email+@leetcode.com", "test.email@leetcode.com"]
    assert (
        num_unique_emails(emails) == 1
    ), "Plus at the end of the local part should not affect uniqueness."


def test_emails_with_dot_at_start():
    emails = [".test.email@leetcode.com", "test.email@leetcode.com"]
    assert (
        num_unique_emails(emails) == 1
    ), "Dot at the start of the local part should not affect uniqueness."
