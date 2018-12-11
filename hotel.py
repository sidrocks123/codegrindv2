from flask import Flask, redirect, url_for, request, render_template
from datetime import date

from string import Template
import subprocess
import re
import base64
hi_page = Template("""
 <!DOCTYPE html>
 <html>
 <head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}

input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}
input[type=number], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}
input[type=date], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}


input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
</head>
<body>

<h3>Hotel-Domestic(IN)</h3>

<div class="container">
  <form>
    <label for="Date">Date</label>
    <input type="date" id="date" name="date" placeholder="Date in dd/mm/yy" value=${date}>
    
    <label for="country">Expense Location </label>
    <select id="country" name="country">
      <option value="australia">Australia</option>
      <option value="canada">Canada</option>
      <option value="usa">USA</option>
      <option value="usa">INDIA</option>
    </select>

    <label for="tamt">Total Amount</label>
    <input type="number" id="amount" name="amount" placeholder="Total Amount">
    <label for="noofdays">No of Days</label>
    <input type="number" id="no of days" name="noofdays" placeholder="Total no of days">
    <label for="damt">Daily Amount</label>
    <input type="number" id="dailyamt" name="dailyamt" placeholder="Daily amount....">
    
     <label for="ramt">Reimbursed Amount</label>
    <input type="number" id="ra" name="ra" placeholder="Total Reimbursed Amount">
    
    <label for="mname">Merchant Name</label>
    <input type="text" id="mname" name="mname" placeholder="Merchant Name">
    

    
    
    
    
    
     <label for="tedt">Check out date</label>
    <input type="date" id="tedt" name="tedt" placeholder="Date in dd/mm/yy">
    
    
    <label for="Description">Description</label>
    <textarea id="disc" name="desc" placeholder="Description about the expense....." style="height:100px"></textarea>
    

    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>
""")


ai_page=Template("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}

input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}
input[type=number], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}
input[type=date], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}


input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
</head>
<body>

<h3>Airfare-Domestic(IN)</h3>

<div class="container">
  <form >
    <label for="Date">Date</label>
    <input type="date" id="date" name="date" placeholder="Date in dd/mm/yy" value=${date}>
    
    <label for="country">Expense Location </label>
    <input type="text" id="eloc" name="eloc"  value=${eloc}>

    <label for="tamt">Total Amount</label>
    <input type="number" id="amount" name="amount" placeholder="Total Amount" value=${totalamt}>
    <label for="noofdays">No of Days</label>
    <input type="number" id="no of days" name="noofdays" placeholder="Total no of days" value=${totaldays}>
    <label for="damt">Daily Amount</label>
    <input type="number" id="dailyamt" name="dailyamt" placeholder="Daily amount...."   value=${dailyamt}>
    
     <label for="ramt">Reimbursed Amount</label>
    <input type="number" id="ra" name="ra" placeholder="Total Reimbursed Amount" value=${ramt}>
    
    <label for="mname">Merchant Name</label>
    <input type="text" id="mname" name="mname" placeholder="Merchant Name" value=${mname}>
    

    <label for="class">Class</label>
    <input type="text" id="class" name="class" placeholder="Class". value=${fclass}>
    
    <label for="tno">Ticket Number</label>
    <input type="number" id="tno" name="tno" placeholder="Ticket Number" value=${tno}>
    
    <label for="tstrt">Travel start date</label>
    <input type="date" id="tsdate" name="tsdate" placeholder="Date in  dd/mm/yy".  value=${sdt}>
     <label for="tedt">Travel end date</label>
    <input type="date" id="tedt" name="tedt" placeholder="Date in dd/mm/yy". value=${edt}>
    
    
    <label for="Description">Description</label>
    <textarea id="disc" name="desc" placeholder="Description about the expense....." style="height:100px" value=${desc}></textarea>
    

    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>











""")
year= 1995
month=10
day=24
totalamt=2000
totaldays=100
dailyamt=2000
ramt=2000
mname='Indigo'
fclass='economy'
tno=123456
sdatey=2019
sdatem=10
sdated=21
edatey=2019
edatem=10
edated=21
eloc="INDIA"
desc="I am travelling to pune from hyd on 21 jan"
app = Flask(__name__)
dt = date(year, month, day)
sdt=date(sdatey,sdatem,sdated)
edt=date(edatey,edatem,edated)

@app.route('/')
def homepage():
	return render_template("index.html")
@app.route('/flight/<name>')
def flight(name):
   # g = test.numpy.exp(2)
	return ai_page.substitute(date=dt,sdt=sdt,edt=edt,totalamt=totalamt,totaldays=totaldays,dailyamt=dailyamt,
		ramt=ramt,mname=mname,fclass=fclass,tno=tno,eloc=eloc,desc=desc)

@app.route('/Hotel/<name>')
def hotel(name):
   # g = test.numpy.exp(2)
	return hi_page.substitute(date=dt)
	


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
