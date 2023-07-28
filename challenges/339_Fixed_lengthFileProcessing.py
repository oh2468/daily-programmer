## https://old.reddit.com/r/dailyprogrammer/comments/7b5u96/20171106_challenge_339_easy_fixedlength_file/

from urllib import request


def highest_salary():
    salary_file = request.urlopen("https://gist.githubusercontent.com/anonymous/747d5e3bbc57949d8bfe5fd82f359acb/raw/761277a2dcacafb3c06a1e6d0e405ca252098c09/Employee%2520Records.txt").read()
    lines = str(salary_file, "UTF-8").split("\n")
    earner, salary = "", 0

    for line in lines:
        if not line.startswith("::EXT::"):
            name = line[0:20].strip()
        elif line.startswith("::EXT::SAL"):
            income = int(line[11:])
            if income >= salary:
                earner = name
                salary = income
    return f"{earner}, ${salary:,d}"

assert highest_salary() == "Randy Ciulla, $4,669,876"
