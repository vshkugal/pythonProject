# ------------------------------------------------------------------------------------------------
# SauceDemo site item ids
# ------------------------------------------------------------------------------------------------
import re
ID_REGEX = re.compile(r'\d+')

# ------------------------------------------------------------------------------------------------
# SauceDemo site links
# ------------------------------------------------------------------------------------------------
SAUCEDEMO_MAIN = "https://www.saucedemo.com/"
SAUCELABS_MAIN = "https://saucelabs.com/"
TWITTER_LINK = "https://twitter.com/saucelabs"
FACEBOOK_LINK = "https://www.facebook.com/saucelabs"
LINKEDIN_LINK = "https://www.linkedin.com/company/sauce-labs/"
SAUCEDEMO_INVENTORY = "https://www.saucedemo.com/inventory.html"
SAUCEDEMO_CART = "https://www.saucedemo.com/cart.html"

# ------------------------------------------------------------------------------------------------
# SauceDemo site title and log name
# ------------------------------------------------------------------------------------------------
SAUCEDEMO_TITLE = "Swag Labs"
SAUCEDEMO_LOG = "saucedemo.log"

# ------------------------------------------------------------------------------------------------
# SauceDemo site user login details
# ------------------------------------------------------------------------------------------------
standard_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
user_password = "secret_sauce"
incorrect_user = "incorrect_user"
incorrect_password = "incorrect_password"

# ------------------------------------------------------------------------------------------------
# SauceDemo site user login error messages
# ------------------------------------------------------------------------------------------------
INCORRECT_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
LOCKED_OUT_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
LOGGED_OUT_MESSAGE = "Epic sadface: You can only access '/inventory.html' when you are logged in."
