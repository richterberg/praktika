#include <windows.h>
#include <iostream.h>
#include <stdio.h>
 
void encrypt (char buf[])
{
   for( int i=0; buf[i] != '\0'; ++i)
    {
      ++buf[i];
    }
}
 
void decrypt(char buf[])
{
    for(int i = 0; buf[i] != '\0'; ++ buf)
     {
      --buf[i];
     }
}
 
int main (int argc, char *argv[])
{
      char string[] = "This string must be encrypted";
      encrypt(string);
      cout << "Enrypted string: " << string << endl;
 
      decrypt(string);
      cout << "Decrypted string:" << string << endl ;
      system("PAUSE");
}