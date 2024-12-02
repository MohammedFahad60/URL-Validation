from dfa_validator import validate_url

if __name__ == "__main__":
    print("Enter a URL to validate:")
    url = input().strip()
    if validate_url(url):
        print(f"'{url}' is a valid URL.")
    else:
        print(f"'{url}' is not a valid URL.")
