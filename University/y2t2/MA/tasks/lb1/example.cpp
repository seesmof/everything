#include "../simc/simc.h"

int main()
{
  pfacility f;
  initlist(100);
  starttrace();
  initcreate(1, 0);
  newfac(f, "Device");
  while (systime < 100)
  {
    plan();
    switch (sysevent)
    {
    case 1:
      create(10);
      break;
    case 2:
      seize(f);
      break;
    case 3:
      delayt(20);
      break;
    case 4:
      outfac(f);
      break;
    case 5:
      destroy();
      break;
    }
  }
  printall();
  return 0;
}