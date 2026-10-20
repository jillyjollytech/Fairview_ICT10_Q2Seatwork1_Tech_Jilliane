from pyscript import document, display

def check_candidate_status(e):

 club_members = (
 'Monika Chan',
 'Sayori Chan',
 'Natsuki Chan',
 'Yuri San',
 'TJ Sales',
 'Jilliane Tech'                
) 

 document.getElementById("div2").innerHTML = "" 
 first_name = document.getElementById("fname").value.strip()
 last_name = document.getElementById("lname").value.strip()
 candidate_name = f"{first_name} {last_name}"
 is_member = candidate_name in club_members

 messages = {
     True: f"Congratulations {candidate_name}! You are now part of the CAC club!!",
     False: f"Sorry {candidate_name}, your name is not on the list..."
 }

 result = messages[is_member]
 display(result, target = "div2") 
