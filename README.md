# Password Cracking & Credential Attack Suite
**A Practical Toolkit for Password Policy Testing & Security Assessment**

## 📌 Project Overview
This project is an ethical security toolkit designed to simulate credential attacks and evaluate password robustness. It provides a controlled environment to understand how hashes are stored, how attackers exploit weak policies, and how security teams can reinforce authentication mechanisms.

## 🛠️ Key Features
*   **Dictionary Generator:** Build custom wordlists using pattern-based generation (Name+DOB) and mutation rules like leet-speak and case variations.
*   **Hash Extraction:** Demonstrates ethical extraction of Linux `/etc/shadow` entries and offline Windows SAM/SYSTEM registry hives.
*   **Brute-Force Simulator:** Includes incremental and dictionary-based cracking modules to calculate "time-to-crack" metrics.
*   **Strength Analyzer:** Evaluates mathematical entropy and complexity to identify dictionary-based weaknesses.
*   **Security Auditor:** Generates detailed reports with mitigation steps and recommended password policies.

## 🏗️ Architecture & Workflow
The suite follows a 6-stage security workflow:
1. **Input:** Import user/hash data.
2. **Generation:** Create mutated wordlists.
3. **Extraction:** Retrieve target hashes from Linux or Windows.
4. **Simulation:** Execute brute-force or dictionary attacks.
5. **Analysis:** Evaluate entropy and predictability.
6. **Reporting:** Generate a final vulnerability audit.

## 💻 Technologies Used
*   **Language:** Python 3, Bash
*   **Libraries:** `hashlib`, `passlib`, `crypt`
*   **System Tools:** `reg.exe`
*   **Design:** Draw.io for architecture flowcharts

## 🎓 Learning Outcomes
*   Mastered secure password storage and hashing algorithm identification (MD5, SHA-512, NTLM).
*   Implemented ethical Red Team (offensive) and Blue Team (defensive) methodologies.
*   Conducted authentication security auditing and policy enforcement.

## ⚠️ Ethical Disclaimer
This toolkit is strictly for **educational and authorized security testing purposes** within a controlled lab environment. Unauthorized use against systems without explicit permission is illegal and unethical.
