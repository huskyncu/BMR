import bmi
def value(height, weight, gender,age):   
  return 1.2*bmi.value(height,weight)+ 0.23 * age - 5.4 - 10.8*(2-gender)
#函式回傳以bmr判定的體態
def type(b,gender):            
  if gender == 1:
      if b >=2 and b < 6 :
       return "基礎脂肪"
      elif b >=6 and b < 14:
        return "運動員"
      elif b >=14 and b < 18:
        return "健康"
      elif b >=18 and b < 25:
        return "正常"
      elif b >=25:
       return "肥胖"
  elif gender == 2:
    if b >=10 and b < 14 :
      return "基礎脂肪"
    elif b >=14 and b < 21:
      return "運動員"
    elif b >=21 and b < 25:
      return "健康"
    elif b >=25 and b < 32:
      return "正常"
    elif b >=32:
      return "肥胖"