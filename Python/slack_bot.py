''' Usage: Slack_bot <slack_token> <slack_channel> <slack_bot_name> <slack_message>
'''
import sys
import os
import requests

from slackclient import SlackClient

slack_token = sys.argv[1]
slack_channel = sys.argv[2]
bot_name = sys.argv[3]
slack_message = sys.argv[4]

def post_to_slack(slack_token, slack_channel, bot_name ,slack_message):
    '''Post slack_message to slack using bot
    '''
    try:
        sco = SlackClient(slack_token)
        result = sco.api_call("chat.postMessage", channel=slack_channel,
                              text=slack_message, username=bot_name,
                              icon_emoji=':robot_face:')
        return result.get('ok', False)
    except requests.exceptions.RequestException as exception:
        print(exception('Exception: %s', exception))
        sys.exit(1)

if __name__ == "__main__":
    post_to_slack(slack_token,slack_channel,bot_name,slack_message)
