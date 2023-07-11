# OSC Replay
It's a pain to test face-tracked VRChat avatars while you're developing them because you have to keep taking the headset off and putting it on. This solves that issue by allowing you to record OSC messages from your face tracking software and replay them whenever you want.

### How to use
1. Download and install https://hexler.net/protokol
2. Upload an avatar that includes in its Parameters object all the parameters you want to record (This step is necessary because VRCFaceTracking only sends parameters it detects in the avatar OSC configuration)
3. Launch VRChat, Protokol, and VRCFaceTracking
4. Configure VRChat or VRCFaceTracking so that VRCFaceTracking is sending data to a different port than VRChat is listening on
5. Launch Protokol and have it listen on the port VRCFaceTracking is sending to
6. In Protokol, go to Options -> More..., select the General tab on the side, and set "Keep log lines" to some huge number like 5000 or 10000
7. Once you have your headset on and it's tracking your face, check the Enabled box in Protokol
8. Make funny faces
9. Uncheck the Enabled box
10. In Protokol, use File -> Save As to save the .txt file to the same folder as osc_replay.exe
11. Open a command line in the folder containing osc_replay.exe
12. `osc_replay.exe --file .\example_data.txt --port 9000`

### Contact
I'm `@kadachii` on Discord, hit me up there