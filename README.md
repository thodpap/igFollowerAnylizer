# igFollowerAnylizer

- There is a requirements.txt file that tell you the dependencies you need to have
- You need to install a chrome Webdriver (For linux users: `https://pypi.org/project/chromedriver-binary/`, in case you have an issue with the PATH you can see `https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path`).
- Check https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.48/
- Update line 9 of `main.py` with your ig page name
- Run `python3 main.py` or `python main.py` accordingly
- Once you type your credentials in the browser DO NOT press anything on the browser
- Press enter on the terminal to continue
- Let the app run. When it finishes you will have 2 files `followers.txt` and `following.txt` with a list on each file
- On the terminal you will see the differences between the 2 files
