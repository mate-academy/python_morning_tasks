from reference.reverse_only_letters import reverse_only_letters


def test_reverse_only_letters():
    assert (
        reverse_only_letters("ab-cd") == "dc-ba"
    ), "Test failed: Expected 'dc-ba' for input 'ab-cd'"
    assert (
        reverse_only_letters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    ), "Test failed: Expected 'j-Ih-gfE-dCba' for input 'a-bC-dEf-ghIj'"
    assert (
        reverse_only_letters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
    ), "Test failed: Expected 'Qedo1ct-eeLg=ntse-T!' for input 'Test1ng-Leet=code-Q!'"
    assert (
        reverse_only_letters("123-456") == "123-456"
    ), "Test failed: Expected '123-456' for non-letter input '123-456'"
