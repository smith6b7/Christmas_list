import sqlite3
import argparse
import re

def create_shopping_list_table():
    conn = sqlite3.connect('christmas_shopping_list.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gift TEXT NOT NULL,
            recipient TEXT NOT NULL,
            purchased BOOLEAN DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_gift(gift, recipient):
    conn = sqlite3.connect('christmas_shopping_list.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO gifts (gift, recipient) VALUES (?, ?)', (gift, recipient))
    conn.commit()
    conn.close()
    print(f"Gift '{gift}' for {recipient} added to the list.")

def remove_gift(gift_id):
    conn = sqlite3.connect('christmas_shopping_list.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM gifts WHERE id = ?', (gift_id,))
    conn.commit()
    conn.close()
    print(f"Gift with ID {gift_id} removed from the list.")

def mark_purchased(gift_id):
    conn = sqlite3.connect('christmas_shopping_list.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE gifts SET purchased = 1 WHERE id = ?', (gift_id,))
    conn.commit()
    conn.close()
    print(f"Gift with ID {gift_id} marked as purchased.")

def list_gifts():
    conn = sqlite3.connect('christmas_shopping_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, gift, recipient, purchased FROM gifts')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No gifts in the list.")
    else:
        print("Christmas Shopping List:")
        for row in rows:
            status = "Purchased" if row[3] else "Not Purchased"
            print(f"{row[0]}. {row[1]} for {row[2]} ({status})")

def main():
    parser = argparse.ArgumentParser(description='Christmas Shopping List Manager')
    parser.add_argument('-a', '--add', nargs=2, type=str, help='Add a gift and recipient to the list')
    parser.add_argument('-r', '--remove', type=int, help='Remove a gift by ID')
    parser.add_argument('-m', '--mark', type=int, help='Mark a gift as purchased by ID')
    parser.add_argument('-l', '--list', action='store_true', help='List all gifts')
    args = parser.parse_args()

    create_shopping_list_table()

    if args.add:
        add_gift(args.add[0], args.add[1])
    elif args.remove:
        remove_gift(args.remove)
    elif args.mark:
        mark_purchased(args.mark)
    elif args.list:
        list_gifts()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()