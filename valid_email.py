class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = set()

        for email in emails:
            local_name, domain_name = email.split("@")

            # Verify Local_name
            local_name = local_name.replace(".", "")
            if "+" in local_name:
                plus_idx = local_name.index("+")
                local_name = local_name[:plus_idx]
            
            actl_email = (local_name, domain_name)
            valid_emails.add(actl_email)

        return len(valid_emails)            