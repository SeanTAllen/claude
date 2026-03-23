---
name: graphql-bash
description: Load when writing gh api graphql mutations or queries via the Bash tool. Covers the bash escaping workaround for GraphQL type syntax with !.
disable-model-invocation: false
---

# GraphQL via Bash — Escaping Workaround

Claude Code's bash tool escapes exclamation marks, which corrupts GraphQL type syntax (ID and String with trailing exclamation marks). To work around this, write the query to a temporary file and read it with command substitution. For the body, use -F body=@file to read from a file. Example:
```
# Write query to file (use the Write tool — don't echo/cat, same escaping problem)
# _tmp_query.graphql contains: mutation($id: ID!, $body: String!) { ... }

gh api graphql \
  -f query="$(cat _tmp_query.graphql)" \
  -f id='NODE_ID' \
  -F body=@body_content.md \
  --jq '.data.updateDiscussion.discussion.url'
```
Clean up temp files after use.
