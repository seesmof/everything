#include "../simc/simc.h"
int main()
{
  long long N = 19,
            D = 38,
            T = 190;
  pfacility factory;
  initlist(T);
  starttrace();
  initcreate(1, 0);
  newfac(factory, "\"Chocolate Factory\"");
  while (systime < T)
  {
    plan();
    switch (sysevent)
    {
    case 1:
      create(N);
      break;
    case 2:
      seize(factory);
      break;
    case 3:
      delayt(D);
      break;
    case 4:
      outfac(factory);
      break;
    case 5:
      destroy();
      break;
    }
  }
  printall();
  return 0;
}
// g++ one.cpp ../simc/simc.cpp -o ./executables/one