from dfa_validator import validate_url

def validate_urls_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        urls = file.readlines()
    
    results = []
    for url in urls:
        url = url.strip()
        result = validate_url(url)
        results.append(f"{url}: {'Valid' if result else 'Invalid'}")
    
    with open(output_file, 'w') as file:
        file.write("\n".join(results))

# Example Usage
if __name__ == "__main__":
    validate_urls_from_file("input/urls.txt", "output/validation_results.txt")
