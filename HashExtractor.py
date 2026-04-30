import os

def hash_extraction_module():
    print("--- Hash Extraction Module ---")
    print("1. Extract from Linux shadow file (Requires Root)")
    print("2. Simulate Hash Extraction (Manual Entry for Lab)")
    
    choice = input("Select an option: ")
    
    if choice == '1':
        # Linux Hash Extraction
        path = "/etc/shadow"
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    print("\n[+] Extracted Hashes:")
                    for line in f:
                        parts = line.split(':')
                        if len(parts) > 1 and '$' in parts[1]:
                            print(f"User: {parts[0]} | Hash: {parts[1]}")
            except PermissionError:
                print("[-] Error: Root privileges required to read /etc/shadow.")
        else:
            print("[-] Error: /etc/shadow not found (Are you on Linux?)")
            
    elif choice == '2':
        # Manual/Simulated input for lab environment
        username = input("Enter username: ")
        user_hash = input("Enter the hash to store for cracking (e.g., MD5 or SHA-256): ")
        
        # Save extracted/manual hash to a file for the simulation step
        with open("extracted_hashes.txt", "a") as f:
            f.write(f"{username}:{user_hash}\n")
        print(f"\n[+] Hash for '{username}' saved to 'extracted_hashes.txt'")

if __name__ == "__main__":
    hash_extraction_module()
