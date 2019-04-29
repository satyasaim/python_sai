def getsubscribers(sid,sinfo,sports_subscribed):
    get_gamesubscribers = input("enter C-cricket F-footbal v-volleyball b-basketball: ")
    if get_gamesubscribers == "all":
        for k,v in sports_subscribed.items():
            print(k,"Subscribe sutdents")
            for s in v:
                print(sinfo[s]['name'])
    elif get_gamesubscribers == "c":
        print("student subscriber for cricket")
        for v in sports_subscribed:
            print(sports_subscribed['cricket'])
    elif get_gamesubscribers == "f":
        print("student subscriber for football")
        for v in sports_subscribed:
            print(sports_subscribed['football'])
    elif get_gamesubscribers == "v":
        print("student subscriber for volleyball")
        for v in sports_subscribed:
            print(sports_subscribed['volleyball'])
    elif get_gamesubscribers == "b":
        print("student subscriber for basketball")
        for v in sports_subscribed:
            print(sports_subscribed['basketball'])                           
