import pdb

from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Calvin Harris")
artist_repository.save(artist1)
artist2 = Artist("Jessie Ware")
artist_repository.save(artist2)
artist3 = Artist("Dua Lipa")
artist_repository.save(artist3)

album1 = Album("18 hours", 'pop', artist1)
album_repository.save(album1)
album2 = Album("What's Your Pleasure", 'pop', artist2)
album_repository.save(album2)
album3 = Album("Future Nostalgia", 'pop', artist3)
album_repository.save(album3)

artist_repository.delete(artist1.id)


pdb.set_trace()
