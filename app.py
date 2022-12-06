from flask import Flask, render_template, request, redirect
from sentiment_analysis import interpret_polarity 
from hurst_exponent1 import interpret_hurst



app=Flask(__name__,template_folder='template')
    
# deleted STUDENTS = {}
# Assume one user can only enter one company and its ticker name
# COMPANY = {} # i.e. {Tesla, TSL}
company_name = ""
company_ticker = ""
# deleted COURSES = ['Python', 'Web', 'Blockchain', 'UI']

@app.route("/", methods=["GET", "POST"])
def Search_Company():
    """
    User enters company's name and ticker, submit the form, this function will
     call the analysis function(s) in sentiment_analysis, then display the 
     sentiment of reddit text (float), and call function(s) in hurst_exponent1, and display the hurst exponent for vairous lag values (float). 
    """
    if request.method == "POST":
        company_name = request.form["name"]
        company_ticker = request.form['ticker']
        sentiment_result = interpret_polarity(company_name)
        hurst_result = interpret_hurst(company_ticker)
        return render_template('company.html', company=company_name, sentiment=sentiment_result, hurst=hurst_result)
    else:
        return render_template("form.html")

# @app.route("/ticker", methods=["GET", "POST"])
# def Search_Ticker():
#     if request.method == "POST":
#         ticker_name = request.form["ticker_name"]
#         ticker = request.form.get("ticker") 
#         COMPANY[ticker_name] = ticker
#         return redirect("/output")

#     else:
#         return render_template("tickerform.html") 


#@app.route("/company", methods=["GET", "POST"])
#def company_info():
    #company = request.args.get()
    #return render_template("company.html", company=COMPANY)


#@app.route('/output', methods=["GET", "POST"])
#def get_sentiment():
    #if request.method == "POST":
        #company = request.form["Company Name"]
        #sentiment = interpret_polarity(company)
        #return render_template("company.html", company = company, sentiment = sentiment)

    #return render_template("form.html")

if __name__=="__main__":
    app.run(port=5001, debug=True)