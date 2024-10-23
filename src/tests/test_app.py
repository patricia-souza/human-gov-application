import pytest
from app import home_page

def test_home_page():
    print('Execucao de testes')
    assert home_page('California') == 'Human Resources Management System - State of California'