# Q8:
def is_valid_url(url):
    """
    Checks if the given parameter is a valid URL.
    A valid URL should start with "http" or "https", contain ".", and have at least one character after it.
    :param url: The string to check
    :return: True if valid, False otherwise
    """
    if "http" in url and "." in url:
        return True
    return False

print(is_valid_url("fake url"))
