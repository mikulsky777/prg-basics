facebook = False
twitter = True
instagram = True

if sum([facebook,twitter,instagram]) >= 2:
    print('You are a good influencer!')
else:
    print('You are not a good influencer')