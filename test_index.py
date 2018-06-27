#!/usr/bin/env python
# coding: utf-8

#This is to be provided by Cosign, but for now...

from os import environ
import cgi, cgitb

print """Content-type: text/html
<html>

<head>
<title>Volebný systém FMFI UK</title>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>

<body>

<h1>Vitajte na stránkach volebného systému FMFI UK</h1>

<form method="post" action="test_voting.py">
<input type="text" name="login" placeholder="login" required>
<input type="submit" name ="return" class="btn btn-primary" value="Prihlásiť sa">
</form>
</body>
</html>"""
