def new_game_subscribers(sid,sinfo,sports_subscribed):
    stu_game = input("enter the game C-Cricket,F-football,v-volleyball,b-basketball: ")
    student_id = input ("enter your id: ")
    if student_id in sid:
        if stu_game == "C":
            sports_subscribed['cricket'].add(student_id)
        elif stu_game == "F":
            sports_subscribed['Football'].add(student_id)    
        elif stu_game == "v":
            sports_subscribed['volleyball'].add(student_id)
        elif stu_game == "b":
            sports_subscribed['basketball'].add(student_id)
    else:
        print("id's not find")

    return[sid,sinfo,sports_subscribed]        

