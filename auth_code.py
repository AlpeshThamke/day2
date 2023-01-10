#This module checks for the correct Public Key
private_key = "private_key";


def auth(public_key):
  if private_key==public_key:
    return True;
  else:
    return False;

if __name__ == "__main__":
  auth();
