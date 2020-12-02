def email_list(domains):
    """
    Question 1
    The email_list function receives a dictionary, which contains domain names as keys, 
    and a list of users as values. 
    Fill in the blanks to generate a list that contains c
    omplete email addresses (e.g. diana.prince@gmail.com).
    """
    emails = []
    for domain, users in domains.items():
        print(domain, users)
        for user in users:
            emails.append(user+"@"+domain)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))