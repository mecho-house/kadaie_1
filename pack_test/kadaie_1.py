def kadaie_1(input, length):
    import gzip

    count = 0
    num = 0

    with gzip.open(input, "rt") as f:
        for line in f:
            if line.startswith(">"):
                try:
                    num += 1
                    len = line.split()[2]
                    if int(len[7:]) <= length:
                        count += 1
                except ValueError:
                    print(f"{num + 1}番目の配列でエラーが起きました。-> {line}")
                    continue

    print(100 * count / num, "%")
