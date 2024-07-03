# Import libraries
from googleapiclient.discovery import build

# Replace with your Youtube Data API Key
DEVELOPER_KEY = "YOUR_API_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_playlist_duration(playlist_id):
  """
  This function retrieves video durations from a YouTube playlist and calculates the total duration.

  Args:
      playlist_id: The ID of the YouTube playlist.

  Returns:
      A list containing video durations (in seconds) and the total playlist duration (in seconds).
  """

  # Authenticate with YouTube Data API
  youtube = build(
      YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  # Initial request to get the first page of videos (max 50)
  request = youtube.playlistItems().list(
      part="snippet",
      playlistId=playlist_id,
      maxResults=50
  )
  response = request.execute()

  # Initialize variables
  video_durations = []
  total_duration = 0

  # Loop through playlist items (might require pagination)
  while response:
    for item in response["items"]:
      video_id = item["snippet"]["resourceId"]["videoId"]

      # Get video details including duration
      video_request = youtube.videos().list(
          part="contentDetails",
          id=video_id
      )
      video_response = video_request.execute()
      try:
        # Extract video duration in seconds from ISO 8601 format
        duration = video_response["items"][0]["contentDetails"]["duration"]
        duration_seconds = parse_duration(duration)
        video_durations.append(duration_seconds)
        total_duration += duration_seconds
      except (KeyError, IndexError):
        # Handle potential errors (e.g., missing data)
        print(f"Error retrieving duration for video: {video_id}")

    # Check if there are next page tokens
    next_page_token = response.get("nextPageToken")
    if not next_page_token:
      break

    # Use next page token to retrieve the next set of videos
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()

  # Return video durations and total playlist duration
  return video_durations, total_duration

def parse_duration(duration_string):
  """
  This function parses a YouTube video duration string (ISO 8601) into seconds.

  Args:
      duration_string: The duration string in ISO 8601 format (e.g., PT2H30M5S)

  Returns:
      The video duration in seconds (e.g., 10805)
  """

  # Extract time markers (hours, minutes, seconds)
  hours, minutes, seconds = [int(x) for x in duration_string.split("PT")[1].split("H", "M", "S")]
  # Calculate total duration in seconds
  total_seconds = hours * 3600 + minutes * 60 + seconds
  return total_seconds

# Example usage (replace with your playlist ID)
playlist_id = "YOUR_PLAYLIST_ID"
video_durations, total_duration = get_playlist_duration(playlist_id)

# Print results
print("Individual Video Durations (seconds):")
for duration in video_durations:
  print(duration)
print(f"\nTotal Playlist Duration (seconds): {total_duration}")

# You can further process the results here (e.g., convert to human-readable format)
