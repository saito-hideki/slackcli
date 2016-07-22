# -*- coding: utf-8 -*-
# @Author: saitou
# @Date:   2016-07-21 16:45:43
# @Last Modified by:   Hideki Saito
# @Last Modified time: 2016-07-21 18:08:07

import logging
import os

from cliff.show import ShowOne

import sc.libsc


def _append_global_args(parser):
    parser.add_argument(
        '--token',
        default=os.environ.get('SC_TOKEN'),
        help='Defaults to env[SC_TOKEN] or None.')
    return parser


class MemberShow(ShowOne):
    "Show detail information of user"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(MemberShow, self).get_parser(prog_name)
        parser.add_argument('name', nargs='?', default='.')
        parser = _append_global_args(parser)
        return parser

    def take_action(self, parsed_args):
        client = sc.libsc.Client(parsed_args.token)
        result = client.show_member(parsed_args.name)
        columns = ('Id',
                   'Name',
                   'Email',
                   'RealName',
                   'TimeZone',
                   'Bot',
                   )
        data = (result['id'],
                result['name'],
                result['email'],
                result['real_name'],
                result['tz'],
                result['is_bot'],
                )
        return (columns, data)

#
# [EOF]
#
