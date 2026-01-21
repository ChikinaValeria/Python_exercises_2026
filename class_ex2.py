import xml.etree.ElementTree as ET

def process_local_bulletins(filename, filter_word=None):
    try:
        # Load and parse the local XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Find all <item> elements
        items = root.findall('./channel/item')

        print(f"--- Bulletin Report (Total: {len(items)}) ---")
        if filter_word:
            print(f"Filter: showing entries containing '{filter_word}'\n")

        for item in items:
            # Extract data from child tags
            title_node = item.find('title')
            date_node = item.find('pubDate')
            desc_node = item.find('description')

            title = title_node.text if title_node is not None else "No Title"
            date = date_node.text if date_node is not None else "No Date"
            description = desc_node.text if desc_node is not None else ""

            # Filtering logic
            if filter_word:
                content_to_search = (title + description).lower()
                if filter_word.lower() not in content_to_search:
                    continue

            print(f"TITLE:       {title}")
            print(f"DATE:        {date}")
            # show the first 200 chars
            print(f"DESCRIPTION: {description.strip()[:200]}...")
            print("-" * 40)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please run Step 1 first.")
    except ET.ParseError:
        print(f"Error: Failed to parse XML. The file might be corrupted.")

# Run the program
if __name__ == "__main__":
    # Attribution as required by the license
    print("Source: Latest bulletins from the City of Tampere.")
    print("Maintainer: Viestintäyksikkö.\n")

    # Example: Filter by 'tie' (road) or set to None to see everything
    process_local_bulletins("tampere_bulletins.xml", filter_word="koulu")