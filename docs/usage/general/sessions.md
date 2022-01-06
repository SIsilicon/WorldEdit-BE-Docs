# Sessions

When you select a region or change your preferences in-game, your information will be put into a session that will be kept active as long as you stay logged in. Upon disconnecting, your session will be discarded in 10 minutes (or how long it was set to in [Configuration](/configuration)), allowing you to log back in and keep your session. Every WorldEdit builder gets a unique session.

Sessions contain various things such as the following:

- Your current selection
- Your history
- Your clipboard
- Any currently bound tools/brushes

!!! warning

    WorldEdit drops all sessions as soon as the world is closed/shut down, so it is not possible to directly copy between worlds or retain most tool bindings after closing a world, or shutting down a server.