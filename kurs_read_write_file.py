with open("dataset_24465_4.txt", 'r') as i, open("out", 'w') as j:
    j.writelines(reversed(list(i)))


