#include "../simc/simc.h"
int main()
{
  long long B_N = 19,
            B_D = 38,
            W_N = 29,
            W_D = 57,
            T = 190;
  pfacility factory;
  initlist(T);
  starttrace();
  initcreate(1, 0);
  initcreate(6, 2);
  newfac(factory, "\"Chocolate Factory\"");
  while (systime < T)
  {
    plan();
    switch (sysevent)
    {
    case 1:
      create(B_N);
      break;
    case 2:
      seize(factory);
      break;
    case 3:
      delayt(B_D);
      break;
    case 4:
      outfac(factory);
      break;
    case 5:
      destroy();
      break;

    case 6:
      create(W_N);
      break;
    case 7:
      seize(factory);
      break;
    case 8:
      delayt(W_D);
      break;
    case 9:
      outfac(factory);
      break;
    case 10:
      destroy();
      break;
    }
  }
  printall();
  return 0;
}
// g++ two.cpp ../simc/simc.cpp -o ./executables/two