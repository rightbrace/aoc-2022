print(max(                                                          # print the largest sum
        [sum([int(fruit) for fruit in elf.strip().split("\n")])     # in each elf-chunk, split into fruits and cast to an int, summing them
        for elf in open("input.txt").read()                         # read the file
                                    .split("\n\n")]))               # break into each elf-chunk