from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import pandas as pd
import numpy as np
app=Flask(__name__,template_folder='template')
model=pickle.load(open('Carprice_model.pkl', 'rb'))
@app.route('/',methods=['get'])
def Home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
     
    if request.method == 'POST':
        symbol=0
        symboling=request.form['symboling']
        if(symboling=='zero'):
              symbol=0
        elif(symboling=='one'):
              symbol=1
        elif(symboling=='two'):
              symbol=2
        elif(symboling=='three'):
              symbol=3
        elif(symboling=='none'):
              symbol=-1
        else:
              symbol=-2
        company=0
        companyname=request.form['companyname']
        if(companyname=='alfa'):
            company=0
        elif(companyname=='audi'):
            company=1
        elif(companyname=='bmw'):
            company=2
        elif(companyname=='chevrolet'):
            company=3
        elif(companyname=='dodge'):
            company=4
        elif(companyname=='honda'):
            company=5
        elif(companyname=='isuzu'):
            company=6
        elif(companyname=='jaguar'):
            company=7
        elif(companyname=='mazda'):
            company=8
        elif(companyname=='buick'):
            company=9
        elif(companyname=='mercury'):
            company=10
        elif(companyname=='mitsubishi'):
            company=11
        elif(companyname=='nissan'):
            company=12
        elif(companyname=='peugeot'):
            company=13
        elif(companyname=='plymouth'):
            company=14
        elif(companyname=='porsche'):
            company=15
        elif(companyname=='renault'):
            company=16
        elif(companyname=='saab'):
            company=17
        elif(companyname=='subaru'):
            company=18
        elif(companyname=='toyota'):
            company=19
        elif(companyname=='volkswagen'):
            company=20
        else:
            company=21
        fuel_type=0
        fueltype=request.form['fueltype']
        if(fueltype=='gas'):
            fuel_type=1
        else:
            fuel_type=0
        aspiration_type=0
        aspiration=request.form['aspiration']
        if(aspiration=='std'):
                aspiration_type=1
        else:
                aspiration_type=0
        dnumber=0
        doornumber=request.form['doornumber']
        if(doornumber=='four'):
                dnumber=0
        else:
                dnumber=1
        body_type=0
        carbody=request.form['carbody']
        if(carbody=='sedan'):
                body_type=3
        elif(carbody=='hardtop'):
                body_type=0
        elif(carbody=='hatchback'):
            body_type=2
        elif(carbody=='wagon'):
            body_type=4
        else:
            body_type=1
        drivewheel_type=0
        drivewheel=request.form['drivewheel']
        if(drivewheel=='rwd'):
            drivewheel_type=0
        elif(drivewheel=='4wd'):
            drivewheel_type=1
        else:
             drivewheel_type=2
        engloc=0    
        enginelocation=request.form['enginelocation']
        if(enginelocation=='front'):
                engloc=0
        else:
                engloc=1              
        wheelbase=float(request.form['wheelbase'])
        curbweight=float(request.form['curbweight'])
        engine_type=0
        enginetype =request.form['enginetype']
        if(enginetype=='dohc'):
            engine_type=0
        elif(enginetype=='ohcv'):
            engine_type=1
        elif(enginetype=='ohc'):
            engine_type=2
        elif(enginetype=='l'):
            engine_type=3
        elif(enginetype=='rotor'):
            engine_type=4
        elif(enginetype=='ohcr'):
            engine_type=5
        else:
            engine_type=6
            
            
            
        cylinno=0
        cylindernumber=request.form['hello']
        if(cylindernumber=='four'):
            cylinno=0
        elif(cylindernumber=='six'):
            cylinno=1
        elif(cylindernumber=='five'):
            cylinno=2
        elif(cylindernumber=='three'):
            cylinno=3
        elif(cylindernumber=='twelve'):
            cylinno=4
        elif(cylindernumber=='two'):
            cylinno=5
        else:
            cylinno=6
        fuel_syestem=0    
        fuelsystem = request.form['fuelsystem']
        if(fuelsystem=='mpfi'):
            fuel_syestem=0
        elif(fuelsystem=='2bbl'):
            fuel_syestem=1
        elif(fuelsystem=='mfi'):
            fuel_syestem=2
        elif(fuelsystem=='1bbl'):
            fuel_syestem=3
        elif(fuelsystem=='spfi'):
            fuel_syestem=4
        elif(fuelsystem=='4bbl'):
            fuel_syestem=5
        elif(fuelsystem=='idi'):
            fuel_syestem=6
        else:
            fuel_syestem=7
        enginesize =float(request.form['enginesize'])
        boreratio =float(request.form['boreratio'])
        stroke =float(request.form['stroke'])
        horsepower =float(request.form['horsepower'])
        peakrpm =float(request.form['peakrpm'])
        height =float(request.form['height'])
        width =float(request.form['width'])
        length =float(request.form['length'])
        carvolume=0
        carvolume=height*width*length
        carvolume=np.log(carvolume)
        wheelbase= np.log(wheelbase)
        enginesize=np.log(enginesize)
        stroke=np.log(stroke)
        horsepower=np.log(horsepower)
        peakrpm=np.log(peakrpm)
        data =pd.DataFrame(data=[[symbol,company,fuel_type,aspiration_type,dnumber,body_type,drivewheel_type,engloc,wheelbase,curbweight,engine_type,cylinno,enginesize,fuel_syestem,boreratio,stroke,horsepower,peakrpm,carvolume]],columns=['symboling','CompanyName','fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','wheelbase','curbweight','enginetype','cylindernumber','enginesize','fuelsystem','boreratio','stroke','horsepower','peakrpm','carvolume'])
        prediction=model.predict(data)
        output=(prediction[0])
        return render_template('index.html',prediction_text="The price of car is {}".format(output))
    else:
       return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
