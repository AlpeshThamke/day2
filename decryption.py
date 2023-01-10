#This code will decrypt the data
import sys;
def decrypt(data=None):
  if data is not None:
    print("Data Acknowledged");
    return data.decode('utf-8');
  else:
    return None;

if __name__ == '__main__':
  decrypt(sys.argv[1]);
