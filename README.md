cs-kaist-cal-sync
============
Syncs CS KAIST events to your calendar.

Developer Guide
-----------------
**Create credentials.json file**

Follow the steps outlined [here](https://developers.google.com/calendar/quickstart/python)

**Create virtual environment**
```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv)$
```

**Install python dependencies**
```bash
(venv)$ pip3 install -r requirements.txt
```

**Edit sync_cal.py**
```python 
if __name__ == '__main__':
    ...
    # Update with your own Google calendar ID
    cal = GCalendar('2mg4vsjdeejg8clpd7gvs5iudk@group.calendar.google.com')
```

**Run**
```bash
(venv)$ python sync_cal.py
WARNING:root:Fetching event: 8463
...
```

User Guide
-----------------
A public calendar is shared [here](https://calendar.google.com/calendar/b/2?cid=Mm1nNHZzamRlZWpnOGNscGQ3Z3ZzNWl1ZGtAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ). <br/>
You can directly add it to your account.

License
-----------------
```text
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
```

Authors
-----------------
- Gaurav Kalra (<gvkalra@gmail.com>)