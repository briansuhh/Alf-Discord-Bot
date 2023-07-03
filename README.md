# How to setup environment for project

DISCLAIMER: It is highly recommended to use `Git Bash` while following this guide. `Git Bash` is included in the installation of `Git`. If you want help setting up `Git Bash` with `VS Code`, you can ask [Mark Achiles G. Flores Jr.](https://www.facebook.com/machi9716) for help.

- Setting Up Environment is only for those who want to start their own projects. If you are just trying to contribute to this project, you can skip this part.

## Creating a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Click `New Application` on the top right corner.
3. Give your application a name (this isn't the bot name, don't worry).
4. Go to the `Bot` tab from the side bar.
5. Give your bot a username (this will be the bot name displayed in Discord).
6. Copy the token or reset the token (if no copy token button is found).
   - This token shouldn't be publicized. Keep this token safe. The moment that this token gets leaked, you should immediately request for a new token on the [Discord Developer Portal](https://discord.com/developers/applications).
7. Scroll down and enable all `Privileged Gateway Intents`.
8. Go to the `OAuth2` tab from the side bar.
9. Click the `bot` checkbox. Then, click the `Administrator` checkbox from the `BOT PERMISSIONS`.
10. Copy the link below and use it to add the bot to your own personal testing server.

---

## Setting up environment (Creating a new project)

1. Install `virtualenv` using `pip install virtualenv`.
2. Create a virtual environment with `virtualenv` using `virtualenv .venv`.
3. Open the command palette in VS Code. Then, search for `Python: Select Interpreter`. Then, choose `.venv` from the list.
4. Activate the virtual environment using `source .venv/Scripts/activate`.
5. Install `discord.py` using `pip install discord.py[voice]`.
6. Install `python-dotenv` using `pip install python-dotenv`.
7. Create a new file called `.env`. Open the file using `code .env` and paste your Discord Bot Token under the `TOKEN` variable.
   - Like `TOKEN="paste_token_here"`.
8. Create a `settings.py` file and open it in VS Code using `code settings.py`.
9. Import the `TOKEN` from the `.env` using the following lines of code:

   ```
   import os
   from dotenv import load_dotenv()

   load_dotenv()
   TOKEN = os.getenv("TOKEN")
   ```

---

## Opening working project from GitHub

1. Clone the repository from GitHub (search online how to do so) and open the project in VS Code.
2. Install the `virtualenv` module using `pip install virtualenv`.
3. Create a virtual environment using `virtualenv .venv`.
4. Activate your virtual environment using `source .venv/Scripts/activate`.
5. Install the required modules using `pip install -r requirements.txt`.
6. Create a `.env` file using `code .env` then paste your token there.
   - Example: `TOKEN="paste_token_here"`.
7. Initialize your local git repository using `git init`.
8. Create and add `.env` to your `.gitignore` file using `echo .env >> .gitignore`.
