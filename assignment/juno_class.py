# user_access_detail = [
#     {"username": "2@asherflo", "password": "Tmitity"},
#     {"username": "iseoluwanimi", "password": "1245"},
#     {"username": "asherflo", "password": "folake"}
# ]


# user_access_detail ={
#     "favourite_food" : ["rice", "beans","dodo"],
#     "favourite_player":{"Asernal":"bukayo","chelsea":"lukaku","dekanorbs":"shege"},
#     "favourite_girl": "funke",
#     "favourite_music": ["last last","buga","azonto"],
#     "favourite_language":{"programming":"java","dialect":"yoruba","slag":"breakfast"}
#
# }
#
# def type_checker():
#     for key,value in user_access_detail.items():
#         if type(value) == str:
#             return "favourite_girl"
#         elif type(value) == list:
#             return "i dont know"
#     print("look inward")
#


#
# def check_detail(username, password):
#     for details in user_access_detail:
#         if details["username"] == username and details["password"] == password:
#             return True
#     return False


# print(check_detail("asherflo", "folake"))


user_details = {"name": "Aniyikaye",

                # "school":["semicolon","decagon"],
                "phone_number": ["09131106322"],
                "class": {"cohort09": "dekanorbs", "cohort10": "bright_light"}
                }


def update_contact(phonenumber):
    [value.append(phonenumber) for key, value in user_details.items() if
     isinstance(value, list) and key == "phone_number"]


if __name__ == "__main__":
    update_contact("908787")
    print(user_details)
