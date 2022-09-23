import requests
from scrapy.selector import Selector
# ===== get de l'url dans une variable response
response = requests.get('https://www.amazon.fr/livre-achat-occasion-litterature-roman/b/?ie=UTF8&node=301061&ref_=nav_cs_books')
# == date selector
data = Selector(text=response.text)

price = data.xpath('//div[@class="a-section octopus-pc-card octopus-best-seller-card"]/div[@class="a-section octopus-pc-card-content"]/ul').getall()                                          
# pieces = data.xpath('//div[@class="col_content"]/div[2]/div[@class="col_6"]/p[@class="icon-maison"]/text()').getall()
# calendar = data.xpath('//div[@class="col_content"]/div[2]/div[@class="col_6"]/p[@class="icon-calendrier"]/text()').getall()
# info = data.xpath('//div[@class="col_content"]/div/div[@class="col_content tag_program"]/span/text()').getall()

# with open('url.txt', 'w') as file:
#     for i in range(len(price)):
#         file.write('====== Recherche ' + str(i+1) + ' ========= \n' )
#         file.write('Prix : '+ price[i] + '\n')
#         file.write('Pièces : '+ pieces[i] + '\n')
#         file.write('Trimestres : '+ calendar[i] + '\n\n')
#         file.write('Info : '+ info[i] + '\n\n')
       
print('-----------Prix------------\n\n')
# affiche les valeurs de title (0-99)

print(price)
print(response)
# print('------ PIECES --------\n\n')
# for comp in pieces:
#     print(comp)





# use key : Values
# mesListes = {
#     "Titre":    title,
#     "-----------------"
#     "Company":    compagny,
#     "-----------------"
#     "Date":    date,
# }
# print(mesListes)




# =======Boucle for by range==========
# for i in range(len(title)):
#     print('===== recherches====== ', '\n')
#     print('Emplois :', title[i], '\n')
#     print('Dates :', date[i], '\n')
#     print('les Company :', compagny[i], '\n')
#     print('Localisation :', localisation[i])
# ======== fichier text ===========