#Lista de precios por mayor:
print("Lista de precios")
list_article= ["Pantalones","Camisas","Remeras","Faldas","Corbatas","Jogging"]
list_price=[5000,7500,3990,6000,2400,6750]
for i in range(6):
    print(f"(cod:{i+1}).{list_article[i]} ${list_price[i]}")
#Empezamos con el pedido
name= input("¿Quién realiza el pedido?\n")
print(f"{name}, empecemos con tu pedido!")
new_list=[]
arti_amount=[]
amount_price=[]
while name!="":
    code=int(input("¿Qué artículo deseas comprar? (Ingresa su codigo): "))
    while code<1 or code>6:
        print("Número no es valido")
        code=int(input("¿Qué artículo deseas comprar? (Ingresa su codigo): "))
        if code>0 and code<7:
            print(code)
            break
    new_list.append(list_article[code-1])
    amount=int(input("Cantidad a comprar de este artículo: "))
    arti_amount.append(amount)
    amount_price.append(list_price[code-1]*amount)
    
    going=input("Si ya no deseas agregar otro articulo ingresa 'N' \n").lower()
    if going=="no":
        break 
#Detalle del pedido

print(new_list)
print(arti_amount)
print(amount_price)


