from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import json
import pandas as pd
from gptzero import analyze_with_gptzero
import re

# setup webdriver
options = webdriver.ChromeOptions()
service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# opening webpage
driver.get('https://www.amazon.com/2-Piece-Grinder-Adjustable-Coarseness-Refillable/dp/B09FX2YBBV/')
# driver.get('https://www.amazon.com/dp/B099N4NSSD')
# driver.get('https://www.amazon.com/Jeuhoue-Handmade-Christmas-Birthday-Valentines/dp/B0BVB6DVDC/')

# enter after captcha manually completed
input("Press Enter in the console after solving the CAPTCHA...")

# save product name for file name later
product_name_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'productTitle'))
)
product_name = product_name_element.text.strip()  # .strip() removes any extra whitespace
valid_filename = re.sub(r'[<>:"/\\|?*]', '', product_name).strip()

print(f"Product Name: {valid_filename}")

# click "See all reviews" link
see_all_reviews_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-hook="see-all-reviews-link-foot"]'))
)
see_all_reviews_link.click()

# list for all reviews
all_reviews_data = []

while True:
    try:
        # wait
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'span[data-hook="review-body"]'))
        )
        
        # locate review elements
        review_elements = driver.find_elements(By.CSS_SELECTOR, 'span[data-hook="review-body"]')
        
        # appending each review + detect w/gptzero
        for i in range(len(review_elements)):
            review_text = review_elements[i].text
            analysis_result = analyze_with_gptzero(review_text)
            
            all_reviews_data.append({
                "review_text": review_text,
                "analysis_result": analysis_result
            })
        
        next_page_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next page')]"))
        )
        next_page_link.click()
        
    except (NoSuchElementException, TimeoutException):
        break
    except StaleElementReferenceException:
        continue
    
driver.quit()

# save data to json
json_filename = f'{valid_filename}_reviews_analysis.json'
with open(json_filename, 'w') as f:
    json.dump(all_reviews_data, f, indent=4)

# converting list to excel for "important" data
df = pd.DataFrame([{
    "review_text": review_data.get("review_text", ""),
    "Predicted Class": review_data.get("analysis_result", {}).get("documents", [{}])[0].get("predicted_class", ""),
    "Confidence Score": review_data.get("analysis_result", {}).get("documents", [{}])[0].get("confidence_score", ""),
    "Confidence Category": review_data.get("analysis_result", {}).get("documents", [{}])[0].get("confidence_category", ""),
    **review_data.get("analysis_result", {}).get("documents", [{}])[0].get("writing_stats", {}).get("norm_scores", {}),
} for review_data in all_reviews_data])

# dropping unnecessary info (can change if needed)
df.drop(columns=['analysis_result', 'documents', 'writing_stats', 'confidence_scores_raw', 'confidence_thresholds_raw', 'paragraphs', 'sentences'], errors='ignore', inplace=True)

# save to excel
excel_filename = f'{valid_filename}_reviews_analysis.xlsx'
df.to_excel(excel_filename, index=False)

print("Scraping done.")