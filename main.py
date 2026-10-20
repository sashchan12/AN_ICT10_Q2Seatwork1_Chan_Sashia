from pyscript import document

# First + Last names of the members
CLUB_MEMBERS = ["Sashia Chan", "Luisito Balajadia", "Mica Frigillana", "Denie Red", "Pauline Black", "Maddie Yellow", "David Blue", "Jethro Green", "Lucas Purple"]

# Checks if they are part of the club through a True or False result
RESULT_MESSAGES = {
    True: "Congratulations {name}! You are now part of the SCIENCE CLUB!",
    False: "Sorry {name}, your name is not on the list.",
}

# Combines the First & Last name input
def get_full_name():
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    return f"{first_name} {last_name}"

# True if it's in the list, False if it's not.
def check_membership(full_name):
    return full_name in CLUB_MEMBERS

# Displays the result based on the names in the list.
def show_result(full_name, is_member):
    result_area = document.getElementById("message")
    result_area.textContent = RESULT_MESSAGES[is_member].format(name=full_name)

# For enter: checks name and shows result.
def verify_member(event):
    full_name = get_full_name()
    is_member = check_membership(full_name)
    show_result(full_name, is_member)

# For reset: clears the input of the user.
def reset_form(event):
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
    document.getElementById("message").textContent = ""
