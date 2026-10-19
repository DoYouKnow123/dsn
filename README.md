I reworked this version to work better with turbo 1/6 frames

python bpsk2.py

creates a file called telemetry_output.bin from the webcam

then type, as new bytes are added to the file, 

python3 nhdemod4.py telemetry_output.bin
