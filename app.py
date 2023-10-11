import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

pandas2ri.activate()

from apology import apology


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        hhsize = request.form.get("hhsize")
        age = request.form.get("age")
        race = request.form.get("race")
        edu = request.form.get("edu")
        pmh = request.form.getlist("pmh")

        if not hhsize:
            return apology("Select household size")
        if not race:
            return apology("Select race and ethnicity")
        if not edu:
            return apology("Select education level")
        
        age = float(age)
        hhsize = float(hhsize)

        if race=="white":
            white = float(1)
        else:
            white = float(0)
        if race=="black":
            black = float(1)
        else:
            black = float(0)
        if race=="hispanic":
            hispanic = float(1)
        else:
            hispanic = float(0)

        if edu=="1":
            edu = float(1)
        else:
            edu = float(0)

        if "ast_dx_pre_lottery_inp" in pmh:
            ast_dx_pre_lottery_inp = float(1)
        else: 
            ast_dx_pre_lottery_inp = float(0)
        if "dia_dx_pre_lottery_inp" in pmh:
            dia_dx_pre_lottery_inp = float(1)
        else: 
            dia_dx_pre_lottery_inp = float(0)
        if "hbp_dx_pre_lottery_inp" in pmh:
            hbp_dx_pre_lottery_inp = float(1)
        else: 
            hbp_dx_pre_lottery_inp = float(0)
        if "chl_dx_pre_lottery_inp" in pmh:
            chl_dx_pre_lottery_inp = float(1)
        else: 
            chl_dx_pre_lottery_inp = float(0)
        if "ami_dx_pre_lottery_inp" in pmh:
            ami_dx_pre_lottery_inp = float(1)
        else: 
            ami_dx_pre_lottery_inp = float(0)
        if "chf_dx_pre_lottery_inp" in pmh:
            chf_dx_pre_lottery_inp = float(1)
        else: 
            chf_dx_pre_lottery_inp = float(0)
        if "emp_dx_pre_lottery_inp" in pmh:
            emp_dx_pre_lottery_inp = float(1)
        else: 
            emp_dx_pre_lottery_inp = float(0)
        if "kid_dx_pre_lottery_inp" in pmh:
            kid_dx_pre_lottery_inp = float(1)
        else: 
            kid_dx_pre_lottery_inp = float(0)
        if "cancer_dx_pre_lottery_inp" in pmh:
            cancer_dx_pre_lottery_inp = float(1)
        else: 
            cancer_dx_pre_lottery_inp = float(0)
        if "dep_dx_pre_lottery_inp" in pmh:
            dep_dx_pre_lottery_inp = float(1)
        else: 
            dep_dx_pre_lottery_inp = float(0)
        
        #set other default values (median)
        gender = float(0)
        language_inp = float(1)
        num_visit_pre_cens_ed = float(0)
        any_psysub_pre_ed = float(0)
        any_depres_pre_ed = float(0)
        charg_tot_pre_ed = float(0)
        ed_charg_tot_pre_ed = float(0)

        #convert into pandas df
        dict = {"hhsize":[hhsize], "age":[age], "gender":[gender], "white":[white], "black":[black], "hispanic":[hispanic], "language_inp":[language_inp], "edu":[edu], "ast_dx_pre_lottery_inp":[ast_dx_pre_lottery_inp], "dia_dx_pre_lottery_inp":[dia_dx_pre_lottery_inp], "hbp_dx_pre_lottery_inp":[hbp_dx_pre_lottery_inp], "chl_dx_pre_lottery_inp":[chl_dx_pre_lottery_inp], "ami_dx_pre_lottery_inp":[ami_dx_pre_lottery_inp], "chf_dx_pre_lottery_inp":[chf_dx_pre_lottery_inp], "emp_dx_pre_lottery_inp":[emp_dx_pre_lottery_inp], "kid_dx_pre_lottery_inp":[kid_dx_pre_lottery_inp], "cancer_dx_pre_lottery_inp":[cancer_dx_pre_lottery_inp], "dep_dx_pre_lottery_inp":[dep_dx_pre_lottery_inp], "num_visit_pre_cens_ed":[num_visit_pre_cens_ed], "any_depres_pre_ed":[any_depres_pre_ed], "any_psysub_pre_ed":[any_psysub_pre_ed], "charg_tot_pre_ed":[charg_tot_pre_ed], "ed_charg_tot_pre_ed":[ed_charg_tot_pre_ed]}

        r = robjects.r
        r['source']("model.R")
        cfmodel_r = robjects.globalenv["causalForest"]

        d = robjects.FloatVector([hhsize, age, gender, white, black, hispanic, language_inp, edu, ast_dx_pre_lottery_inp, dia_dx_pre_lottery_inp, hbp_dx_pre_lottery_inp,chl_dx_pre_lottery_inp,ami_dx_pre_lottery_inp,chf_dx_pre_lottery_inp,emp_dx_pre_lottery_inp, kid_dx_pre_lottery_inp,cancer_dx_pre_lottery_inp,dep_dx_pre_lottery_inp,num_visit_pre_cens_ed,any_depres_pre_ed,any_psysub_pre_ed,charg_tot_pre_ed,ed_charg_tot_pre_ed])

        df_result_r = cfmodel_r(d)

        message = ("With health insurance coverage, the probability of depression will decrease by an estimated %s." % str(f"{float(df_result_r):.2%}"))

        flash(message)

        return render_template("index.html", dict=dict)
    
    else:
        return render_template("index.html")
    

@app.route("/publication")
def publication():
        return render_template("publication.html")
    

@app.route("/about")
def about():
        return render_template("about.html")
    