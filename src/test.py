from openai import OpenAI
from selenium import webdriver

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


def scape_posts_from_user():

  url='https://www.facebook.com/HenryFidelBradleyPost'
  
  driver=webdriver.Chrome()
  driver.get(url)
  util.fullpage_screenshot(driver, "test.png")
  driver.quit()

  # scrape posts from single user with selenium, save to nosql

  # client.chat.completions.create

  pass

# create function to scrape users from a single facebook group, save to nosql

# create function to analyze sentiment of a single post, to see if it's propaganda meant to incite strong emotions that could divide people, save to nosql

# create function to draft post to a Person, like "Hey I'm Henry Post, some dude that wrote this tool, to prevent the same hysteria that happened in 2020 from happening in 2024, please help us break this terrible cycle. God bless and be safe, and love thy neighbor etc"

if __name__ == "__main__":
  print("test")

  scape_posts_from_user()