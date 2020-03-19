#!/usr/bin/env python

# Pomodoro timer

from enum import Enum
import logging as log


class Status(Enum):
    """
    Status that a pomodoro can have
    NONE: is the status before th
    """
    STARTED = 'STARTED'
    FINISHED = 'FINISHED'
    INTERRUPTED = 'INTERRUPTED'


class Pomodoro:
    """
    The pomodoro class
    """

    def start(self):
        """
        Start a pomodoro
        """
        status = Status.STARTED

    def interrupt(self, reason='lost track'):
        """
        Interupt a pomodoro.
        """
        if status == Status.STARTED:
            status = Status.INTERRUPTED
        else:
            log.warn "this pomodoro is not started! Actual status: " + status

