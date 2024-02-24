#include "../Simc23_VS/simc.h"

int main()
{
  // initializing our main facility - a chocolate factory
  pfacility mainFascility;
  // allocating memory for it
  initlist(100);
  // creating a first chocolate batch right as our factory opens
  initcreate(1, 0);
  // creating our chocolate factory
  newfac(mainFascility, "Chocolate Factory");
  // run our factory for 100 hours
  while (systime < 100)
  {
    // start the chocolate production
    plan();
    switch (sysevent)
    {
    case 1:
      create(10);
      break;
    case 2:
      seize(mainFascility);
      break;
    case 3:
      delayt(20);
      break;
    case 4:
      outfac(mainFascility);
      break;
    case 5:
      destroy();
      break;
    }
  }
  // view the results of our production
  printall();
  return 0;
}