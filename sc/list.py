# -*- coding: utf-8 -*-
# @Author: saitou
# @Date:   2016-07-18 23:44:37
# @Last Modified by:   Hideki Saito
# @Last Modified time: 2016-07-19 21:42:04

import datetime
import logging
import os

from cliff.lister import Lister

import sc.libsc


def _append_global_args(parser):
    parser.add_argument(
        '--token',
        default=os.environ.get('SC_TOKEN'),
        help='Defaults to env[SC_TOKEN] or None.')
    return parser


class ChannelList(Lister):
    "Show a list of channels in the slack team."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(ChannelList, self).get_parser(prog_name)
        parser = _append_global_args(parser)
        return parser

    def take_action(self, parsed_args):
        client = sc.libsc.Client(parsed_args.token)
        channels = client.list_channels()
        return (('Name', 'Id'),
                ((name, channels[name]) for name in channels)
                )


class MemberList(Lister):
    "Show a list of members in the slack team."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(MemberList, self).get_parser(prog_name)
        parser = _append_global_args(parser)
        return parser

    def take_action(self, parsed_args):
        client = sc.libsc.Client(parsed_args.token)
        members = client.list_members()
        return (('Name', 'Id'),
                ((name, members[name]) for name in members)
                )


class ChannelHistory(Lister):
    "Show a list of channel histroy."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(ChannelHistory, self).get_parser(prog_name)
        parser = _append_global_args(parser)
        parser.add_argument('channel', nargs='?', default='general')
        return parser

    def take_action(self, parsed_args):
        client = sc.libsc.Client(parsed_args.token)
        return (('Timestamp', 'Message'),
                ((datetime.datetime.fromtimestamp(ts), msg)
                 for ts, msg in client.channel_history(parsed_args.channel))
                )

#
# [EOF]
#
