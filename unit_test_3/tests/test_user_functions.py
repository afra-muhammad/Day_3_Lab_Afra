import pytest
import io
import sys
import os

sys.path.append(os.path.abspath('..//src'))

from user_functions import *

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

def test_user_name_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('AfraMuhammad'))
    assert get_user_name_from_input() == 'AfraMuhammad'


def test_password_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Valid@123'))
    assert get_password_from_input() == 'Valid@123'
