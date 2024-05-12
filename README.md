## Features

This is a simple program which does its work perfectly. Nothing more, nothing less

1. Send dynamic emails with unlimited variables pulling data from a xlsx file.
2. Supports Markdown Formatting & embed links or images.
3. Supports Attaching any kind of files.

## Usage

- Make sure you have Python installed in your system.

-Create the python environment
    python3 -m venv myenv
-Activate it
    myenv\Scripts\activate 
- Install all dependancies:
  pip install -r requirements.txt


- Put your data inside `data.xlsx` file

- You you want to put any attachments , put them in the `ATTACH` directory.

put your email in 
EMAIL_HOST_USER =""

- **Do not put original email password.**
  Create Gmail Account then turn on 2 step Verification, and then set up an [App Password](https://support.google.com/accounts/answer/185833?hl=en) for `automailer`.

- All set up 👍 you are now READY TO GO . Run the `send.py` file:
  ```shell
  python3 send.py
  ```

- You will receive a full success report after emails are sent.

