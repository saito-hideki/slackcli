# -*- coding: utf-8 -*-
# @Author: saitou
# @Date:   2016-07-18 13:30:49
# @Last Modified by:   Hideki Saito
# @Last Modified time: 2016-07-21 18:03:59

from slackclient import SlackClient


class Client(object):
    def __init__(self, token):
        self.client = SlackClient(token)
        if not self._check_client():
            raise RuntimeError('API test failed')

    def _check_client(self):
        result = self.client.api_call('api.test')
        return result['ok']

    def _get_channel_by_name(self, name):
        channels = self.list_channels()
        return channels[name]

    def _get_user_by_name(self, name):
        channels = self.list_members()
        return channels[name]

    def list_channels(self):
        result = self.client.api_call('channels.list')
        if not result['ok']:
            return {}
        channels = {ch['name']: ch['id'] for ch in result['channels']}
        return channels

    def list_members(self):
        result = self.client.api_call('users.list')
        if not result['ok']:
            return {}
        members = {ch['name']: ch['id'] for ch in result['members']}
        return members

    def channel_history(self, name):
        id = self._get_channel_by_name(name)
        result = self.client.api_call('channels.history',
                                      channel=id)
        history = []
        for msg in result['messages']:
            history.append((float(msg['ts']), msg['text']))
        return(history)

    def send_message(self, username, channel, message, icon_url):
        result = self.client.api_call('chat.postMessage',
                                      channel=channel,
                                      username=username,
                                      text=message,
                                      icon_url=icon_url)
        return result['ok']

    def show_member(self, name):
        id = self._get_user_by_name(name)
        result = self.client.api_call('users.info',
                                      user=id)
        if not result['ok']:
            return {}
        data = {
            'id': result['user']['id'],
            'name': result['user']['name'],
            'email': result['user']['profile']['email'],
            'real_name': result['user']['profile']['real_name'],
            'tz': result['user']['tz'],
            'is_bot': result['user']['is_bot']
        }
        return data

#
# [EOF]
#
