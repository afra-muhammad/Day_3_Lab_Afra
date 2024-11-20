##import pytest
import io
##import sys
##import os

##sys.path.append(os.path.abspath('..//src'))

##from user_functions import *
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email
def get_user_name_from_input():
    """ Not empty string. No spaces. """
    return input("Create your user name: ")
def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    return input("Create your password: ")

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

def test_user_name_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('AfraMuhammad'))
    assert get_user_name_from_input() == 'AfraMuhammad'


def test_password_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Valid@123'))
    assert get_password_from_input() == 'Valid@123'
