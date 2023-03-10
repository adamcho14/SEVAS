#!/usr/bin/env python
# coding: utf-8

from os import environ
import cgi, cgitb

login = ""

print """Content-type: text/html

<form method="post" action="paper_voting.py">
<input type="text" name="login" placeholder="Login" required>
<br/>
<input type="password" name="password" placeholder="Password" required>
<input type="submit" value="Submit">
</form>"""
