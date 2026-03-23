---
name: zulip
description: Load when Sean shares a Zulip link or asks to read Zulip messages. Covers credential parsing and API usage.
disable-model-invocation: false
---

# Reading Zulip Messages

Credentials are in ~/.zuliprc. Parse and use with curl:

```bash
EMAIL=$(grep '^email' ~/.zuliprc | cut -d= -f2); KEY=$(grep '^key' ~/.zuliprc | cut -d= -f2); SITE=$(grep '^site' ~/.zuliprc | cut -d= -f2); curl -s -u "$EMAIL:$KEY" "$SITE/api/v1/messages?anchor=newest&num_before=50&num_after=0&narrow=$(python3 -c 'import json,urllib.parse; print(urllib.parse.quote(json.dumps([{"operator":"channel","operand":"CHANNEL_NAME"},{"operator":"topic","operand":"TOPIC NAME"}])))')"
```

Sean provides URLs like: https://ponylang.zulipchat.com/#narrow/channel/CHANNELID-channel-name/topic/Topic.20Name

Parse these to extract the channel name and topic (.20 = space), then substitute into the API call above.

The response is JSON with a messages array. Each message has sender_full_name, content (HTML), and timestamp. Summarize the conversation for Sean rather than dumping raw JSON.
