#!/usr/bin/env python
# coding: utf-8

import functions as f
import config as c
import cgi, cgitb
import sqlite3

form = cgi.FieldStorage()
login = form.getvalue('login')

connection = sqlite3.connect("db/persons.sqlite")
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM voters WHERE login=?", (login,))
result = cursor.fetchall()
connection.close()

if result !=[(0,)]:

    with open("login.txt", 'w') as file:
        file.write(login)

    print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">
<title>Hlasovanie</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script type="text/javascript" src="static/dist/openpgp.min.js"></script>
<script type="text/javascript" src="static/form_processing.js">
</script>
</head>
<body>

<h1> %s, vitajte vo volebnej aplikácii</h1>
<h2>Zvoľte maximálne %s kandidátov</h2>
<form name="voting" method="post" action="test_collection.py">""" % (login, str(c.CAND_NUM))
    print(f.print_form_field(f.select_candidates()))

    print """<input type="hidden" name="vote" value="0">
<input type="hidden" class="btn btn-primary" name ="submit" value="">
</form>
<button type="button" class="btn btn-primary" onclick="processForm(%s);">Vytvor hlas</button><br>
<textarea rows="10" cols="50" id="display_vote">Tvoj zašifrovaný hlas</textarea>
</body>
</html>""" % (str(c.CAND_NUM))

else:
    print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

</head>
<body>
<p>Nie ste platne prihlásení. Skúste to znova.</p>

<form method="post" action="voting.py">
<input type="text" name="login" placeholder="login" required>
<input type="submit" name ="return" class="btn btn-primary" value="Prihlásiť sa">
</form>
</body>
</html>"""


