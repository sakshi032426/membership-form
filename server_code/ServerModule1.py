import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def submit(NAME,WEIGHT,ADDRESS,PERSONAL):
  app_tables.gym.add_row(NAME=NAME,WEIGHT=WEIGHT,ADDRESS=ADDRESS,PERSONAL=PERSONAL)
  anvil.email.send(to="sakshi_r.it2020@msit.edu.in", subject="response from anvil app", 
                     text=f"Feedback from {NAME}: Weight is {WEIGHT} and they live at: {ADDRESS}. Personal training required: {PERSONAL}")