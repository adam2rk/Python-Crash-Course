from name_func import get_formatted_name

def test_first_last_name():
    formattedName = get_formatted_name("janis", "joplin")
    #The assertion is a claim about the condition there were claiming
    assert formattedName == "Janis Joplin"

#well use pytest to run this for us
#python -m pytest the test ran and passed

#ima skip the rest of this chapter not needed for right now