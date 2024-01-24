def num_unique_emails(emails: list[str]) -> int:
    unique_emails = set()
    for email in emails:
        local_name, domain_name = email.split("@")
        local_name = local_name.replace(".", "")
        local_name = local_name.split("+")[0]
        unique_emails.add(local_name + "@" + domain_name)
    return len(unique_emails)
