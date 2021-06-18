from podcast_generator import PodcastGenerator
from helper import Helper
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def main()
    generator = PodcastGenerator()
    generator.generate_podcast(Helper.get_keyword())
    voice_rate = Helper.get_voice_rate()

    generator.read_podcast(voice_rate)


if __name__ == "__main__":
    main()

