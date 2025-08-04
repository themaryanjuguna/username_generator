# Random Username Generator

This is a simple Python script that generates random usernames using lowercase letters and digits.  
It produces short, clean usernames like `6vrmb`, `x3nlq`, or `a7fks` — perfect for social media handles, gamertags, or testing.

## 🔧 Features
- Generates 5-character usernames
- Alphanumeric (lowercase + digits)
- Easily customizable
- Lightweight and beginner-friendly

## 🚀 How to Use

### 1. Install Python

Download and install Python from: [https://python.org](https://python.org)

Make sure to check the box **“Add Python to PATH”** during installation.

---

### 2. Clone or Download the Script

Save the `username_generator.py` file from this repo or copy the code below:

```python
import random
import string

def generate_username(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Generate 10 usernames
for i in range(10):
    print(generate_username())
````


### 3. Run the Script

In your terminal or command prompt:

```bash
python username_generator.py
```

---

## 🛠 Customize

You can easily tweak the script:

* Change username length:

  ```python
  generate_username(length=8)
  ```

* Add uppercase letters:

  ```python
  string.ascii_letters + string.digits
  ```

* Save to file instead of printing.

---

## 📄 License

This project is open-source and free to use under the MIT License.

```
# username_generator
