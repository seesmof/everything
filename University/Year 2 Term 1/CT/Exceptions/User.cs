using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace code
{
  public class User
  {
    public string Name { get; set; }
    public string Email { get; set; }
    public string Password { get; set; }
    public List<Listing> BoughtListings { get; set; }
    public List<Listing> AddedListings { get; set; }

    public User()
    {
      BoughtListings = new List<Listing>();
      AddedListings = new List<Listing>();
    }

    public void BuyListing(Listing listing)
    {
      // Add the listing to the user's bought listings
      BoughtListings.Add(listing);
      // Remove the listing from the market
      Forms.FormMarket.RemoveListing(listing);
    }

    public void AddListing(Listing listing)
    {
      // Add the listing to the user's added listings
      AddedListings.Add(listing);
      // Add the listing to the market
      Forms.FormMarket.AddListing(listing)
    }
  }
}
