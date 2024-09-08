# classifier.py

from config import CATEGORIES

def classify_email(subject, body):
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword.lower() in subject.lower() or keyword.lower() in body.lower():
                return category
    return "Uncategorized"

def process_emails(file_path):
    with open(file_path, 'r') as file:
        emails = file.read().split("\n\n")

    classified_emails = {}
    for email in emails:
        if email.strip():
            lines = email.split("\n")
            subject = lines[0].replace("Subject: ", "")
            body = lines[1].replace("Body: ", "")
            category = classify_email(subject, body)
            classified_emails[email] = category

    return classified_emails

if __name__ == "__main__":
    file_path = "emails.txt"
    classified_emails = process_emails(file_path)

    for email, category in classified_emails.items():
        print(f"Email:\n{email}\nClassified as: {category}\n{'-'*40}")
