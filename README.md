# 🔐 Password Strength Checker (Star Rating)

A simple **Python-based password strength checker** that evaluates the security of your password and provides a **star rating (★)** along with **suggestions for improvement**.  

This tool helps users create stronger passwords by checking for:
- Length
- Uppercase & lowercase mix
- Numbers
- Special symbols  

---

## 🧠 Features

✅ Real-time password evaluation  
✅ Star rating system (0–5 stars)  
✅ Quality feedback: **Poor**, **Average**, **Good**  
✅ Helpful suggestions for improving weak passwords  
✅ Simple and interactive **command-line interface (CLI)**  

---

## 📂 Project Structure

```
📦 Password-Strength-Checker
├── password_checker.py   # Main script
└── README.md             # Documentation
```

---

## ⚙️ How It Works

The program uses **regular expressions (regex)** to check if the entered password includes:
- Lowercase letters (`[a-z]`)
- Uppercase letters (`[A-Z]`)
- Digits (`\d`)
- Special symbols (`[^A-Za-z0-9]`)

Each matching criterion increases the password’s score.  
A star rating (★) is generated based on this score, along with improvement suggestions.

---

## 🧩 Example Output

```
🔐 Password Strength Checker (Star Rating)

Enter a password: Test123

Password Rating: ★★★☆☆  (3/5 Stars, Average)
Suggestions to improve:
 • Add at least one special symbol (!,@,#,$).

⚠️ Try again with a stronger password.
```

---

## 🚀 How to Run

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/Password-Strength-Checker.git
cd Password-Strength-Checker
```

### 2️⃣ Run the script
```bash
python password_checker.py
```

---

## 💡 Example Strong Password
```
Str0ng@Passw0rd!
```

Output:
```
Password Rating: ★★★★★  (5/5 Stars, Good)
Great job! ✅ Strong password.
```

---

## 🧰 Requirements

- Python 3.7+
- No external dependencies (uses only built-in modules)

---

## 🤝 Contributing

Contributions are welcome!  
If you’d like to enhance this project (e.g., add GUI or web version), feel free to fork and submit a pull request.

---

## 👨‍💻 Author

**Pragadesh Sundhar**  
💼 [GitHub Profile](https://github.com/pragadeshsundar)  

