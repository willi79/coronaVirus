from selenium import webdriver
import smtplib
import time
class Coronavirus():
  def __init__(self):
    while(1):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries"]/tbody[1]')
        country_element = table.find_element_by_xpath("//td[contains(text(), 'Indonesia')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")

        total_cases = data[1]
        new_cases = data[2]
        total_deaths = data[3]
        
        try:
            if total_cases!=total_cases_now or new_cases!=new_cases_now or total_deaths!=total_deaths_now:
                print("Sending Email")
                send_mail(country_element, total_cases, new_cases, total_deaths)
                total_cases_now=total_cases
                new_cases_now=new_cases
                total_deaths_now=total_deaths
        except:
            print("Error, not defined")
            total_cases_now=total_cases
            new_cases_now=new_cases
            total_deaths_now=total_deaths

        print(total_cases,new_cases,total_deaths,total_cases_now,new_cases_now,total_deaths_now)
        self.driver.close
        time.sleep(300)
def send_mail(country_element, total_cases, new_cases, total_deaths):
    server = smtplib.SMTP('smtp.mailgun.org', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('postmaster@sandbox9a81f6ab2bed4f17801a176da0ad5b42.mailgun.org', 'b64eb177bc7caa81f841ef64fa43b99b-1df6ec32-d0c0f265')
    subject = 'Coronavirus di Indonesia!'
    body = f"Total Kasus : {total_cases} ,\n\nBaru terjangkit :{new_cases}, \n\nYang mati:{total_deaths}"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('postmaster@sandbox9a81f6ab2bed4f17801a176da0ad5b42.mailgun.org','willigeraldy@gmail.com',msg)
    server.quit()

bot=Coronavirus()