#I, Gregory Carroll, student number 000101968,
#certify that all code submitted is my own work; that I have not
#copied it from any other source.  I also certify that I have not
#allowed my work to be copied by others.

def user_address():
    min_length = 6
    
    validAddress = False
    while not validAddress:
        address = str(input("enter your street adress: "))
        addr_split = address.split(" ")
        validAddress = True
        if not address.isspace() and not addr_split[0].isdigit():
            validAddress = False
            print("address needs atleast 1 digit and a space")
        elif len(address) <= min_length:
            validAddress = False
            print("address needs to be atleast 6 charactors long")
        if validAddress:
            return address
 

# city and province, must be an abbreviation in the below list and seperated with a ,
def user_area():
    areas = [ "AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT" ]
    
    validArea = False
    while not validArea:
        city_province = str(input("enter your province and city: "))
        validArea = True
        area = city_province.split(",")[0]
        if area.upper() not in areas:
            validArea = False
            print("invalid province abbreviation")
        if len(area) == len(city_province):
            validArea = False
            print("you need to have a comma after the abbreviation")
        if validArea:
            return area, city_province.split(",")[1]
            

#Postal code must begin with a letter in the list below. It should also be in the format
#   L#L #L#  ( LETTER NUMBER LETTER  NUMBER LETTER NUMBER) (ex. A5K 1Y9)
def postal_code():
    postal = False
    while not postal:
        postal = str(input("enter your postal code"))
        if postal[0].isalpha() and postal[1].isdecimal() and postal[2].isalpha() and postal[3].isspace() and postal[4].isdecimal() and postal[5].isalpha and postal[6].isdecimal():
            return str(postal)
            postal = True
        else:
            postal = False 
            print("not correct format *Requires L#L #L#*")
        
        
def shipping_cost(area):
    cost_shipping = {
        "AB": 12,
        "BC": 12,
        "MB": 12,
        "SK": 12,
        "NB": 15,
        "NL": 15,
        "NS": 15,
        "PE": 15,
        "NT": 20,
        "NU": 20,
        "YK": 20,
        "ON": 8,
        "QC": 8,
        }
    
    return cost_shipping[area.upper()]

        
address = user_address()
area, city = user_area()
postal = postal_code() 
print("cost of shipping to", address, area, postal, " is $" + str(shipping_cost(area)))
