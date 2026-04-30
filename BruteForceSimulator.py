import hashlib
import time
import os

def brute_force_simulator():
    print("--- Brute-Force & Dictionary Attack Simulator ---")
    
    # 1. Load the Dictionary
    dict_file = "generated_dictionary.txt"
    if not os.path.exists(dict_file):
        print(f"[-] Error: {dict_file} not found. Run the Dictionary Generator first.")
        return
        
    with open(dict_file, 'r') as f:
        wordlist = [line.strip() for line in f]

    # 2. Input Target Hash and Algorithm
    target_hash = input("Enter the target hash to crack: ").strip()
    print("Select Algorithm: 1. MD5 | 2. SHA-256 | 3. SHA-512")
    algo_choice = input("Choice: ")
    
    algo_map = {'1': 'md5', '2': 'sha256', '3': 'sha512'}
    selected_algo = algo_map.get(algo_choice, 'sha256')

    print(f"[*] Starting attack simulation using {selected_algo}...")
    start_time = time.time()
    found = False
    attempts = 0

    # 3. Simulation Loop
    for word in wordlist:
        attempts += 1
        
        # Hashing logic (Requirement: hashlib)
        if selected_algo == 'md5':
            guess_hash = hashlib.md5(word.encode()).hexdigest()
        elif selected_algo == 'sha256':
            guess_hash = hashlib.sha256(word.encode()).hexdigest()
        elif selected_algo == 'sha512':
            guess_hash = hashlib.sha512(word.encode()).hexdigest()
        
        # Comparison logic
        if guess_hash == target_hash:
            duration = time.time() - start_time
            print(f"\n[+] SUCCESS! Password found: {word}")
            print(f"[+] Total attempts: {attempts}")
            print(f"[+] Time taken: {round(duration, 4)} seconds")
            found = True
            break
            
    if not found:
        duration = time.time() - start_time
        print(f"\n[-] Finished. Password not found in dictionary.")
        print(f"[-] Total attempts: {attempts}")
        print(f"[-] Simulation time: {round(duration, 4)} seconds")

if __name__ == "__main__":
    brute_force_simulator()
