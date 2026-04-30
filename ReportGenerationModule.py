import datetime

def generate_audit_report(cracked_passwords, analysis_results):
    """
    Generates a final security audit report based on findings.
    """
    print("--- Generating Final Audit Report ---")
    filename = "security_audit_report.txt"
    
    with open(filename, "w") as report:
        # 1. Header and Metadata
        report.write("===========================================\n")
        report.write("      PASSWORD SECURITY AUDIT REPORT       \n")
        report.write(f"      Generated on: {datetime.datetime.now()}\n")
        report.write("===========================================\n\n")

        # 2. Findings Summary (Red Team Results)
        report.write("1. CREDENTIAL CRACKING SUMMARY\n")
        report.write("-------------------------------------------\n")
        if not cracked_passwords:
            report.write("No passwords were successfully cracked during this simulation.\n")
        else:
            for item in cracked_passwords:
                report.write(f"[!] Cracked - User: {item['user']} | Password: {item['password']}\n")
                report.write(f"    Time taken: {item['time']} seconds\n\n")

        # 3. Vulnerability Analysis (Blue Team Results)
        report.write("2. PASSWORD STRENGTH ANALYSIS\n")
        report.write("-------------------------------------------\n")
        for res in analysis_results:
            report.write(f"Password Evaluated: {res['password']}\n")
            report.write(f"Entropy: {res['entropy']} bits\n")
            report.write(f"Rating: {res['rating']}\n\n")

        # 4. Mitigation Recommendations
        report.write("3. RECOMMENDED MITIGATION STEPS\n")
        report.write("-------------------------------------------\n")
        report.write("- Implement Multi-Factor Authentication (MFA).\n")
        report.write("- Enforce a minimum password length of 14 characters.\n")
        report.write("- Use salts for password hashing to prevent rainbow table attacks.\n")
        report.write("- Prohibit common dictionary words in password policies.\n")
        report.write("===========================================\n")

    print(f"[+] Success! Audit report saved as: {filename}")

# Example of how to integrate and run it:
if __name__ == "__main__":
    # Sample data collected from previous modules
    sample_cracked = [
        {"user": "admin", "password": "Password123", "time": 0.045}
    ]
    sample_analysis = [
        {"password": "Password123", "entropy": 38.5, "rating": "Weak"}
    ]
    
    generate_audit_report(sample_cracked, sample_analysis)
