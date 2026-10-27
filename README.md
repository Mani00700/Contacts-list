# Contact Book

A simple command-line contact manager written in Python.
Contacts are saved in a JSON file, so they are still there the next time you run it.

## Features

- Add a contact (name and phone number)
- View all contacts as a numbered list
- Delete a contact by its number
- Handles invalid input and a corrupted data file without crashing

## Requirements

Python 3.8 or newer. No extra packages are needed.

## Usage

```bash
python contacts.py
```

You will see a menu:

```
==============================
        CONTACT BOOK
==============================
  1. Add a contact
  2. View contacts
  3. Delete a contact
  4. Quit
------------------------------
```

## How it works

- Contacts are stored as a list of dictionaries in `contacts.json`, created automatically on first use.
- Each action loads the file, makes its change, and saves it back.
- The file path is built from the script's location, so the app works from any folder.

## What I practiced

`json` (load/dump), file handling, `try/except`, functions, and input validation.
