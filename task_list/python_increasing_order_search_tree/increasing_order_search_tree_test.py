from increasing_order_search_tree import \
    increasing_binary_search_tree, TreeNode


def test_increasing_binary_search_tree_with_six_nodes():
    root = TreeNode(6, TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))))))
    result = increasing_binary_search_tree(root)
    assert result.val == 1, "The root of the new tree should be the smallest value, which is 1."
    assert result.right.val == 2, "The second node should be the second smallest value, which is 2."
    assert result.right.right.val == 3, "The third node should be the third smallest value, which is 3."
    assert result.right.right.right.val == 4, "The fourth node should be the fourth smallest value, which is 4."
    assert result.right.right.right.right.val == 5, "The fifth node should be the fifth smallest value, which is 5."
    assert result.right.right.right.right.right.val == 6, "The sixth node should be the largest value, which is 6."


def test_increasing_binary_search_tree_with_seven_nodes():
    root = TreeNode(7, TreeNode(6, TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))))))
    result = increasing_binary_search_tree(root)
    current = result
    for i in range(1, 8):
        assert current.val == i, f"The node at position {i} should have value {i}."
        current = current.right


def test_increasing_binary_search_tree_with_eight_nodes():
    root = TreeNode(8, TreeNode(7, TreeNode(6, TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))))))))
    result = increasing_binary_search_tree(root)
    current = result
    for i in range(1, 9):
        assert current.val == i, f"The node at position {i} should have value {i}."
        current = current.right


def test_increasing_binary_search_tree_with_nine_nodes():
    root = TreeNode(9, TreeNode(8, TreeNode(7, TreeNode(6, TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(
        1)))))))))
    result = increasing_binary_search_tree(root)
    current = result
    for i in range(1, 10):
        assert current.val == i, f"The node at position {i} should have value {i}."
        current = current.right


def test_increasing_binary_search_tree_with_ten_nodes():
    root = TreeNode(10, TreeNode(9, TreeNode(8, TreeNode(7, TreeNode(6, TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2,
                                                                                                                     TreeNode(
                                                                                                                         1))))))))))
    result = increasing_binary_search_tree(root)
    current = result
    for i in range(1, 11):
        assert current.val == i, f"The node at position {i} should have value {i}."
        current = current.right


def test_increasing_binary_search_tree_with_random_values_2():
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, TreeNode(13), TreeNode(17)))
    result = increasing_binary_search_tree(root)
    assert result.val == 3
    assert result.right.val == 5
    assert result.right.right.val == 7
    assert result.right.right.right.val == 10
    assert result.right.right.right.right.val == 13
    assert result.right.right.right.right.right.val == 15
    assert result.right.right.right.right.right.right.val == 17, "Test for a tree with random values. The tree should be in increasing order."


def test_increasing_binary_search_tree_with_random_values_3():
    root = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(15)), TreeNode(30, TreeNode(25), TreeNode(35)))
    result = increasing_binary_search_tree(root)
    assert result.val == 5
    assert result.right.val == 10
    assert result.right.right.val == 15
    assert result.right.right.right.val == 20
    assert result.right.right.right.right.val == 25
    assert result.right.right.right.right.right.val == 30
    assert result.right.right.right.right.right.right.val == 35, "Test for a tree with random values. The tree should be in increasing order."
