from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random

my_long_query = """
let linkLocationQuery = "ol li a[href]:first-child"
if (document.querySelectorAll(linkLocationQuery).length === 0) {
    linkLocationQuery = "h3 a[href]:first-child"
}
if (document.querySelectorAll(linkLocationQuery).length === 0) {
    linkLocationQuery = "a[href]"
}

function cekLink() {
    let counter = 1;
    document.querySelectorAll(linkLocationQuery).forEach(x => {
        console.log(`${counter++}.) ${x.href}`);
    })
}

function mulaiCek() {
    let counter = 1;
    document.querySelectorAll(linkLocationQuery).forEach(x => {
        let number = counter++;
        fetch(`https://cors-anywhere.herokuapp.com/${x.href}`).then(resp => {
            if (resp.status === 200) console.log(`${number} OK`);
            else console.log(`${number} FAIL`);
        })
    })
}

console.log("Listing Link...");
cekLink();
console.log("Checking Link");
mulaiCek();
"""

def request_cors_access(selenium):
    print("Requesting CORS access...")
    selenium.get("https://cors-anywhere.herokuapp.com/corsdemo")
    request_btn = selenium.find_element_by_css_selector('input[type=submit]')
    request_btn.send_keys(Keys.RETURN)
    time.sleep(1)

def mulai_koreksi_github_os(selenium):
    # Change this as needed
    os_repo = 'os211'
    os_week = 'W03'

    with open('asdosan.txt', 'r') as reader:
        asdosan = reader.readline()
        while asdosan != '':
            asdosan = asdosan.strip()
            print(f"Checking {asdosan}'s repository...")
            topten_url = f'https://{asdosan}.github.io/{os_repo}/{os_week}'
            selenium.get(topten_url)
            time.sleep(1)
            selenium.execute_script(my_long_query)
            time.sleep(1)
            input("Ready to continue? ")
            asdosan = reader.readline()

def main():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    selenium = webdriver.Chrome(options = chrome_options)

    request_cors_access(selenium)
    mulai_koreksi_github_os(selenium)

if __name__ == '__main__':
    main()
