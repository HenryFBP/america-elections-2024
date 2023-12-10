import selenium
import os
import openai

# start LM Studio, rest API?

openai.api_base = "http://localhost:1234/v1" # point to the local server
openai.api_key = "" # no need for an API key

completion = openai.ChatCompletion.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ]
)

print(completion.choices[0].message)

# init local noSQL database

def scape_posts_from_user():
    # scrape posts from single user with selenium, save to nosql
    pass

# create function to scrape users from a single facebook group, save to nosql

# create function to analyze sentiment of a single post, to see if it's propaganda meant to incite strong emotions that could divide people, save to nosql

# create function to draft post to a Person, like "Hey I'm Henry Post, some dude that wrote this tool, to prevent the same hysteria that happened in 2020 from happening in 2024, please help us break this terrible cycle. God bless and be safe, and love thy neighbor etc"