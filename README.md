# AWS RDS + Selenium Automation Script

This project demonstrates how to use **Selenium** to automate login to a website and **Python with PyMySQL** to store the login credentials into an **AWS RDS MySQL database**.

## 📌 Features

- Automates login to [Practice Test Automation](https://practicetestautomation.com/practice-test-login/)
- Connects to an AWS RDS MySQL instance
- Creates a table (`submision_form`) if it doesn't exist
- Inserts the submitted login credentials into the database

## 🛠️ Technologies Used

- Python
- Selenium
- PyMySQL
- AWS RDS (MySQL)
- WebDriver Manager for automatic ChromeDriver setup

## 📁 File Structure

python-selenium/ │ ├── aws_rds-selenium.py # Main Python script

markdown

## 🚀 How to Run

1. **Clone the repository** or copy the script into your local project.
2. **Install dependencies**:
   ```bash
   pip install selenium pymysql webdriver-manager
Run the script:

bash
python aws_rds-selenium.py
✅ Make sure your AWS RDS instance is up and accessible from your IP address. 🔐 Avoid using plain text credentials in production scripts.

⚠️ Disclaimer
This project is for educational purposes only. Never store real credentials in plaintext or expose your database access in public repositories.

📧 Contact
For any inquiries, feel free to reach out to Abdullah.

---

Let me know if you'd like to add a badge, screenshot, or turn this into a portfolio project description too.
