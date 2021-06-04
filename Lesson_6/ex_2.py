import collections


with open("ip_it.txt", "r", encoding = "utf-8") as f:
    spamers_ip = collections.Counter()
    for i in f:
        i = i.split()[0]
        spamers_ip[i] += 1
    ip, counts = spamers_ip.most_common()[0][0], spamers_ip.most_common()[0][1]
    print("Ip: ", ip, " counts: ", counts)
