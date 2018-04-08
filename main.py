from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    user = request.args.get("user")
    usererror= request.args.get("usererror")
    email = request.args.get("email")
    emailerror = request.args.get("emailerror")
    passerror = request.args.get("passerror")
    vpasserror = request.args.get("vpasserror")
    if user == None:
        user = ""
    if email == None:
        email = ""
    if usererror == None:
        usererror = ""
    if emailerror == None:
        emailerror = ""
    if passerror == None:
        passerror = ""
    if vpasserror == None:
        vpasserror = ""
    return render_template("index.html", user=user, usererror=usererror, email=email, emailerror=emailerror, passerror=passerror, vpasserror=vpasserror)


@app.route("/validate", methods=["POST"])
def validate():
    user = cgi.escape(request.form["user"])
    usererror = ""
    email = cgi.escape(request.form["email"])
    emailerror = ""
    format1 = False
    format2 = False
    password = cgi.escape(request.form["password"])
    passerror = ""
    vpass = cgi.escape(request.form["vpass"])
    vpasserror = ""

    #Check Username for validation
    count = 0
    for i in user:
        if i.isalpha():
            count += 1
    if count < 3 or count > 20:
        usererror += "Username must be at least 3 characters, and no longer than 20. "
    if " " in user:
        usererror  += "Username cannot contain spaces."

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
        emailerror += "Your email address must follow the format xxxx@xxxx.xxx. "
    if count < 3 or count > 20:
        emailerror += "Email must be at least 3 characters, and no longer than 20. "
    if " " in email:
        emailerror += "Email cannot contain spaces"
    if count == 0:
        emailerror = ""

#Validate Password
    count = 0
    for i in password:
        if i.isalpha() or i.isdigit():
            count += 1
        elif i == " ":
            passerror = "Password cannot contain spaces. "
    if count < 3 or count > 20:
            passerror += "Password must be at least 3 spaces, and no more than 20."
    if password != vpass:
            vpasserror = "Your passwords do not match"


        #Validates that there are no errors.
    if usererror == "" and emailerror == "" and passerror == "" and vpasserror == "":
        return redirect("/success?user=" + user)
    else:
        redirectstr = ""
        if usererror != "":
            redirectstr += "usererror=" + usererror + "&"
        if emailerror != "":
            redirectstr += "emailerror=" + emailerror + "&"
        if passerror != "":
            redirectstr += "passerror=" + passerror + "&"
        if vpasserror != "":
            redirectstr += "vpasserror=" + vpasserror + "&"
        redirectstr += "user=" + user + "&email=" + email

        return redirect("/?"+ redirectstr)

@app.route("/success")
def success():
    user = request.args.get("user")
    return render_template("success.html", user=user)

app.run()
