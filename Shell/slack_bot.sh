#!/bin/sh
#Usage: Slack_bot <slack_token> <slack_channel> <slack_bot_name> <slack_message>
#Created by Aaron Mulvaney

token=$1
channel=$2
bot_name=$3
message=$4

if [ "$token" = "" ]
then
    echo "No token specified"
    exit 1
fi

if [ "$channel" = "" ]
then
    echo "No channel specified"
    exit 1
fi

if [ "$bot_name" = "" ]
then
    echo "No bot name specified"
    exit 1
fi

if [ "$message" = "" ]
then
    echo "No message specified"
    exit 1
fi

curl -X POST -H "Authorization: Bearer $token" \
-H 'Content-type: application/json' \
--data '{"channel": "'"$channel"'", "username": "'"$bot_name"'", "text": "'"$message"'",  "icon_emoji": ":robot_face:"}' \
https://slack.com/api/chat.postMessage
