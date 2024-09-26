buah = ["kelapa", "semangki", "kedungdung"]
print(buah[2])  
# untuk memilih aray ke berapa yang mau di print


coordinates = (3,4,5)
print(coordinates[0])
print(coordinates[2])


# access dictionary value
person = {
    "nama: ": "Fath",
    "umur: ": "17",
    "asal: ": "Berlin"
}
print(person["nama: "])
print(person["umur: "])
print(person["asal: "])

# day 10
# menambahkan, menghapus & modifikasi list

rank = ["epic", "legend", "mythic", "honor", "glory", "immortal"]
rank.append("master")
rank.remove("epic")
rank[3] = "epic neraka"
print(rank[4])

# dictionary manipulation:
person = {"nama": "Fathh", "umur" : "17", "asal": "Berlin"}
person["negara asal"] = "Jermany"
del person["asal"]
person["umur"] = "22"
print(person)