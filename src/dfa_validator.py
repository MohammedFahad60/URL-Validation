def validate_url(url):
    state = 0
    i = 0
    
    while i < len(url):
        char = url[i]
        
        if state == 0:  # Start state
            if url.startswith("http://"):
                state = 1
                i += 7
            elif url.startswith("https://"):
                state = 1
                i += 8
            else:
                return False
        
        elif state == 1:  # Domain state
            if char.isalnum() or char in ['-', '.']:
                state = 1
                i += 1
            elif char == '/':
                state = 2
                i += 1
            else:
                return False
        
        elif state == 2:  # Path state
            if char.isalnum() or char in ['-', '_', '.', '/', '?', '=', '&']:
                state = 2
                i += 1
            else:
                return False
        
        else:
            return False
    
    return state in [1, 2]  # Accept states
