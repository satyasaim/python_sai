def addnewgame (sid,sinfo):
    get_id = input("please enter Id:")
    get_game = input('enter your game')

    sid.add(get_id)
    sinfo[get_id] = {'game':get_game}

    return[sid,sinfo]


