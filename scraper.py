from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://summerofcode.withgoogle.com/programs/2023/organizations"

driver = webdriver.Chrome()
driver.get(url)
delay = 10

WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'content')))

organization_urls = []

for num_clicks in range(100):
    for element in driver.find_elements(By.CLASS_NAME, 'content'):
        organization_urls.append(element.get_attribute("href"))
    try:
        btnNext = driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator mat-tooltip-trigger mat-paginator-navigation-next mat-icon-button mat-button-base']")
        driver.execute_script("arguments[0].scrollIntoView();", btnNext)
        driver.execute_script("arguments[0].click();", btnNext)
        WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'content')))
    except:
        break

skills_required = dict()

print(len(organization_urls))
for organization_url in organization_urls:
    driver.get(organization_url)

    WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'tech__content')))
    for all_skills in driver.find_elements(By.CLASS_NAME, 'tech__content'):
        for skill in all_skills.text.split(", "):
            if skill in skills_required.keys():
                skills_required[skill] += 1
            else:
                skills_required[skill] = 1

sorted_skills_required = sorted(skills_required, key=skills_required.get, reverse=True)
for skill in sorted_skills_required:
    print(skill, skills_required[skill])

