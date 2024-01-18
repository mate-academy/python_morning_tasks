from unique_email_addresses import num_unique_emails


def test_emails_with_dot_and_plus():
    """Test emails with dots and plus signs in the local part."""
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]
    assert num_unique_emails(emails) == 2


def test_different_simple_emails():
    """Test different simple emails without dots or plus signs."""
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    assert num_unique_emails(emails) == 3


def test_emails_with_only_dots():
    """Test emails with only dots in the local part."""
    emails = [
        "test.email@leetcode.com",
        "test.email@leetcode.com",
        "testemail@leetcode.com",
    ]
    assert num_unique_emails(emails) == 1


def test_emails_with_only_plus():
    """Test emails with only plus signs in the local part."""
    emails = [
        "test+email@leetcode.com",
        "test+hello@leetcode.com",
        "test+world@leetcode.com",
    ]
    assert num_unique_emails(emails) == 1


def test_emails_with_both_dot_and_plus_mixed():
    """Test emails with a mix of dots and plus signs in the local part."""
    emails = [
        "test.email+alex@leetcode.com",
        "testemail+alex@leetcode.com",
        "test.email.leet+code@leetcode.com",
    ]
    assert num_unique_emails(emails) == 1


def test_emails_with_different_domains():
    """Test emails with different domain names."""
    emails = [
        "test.email@leetcode.com",
        "test.email@leet.code.com",
        "test.email@lee.tcode.com",
    ]
    assert num_unique_emails(emails) == 3


def test_no_emails():
    """Test with no email addresses provided."""
    emails = []
    assert num_unique_emails(emails) == 0


def test_all_identical_emails():
    """Test with all email addresses being identical."""
    emails = ["user@example.com", "user@example.com", "user@example.com"]
    assert num_unique_emails(emails) == 1


def test_complex_emails():
    """Test with complex email addresses including multiple tags and sorting."""
    emails = [
        "user.name+tag+sorting@example.com",
        "user.name+tag@example.com",
        "user.name@example.com",
    ]
    assert num_unique_emails(emails) == 1


def test_emails_with_plus_at_end():
    """Test emails with plus signs at the end of the local part."""
    emails = ["test.email+@leetcode.com", "test.email@leetcode.com"]
    assert num_unique_emails(emails) == 1


def test_emails_with_dot_at_start():
    """Test emails with a dot at the start of the local part."""
    emails = [".test.email@leetcode.com", "test.email@leetcode.com"]
    assert num_unique_emails(emails) == 1
