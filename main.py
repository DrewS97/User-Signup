from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def start_page():
  return render_template("index.html")

#Rendered upon submit button
@app.route('/', methods=["POST"])
def sign_up():
  #User Inputs
  email = str(request.form.get('email'))
  username = str(request.form.get('username'))
  password = str(request.form.get('password'))
  verify = str(request.form.get('verify'))

  #Checks lengths of inputs
  elen = len(email)
  ulen = len(username)
  plen = len(password)
  vlen = len(verify)

  #Keeps track of spaces in inputs
  ecount = 0
  ucount = 0
  pcount = 0
  vcount = 0

  #Email Specific
  at = "@"
  period = "."
  atBool = False
  periodBool = False

  if "@" in email:
    atBool = True
  if "." in email:
    periodBool = True
  
  if email != "" and atBool == False or email != "" and periodBool == False:
    error = "Please enter a vaild email address."
    return render_template("index.html", invalidEmail = error, email = email, username = username)

  #Error Messages
  blankError = "You cannot leave this field blank"
  lenError = "Your entry must be between 3-20 characters long"
  matchError = "Passwords did not match"
  spaceError = "No spaces are allowed in any field"

  #Renders for blank Error Messages
  if ulen == 0 and plen == 0 and vlen == 0:
    return render_template("index.html", uBlankError = blankError, pBlankError = blankError, vBlankError = blankError, username = username, email = email)
  elif plen == 0 and vlen == 0:
    return render_template("index.html", pBlankError = blankError, vBlankError = blankError, username = username, email = email)
  elif ulen == 0 and plen == 0:
    return render_template("index.html", pBlankError = blankError, uBlankError = blankError, username = username, email = email)
  elif ulen == 0 and vlen == 0:
    return render_template("index.html", uBlankError = blankError, vBlankError = blankError, username = username, email = email)
  elif ulen == 0:
    return render_template("index.html", uBlankError = blankError, username = username, email = email)
  elif plen == 0:
    return render_template("index.html", pBlankError = blankError, username = username, email = email)
  elif vlen == 0:
    return render_template("index.html", vBlankError = blankError, username = username, email = email)
  
  #Renders for length errors
  if elen != 0 and elen < 3 or elen > 30:
    return render_template("index.html", eLenError = lenError, username = username, email = email)
  elif ulen < 3 or ulen > 30:
    return render_template("index.html", uLenError = lenError, username = username, email = email)
  elif plen < 3 or plen > 30:
    return render_template("index.html", pLenError = lenError, username = username, email = email)
  elif vlen < 3 or vlen > 30:
    return render_template("index.html", vLenError = lenError, username = username, email = email)


  #Checking for spaces
  for a in email:
    if (a.isspace()) == True:
        ecount+=1
  for a in username:
    if (a.isspace()) == True:
        ucount+=1
  for a in password:
    if (a.isspace()) == True:
        pcount+=1
  for a in verify:
    if (a.isspace()) == True:
        vcount+=1
  
  #Renders for spaces
  if ecount > 0 or ucount > 0 or pcount > 0 or vcount > 0:
    if ecount > 0:
      return render_template("index.html", eSpaceError = spaceError, username = username, email = email)
    
    if ucount > 0:
      return render_template("index.html", uSpaceError = spaceError, username = username, email = email)
    
    if pcount > 0:
      return render_template("index.html", pSpaceError = spaceError, username = username, email = email)

    if vcount > 0: 
      return render_template("index.html", vSpaceError = spaceError, username = username, email = email)


  #Check for matching passwords
  if password != verify:
    return render_template("index.html", passwordVerification = matchError, username = username, email = email)

  

  return render_template("welcome.html", username = username)

app.run(host='0.0.0.0', port=8080)