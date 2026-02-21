import CSP_6_01_Library_Basics as HW


def test_process_expenses():
    assert HW.process_expenses([1, 10, 15]) == ([1.15, 11.5, 17.25])

def test_analyze_scores():
    assert HW.analyze_scores([1, 3, 5, 7, 9]) == (9, 5)

def test_sanitize_usernames():
    assert HW.sanitize_usernames(["  Apple", "Banana ", "  CHERRY  ", " date "]) == (["apple", "banana", "cherry", "date"])

def test_identify_outliers():
    assert HW.identify_outliers([1, 107, 100, 567, 12, 435]) == ([107, 567, 435])

def test_search_and_report():
    assert HW.search_and_report(["  Apple", "Banana ", "  CHERRY  ", " date "], "apple") == 0
    assert HW.search_and_report(["  Apple", "Banana ", "  CHERRY  ", " date "], "cherry") == 2
    assert HW.search_and_report(["  Apple", "CHERRY ", "  date  ", " Banana "], "banana") == 3
    assert HW.search_and_report(["  Apple", "Banana ", "  CHERRY  ", " date "], "grape") == -1
    assert HW.search_and_report(["  Apple", "CHERRY ", "  date  ", " Banana "], "grape") == -1
