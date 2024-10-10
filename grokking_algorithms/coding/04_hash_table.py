def check_vote(name, d: dict):
    d.setdefault(name, 0)
    if d[name] == 0:  # already voted
        print("let", name, "vote")
        d[name] = 1
    else:  # not voted yet
        print("kick", name, "out")

d = {}
check_vote("john", d)
check_vote("mike", d)
check_vote("john", d)