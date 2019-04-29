from Manage_student import add_Student,get_Student
from Manage_Game import add_game,get_subscribers,subscribe_togame

# declaring student data
student_ids = {'A101','A102','A103'}
student_ids.add('A104')
student_ids.add('A105')
print(student_ids)
games = ('cricket','football','basketball','volleyball','chess')

student_info = {
    'A101':{'name':'Teja','branch':'CSE','year':4},
    'A102':{'name':'Vinay','branch':'Mech','year':4},
    'A103':{'name':'Kanthi','branch':'Civil','year':4},
    'A104':{'name':'Nandan','branch':'BSC','year':3}
    }
#student_info['A105'] = {'name':'Chaitanya','branch':'BSC','year':3}
sports_subscribed = {
    'cricket':{'A101','A102','A103'},
    'basketball':{'A101','A102'},
    'volleyball':{'A103'}
}
# print(student_ids)
# print(student_info['A101']['name'])
while True:
    get_user_option = input("What do you want to do? ")
    if get_user_option=="p":
        get_Student.getStudentInfo(student_info)
    elif get_user_option=="i":    
        result = add_Student.addNewstudent(student_ids,student_info)
        student_ids = result[0]
        student_info = result[1]
        get_Student.getStudentInfo(student_info)
    elif get_user_option=="g":
        get_subscribers.getsubscribers(student_ids,student_info,sports_subscribed)
        
        

    elif get_user_option == "gs":
        result = subscribe_togame.new_game_subscribers(student_ids,student_info,sports_subscribed)
        student_ids = result[0]
        student_info = result[1]
        sports_subscribed = result[2]



        
    else:
        break

# for k,v in student_info.items():
#     print(k,end=" ")
#     print(v['name'])