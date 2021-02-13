""" Constants related to Entertainment System."""
from homeassistant.const import (
  CONF_NAME,
  CONF_DEFAULT,
  STATE_IDLE,
  STATE_OFF,
  STATE_ON,
  STATE_PAUSED,
  STATE_PLAYING,
  STATE_UNAVAILABLE,
  STATE_UNKNOWN,
  )
from homeassistant.components.remote import DOMAIN as REMOTE_DOMAIN
from homeassistant.components.media_player.const import (
  DOMAIN as MEDIA_PLAYER_DOMAIN,
  ATTR_APP_ID,
  ATTR_APP_NAME,
  ATTR_INPUT_SOURCE,
  ATTR_INPUT_SOURCE_LIST,
  ATTR_MEDIA_ALBUM_ARTIST,
  ATTR_MEDIA_ALBUM_NAME,
  ATTR_MEDIA_ARTIST,
  ATTR_MEDIA_CHANNEL,
  ATTR_MEDIA_CONTENT_ID,
  ATTR_MEDIA_CONTENT_TYPE,
  ATTR_MEDIA_DURATION,
  ATTR_MEDIA_ENQUEUE,
  ATTR_MEDIA_EXTRA,
  ATTR_MEDIA_EPISODE,
  ATTR_MEDIA_PLAYLIST,
  ATTR_MEDIA_POSITION,
  ATTR_MEDIA_POSITION_UPDATED_AT,
  ATTR_MEDIA_REPEAT,
  ATTR_MEDIA_SEASON,
  ATTR_MEDIA_SEEK_POSITION,
  ATTR_MEDIA_SERIES_TITLE,
  ATTR_MEDIA_SHUFFLE,
  ATTR_MEDIA_TITLE,
  ATTR_MEDIA_TRACK,
  ATTR_MEDIA_VOLUME_LEVEL,
  ATTR_MEDIA_VOLUME_MUTED,
  ATTR_SOUND_MODE,
  ATTR_SOUND_MODE_LIST,
  )

DOMAIN = "entertainment_system"

CONF_AVAILABILITY = "availability"
CONF_DISPLAY = "display"
CONF_POWER = "power"
CONF_TURN_ON_ACTION = "turn_on_action"
CONF_TURN_OFF_ACTION = "turn_off_action"
CONF_POWER_STATE_TEMPLATE = "power_state_template"
CONF_MEDIA_SOURCES = "media_sources"
CONF_MEDIA_PLAYER = "media_player"
CONF_REMOTE = "remote"

VALID_STATES = [
    STATE_ON,
    STATE_OFF,
    "true",
    "false",
    STATE_IDLE,
    STATE_PAUSED,
    STATE_PLAYING,
    STATE_UNKNOWN,
    STATE_UNAVAILABLE
    ]
