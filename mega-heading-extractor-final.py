from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setting up options for headless operation
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Take input:
input_file = input("Enter the filename with link: ")
output_file = input("Enter output filename: ")



# Open the file with links and the output file
with open(input_file, 'r') as links_file, open(output_file, "w") as final_file:
    links_content = links_file.readlines()

    for link in links_content:
        link = link.strip()  # Remove any extra whitespace or newline characters

        if link:
            try:
                # Navigate to the link
                print(f"Processing link: {link}")
                driver.get(link)

                # Wait until the folder name element is visible (increase wait time if necessary)
                wait = WebDriverWait(driver, 30)
                folder_name_element = wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "span.not-loading.selectable-txt")
                ))

                # Extract folder name
                folder_name = folder_name_element.text.strip()

                # Format the output
                formatted_output = f"[{folder_name} - {link} ]\n\n"

                # Write the formatted output to the final file
                final_file.write(formatted_output + "\n")

                print(f"Processed link: {link}")

            except Exception as e:
                # Handle any errors that occur and log them
                final_file.write(f"Failed to retrieve info for {link}:\n")
                print(f"Failed to retrieve folder name for {link}: {e}")

# Close the browser after processing all links
driver.quit()
