#!/usr/bin/env python
# coding: utf-8

import cgi
import sqlite3
import os

if 'REMOTE_USER' in os.environ:
    login = os.environ['REMOTE_USER']

    form = cgi.FieldStorage()
    vote = form.getvalue('vote')

    connection = sqlite3.connect("db/persons.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM voters WHERE login=?", (login,))
    result = cursor.fetchall()
    connection.close()

    print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">
<title>Prijatie hlasu</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>

<body>

"""

    sent = False
    if result != [(0,)]:
        connection = sqlite3.connect("db/votes.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM votes WHERE login=?", (login,))
        result2 = cursor.fetchall()
        if result2 == [(0,)]:
            cursor.execute("INSERT INTO votes (login, vote) VALUES(?, ?)", (login, vote,))
            sent = True
        else:
            cursor.execute("SELECT CASE WHEN vote=0 THEN 0 ELSE 1 END FROM votes WHERE login=?", (login,))
            result3 = cursor.fetchall()
            if result3 ==[(0,)]:
                print """Už ste hlasovali papierovo. Nemožno už hlasovať elektronicky."""
            else:
                cursor.execute("UPDATE votes SET vote = ? WHERE login = ?", (vote, login,))
                sent = True
        connection.commit()
        if sent:
            print """Úspešne si poslal svoj hlas.<br>
    <textarea rows="10" cols="50" id="display_vote">%s</textarea>""" % vote

    else:
        print """Prepáč, ale nemôžeš hlasovať."""

    connection.close()


    print """<br>
<a href=cosign/coslogout.php?backurl=/index.py>Odhlásiť sa</a>
</body>

</html>"""

else:
    print
    """Content-type: text/html
    <html>
    <head>

    <meta charset="UTF-8">
    <title>Prístup zakázaný</title>

    </head>

    <body>
    <p>Prístup zakázaný!</p>
    </body>"""






