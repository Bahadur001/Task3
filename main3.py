class Car():
    sinif = "cars"
    def __init__(self, marka, model, qiymet):
        self.marka = marka    
        self.model = model
        self.qiymet = qiymet

    def suret(self):
        return f"{self.model} maksimum 450 suretle gede bilir"   
    def usdu_acilan(self, usdu_acilan  = False): 
        if usdu_acilan == False:
          return f"{self.model} usdu acila bilmir"
        else:
          return f"{self.model} usdu acila bilir"



mercedes = Car("Mercedes", "Maybach", "100000$")
print(f"dunyanin en mehsur masinlarindan biri {mercedes.marka} en cox sevilen modeli {mercedes.model}, qiymeti {mercedes.qiymet}")
print(mercedes.suret())
print(mercedes.usdu_acilan())
