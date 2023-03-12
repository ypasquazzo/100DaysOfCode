from addressScraper import AddressScraper
from sheetCreator import SheetCreator

NB_LISTINGS = 50

listing = AddressScraper(NB_LISTINGS)
listing.get_listings()

sheet = SheetCreator(listing.listing)
sheet.add_listings_to_sheet()
