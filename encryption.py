#This code will encrypt the data
import sys;
def encrypt(data=None):
  if data is not None:
    print(">>> Data acknowledged and sent");
    return data.encode('utf-8');                  #assuming the data is of the type str;
  else:
    return None;

if __name__ == '__main__':
  encrypt(sys.argv[1]);
