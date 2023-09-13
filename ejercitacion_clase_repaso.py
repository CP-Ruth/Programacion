#Lista de precios por mayor:
print("Lista de precios")
list_article= ["Pantalones","Camisas","Remeras","Faldas","Corbatas","Jogging"]
list_price=[5000,7500,3990,6000,2400,6750]
for i in range(6):
    print(f"(cod:{i+1}).{list_article[i]} ${list_price[i]}")
#Empezamos con el pedido
name= input("¿Quién realiza el pedido?\n")
new_list=[]
amount_price=[]
while name!="":
    code=int(input("¿Qué artículo deseas comprar? Ingresa su codigo.\n"))
    new_list.append(list_article[code-1])
    amount=int(input("Cantidad a comprar de este artículo:\n"))
    amount_price.append(list_price[code-1]*amount)
    
    going=input("¿Desea agregar otro artículo? si/no \n").lower()
    if going!="si":
        break
print(new_list)
print(amount_price)


