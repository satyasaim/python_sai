def addNewstudent(sid,sinfo):
    get_id = input("please enter Id: ")
    get_name = input("please enter name: ")
    get_branch = input("please enter branch: ")
    get_year = input("please enter year: ")

    sid.add(get_id)
    sinfo[get_id] = {'name':get_name,'branch':get_branch,'year':get_year}

    return [sid,sinfo]

    