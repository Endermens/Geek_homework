def main():
    from sys import argv


    with open("price.csv", "a+", encoding= 'utf-8') as prise:
        with open("price.csv", "r", encoding= 'utf-8') as prise_r:
            if len(argv) > 1 and [i for i in argv[1:] if i.replace(".", "").isdigit()]:
                if len(argv) >= 3:
                    start, finish = map(int, argv[1:])
                    print(*(v for i, v in enumerate(prise_r) if start - 1 <= i < finish), sep = "")

                if "," in argv[1] or "." in argv[1]:
                    if round(float(argv[1].replace(",", ".")), 3) < 9999.999:
                        print(f'{round(float(argv[1].replace(",", ".")), 3):>010}', file = prise)
                    else:
                        print("the number exceeds the allowed value - max'9999.999'")

                else:
                    print(*(v for i, v in enumerate(prise_r) if i >= int(argv[1]) -1))
            else:
                print(prise_r.read())
main()
