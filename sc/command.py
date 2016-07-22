# -*- coding: utf-8 -*-
# @Author: Hideki Saito
# @Date:   2016-07-19 14:24:10
# @Last Modified by:   Hideki Saito
# @Last Modified time: 2016-07-21 01:00:39

import logging
import os

from cliff.command import Command

import sc.libsc


class MessagePost(Command):
    "Sending message to the specified channel."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(MessagePost, self).get_parser(prog_name)
        parser.add_argument(
            '--token',
            default=os.environ.get('SC_TOKEN'),
            help='Defaults to env[SC_TOKEN] or None.')
        parser.add_argument(
            '--channel',
            default='general',
            help='Defaults to "general"')
        parser.add_argument(
            '--user',
            default='None',
            help='Defaults to None')
        parser.add_argument(
            '--icon_url',
            default=os.environ.get('SC_ICON_URL'),
            help='Defaults to env[SC_ICON_URL] or None.')
        parser.add_argument('message', nargs='?', default='')
        return parser

    def take_action(self, parsed_args):
        client = sc.libsc.Client(parsed_args.token)
        result = client.send_message(username=parsed_args.user,
                                     channel=parsed_args.channel,
                                     message=parsed_args.message,
                                     icon_url=parsed_args.icon_url)
        print('Send message: "{0:s}" to "{1} channel"'.format(
            parsed_args.message,
            parsed_args.channel))
        if result:
            print('Succeeded')
        else:
            print('Failed')

#
# [EOF]
#
