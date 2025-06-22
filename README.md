# 🔗 Mega Link Title Extractor

This Python script automates the process of extracting folder names (titles/headings) from a list of [Mega.nz](https://mega.nz) links using **Selenium**.

I created this tool while practicing Selenium and solving a real-world problem — I had over **250 Mega links** and needed to know what each folder contained, but manually checking them wasn’t practical. This script does it for you.

---

## 🚀 Features

- Opens each Mega.nz link using a browser automation
- Extracts the folder or file title
- Saves the result as: `folder-name : mega-link` in a new output file
- CLI-based and works on any system with Python & Selenium

---

## ⚙️ Requirements

- Python 3.x
- pip
- Google Chrome
- ChromeDriver (matching your browser version)

---

## 📦 Installation & Usage

```bash
# Clone the repo
git clone https://github.com/yourusername/mega-link-title-extractor.git
cd mega-link-title-extractor

# Install dependencies
pip install -r requirements.txt

# Run the script
python3 mega-heading-extractor-final.py
```
When prompted:

Enter the input file path (one Mega link per line)

Enter the desired output file path

### Why This Exists
This was one of my early automation experiments with Python and Selenium, created to solve a real need and practice working with browser automation.
It reflects my journey of:

Applying what I was learning

Using AI-assisted coding to build useful tools

Solving time-consuming manual tasks with automation

📌 Note: This script is for personal/educational use only. Mega.nz may update their layout or block automated access, so use responsibly.
