# Recipe — set a GitHub issue's type

GitHub issue types (Task/Bug/Feature) can't be set through `gh issue create`/`gh issue edit` — only through GraphQL. After creating the issue, set its type in three steps. Step 3's mutation uses `ID!` variables, so it needs the temp-file escaping workaround from this skill's `SKILL.md`.

1. Resolve the type's node ID by name. Query the repo (org-owned repos inherit the org's types; personal repos have none). Swap `Bug` for the type you're setting:
```
gh api graphql \
  -f query='{ repository(owner: "OWNER", name: "REPO") { issueTypes(first: 20) { nodes { id name } } } }' \
  --jq '.data.repository.issueTypes.nodes[]? | select(.name == "Bug") | .id'
```
The `?` makes a repo with no issue types return nothing instead of a jq error. If this returns nothing — a personal-account repo has none — there's no type to set, so stop here; don't ask Sean to set it by hand.

2. Get the issue's node ID:
```
gh issue view NUMBER --repo OWNER/REPO --json id --jq '.id'
```

3. Run the mutation. Write the query to a temp file per the escaping workaround, then:
```
# _tmp_set_type.graphql contains:
# mutation($issueId: ID!, $issueTypeId: ID!) {
#   updateIssueIssueType(input: {issueId: $issueId, issueTypeId: $issueTypeId}) {
#     issue { number issueType { name } }
#   }
# }

gh api graphql \
  -f query="$(cat _tmp_set_type.graphql)" \
  -f issueId='ISSUE_NODE_ID' \
  -f issueTypeId='TYPE_NODE_ID' \
  --jq '.data.updateIssueIssueType.issue.issueType.name'
```
The mutation echoes the type name back, so you can confirm it stuck. Clean up the temp file.
