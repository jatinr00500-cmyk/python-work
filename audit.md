# Audit Documentation

## 1. README Audit Table

| Claim made in AI README | True? | Evidence or correction made |
| :--- | :--- | :--- |
| `struct.py` uses `@dataclass` to store data. | No | **Correction:** Checked the source code. It uses a standard dict() to store details. Removed mention of @dataclass. |
| `pronic.py` requires installing external libraries. | No | **Correction:** The script uses the built-in math module. No pip installations are needed. Corrected the description to reflect this. |
| `factorial.py` calculates factorial recursively. | No | **Correction:** The code uses a standard iterative for loop. Corrected the README to state this. |
| The scripts handle invalid inputs automatically. | No | **Correction:** The code only evaluates integers. It ignores string handling completely rather than handling them. Corrected the description to reflect this. |

## 2. Commit Comparison Table

| Commit | My original manual message | AI-generated message | Which is clearer, and why? |
| :--- | :--- | :--- | :--- |
| **1** | Added code for armstrong number check | `feat: add script to check armstrong numbers` | AI is clearer. Follows conventional formatting and is concise. |
| **2** | Factorial program python | `feat: add iterative factorial calculation` | AI is clearer. Drops the conversational tone for direct impact. |
| **3** | Code for fibonacci series | `feat: implement fibonacci series generation` | AI is clearer. Removes the trailing incomplete thought from my draft. |
| **4** | Wrote prime number checking code | `feat: add basic prime number checker` | AI is clearer. It specifies the exact file modified and standardizes the phrasing. |
| **5** | Checking for pronic number with math | `feat: add pronic number checker using math module` | AI is clearer. It stays well under the 50-character limit while retaining the core meaning. |
| **6** | Added my details using struct dict | `feat: add student dictionary data structure` | AI is clearer. "Add" is a stronger imperative verb than "Added," and it omits the redundant word "using." |

## 3. Partner Review Notes
**Reviewed by:** Jainam

*   **pronic.py:** The math.sqrt logic works well. Adding a quick inline comment explaining the logic would make it instantly clear to beginners.
*   **armstrong.py:** Great use of len(str(n)) to dynamically find the digits! One small fix: add an empty `print()` at the very end of the script so the final tabbed output doesn't bleed into the terminal prompt.
*   **struct.py:** Using a dictionary keeps the definition perfectly clean. Formatting the print output using f-strings was a great attention to detail.

## 4. Partner Review Notes
**Reviewed by:** Jainam
*   *factorial.py:* The reverse loop logic works well. Adding a quick inline comment explaining that -1 is the step parameter in range(n, 0, -1) would make it instantly clear to beginners.
*   *fibonacci.py:* Great use of tuple unpacking (a, b = b, a + b)! One small fix: add an empty print() at the very end of the script so the final tabbed output doesn't bleed into the terminal prompt.
*   *struct.py:* Using @dataclass keeps the class definition perfectly clean. Formatting the marks output to one decimal place ({s1.marks:.1f}) was a great attention to detail.
