from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH


app = Flask(__name__)


def exam():
        
    c = 0

    

    name = input("Please enter your name to start the test.", type ="text")


    q1 = radio("Q1.Which of the following is the Base language of web?",['javaScript','ASP','PHP','HTML'])
    if q1 =='HTML':
        c+=1

    q2 = radio("Q2. Which is not a programming language ?",['Python','HTML','Scala','Java'])
    if q2 =='HTML':
        c+=1

    q3 = radio("Q3. Secondary memory is also called _____.",['Virtual memory','RAM','ROM','Hard drives'])
    if q3 =='ROM':
        c+=1

    q4 = radio("Q4. Functions that is used to get the length of string in Python",['count()','length()','dis()','len()'])
    if q4 == 'len()':
        c+=1

    q5 = radio("Q5. Which is not a web framework?",['Django','React','Numpy','Angular'])
    if q5 == 'Numpy':
        c+=1

    if c>3:
        style(put_text("Congratulations!, " + name + ", your score is "+ str(c)),'color:green')
        style(put_text("Result : PASSED"),'color:green')
        put_text("Thank You for your participation.")

    else:
        style(put_text("Oops!, " +name + ", your score is "+ str(c)),'color:red')
        style(put_text("Result : FAILED"), 'color:red')
        put_text("Thank You for your participation.")



app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
