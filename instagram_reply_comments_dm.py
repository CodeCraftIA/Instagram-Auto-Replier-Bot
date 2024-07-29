import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import random
from tqdm import tqdm

options = uc.ChromeOptions()
#options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--lang=en')  # Set browser language to English
driver = uc.Chrome(options=options)


reply_message = "Hello there!"
emojis = " "
reply_message2 = "How are you?"
username = "xxx"
password="xxxxx"
post_url = "https://www.instagram.com/p/C8pryI-ObMP/"




url = "https://www.instagram.com/"
driver.get(url)

try:
    print("Trying to login...")
    try:
        # Wait for the div element to be located
        div_element = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a"))
        )
        time.sleep(random.randint(1, 3))
        
        # Find the button within the div element
        button = div_element.find_element(By.CSS_SELECTOR, 'button._a9--._ap36._a9_1')

        time.sleep(random.randint(1, 3))
        # Click on the button
        button.click()

        time.sleep(random.randint(1, 3))
    except Exception as e:
        print("No cookies found")
        print(" ")
    # Wait for the username input field to be visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )

    time.sleep(random.randint(1, 3))
    # Type the email or username with human-like typing

    for char in username:
        username_input.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between keystrokes

    time.sleep(random.randint(1, 3))
    # Locate the password input field
    password_input = driver.find_element(By.NAME, 'password')

    time.sleep(random.randint(1, 3))
    # Type the password with human-like typing
    for char in password:
        password_input.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between keystrokes
    
    time.sleep(random.randint(1, 3))
    # Press the Enter key
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    print("Logged in Succesfully!")
    time.sleep(10)
    
except Exception as e:
    print(e)
    sys.exit()


# Load previously saved profiles from a file
def load_saved_profiles():
    try:
        with open("messaged_profiles.txt", 'r') as file:
            saved_profiles = {line.strip() for line in file.readlines()}
    except FileNotFoundError:
        saved_profiles = set()
    return saved_profiles

# Save profiles to a file
def save_profiles(profiles):
    with open("messaged_profiles.txt", 'a') as file:
        for profile in profiles:
            file.write(profile + "\n")

