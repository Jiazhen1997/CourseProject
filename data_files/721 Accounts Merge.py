

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email_to_ids = defaultdict(set)
        for i, v in enumerate(accounts):
            for email in v[1:]:
                email_to_ids[email].add(i)

        
        visited = [False for _ in accounts]
        ret = []
        for i, v in enumerate(accounts):
            if not visited[i]:
                emails = set()
                self.dfs(i, accounts, email_to_ids, emails, visited)
                ret.append([v[0]] + sorted(emails))

        return ret

    def dfs(self, i, accounts, email_to_ids, emails, visited):
        visited[i] = True
        for email in accounts[i][1:]:
            emails.add(email)
            for nbr in email_to_ids[email]:
                if not visited[nbr]:
                    self.dfs(nbr, accounts, email_to_ids, emails, visited)


    def accountsMerge_error(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email_id = {}
        id_emails = defaultdict(list)
        for i in range(len(accounts)):
            person = None
            for email in accounts[i][1:]:
                if email in email_id:
                    person = email_id[email]
                    break

            for email in accounts[i][1:]:
                if person is None:
                    person = i
                    email_id[email] = person
                    id_emails[person].append(email)
                elif email not in email_id:
                    email_id[email] = person
                    id_emails[person].append(email)

        ret = []
        for k, v in id_emails.items():
            ret.append([accounts[k][0]] + sorted(v))

        return ret
