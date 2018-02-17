import sqlite3
 
def create_database():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
 
    # create a table
    cursor.execute("""CREATE TABLE albums
                            (title text, artist text, year text)
                        """)
    # insert some data
    cursor.execute("INSERT INTO albums VALUES "
                   "('Master of Puppets', 'Metallica', '1986')")
 
    # save data to database
    conn.commit()
 
    # insert multiple records using the more secure "?" method
    albums = [('Reign in Blood', 'Slayer', '1986'),
              ('Among The Living', 'Anthrax', '1987'),
              ('Rust In Peace', 'Megadeth','1990')]

    cursor.executemany("INSERT INTO albums VALUES (?,?,?)",albums)
    conn.commit()
 
def delete_artist(artist):
    """
    Delete an artist from the database
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
 
    sql = """
    DELETE FROM albums
    WHERE artist = ?
    """
    cursor.execute(sql, [(artist)])
    conn.commit()
    cursor.close()
    conn.close()
 
 
def update_artist(artist, new_name):
    """
    Update the artist name
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
 
    sql = """
    UPDATE albums
    SET artist = ?
    WHERE artist = ?
    """
    cursor.execute(sql, (new_name, artist))
    conn.commit()
    cursor.close()
    conn.close()
 
 
def select_all_albums(artist):
    """
    Query the database for all the albums by a particular artist
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
 
    sql = "SELECT * FROM albums WHERE artist=?"
    cursor.execute(sql, [(artist)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
 
 
if __name__ == '__main__':
    import os
    if not os.path.exists("mydatabase.db"):
        create_database()
 
    delete_artist('Megadeth')
    update_artist('Anthrax', 'Anthrat')
    print(select_all_albums('Slayer'))