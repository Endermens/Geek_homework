def add_sale(coin = 0):
    """ вносит цену продукта
        в файл для хранения цен"""
    while coin > 9999.999:
        print("You have exceeded the allowed amount")
        coin = float(input("Enter another amount: "))

    coins = open("coin_list.txt", "a+", encoding = 'utf-8')
    coin = round(coin, 3)
    price = str(coin)
    n = "\n"
    coins.write(price + "\n")
    print("add ", coin, " coins")
    coins.readlines()
    with open('coin_list.txt') as fp:
        lines = fp.readlines()
        print(lines)

    coins.close()
def show_sales():
    sale = int(input("enter a boring page with a valuable: "))
    with open('coin_list.txt') as fp:
        lines = fp.readlines()
    print(zip(lines[sale]))

def main():
    print("write 'help' to find out the available commands")
    with open('coin_list.txt') as f:
        line_count = 0
        for line in f:
            line_count += 1
        print("prices available in the list: ", line_count)
    a = " "
    while a != "exit":
        a = input()
        if a == "help":
            print("""
            print 'price' - add_sale('float')
            print 'show' - show_sales('int')
            print 'exit' - close programm """)
        elif a == "price":
            price = float(input("Enter price - max(9999.999): "))
            add_sale(price)
        elif a == "show":
            show_sales()

        elif a == "exit":
            break
main()
