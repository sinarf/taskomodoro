#!/usr/bin/env python

"""Tests for `taskomodoro` package."""

import pytest
from taskomodoro import taskomodoro


def test_start():
    assert "TODO: do something" == taskomodoro.start()


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
