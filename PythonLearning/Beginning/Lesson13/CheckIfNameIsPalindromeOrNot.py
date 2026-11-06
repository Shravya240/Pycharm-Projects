list = ['Suhani', 'Alinaa', 'Shravya', 'Arav', 'madam', 'Yedhant', 'Monit']
for name in list:
    reverse_name = name[:: -1]
    if name == reverse_name:
        print(name, "Is Palindrome Word")
else:
    print("Name List is over")