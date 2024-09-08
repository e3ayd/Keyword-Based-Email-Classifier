# Keyword-Based Email Classifier

This project is a Python-based script that automatically classifies emails into categories like "Work," "Personal," "Promotions," and "Spam" based on specific keywords in the email's subject and body. This tool can be useful for sorting emails and managing inboxes more effectively.

## Features

- Classifies emails based on predefined keywords.
- Supports multiple categories.
- Simple text-based simulation using a sample emails file.

## Installation

1. Clone the repository to your local machine.
2. Ensure Python is installed.

## Usage

To run the project, use the following command:

```bash
python classifier.py
```

## Example outputs

```bash
Email:
Subject: Upcoming Project Meeting
Body: Please prepare the project proposal for our next meeting with the client. The deadline is next Friday.
Classified as: Work
----------------------------------------
Email:
Subject: Your exclusive discount code!
Body: Use the code DISCOUNT2024 to get 50% off your next purchase. This offer is valid until the end of the month.
Classified as: Promotions
----------------------------------------
Email:
Subject: Birthday Party Invitation
Body: You are invited to my birthday party this weekend! Let's have fun with family and friends.
Classified as: Personal
----------------------------------------
Email:
Subject: Congratulations! You have won a prize!
Body: Click here to claim your free lottery prize now!
Classified as: Spam
----------------------------------------
```
