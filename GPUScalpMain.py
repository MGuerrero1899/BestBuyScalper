from tkinter import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#Timing purchase
#start_time = time.time()

#Takes info from submit button and passes to main program
def click():
    scalp_bot_3000(bestbuy_link.get(),email_pypal.get(),password_pypal.get())

#GUI Setup
app = Tk()
app.geometry("700x700")
app.title("Best Buy Scalper")
app.configure(background="black")
gpu_photo = PhotoImage(file="N6SqRbVmDQzZWQMDjtntrW.png")
gpu_photo.subsample(2, 2)
gpu_label = Label (app, image=gpu_photo, bg="black").grid(row=0,column=0,columnspan=2,rowspan=1,padx=3,pady=3)

#Widget Declaring
bestbuy_link_form = Label(app,text="Enter Best Buy Link",bg="black",fg="white",font="none 12 bold")
bestbuy_link = Entry(app,width=50)
email_text_form = Label (app,text="Enter Paypal Email", bg="black", fg="white", font="none 12 bold")
email_pypal = Entry(app,width=50)
password_text_form = Label(app,text="Enter Paypal Password", bg="black", fg="white", font="none 12 bold")
password_pypal = Entry(app,width=50)
submit_button = Button(app, text="SUBMIT", width=8, command=click)


#Label GUI Setup
bestbuy_link_form.grid(row=1,column=0)
bestbuy_link.grid(row=1,column=1)
email_text_form.grid(row=2,column=0)
email_pypal.grid(row=2,column=1)
password_text_form.grid(row=3,column=0)
password_pypal.grid(row=3,column=1)
submit_button.grid(row=5,column=1)

#Main Function of scalp bot
def scalp_bot_3000(link,pyplemail,pyplpw):
    # Location of webdriver.exe
    PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
    #URL to download chrome driver
    #(https://sites.google.com/a/chromium.org/chromedriver/downloads)
    driver = webdriver.Chrome(PATH)

    driver.get(link)
    #Test Link
    #driver.get("https://www.bestbuy.com/site/logitech-m325-wireless-optical-mouse-works-with-chromebook-silver/2577677.p?skuId=2577677")
    Available = False

    while(Available != True):
        try:
            buy_item = driver.find_element_by_class_name("btn-disabled")
            print(driver.title)
            print("Out of Stock")
            driver.implicitly_wait(1)
            driver.refresh()
        except:
            buy_item = driver.find_element_by_class_name("btn-primary")
            print(driver.title)
            print("In Stock Purchasing")
            driver.implicitly_wait(1)
            buy_item.click()
            Available = True

        bestbuy_cart = driver.get("https://www.bestbuy.com/cart")
        #Wait for BestBuy Paypal Purchase Button to Load
        try:
            bestbuy_checkout = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "checkout-buttons__paypal"))
            )
            bestbuy_checkout.click()
            #Wait for Paypal Email Prompt to Load
            try:
                paypal_email_textbox = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "email"))
                )
                paypal_email_textbox.send_keys(pyplemail)
                driver.find_element_by_id("btnNext").click()
                driver.implicitly_wait(1)
                paypal_password_textbox = driver.find_element_by_xpath('//*[@id="password"]')
                paypal_password_textbox.send_keys(pyplpw)
                login_paypal = driver.find_element_by_id("btnLogin")
                login_paypal.click()
                continue_paypal = driver.find_element_by_id("payment-submit-btn")
                continue_paypal.click()
                placeorder = driver.find_element_by_class_name("btn-primary")
                placeorder.click()
                print("Order successful")
                #print("%s seconds" % (time.time()-start_time))
                driver.quit()
            except:
                print("Error on Login")
                driver.quit()
        except:
            print("Error during checkout")
            driver.quit()

app.mainloop()