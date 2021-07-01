"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self.isPlaying = False
        self.isPaused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()  # Fetch all the videos
        all_videos.sort(key=lambda x: x.title)  # Use key with lambda to dictate sort to only go through video title
        print("Here's a list of all available videos:")

        for video in all_videos:  # Loop through txt file, reading each video line by line
            tagString = str(video.tags)  # Convert to string to allow stripping of brackets
            # tagStrip.strip("()") # Old code - this didn't make a difference with this line placement
            print(video.title, "(", video.video_id, ")", "[", tagString.strip("()"), "]")


    def play_video(self, video_id):
        video = self._video_library.get_video(video_id)

        if video:
            print(f"Stopping video: {self._current_video}")
            print(f"Playing video: {video.title}")
            self._current_video = video.title
        else:
            print("Cannot play video: Video does not exist")



    def stop_video(self):
        """Stops the current video."""
        current_video = self._video_library.get_video()

        if current_video:
            print(f'Stopping video: {self._current_video.title}')
            self._current_video = current_video
        else:
            print("Cannot play video: Video does not exist")


    def play_random_video(self):
        """Plays a random video from the video library."""
        get_video = self._video_library.get_all_videos()  # acquire all videos
        num_videos = len(self._video_library.get_all_videos())

        if num_videos == 0:
            print("There are no videos available to play")
        else:
            if self.isPlaying is True:
                print("Stopping video:", self.current_video.title)
                self.isPaused = False
            pick_video = random.choice(get_video)
            print("Playing video:", pick_video.title)
            self.isPlaying = True
            self.current_video = pick_video

    def pause_video(self):
        """Pauses the current video."""

        if self.isPaused == False:
            print(f"Pausing video: {self._current_video}")
            print(f"Pausing video: {self._current_video.title}")
            self.isPaused = True

        else:
            print(f"Video already paused : {self._current_video.title}")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.isPaused == False:
            print(f"Continue video: {self._current_video.title}")
        if self.current_video == None:
            print("Cannot continue video, no video is currently playing")
        if self.isPaused == False and self._current_video != None:
            print("Cannot continue video: video is not paused")
        self.isPaused = False

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
