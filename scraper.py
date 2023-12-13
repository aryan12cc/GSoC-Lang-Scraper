from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# change url to corresponding GSoC year's url
url = "https://summerofcode.withgoogle.com/programs/2023/organizations"
organization_urls = {}
all_skills = {}

def initialize_driver():
    driver = webdriver.Chrome()
    driver.get(url)
    delay = 10
    WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "content")))
    return driver, delay

def get_organizations_urls_in_current_page(driver, delay):
    for element in driver.find_elements(By.CLASS_NAME, "content"):
        organization_url = element.get_attribute("href")
        if organization_url in organization_urls.keys():
            print("Error: Duplicate Organizations Found")
            exit(0)
        else:
            organization_urls[organization_url] = 1


def get_all_organization_urls(driver, delay):
    # 100 needs to be greater than the number of clicks needed to see all organizations
    for num_clicks in range(100):
        get_organizations_urls_in_current_page(driver, delay)
        try:
            next_button = driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator mat-tooltip-trigger mat-paginator-navigation-next mat-icon-button mat-button-base']")
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            driver.execute_script("arguments[0].click();", next_button)
            WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "content")))
        except:
            return

def get_all_skills(driver, delay):
    for organization_url in organization_urls:
        driver.get(organization_url)

        WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'tech__content')))
        for current_skills in driver.find_elements(By.CLASS_NAME, 'tech__content'):
            for skill in current_skills.text.split(", "):
                if skill in all_skills.keys():
                    all_skills[skill] += 1
                else:
                    all_skills[skill] = 1

def main():
    driver, delay = initialize_driver()
    get_all_organization_urls(driver, delay)
    print(f"Number of organizations: {len(organization_urls)}")
    get_all_skills(driver, delay)
    sorted_all_skills = sorted(all_skills, key = all_skills.get, reverse = True)
    for skill in sorted_all_skills:
        print(skill, all_skills[skill])

if __name__ == "__main__":
    main()