def send_reply(url):
    driver.get(url)
    time.sleep(random.uniform(0.8, 1.2))  # Adjust as needed
    #active story
    try:
        # Find the story element
        story_element = driver.find_element(By.CSS_SELECTOR, "div.x6s0dn4.x78zum5.xdt5ytf.x1iyjqo2.x2lah0s.xl56j7k.x1n2onr6")

        # Click on the story to watch it
        story_element.click()
        #print("Clicked on the story.")

        # Here you can interact with the story, e.g., view content, navigate through slides, etc.
        # Wait for the story to load (adjust wait time as needed)
        time.sleep(random.uniform(0.1, 0.5))  # Adjust as needed

        # Find and click on the reply textarea
        reply_textarea = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.x1i10hfl.xjbqb8w.x972fbf.xcfux6l.x1qhh985.xm0m39n.x7e90pr.xw3qccf.x1a2a7pz.xw2csxc.x1odjw0f.x1y1aw1k.xpvbz4a.xwib8y2.xohu8s8.xtt52l0.xh8yej3.xomwbyg"))
        )
        reply_textarea.click()
        #print("Clicked on the reply textarea.")

        # Enter text into the textarea
        #reply_textarea.send_keys(reply_message)
        # Type the password with human-like typing
        for char in reply_message:
            reply_textarea.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))  # Random delay between keystrokes
        emojis_exte = " " + emojis
        reply_textarea.send_keys(emojis_exte)
        #print("Entered text in the reply textarea.")
        time.sleep(random.uniform(0.2, 0.5))
        # Submit the reply (if there's a submit button or ENTER key action required, add that here)

        # Optionally, simulate sending the reply (if needed)
        # For example, press ENTER to send the reply
        reply_textarea.send_keys(Keys.ENTER)
        print(" ")
        print("Replied to active story")

        # Wait for the story to load (adjust wait time as needed)
        time.sleep(random.uniform(0.2, 0.4))  # Adjust as needed

        reply_textarea.click()
        #print("Clicked on the reply textarea.")

        # Enter text into the textarea
        #reply_textarea.send_keys(reply_message)
        # Type the password with human-like typing
        for char in reply_message2:
            reply_textarea.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))  # Random delay between keystrokes
        #print("Entered text in the reply textarea.")
        time.sleep(random.uniform(0.2, 0.5))
        # Submit the reply (if there's a submit button or ENTER key action required, add that here)

        # Optionally, simulate sending the reply (if needed)
        # For example, press ENTER to send the reply
        reply_textarea.send_keys(Keys.ENTER)
        print(" ")
        print("Sent second message also")

        return True
    except Exception as e:
        print(" ")
    
    #reply on highlight
    try:
        # Find the story element
        story_element = driver.find_element(By.CSS_SELECTOR, "div.x1upo8f9.xpdipgo.xamitd3.x1n2onr6.x87ps6o.x1ypdohk")

        # Click on the story to watch it
        story_element.click()
        #print("Clicked on the story.")

        # Here you can interact with the story, e.g., view content, navigate through slides, etc.
        # Wait for the story to load (adjust wait time as needed)
        time.sleep(random.uniform(0.9, 1.3))  # Adjust as needed

        # Find and click on the reply textarea using WebDriverWait
        reply_textarea = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.x1i10hfl.xjbqb8w.x972fbf.xcfux6l.x1qhh985.xm0m39n.x7e90pr.xw3qccf.x1a2a7pz.xw2csxc.x1odjw0f.x1y1aw1k.xpvbz4a.xwib8y2.xohu8s8.xtt52l0.xh8yej3.xomwbyg"))
        )
        reply_textarea.click()
        #print("Clicked on the reply textarea.")
        # Enter text into the textarea
        #reply_textarea.send_keys(reply_message)
        # Type the password with human-like typing
        for char in reply_message:
            reply_textarea.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))  # Random delay between keystrokes
        #print("Entered text in the reply textarea.")
        time.sleep(random.uniform(0.2, 0.5))
        # Submit the reply (if there's a submit button or ENTER key action required, add that here)

        # Optionally, simulate sending the reply (if needed)
        # For example, press ENTER to send the reply
        reply_textarea.send_keys(Keys.ENTER)
        print(" ")
        print("Replied to highlight story")
        # Wait for the story to load (adjust wait time as needed)
        time.sleep(random.uniform(0.2, 0.4))  # Adjust as needed

        reply_textarea.click()
        #print("Clicked on the reply textarea.")

        # Enter text into the textarea
        #reply_textarea.send_keys(reply_message)
        # Type the password with human-like typing
        for char in reply_message2:
            reply_textarea.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))  # Random delay between keystrokes
        #print("Entered text in the reply textarea.")
        time.sleep(random.uniform(0.2, 0.5))
        # Submit the reply (if there's a submit button or ENTER key action required, add that here)

        # Optionally, simulate sending the reply (if needed)
        # For example, press ENTER to send the reply
        reply_textarea.send_keys(Keys.ENTER)
        print(" ")
        print("Sent second message also")
        return True
    except Exception as e:
        print(" ")

    return False#neither replied on storie or highlight



#get user profile from comments

driver.get(post_url)

time.sleep(5)


try:
    # Find the comment section element
    comment_section = driver.find_element(By.CSS_SELECTOR, "div.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6")

    # Calculate the initial height of the comment section
    last_height = driver.execute_script("return arguments[0].scrollHeight", comment_section)

    # Scroll inside the comment section using JavaScript
    while True:
        # Scroll to the bottom of the comment section
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", comment_section)
        time.sleep(3)  # Adjust sleep time as needed
        
        # Calculate new height and break the loop if no more scrolling is possible
        new_height = driver.execute_script("return arguments[0].scrollHeight", comment_section)
        if new_height == last_height:
            break
        last_height = new_height

    print("Finished scrolling through comments.")
    # Find all profile links in the comment section
    profile_links = set()  # Use a set to store unique URLs
    elements = comment_section.find_elements(By.CSS_SELECTOR, "a[href^='/']")  # Select links that start with '/'

    for element in elements:
        href = element.get_attribute("href")
        if ("/explore/tags/" not in href) and ("https://www.instagram.com/p/" not in href):  # Filter out hashtag links
            profile_links.add(href)
    print("Found unique profiles: ", len(profile_links))
    time.sleep(2)
    saved_profiles = load_saved_profiles()
    # Process only new profiles
    new_profiles = profile_links - saved_profiles
    print("New profiles to process: ", len(new_profiles))

    # Process and save new profiles
    processed_profiles = set()
    for link in tqdm(new_profiles):
        response = send_reply(link)
        if response:  # Only save profiles if response is True
            processed_profiles.add(link)
        time.sleep(1.5)  # Adjust sleep time as needed

    # Save new profiles to the file
    save_profiles(processed_profiles)

    print("Finished processing profiles.")
    
except Exception as e:
    print(f"Error: {e}")



time.sleep(10)

driver.quit()