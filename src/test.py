from openai import OpenAI
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import pickle
import tkinter as tk
from tkinter import messagebox
import tinydb

from dotenv import load_dotenv

load_dotenv()

import util

client = OpenAI()

def test_can_query_api():
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ]
  )

  print(completion.choices[0].message)


class FacebookWebDriver(webdriver.Chrome):
    
    def is_logged_in(self)->bool:
      return ("Memories" in self.page_source)

    def login_to_facebook(self, username, password):
        
        def save_cookies(self=self):
        # Check if we're logged in. if so, save cookies
          if(self.is_logged_in()):
            cookies = self.get_cookies()
            with open("cookies.pkl", "wb") as file:
              pickle.dump(cookies, file)
          else:
             raise Exception("We apparently aren't logged in, so we can't save cookies.")

        # Navigate to the Facebook login page
        self.get('https://www.facebook.com/')

        # use cookies if they exist
        if os.path.exists("cookies.pkl"):
            # Load the cookies from the file
            with open("cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.add_cookie(cookie)

            # Navigate to the Facebook login page
            self.get('https://www.facebook.com/')
            time.sleep(2)

            if self.is_logged_in():
                print("Successfully logged in.")
            else:
               raise Exception("Not logged in after loading cookies.")

            return


        # Navigate to the Facebook login page
        self.get('https://www.facebook.com/')

        # Wait for the login page to load
        time.sleep(2)

        # Locate the email/phone number field and enter the username
        email_input = self.find_element(By.ID, 'email')
        email_input.send_keys(username)

        # Locate the password field and enter the password
        password_input = self.find_element(By.ID, 'pass')
        password_input.send_keys(password)

        # Press Enter to submit the form and log in
        password_input.send_keys(Keys.RETURN)

        # Wait for the main page to load after login
        time.sleep(5)

        # Ask the user to manually log in
        root = tk.Tk()
        root.title("Click OK when you're logged in")

        ok_button = tk.Button(
            root, text="I'm logged in", 
            command=(lambda x: [save_cookies(), root.quit()])
        )
        ok_button.pack(pady=20, padx=20)

        root.mainloop()




def scape_posts_from_user(url:str):

  
  driver=FacebookWebDriver()
  driver.login_to_facebook(
    os.environ.get("FACEBOOK_USERNAME"),
    os.environ.get("FACEBOOK_PASSWORD")
  )
  # util.fullpage_screenshot(driver, "test.png")
  driver.save_screenshot("test.png")
  driver.quit()

  # scrape posts from single user with selenium, save to nosql

  # client.chat.completions.create

  pass

# create function to scrape users from a single facebook group, save to nosql

# create function to analyze sentiment of a single post, to see if it's propaganda meant to incite strong emotions that could divide people, save to nosql

# create function to draft post to a Person, like "Hey I'm Henry Post, some dude that wrote this tool, to prevent the same hysteria that happened in 2020 from happening in 2024, please help us break this terrible cycle. God bless and be safe, and love thy neighbor etc"

if __name__ == "__main__":
  print("test")

  scape_posts_from_user('https://www.facebook.com/HenryFidelBradleyPost')