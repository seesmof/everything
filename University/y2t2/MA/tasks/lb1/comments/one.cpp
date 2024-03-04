#include "../simc/simc.h"

int main()
{
  long long N = 19,
            D = 38,
            T = 190;

  /*
  N - inteval of creating
  D - delay between creating
  T - time of simulation
  */

  // creating our chocolate factory
  pfacility factory;

  // allocating free machines on our factory for future chocolate production
  initlist(T);

  // appoint a safety officer for our factory - he will trace our production
  starttrace();

  // getting all of our raw material for chocolate and producing the first batch - right as our factory opens
  initcreate(1, 0);
  /*
  for initcreate function:
  first - what machinery will our material go to when being processed,
  second - delay between opening of our factory and the material going to our machinery
  */

  // initializing or opening our chocolate factory, hooray!
  newfac(factory, "\"Chocolate Factory\"");

  while (systime < T)
  {
    // starting our production process
    plan();

    // passing our raw material to our machinery
    switch (sysevent)
    {
    // creating our new chocolate batch - assigning a new task for our factory workers
    case 1:
      create(N);
      break;
    // workers get the raw material and start processing it
    case 2:
      seize(factory);
      break;
    // the work takes time, so we will wait for it to get produced for D relative time points
    case 3:
      delayt(D);
      break;
    // our raw material is processed into chocolate and can now leave machinery into our warehouse
    case 4:
      outfac(factory);
      break;
    // we no longer have to keep track of it, this is not our responsibility anymore, so we destroy our memory of it for good
    case 5:
      destroy();
      break;
    }
  }

  // approach our safety officer for a report of our production day
  printall();

  return 0;
}