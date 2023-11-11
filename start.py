from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from chat_functionality import *
from setup import *

# General Stuff about the website
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(
    service=Service(executable_path=ChromeDriverManager().install()), options=options
)
website = "https://www.kahoot.it/"
driver.get(website)

def testing_prints(app):
    print(driver.title)
    app.print_to_text_box(driver.title)

def log_in():
    kahootpin = input("Kahoot Pin: ")
    driver.find_element(By.ID, "game-input").send_keys(kahootpin)
    enter_button = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div[1]/div/div/div/div[3]/div[2]/main/div/form/button',
    )
    enter_button.click()

    print("Log in successful")
    time.sleep(2)
    username = input("Username: ")
    driver.find_element(By.ID, "nickname").send_keys(username)
    enter_button = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div[1]/div/div/div/div[3]/div[2]/main/div/form/button',
    )
    enter_button.click()

    print(f"Bot created at {kahootpin} with username '{username}'\n")

    answer_bot()

def answer_bot():
    red = '//*[@id="root"]/div[1]/div/div/main/div[2]/form/div[2]/button[1]/span/span'
    blue = '//*[@id="root"]/div[1]/div/div/main/div[2]/form/div[2]/button[2]/span/span'
    yellow = '//*[@id="root"]/div[1]/div/div/main/div[2]/form/div[2]/button[3]/span/span'
    green = '//*[@id="root"]/div[1]/div/div/main/div[2]/form/div[2]/button[4]/span/span'
    wait_time = 5

    while True:
        element_found = False
        print("Waiting for next question...")
        while not element_found:
            try:
                element = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="root"]/div[1]/div/div/main/main/main/div/div/div[2]/div/h1',
                        )
                    )
                )
                element_found = True
            except TimeoutException:
                pass

        question = driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div[1]/div/div/main/main/main/div/div/div[2]/div/h1',
        ).text
        print(question)

        xpaths = [red, blue, yellow, green]
        answer_choices = []
        while not answer_choices:
            time.sleep(2)
            for xpath in xpaths:
                try:
                    element = driver.find_element(By.XPATH, xpath)
                    answer_choices.append(element.text)
                except NoSuchElementException:
                    pass

        red_choice = ""
        green_choice = ""
        blue_choice = ""
        yellow_choice = ""
        variables = [red_choice, green_choice, blue_choice, yellow_choice]

        for i, choice in enumerate(answer_choices):
            variables[i] = choice

        red_choice, green_choice, blue_choice, yellow_choice = variables

        answer_choices_str = ""
        for i, choice in enumerate(answer_choices):
            answer_choices_str += f"{i+1}. {choice}"
            if i < len(answer_choices) - 1:
                answer_choices_str += ", "

        prompt = f"Question: {question}. Possible Answers: {answer_choices_str}."
        print(f"Question: {question}\nPossible Answers: {answer_choices_str}")

        correct_answer = completed_assistant(prompt)

        if correct_answer == "1":
            red_button = driver.find_element(
                By.XPATH,
                "/html/body/div/div[1]/div/div/main/div[2]/form/div[2]/button[1]",
            )
            red_button.click()
        elif correct_answer == "2":
            green_button = driver.find_element(
                By.XPATH,
                "/html/body/div/div[1]/div/div/main/div[2]/form/div[2]/button[2]",
            )
            green_button.click()
        elif correct_answer == "3":
            blue_button = driver.find_element(
                By.XPATH,
                "/html/body/div/div[1]/div/div/main/div[2]/form/div[2]/button[3]",
            )
            blue_button.click()
        elif correct_answer == "4":
            yellow_button = driver.find_element(
                By.XPATH,
                "/html/body/div/div[1]/div/div/main/div[2]/form/div[2]/button[4]",
            )
            yellow_button.click()
        else:
            red_button = driver.find_element(
                By.XPATH,
                "/html/body/div/div[1]/div/div/main/div[2]/form/div[2]/button[1]",
            )
            red_button.click()

        # For Multiple Choice Questions: Still working on making it able to give multiple answers. 
        # Currently it will only choose one of possible answers and press the submit button.
        try:
            submit = driver.find_element(
                By.XPATH, "/html/body/div/div[1]/div/div/main/div[2]/form/div[3]/button"
            )
            submit.click()
        except NoSuchElementException:
            pass

        print(f"Clicked on {correct_answer}\n")


def main():
    log_in()


if __name__ == "__main__":
    main()