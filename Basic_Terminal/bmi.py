def value(height, weight):    
  return weight / (height/100)**2
    
def type(bmi):
    if bmi>=24 and bmi<27:
        return "過重"
    elif bmi>=27 and bmi<30:
        return "輕度肥胖"
    elif bmi>=30 and bmi<35:
        return "中度肥胖"
    elif bmi>=35:
        return "重度肥胖"
    elif bmi>=18.5 and bmi<24:
        return "適中體重"
    elif bmi<18.5:
        return "過輕"