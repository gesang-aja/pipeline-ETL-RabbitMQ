import psycopg2

def save_to_postgres(berita, berita_clean, hasil, tabel):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="UAS_DWH",
            user="postgres",
            password="098765",
            port="5432"
        )
        cursor = conn.cursor()

        if tabel == 'berita_clickbait':
            cursor.execute(
                """
                INSERT INTO berita_clickbait (berita, berita_clean, label_clickbait)
                VALUES (%s, %s, %s)
                """,
                (berita, berita_clean, hasil)
            )
        elif tabel == 'berita_topik':
            cursor.execute(
                """
                INSERT INTO berita_topik (berita, berita_clean, label_topik)
                VALUES (%s, %s, %s)
                """,
                (berita, berita_clean, hasil)
            )
        else:
            raise ValueError(f"Jenis '{tabel}' tidak dikenal. Harus 'clickbait' atau 'topik'.")

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Berhasil disimpan ke tabel '{tabel}'.")
    except Exception as e:
        print("Gagal menyimpan ke PostgreSQL:", e)
