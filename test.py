def validate():
    user = request.form["user"]
    usererror = ""
    usererror2 = ""
    email = request.form["email"]
    emailerror = ""
    emailerror2 = ""
    emailerror3 = ""
    format1 = False
    format2 = False
    password = request.form["password"]
    passerror = ""
    passerror2 = ""
    vpass = request.form["vpass"]
    vpasserror = ""

    #Check Username for validation
    count = 0
    for i in user:
        if i.isalpha():
            count += 1
    if count < 3 or count > 20:
        usererror += "Username must be at least 3 characters, and no longer than 20."
    if " " in user:
        usererror2  += "Username cannot contain spaces."

#Validate Email
    count = 0
    for i in email:
        if i.isalpha():
            count +=1
        if i == "@":
            format1 = True
        if i == ".":
            format2 = True
    if format1 != True or format2 != True:
        emailerror3 += "Your email must follow the format xxx@xxx.xxx"
    if count < 3 or count > 20:
        emailerror += "Email must be at least 3 characters, and no longer than 20."
    if " " in email:
        emailerror2 += "Email cannot contain spaces."


#Validate Password
    count = 0
    for i in password:
        if i.isalpha():
            count += 1
        elif i == " ":
            passerror = "Password cannot contain spaces."
    if count < 3 or count > 20:
            passerror2 = "Password must be at least 3 spaces, and no more than 20."
    if password != vpass:
            vpasserror = "Your passwords do not match. "


        #Validates that there are no errors.
    if usererror == "" and usererror2 == "" and emailerror == "" and emailerror2 == "" and emailerror3 == "" and passerror == "" and passerror2 =="" and vpasserror =="":
        #return redirect("/success?user=" + user)
        return redirect("/success?user=" + user)
    else:
        redirectstr = ""
        if usererror != "":
            redirectstr += "usererror=" + usererror + "&"
        if usererror2 != "":
            redirectstr += "usererror2=" + usererror2 + "&"
        if emailerror != "":
            redirectstr += "emailerror=" + emailerror + "&"
        if emailerror2 != "":
            redirectstr += "emailerror2=" + emailerror2 + "&"
        if emailerror3 != "":
            redirectstr += "emailerror3=" + emailerror3 + "&"
        if passerror != "":
            redirectstr += "passerror=" + passerror + "&"
        if passerror2 != "":
            redirectstr += "passerror2=" + passerror2 + "&"
        if vpasserror != "":
            redirectstr += "vpasserror=" + vpasserror + "&"
        if redirectstr[-1] == "&":
            redirectstr = redirectstr[:len(redirectstr)-1]
        return redirect("/?"+ redirectstr)


validate()
