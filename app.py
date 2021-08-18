# -*- coding: utf-8 -*-

from flask import Flask, request, render_template


# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def whitematter():
    return render_template('whitematter.html', data={})

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def whitematter_predict():
    from wm_util import  positive, negative, all_features, labels, prevalence, whitemattet_calculator

    user_input = request.form.getlist("wm")
    #user_input = ['ependymal', 'delta', 'moyamoya', 'vfspace', 'atrophy', 'vermial_atrophy', 'symmetrical_bg', 'discrete']
    
    result1 =  whitemattet_calculator(user_input, positive, negative, all_features, labels, prevalence)
    first = {'Type': 'Score'} 
    
    # Check the output values and retrive the result with html tag based on the value
    # Check the output values and retrive the result with html tag based on the value
    if len(user_input) != 0:
        return render_template('whitematter.html', data =  {**first, **result1})

    else:
        return render_template('whitematter.html', 
                               data = {**first, **result1})

                            
if __name__ == '__main__':
#Run the application
    app.run()
    
