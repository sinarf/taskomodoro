#!/usr/bin/env python

import ./pomodoro.py


def test_start():
    pom = pomodoro.Pomodoro()
    assert type(pom) is pomodoro.Pomodoro
