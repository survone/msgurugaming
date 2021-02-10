Python script to notify a Discord server when the streamer goes live, with the current game and box art.

This was made to partially automate the process of notifying a Discord server that the broadcaster has gone live, while still adding useful information like the stream's title and game that would otherwise have to be done manually.

How it works
Once running, the script will keep checking for your stream to go live and post in the Discord channel when it goes live with the message and description of your choosing, along with the box-art for the current game/activity.

The program will run once and then stop, and will only allow one execution at a time in case your finger slips and you hit it twice really quick by mistake, which tends to happen a lot personally when using a Stream Deck. ;)

Don't worry if there's a little delay before it says you're live, that's a Twitch issue.

Example Notification
Example Notification

Getting Started
The only thing you will need to run this is Python 3, which can be downloaded easily here.

Once you've got that, head on over to the Releases tab and download the latest TwitchLiveNotifier-vX.X.X.zip file and extract it somewhere convenient on your PC.

From there, make it your own by creating a config.ini file in the format of the existing config_example.ini file with your details. (I.e. Just rename the one there to config.ini) See the below "Config file details" section for how to fill this all out.

When you're all configured, run it in the foreground with start.bat or in the background with TwitchLiveNotifierHidden.exe thanks to the included AutoHotkey script that comes pre-compiled in all releases. You can recompile it yourself if you have AutoHotkey using the included TwitchLiveNotifierHidden.ahk if you run into any issues with the exe.

Updating
All that is required to update to a newer version is copying your config.ini file from your previous installation into your newly downloaded one and adding any additional values that may be missing based on the new config_example.ini file.

Config file details
The included config_example.ini should give you a good idea of what the config.ini file should look like, but I'll explain where to get all these values in detail.

Twitch
User
This is simply the username/handle of the streamer/broadcaster.
It can be written in whatever case you would like it to appear in the below Discord message/description placeholders, as it will be converted to lowercase automatically for internal functionality.

ImagePriority
This is what image should be attempted to be used first for the message, Game or Preview.
If the game logo or stream preview cannot be loaded, it will fall back to the user logo.

ClientId
This is the Client ID you can get from the Twitch Developers console.
