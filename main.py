#This is for initiating conversation
import sys;
from auth_code import auth;
from encryption import *;
from decryption import *;

def start_conversation():
  trials_left=3;                                                    #3 trials for user
  while trials_left:
    trials_left-=1;
    state = 0;
    print("Public Key please (in this case key is 'private_key')");
    public_key = input();
    if auth(public_key):                                            #auth method is from auth_code module
      print("Conversation Started");
      turn = 1;
      while True:
        if turn%2==1:
          print("Client's Terminal\nTo stop enter 'ssh_stop'");
          data = input();
          if data == 'ssh_stop':
            print("Session Terminated");
            state = 1;
            break;
          else:
            data = encrypt(data);
            #send to client;
        else:
          print("Server's Terminal\nEnter Data in Bytes format not string>>>");
          data = input();
          data = encrypt(data);  
          print(data);
        turn+=1;
      if state==1:
            break;
    elif state==0:
      print("Public Key is not matching");
      print(trials_left,"attempts remaining");
    else:
      break;

def main():
  start_conversation();

if __name__=="__main__":
    main();
