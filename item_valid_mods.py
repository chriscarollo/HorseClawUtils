
import requests
from requests.exceptions import HTTPError


test_item_1 = 'Item Class: Rings \
Rarity: Rare \
Spirit Coil \
Breach Ring \
-------- \
Requirements: \
Level: 48 \
-------- \
Item Level: 71 \
-------- \
Properties are doubled while in a Breach (implicit) \
-------- \
+9 to Strength \
+299 to Accuracy Rating \
+16 to maximum Mana \
53% increased Mana Regeneration Rate \
-------- \
Corrupted \
-------- \
Note: ~price 1 alch \
'

# ---------------------------------------------------------

# All the URLs to the RePOE JSON data
url_base_items = 'https://raw.githubusercontent.com/brather1ng/RePoE/master/RePoE/data/base_items.min.json'
url_item_classes = 'https://raw.githubusercontent.com/brather1ng/RePoE/master/RePoE/data/item_classes.min.json' 
url_stat_translations = 'https://raw.githubusercontent.com/brather1ng/RePoE/master/RePoE/data/stat_translations.min.json' 
url_tags = 'https://raw.githubusercontent.com/brather1ng/RePoE/master/RePoE/data/tags.min.json' 
url_stats = 'https://raw.githubusercontent.com/brather1ng/RePoE/master/RePoE/data/tags.min.json' 
 
 
# ---------------------------------------------------------

def fetch_repoe_data( url ):
    try:
        response = requests.get( url )
        response.raise_for_status()

        return response.json()
    
    except HTTPError as http_error:
        print( f'HTTP error occurred when fetching RePOE data: { url }, { http_error }' )

    except Exception as error:
        print( f'Other error occurred when fetching RePOE data: { url }, { error }' )

# ---------------------------------------------------------

json_base_items = fetch_repoe_data( url_base_items )
json_item_classes = fetch_repoe_data( url_item_classes )
json_stat_translations = fetch_repoe_data( url_stat_translations )
json_tags = fetch_repoe_data( url_tags )
json_stats = fetch_repoe_data( url_stats )

