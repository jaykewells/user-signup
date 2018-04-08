from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    user = request.args.get("user")
    usererror= request.args.get("usererror")
    usererror2 = request.args.get("usererror2")
    email = request.args.get("email")
    emailerror = request.args.get("emailerror")
    emailerror2 = request.args.get("emailerror2")
    emailerror3 = request.args.get("emailerror3")
    passerror = request.args.get("passerror")
    passerror2 = request.args.get("passerror2")
    vpasserror = request.args.get("vpasserror")
    if usererror == None:
        usererror = ""
    if usererror2 == None:
        usererror2 = ""
    if emailerror == None:
        emailerror = ""
    if emailerror2 == None:
        emailerror2 = ""
    if emailerror3 == None:
        emailerror3 = ""
    if passerror == None:
        passerror = ""
    if passerror2 == None:
        passerror2 = ""
    if vpasserror == None:
        vpasserror = ""
    return render_template("index.html", user=user, usererror=usererror, usererror2=usererror2, email=email, emailerror=emailerror, emailerror2=emailerror2, emailerror3=emailerror3, passerror=passerror, passerror2=passerror2, vpasserror=vpasserror)


@app.route("/validate", methods=["POST"])
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
        usererror += "Username must be at least 3 characters, and no longer than 20"
    if " " in user:
        usererror2  += "Username cannot contain spaces"

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
        emailerror3 += "Your email address must follow the format xxxx@xxxx.xxx"
    if count < 3 or count > 20:
        emailerror += "Email must be at least 3 characters, and no longer than 20"
    if count == 0:
        emailerror = ""
    if " " in email:
        emailerror2 += "Email cannot contain spaces"


#Validate Password
    count = 0
    for i in password:
        if i.isalpha() or i.isdigit():
            count += 1
        elif i == " ":
            passerror = "Password cannot contain spaces"
    if count < 3 or count > 20:
            passerror2 = "Password must be at least 3 spaces, and no more than 20"
    if password != vpass:
            vpasserror = "Your passwords do not match"


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
        redirectstr += "user=" + user + "&email=" + email

        return redirect("/?"+ redirectstr)

@app.route("/success")
def success():
    user = request.args.get("user")
    return render_template("success.html", user=user)

app.run()
