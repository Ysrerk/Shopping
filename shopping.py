# Given below sales data:
#
# City	Amount	Product	Brand
# New York	158    	Shoe Pair	New Balance
# New York	53    	T-Shitrt	Adidas
# New York	95    	Short	Adidas
# New York	233    	Short	Nike
# Atlanta	4543    	T-Shitrt	Nike
# Tucson	4321    	Shoe Pair	New Balance
# Houston	155    	T-Shitrt	Adidas
# Tucson	59    	Short	Adidas
# Miami	345    	Short	Nike
#
# Write function for each feature below:
#
# 1 - Print only cities in descending sell amount order
#
# 2 - Print product amount that are sold for each city (order not important)
#
# 3 - Print total product amount that are sold
#
# 4 - Print total income if each product is $20
#
# 5 -Print the total number of Adidas produtcs sold.

s1={"City":"New York","Amount":158,"Product":"Shoe Pair","Brand":"New Balance"}
s2={"City":"New York","Amount":53,"Product":"T-Shitrt","Brand":"Adidas"}
s3={"City":"New York","Amount":95,"Product":"Short","Brand":"Adidas"}
s4={"City":"New York","Amount":233,"Product":"Short","Brand":"Nike"}
s5={"City":"Atlanta","Amount":4543,"Product":"T-Shitrt","Brand":"Nike"}
s6={"City":"Tucson","Amount":4321,"Product":"Shoe Pair","Brand":"New Balance"}
s7={"City":"Houston","Amount":155,"Product":"T-Shitrt","Brand":"Adidas"}
s8={"City":"Tucson","Amount":59,"Product":"Short","Brand":"Adidas"}
s9={"City":"Miami","Amount":345,"Product":"Short","Brand":"Nike"}

saless = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
def descamount():
    totalnwy = 0
    totalatl = 0
    totalTucson = 0
    totalMiami = 0

    sehiramount = {"New York": totalnwy, "Atlanta": totalatl}

    saless = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    for i in saless:
        if i["City"] == "New York":
            totalnwy += i["Amount"]
            sehiramount["New York"] = totalnwy

        elif i["City"] == "Atlanta":
            totalatl += i["Amount"]
            sehiramount["Atlanta"] = totalatl
        elif i["City"] == "Tucson":
            totalTucson += i["Amount"]
            sehiramount["Tucson"] = totalTucson
        elif i["City"] == "Miami":
            totalMiami += i["Amount"]
            sehiramount["Miami"] = totalMiami

    listofTuples = sorted(sehiramount.items(), key=lambda x: x[1],reverse=True)
    # Iterate over the sorted sequence
    for elem in listofTuples:
        print(elem[0], " ::", elem[1])
    print("##############################")
def totalmount():
    totalamount = 0
    for i in saless:
        totalamount += (i["Amount"])
    print("Total sales amount "+str(totalamount))
    print("##############################")
    return totalamount

def totalproductincome():
    totaltshirt = 0
    totalshort = 0
    totalshoepair = 0

    productamount = {"Short": totalshort, "T-Shitrt": totaltshirt, "Shoe Pair": totalshoepair}

    saless = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    for i in saless:
        if i["Product"] == "Short":
            totalshort += i["Amount"]
            productamount["Short"] = totalshort

        elif i["Product"] == "T-Shitrt":
            totaltshirt += i["Amount"]
            productamount["T-Shitrt"] = totaltshirt
        elif i["Product"] == "Shoe Pair":
            totalshoepair += i["Amount"]
            productamount["Shoe Pair"] = totalshoepair

    for key, value in productamount.items():
        print(key, value * 20)
    print("##############################")


def adidasamount():
    adidasamount = 0
    for i in saless:
        if i["Brand"] == "Adidas":
            adidasamount += i["Amount"]
    print("Total Adidas product amount "+str(adidasamount))






descamount()
#
totalmount()

totalproductincome()

adidasamount()






