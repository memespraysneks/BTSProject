# BTSProject - SimplyCalendar

Helps users record events and activities, keep track of upcoming meeting and deadlines, and set reminders along with important and personal future events.

## Installation/Setup
### Windows
1. Clone the repo
2. Run setup.bat
3. Define database details in dbconnection.py
4. Start the app with start.bat

### Linux
1. Clone the repo
2. Run `pip install -r requirements.txt`
3. Define database details in dbconnection.py
4. Run `guinicorn "flaskr:create_app()"`

## Deploy
- Built-in support for deploying with Heroku.
