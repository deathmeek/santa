from Crypto.Random import random
from Crypto.PublicKey import RSA
import binascii

# import helper's list
helpers_list = []
with open("santa.pub", "r") as f:
    for line in f:
        helper = line.split("\t")
        helper_name = helper[0]
        helper_key = RSA.importKey(helper[1])
        helpers_list.append((helper_name, helper_key))

# create santa's suffled list
santas_list = [helper[0] for helper in helpers_list]
while True:
    random.shuffle(santas_list)
    santas_choice = dict(zip(santas_list, helpers_list))
    # skip x gives to x
    if(reduce(lambda x, y: x or (y[0] == y[1][0]), santas_choice.items(), False)):
        continue;
    # skip x give to y and y gives to x
    if(reduce(lambda x, y: x or (y[0] == santas_choice[y[1][0]][0]), santas_choice.items(), False)):
        continue;
    break;

max_name_len = reduce(lambda x, y: y if x < y else x, [len(helper[0]) for helper in helpers_list], 0);
for choice in santas_choice.items():
    helper_name = choice[1][0]
    helper_key = choice[1][1]
    secret_name = choice[0]
    secret_msg = "Mosul a decis sa iei un cadou pentru %*s. Urmeaza un numar aleator secret %32x." \
            % (max_name_len, secret_name, random.getrandbits(128))
    with open(helper_name.replace(" ", "_").lower() + ".txt", "w") as f:
        enc_msg = binascii.hexlify(helper_key.encrypt(secret_msg, 0)[0]);
        f.write(enc_msg);
