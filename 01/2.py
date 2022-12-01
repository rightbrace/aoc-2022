print(sum(                                                                      # print the sum
    sorted([sum([int(fruit) for fruit in elf.strip().split("\n")])              # of the sum of each chunk, sorted
    for elf in open("input.txt").read()           # read the file
                                .split("\n\n")]   # split into elf-chunks
                                                                  )[-3:]))      # filtered to the top three elves