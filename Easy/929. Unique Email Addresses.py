class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        remails = []
        for email in emails:
            email = email.split('@')
            email[0] = email[0].replace('.', '')
            if '+' in email[0]:
                email[0] = list(email[0])
                email[0] = email[0][:email[0].index('+')]

            email[0] = ''.join(email[0]) + "@"
            print(''.join(email))
            if ''.join(email) not in remails:
                remails.append(''.join(email))

        return len(remails)
