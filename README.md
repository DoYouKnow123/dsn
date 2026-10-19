I reworked this version to work better with turbo 1/6 frames

python bpsk2.py

creates a file called telemetry_output.bin from the webcam

then type, as new bytes are added to the file, 

python3 nhdemod4.py telemetry_output.bin




----------------------------
you get frames like: 

[+] Synchronized Frame 166 Isolated at Symbol Offset 1786160:

    ├── Extracted APID Subsystem ID : 0x1FC
    
    └── Full Decoded Frame Payload Hex (223 Bytes):
    
        21 FC AA 63 B2 1F 8B 66 1A 68 FB B2 E2 A2 5F FD
        
        5F 5A 14 BD B6 33 93 4F 3D B7 11 10 FE 51 72 C1
        
        0F A5 B3 0D 24 FF B9 79 73 0F EB A1 0D 80 FE DA
        
        58 D8 07 AC DA 88 88 74 2C 99 C0 07 A2 D1 86 8A
        
        7F A7 BC E9 87 69 51 96 05 3B 7E 0C CC 83 FE 4C
        
        C4 44 3A 86 4C 84 03 E1 68 C3 49 3E D6 4C 54 41
        
        FE E9 6A 44 B5 BE 04 22 61 E1 BA 62 22 1D 4A 2E
        
        BC 21 F6 B2 64 A6 1F 73 26 3F 20 F9 D5 B5 F0 4E
        
        CA 02 31 20 FF BF 39 91 0E A5 97 3D 90 F9 5B 30
        
        51 4F D9 B7 0D 10 BD 2A 98 90 A5 6F A1 88 91 7E
        
        FF 58 C8 97 7A 8B 9E C8 5F 2C 98 69 23 D2 7B C6
        
        19 7E 95 0D 4D 53 93 B0 C6 4C 3C A6 C4 64 43 BB
        
        75 CD 40 3C 96 4C F6 D3 F5 AD F5 4C 3F 4A 44 A4
        
        89 FA 68 62 22 5F 33 6E 22 21 D9 A2 E8 20 1E
        
        -------------------------------------------------
        
    └── Extracted ASCII Strings (Skipping Non-Printable):
    
        └─ "!cfh__Z3O=Qr$ysXt,iQ;~LD:LhI>LTAjD"ab"J.!ds&? N1 9=[0QO*o~Xz_,i#{~MSL<dCu@<LL?JDhb"_3n"! "

from MSL (Curiosity)

