#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: saitou
# @Date:   2016-07-18 23:19:33
# @Last Modified by:   Hideki Saito
# @Last Modified time: 2016-07-22 13:57:29

import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


VERSION = "1.0"


class SlackClientCommand(App):

    def __init__(self):
        super(SlackClientCommand, self).__init__(
            description='Slack Command-line Client',
            version=VERSION,
            command_manager=CommandManager('sc.cli'),
            deferred_help=True)

    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    return SlackClientCommand().run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

#
# [EOF]
#
