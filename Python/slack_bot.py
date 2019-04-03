''' Usage: Slack_bot <slack_token> <slack_channel> <slack_bot_name> <slack_message>
Created by Aaron Mulvaney
'''
import sys
import requests

from slackclient import SlackClient

if len(sys.argv) < 2:
    print("Slack token missing")
    sys.exit(1)
else:
    SLACK_TOKEN = sys.argv[1]

if len(sys.argv) < 3:
    print("Slack channel missing")
    sys.exit(1)
else:
    SLACK_CHANNEL = sys.argv[2]

if len(sys.argv) < 4:
    print("Bot name missing")
    sys.exit(1)
else:
    BOT_NAME = sys.argv[3]

if len(sys.argv) < 5:
    print("Slack message missing")
    sys.exit(1)
else:
    SLACK_MESSAAGE = sys.argv[4]


def post_to_slack(slack_token, slack_channel, bot_name, slack_message):
    '''Post slack_message to slack using bot
    '''
    try:
        sco = SlackClient(slack_token)
        result = sco.api_call("chat.postMessage", channel=slack_channel,
                              text=slack_message, username=bot_name,
                              icon_emoji=':robot_face:')
        return result.get('ok', False)
    except requests.exceptions.RequestException as exception:
        print('Exception: %s', exception)
        sys.exit(1)


if __name__ == "__main__":
    post_to_slack(SLACK_TOKEN, SLACK_CHANNEL, BOT_NAME, SLACK_MESSAAGE)
