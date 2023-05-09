import bmi
import bmr
def cal(gender,height,weight,age):
    print("bmi:%5.2f" % bmi.value(height,weight))
    print("bmi判定體位:"+bmi.type(bmi.value(height,weight)))
    print("以bmi計算，您的理想體重應為%5.2f公斤至%5.2f公斤之間"%(18.5*(int(height)/100)**2,24*(int(height)/100)**2))
    print("體脂率：%5.2f" % bmr.value(height,weight,gender,age))
    print("體脂判定體型：%s" % bmr.type(bmr.value(height,weight,gender,age),gender))