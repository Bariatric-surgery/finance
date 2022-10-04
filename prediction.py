import joblib

def predict1(data):
    reg = joblib.load('reg_model.sav')
    return reg.predict(data)

def predict2(data):
    reg = joblib.load('reg2_model.sav')
    return reg.predict(data)


