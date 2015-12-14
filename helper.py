from Crypto.PublicKey import RSA
import binascii
import sys

helper_file = None
helper_key = None
helper_passphrase = None

if(len(sys.argv) > 1):
    helper_file = sys.argv[1];
if(len(sys.argv) > 2):
    helper_key = sys.argv[2];
if(len(sys.argv) > 3):
    helper_key = sys.argv[3];

if helper_file is None:
    print "Secret not provided"
    sys.exit(1);

if helper_key is None:
    print "Private key not provided"
    sys.exit(1);

# import key
with open(helper_key, "r") as f:
    helper_key = ""
    for line in f:
        helper_key += line
helper_key = RSA.importKey(helper_key, helper_passphrase)

with open(helper_file, "r") as f:
    enc_msg = f.read()

secret_msg = helper_key.decrypt(binascii.unhexlify(enc_msg));

print secret_msg
