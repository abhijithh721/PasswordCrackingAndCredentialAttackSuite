import os


def dictionary_generator():
    """
    Generates a custom wordlist based on user-provided patterns and mutations.
    """
    print("--- Password Dictionary Generator ---")
    
    # 1. User Input 
    base_input = input("Enter base keywords (separated by commas, e.g., 'admin, company'): ")
    bases = [word.strip() for word in base_input.split(',')]
    
    dob_input = input("Enter significant years (separated by commas, e.g., '2026, 1998'): ")
    years = [year.strip() for year in dob_input.split(',')]
    
    use_leet = input("Enable leet-speak (e.g., a=@, s=$)? (y/n): ").lower() == 'y'
    
    wordlist = []
    # Mutation Rules
    leet_map = {'a': '@', 's': '$', 'o': '0', 'i': '1', 'e': '3'}
    
    for word in bases:
        # Standard variations
        wordlist.append(word)
        wordlist.append(word.capitalize())
        wordlist.append(word.upper())
        
        # Leet-speak mutations 
        if use_leet:
            leet_word = "".join(leet_map.get(c.lower(), c) for c in word)
            wordlist.append(leet_word)
        
        # Hybrid patterns (e.g., name + DOB) 
        for year in years:
            wordlist.append(f"{word}{year}")
            wordlist.append(f"{word.capitalize()}{year}")
            wordlist.append(f"{year}{word}")

    # Remove duplicates and save to file 
    final_list = list(set(wordlist))
    output_file = "generated_dictionary.txt"
    
    with open(output_file, "w") as f:
        for item in final_list:
            f.write(f"{item}\n")
            
    print(f"\n[+] Success: {len(final_list)} variations generated.")
    print(f"[+] Wordlist saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    dictionary_generator()
