import pywhatkit

try:
    pywhatkit.sendwhatmsg_instantly("Phone_Number","This is an automated whatsapp message sent as a result of me trying a project. If you are are receiving this message then it means I was successful",15,True,10)
    print("Message was successfully sent. ")
except:
    print("Error in sending the message!")
try:
    pywhatkit.sendwhatmsg_to_group_instantly("Group_ID","This is an automated whatsapp message sent as a result of me trying a project. If you are are receiving this message then it means I was successful",15,True,10)

except:
    print("Error in sendinThis is an automated whatsapp message sent as g the message!")
try:
    pywhatkit.sendwhats_image("Group_ID",r"image_path", "Again checking if I can make Whatsapp send an image on it's own",15,True,30)
    print("Message was successfully sent. ")
except:
    print("Error in sending the message!")

try:
    pywhatkit.sendwhats_image("Phone_Number",r"image_path", "Again checking if I can make Whatsapp send an image on it's own",15,True,30)
    print("Message was successfully sent. ")
except:
    print("Error in sending the message!")

try:
    pywhatkit.send_mail("sender's_email_id","password","Subject","This is an automated email sent as a result of me trying a project. If you are are receiving this mail then it means I was successful","receiver's_email_id")
    
except:
    print("Error in sending the Mail!")
