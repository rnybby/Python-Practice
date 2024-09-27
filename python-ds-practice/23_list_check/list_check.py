def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for lsts in lst:
        if not isinstance(lsts, list):
            return False
    return True
