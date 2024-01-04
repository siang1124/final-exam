class fried_chicken : #定義類別

    def __init__(self,spiciness,salinity,taste,thickness,seasoning):
        self.spiciness = spiciness  #辣度
        self.salinity = salinity    #鹹度
        self.taste = taste          #口味
        self.thickness = thickness  #外皮厚度
        self.seasoning = seasoning  #調味

    def get_spiciness(self):                                                        #使用get
        return self.spiciness
    
    def get_salinity(self):                                                         #使用get
        return self.salinity
    
    def get_taste(self):                                                            #使用get
        return self.taste
    
    def get_thickness(self):                                                        #使用get
        return self.thickness
    
    def get_seasoning(self):                                                        #使用get
        return self.seasoning
    
#建立4個物件
P1 = fried_chicken("微辣","微鹹","台式","軟皮","起司")
P2 = fried_chicken("中辣","不鹹","美式","薄皮","胡椒")
P3 = fried_chicken("不辣","重鹹","義式","厚皮","梅粉")
P4 = fried_chicken("大辣","中鹹","韓式","脆皮","辣粉")

print(f"顧客1")
print(f"辣度:{P1.get_spiciness()}")
print(f"鹹度:{P1.get_salinity()}")
print(f"口味:{P1.get_taste()}")
print(f"外皮厚度:{P1.get_thickness()}")
print(f"調味:{P1.get_seasoning()}")

print(f"顧客2")
print(f"辣度:{P2.get_spiciness()}")
print(f"鹹度:{P2.get_salinity()}")
print(f"口味:{P2.get_taste()}")
print(f"外皮厚度:{P2.get_thickness()}")
print(f"調味:{P2.get_seasoning()}")

print(f"顧客3")
print(f"辣度:{P3.get_spiciness()}")
print(f"鹹度:{P3.get_salinity()}")
print(f"口味:{P3.get_taste()}")
print(f"外皮厚度:{P3.get_thickness()}")
print(f"調味:{P3.get_seasoning()}")

print(f"顧客4")
print(f"辣度:{P4.get_spiciness()}")
print(f"鹹度:{P4.get_salinity()}")
print(f"口味:{P4.get_taste()}")
print(f"外皮厚度:{P4.get_thickness()}")
print(f"調味:{P4.get_seasoning()}")
