from django.core.management.base import BaseCommand
from music.models import Artist, Track  # Giả sử bạn có model Artist và Track

class Command(BaseCommand):
    help = 'Seed database with artist and track data'

    def handle(self, *args, **kwargs):
        # Seed artists
        artists = [
            {"name": "Taylor Swift", "avatar_url": "https://images.wsj.net/im-951977/?width=1278&size=1", "artist_id": "1"},
            {"name": "Ed Sheeran", "avatar_url": "https://th.bing.com/th/id/OIP.5qGGmhvQI0eImfh1_6QizwAAAA?rs=1&pid=ImgDetMain", "artist_id": "2"},
            {"name": "Adele", "avatar_url": "https://y.gtimg.cn/music/photo_new/T062M000002Jwwfm2iEMgy.jpg?max_age=0", "artist_id": "3"},
            {"name": "Drake", "avatar_url": "https://images.genius.com/576b0d161eb08515aae3095a399d970a.1000x1000x1.jpg", "artist_id": "4"},
            {"name": "BTS", "avatar_url": "https://assets.pikiran-rakyat.com/crop/0x946:996x2004/x/photo/2020/06/19/2624712725.jpg", "artist_id": "5"},
        ]

        for artist in artists:
            Artist.objects.create(
                name=artist["name"],
                avatar_url=artist["avatar_url"],
                artist_id=artist["artist_id"]
            )

        # Seed tracks
        tracks = [
            {"name": "Anti-Hero", "artist": "Taylor Swift", "cover_url": "https://is2-ssl.mzstatic.com/image/thumb/Music122/v4/ff/13/36/ff1336fd-2fe4-2ca7-8b9d-e5c548ebc50e/22UM1IM30667.rgb.jpg/1200x1200bf-60.jpg", "track_id": "101"},
            {"name": "Shape of You", "artist": "Ed Sheeran", "cover_url": "https://th.bing.com/th/id/OIP.J-z8JrhX2EhcIfugldA8sQHaHa?rs=1&pid=ImgDetMain", "track_id": "102"},
            {"name": "Hello", "artist": "Adele", "cover_url": "https://akns-images.eonline.com/eol_images/Entire_Site/2015923/rs_600x600-151023033104-600.adele-hello.102315.jpg?fit=around|1080:1080&output-quality=90&crop=1080:1080;center,top", "track_id": "103"},
            {"name": "God's Plan", "artist": "Drake", "cover_url": "https://th.bing.com/th/id/OIP.DgxeYQA9ZVszvVTYnWK46AHaHa?rs=1&pid=ImgDetMain", "track_id": "104"},
            {"name": "Dynamite", "artist": "BTS", "cover_url": "https://capricho.abril.com.br/wp-content/uploads/2020/08/bts-clipe-dynamite-look-gucci.jpeg?quality=85&strip=info", "track_id": "105"},
        ]

        for track in tracks:
            Track.objects.create(
                name=track["name"],
                artist=track["artist"],
                cover_url=track["cover_url"],
                track_id=track["track_id"]
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded artist and track data!'))
        