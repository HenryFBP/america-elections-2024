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
import facebook

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

  return True

def scape_posts_from_user(url:str):

  # Initialize the Graph API with your access token
  graph = facebook.GraphAPI(access_token=os.environ.get("FACEBOOK_ACCESS_TOKEN"), version="3.1")

  # Get your profile information
  user_profile = graph.get_object('me')

  # Print your profile information
  print(user_profile)

  pass

# create function to scrape users from a single facebook group, save to nosql

# create function to analyze sentiment of a single post, to see if it's propaganda meant to incite strong emotions that could divide people, save to nosql

# create function to draft post to a Person, like "Hey I'm Henry Post, some dude that wrote this tool, to prevent the same hysteria that happened in 2020 from happening in 2024, please help us break this terrible cycle. God bless and be safe, and love thy neighbor etc"

if __name__ == "__main__":
  print("test")

  scape_posts_from_user('https://www.facebook.com/HenryFidelBradleyPost')