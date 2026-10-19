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


------------------------------

example frames:


[*] ===============================================
[*] NEW HORIZONS TELEMETRY PROCESSING PIPELINE
[*] ===============================================
[+] STATUS: Standard CCSDS Descrambler ACTIVE.
[*] PARSER: Skipping unprintable characters enabled.

[+] Synchronized Frame 0 Isolated at Symbol Offset 0:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC A2 EB 86 1F 2B 66 1A 61 FF 96 F3 A6 0F 8D
        57 16 04 EF F4 31 11 2F 19 B1 11 00 FB 51 33 D9
        0F C5 B3 2D 14 7E A9 61 C3 0F C8 A1 A9 A0 7E BA
        19 99 87 C6 FB 88 88 77 68 9B E0 87 DA E9 82 90
        3F E5 BC F1 85 E1 55 C4 C5 3B 1D 3C C4 43 E6 E5
        E6 44 3F 54 4C E4 03 C5 68 D1 45 3F B6 DC 34 C2
        F2 AC 6A 66 B5 BC 96 22 61 F1 B6 62 22 DF CB 2E
        7B 21 F9 B4 60 A0 1F FB EE 18 61 FA 36 A1 30 0F
        CE 6B 19 30 F1 9E 31 11 0E ED 17 7D 10 F8 59 31
        53 4F BB B7 1D 30 3E 2A 52 90 27 6F 01 08 98 7C
        DB B8 C8 87 52 8B 98 80 7C 2C 98 29 A3 DB DA CC
        98 7E 75 0D 4C 03 B5 B2 C4 4C 3D EE D4 44 43 A9
        65 CF 40 3C 14 CC 34 93 E9 ED C6 64 3F 3A 86 B6
        09 D9 EC 62 24 1F 17 4E 22 21 DC A6 61 A0 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+faW1/Q3-~a~wh?U;<CD?TLhE?4jf"ab".{!`a60k01}Y1SO0>*R'o|R|,)~uLL=DCe@<4d?:b$N"!a"

[+] Synchronized Frame 1 Isolated at Symbol Offset 10760:
    ├── Extracted APID Subsystem ID : 0x5DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        25 DD B2 66 B2 1F 0B 66 1A 21 FE 16 E3 E6 15 ED
        4B 56 10 ED 36 21 17 0F 91 A7 11 10 EE 55 73 90
        0F 85 B3 0D 30 FD DF 11 C3 0F A3 AB 09 9A 76 52
        19 89 97 30 9A 8C 88 76 28 B8 E0 07 E2 D3 86 98
        7E ED BD 79 97 E9 51 84 D1 3B 48 2C 44 C3 E3 4D
        C4 44 3B F4 4D F4 83 C9 6C CF 4D 1E 5F 54 76 C3
        F0 A8 43 44 B7 BE 86 26 61 A3 B6 A2 22 1F DA AE
        B2 21 E4 B2 62 A6 9F F1 26 2E 61 FB 56 E5 31 1E
        DB 4B 33 20 FC DD 51 91 0E 9D 53 3C 10 F1 DA 30
        5B 4F D8 B3 25 B0 F8 1A 52 99 07 E7 A5 89 99 78
        41 B8 88 87 F2 89 BE 08 7D 2D 98 6D A7 F8 CB 83
        C9 5E 35 4D 55 12 B6 DA C4 44 BE 3E 74 44 4B E7
        45 DF 20 3D 16 0C 74 91 EF A5 C1 74 1F 06 8E A4
        01 EB E8 63 62 5F 63 6E 22 21 D4 A2 E3 B0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "%ff!KV6!Us0vR0v(~yQ;H,DMD;MlM_TvCD&a"!b&.aV1K3 QS<0[O%RxA}-m^5MUD>tDKE =ttcb_cn"!"

[+] Synchronized Frame 2 Isolated at Symbol Offset 21520:
    ├── Extracted APID Subsystem ID : 0x1DB
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DB B2 6F A2 1F 8B 66 2A 60 FC B6 F3 84 1F 95
        49 57 05 EC B6 31 13 0F 1D B7 11 10 A2 55 71 49
        0F C5 B3 2D 20 FC DB 11 41 0F D7 AB 89 02 76 FB
        19 99 97 C6 DB CA 88 74 AE B8 BC 87 D2 D1 B2 88
        7F 9D B8 B9 87 A0 D4 D4 D9 6B 0D 0C C4 C3 EE FD
        C4 4C 3B B4 DC 90 43 C9 6C C9 4D 3E FD D0 74 C1
        74 A9 42 66 9D A6 46 E2 45 E3 3E A2 22 1D CF A6
        1A 21 E0 B2 61 A2 0F F3 EA 38 60 FA D2 B5 B2 4F
        CF 63 31 14 F1 9B 71 91 0E ED 75 15 90 F9 5B 10
        D3 4F 97 F7 86 10 FC 0A 5A D1 27 6D 91 98 90 79
        CD B0 88 87 7A 9B 9E E8 7A 2D 98 69 A7 DF 5B C2
        18 3E 44 89 5C 86 B5 D0 CE 48 B9 77 DC 44 43 E9
        75 CF 64 3E 16 CC 34 53 FB A5 65 8C 3F 82 96 A4
        03 D9 6C 66 22 1F 3A 83 A2 21 D9 A2 69 22 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!of*`IW1UqI- AvtkL;ClM>ttBfFE>"!a8`Oc1qu[OZ'myzz-i[>D\HwDCud>4Se?lf":!i""

[+] Synchronized Frame 3 Isolated at Symbol Offset 32280:
    ├── Extracted APID Subsystem ID : 0x1D2
    └── Full Decoded Frame Payload Hex (223 Bytes):
        61 D2 B2 E5 82 1F 0B 66 9A 29 F7 16 61 B2 5F 85
        76 51 55 FC 76 31 93 2F AD 01 91 10 EC 51 72 C0
        0B A5 B3 35 34 FB F9 51 D3 2F D3 B1 AB A0 F6 BB
        19 8B 87 9D DA C8 8A 77 28 88 4C 07 E2 D9 86 80
        3D FD B8 71 97 E8 D2 96 C8 3B 6F 0C 64 4B E6 4D
        C4 44 3B 95 5C D6 43 E1 68 C1 49 1E E6 FE 74 C2
        F0 28 6B 48 9D 97 C6 2A 41 F3 F6 73 22 1D CA 2E
        70 05 E4 B4 65 A2 9F DF 6F 1A E1 7B 74 35 24 4A
        DE 6B 13 10 FC 9B 71 91 0F E5 D3 2C 32 FA 5B 31
        91 6F FF B1 14 B0 BC 8A 90 F8 07 ED 85 98 80 7E
        AF 39 88 87 FA 8B B0 00 7C AD 1A 68 A7 F8 C8 8B
        58 7F 4D D9 6C 16 F6 A0 C6 CC 3C FD DC 44 43 BD
        45 CD C5 3E 56 CC 34 D3 FF 6D C3 6C 7F 66 84 24
        09 59 CD E2 26 1E 97 4A 32 21 DC EA E7 E6 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "af)a_vQUv1/Qr54Q/w(L=q;odKMD;\ChIt(kH*As".peo{t5$Jkq,2[1o~9|hXMl<DCE>V4mlf$Y&J2!"

[+] Synchronized Frame 4 Isolated at Symbol Offset 43040:
    ├── Extracted APID Subsystem ID : 0x15C
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 5C AA 67 30 1E 4B 26 FA 60 FF FE 63 A6 17 99
        62 1F 74 FD AE 31 33 0F D9 E7 11 10 EC 51 72 D1
        4F 95 B3 05 24 7E FF 51 E3 27 EB A9 AF 82 D6 52
        18 99 87 AC CA 8E 88 7E 28 B8 64 07 3A D9 B6 9A
        3C CD E8 A5 D5 F5 DE C4 C5 7B 0F AC 4C C3 D2 6D
        84 44 3F F4 5C F4 43 E1 6C C3 40 3F F2 D4 64 4B
        F0 A9 6A 60 95 A6 86 36 61 E3 BE E2 22 1C 4A 2E
        3A 01 F4 B6 60 A6 8F 2B 62 3E 61 78 D4 B4 A0 4E
        5F C2 11 10 F9 9B 31 91 4E E5 57 1C 90 F8 58 30
        D3 67 DF B7 1D 90 BC 3B 5A 98 2F 65 E1 89 88 7A
        ED 98 88 87 3A C9 9E 88 7D 2D 18 69 27 FE DB EF
        58 7E 95 4D 48 43 B3 D0 8D 4C 3E 76 98 64 43 F1
        45 CB 34 3F 16 8C B4 D3 EF 6D 41 4C AF 2E D6 FE
        A9 FB CC 62 20 5F 3B 4B 22 01 DD A2 63 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!\g0K&`cbt13QrO$~Q'R~(d:<{LmD?\Cl@?dKj`6a"J.:`+b>axN_1NWX0g;Z/ez:}-i'X~MHCL>vdCE4?mAL.b _;K"c"

[+] Synchronized Frame 5 Isolated at Symbol Offset 53800:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DF A2 E7 82 5E CB 06 12 61 F3 36 A2 96 1F 85
        63 1B 04 AD F4 B1 B3 0F 91 B7 11 10 FE 5D 73 D1
        0B D5 93 3D 30 FF 5A 31 F1 0B CA A3 A9 08 56 F8
        39 89 87 C4 D9 88 88 77 6C B9 EC 07 C2 D1 86 9A
        3D E5 A8 E9 85 E1 5B 87 C0 2B 7F 0C 64 C3 C7 6D
        C4 44 3F 95 5C F4 43 C1 64 C7 4D 3F 8E D4 76 C3
        F0 2A 42 60 9F BC C6 72 61 F3 6F A3 22 1D 6B A6
        32 01 F4 B4 63 A6 9F F3 6E 08 65 F8 F5 25 30 4E
        DB 63 11 60 FD 99 39 13 0E FD 53 3D 10 F0 5B 30
        D3 4F D9 F2 94 90 BD 5A 12 C9 0F 63 A1 98 98 7C
        CD B8 88 87 52 CB AE 88 7C 2D 98 E9 87 FE FA 8F
        DD 3E 05 2D 4C 12 B7 80 C4 48 3D E5 1C 44 43 B9
        65 DB 44 3E 16 CC 34 51 FF 65 E5 CC 3F 32 86 B6
        89 5B A4 63 66 1F 33 2F 22 21 F5 A2 E3 B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!^a6c]s=0Z1V9wl=[+dmD?\CdM?v*B`rao"k2cne%0Nc`9S=[0OZc|R|->-LH=DCeD>4Qe?2[cf3/"!"

[+] Synchronized Frame 6 Isolated at Symbol Offset 64560:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC AA E6 82 1F 0B 46 1A 61 F9 BE 61 A2 1F 95
        56 13 04 EC BC 23 13 0F 81 B4 11 10 EC 59 53 D1
        0F 85 B3 2D 34 FB EB 71 DB 0F CE B1 AD 82 F6 BA
        19 99 97 ED DB 89 88 74 28 B9 40 87 EA D9 8E 8A
        3F 6D AA 68 97 E2 D1 D4 C1 6F 3C AC 44 C3 C6 75
        E4 44 3B 15 5D 54 43 C1 68 C7 49 3F 6E DC 7C 49
        F5 AB 6B 6A 9D BF 06 32 41 F3 3E F2 22 1D 4A 2E
        7A 01 F0 B6 61 A6 9F FB E7 32 60 F9 94 F1 33 1B
        DA C3 33 00 F9 9B 31 91 0E C5 17 38 90 F0 5B 31
        D3 4F FD B7 9D 30 FC 2B 1A D8 27 ED A5 8E 98 7C
        DE B8 C8 87 4A 8B B8 18 7C 2D 98 E8 03 DA DB 86
        98 5E 45 2D 4D 02 B7 80 C4 4C BE F6 5C 44 43 AB
        45 CD 04 3E 16 8C B4 D3 EE 2C C3 8C BF 0A DE 3E
        8B DB 69 66 26 1E 33 7A 32 21 FC A2 E5 82 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!FaaV#YS-4qt(@?mho<DuD;]TChI?n|Ikj2A>"J.za2`3318[1O0+'|J|-^E-ML\DCE>,>if&3z2!"

[+] Synchronized Frame 7 Isolated at Symbol Offset 75320:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        A1 FC B2 65 A2 1F 0B 26 2A 09 F1 36 61 A6 07 99
        63 1A 24 ED 74 33 13 2F FD 97 91 10 FA 51 73 99
        0F 05 B3 1D 34 FE DF 71 53 27 C8 A3 A9 00 5E DA
        18 99 07 FF DB 88 8A 75 28 B9 40 87 C2 89 8E 8A
        7F CF A8 ED 87 E5 50 D6 C9 2B 59 0C 44 C3 E6 6C
        44 44 2B 97 5C C0 43 ED 6C C7 45 3F F7 DE 38 C3
        F8 69 42 60 9F BC 86 22 61 F9 3E 62 22 1F CA AE
        7E 21 E2 B2 61 A6 1F FB 6B 38 61 BC 56 35 72 0B
        DF C3 11 22 FC 9C 71 11 0E 8D 17 39 00 F8 5B 31
        51 4F DD BF 8D 10 FC 0B 1A 58 27 6B A1 88 90 78
        D9 98 88 87 72 EB 98 48 7D AD 99 E9 A7 EE DB 8A
        88 7F 55 2C 4C 13 F4 9A C4 44 3F 66 D4 64 43 B3
        45 CE 04 3F 16 CC 74 D3 FF 2D C7 EC 0F 2E 86 AE
        49 DB E8 62 66 5F B3 6A 32 21 FD A2 66 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "e&*6ac$t3/Qs4qS'^u(@P+YDlDD+\ClE?8iB`"a>b"~!ak8aV5r"q9[1QOX'kxrH}U,LD?fdCE?t-.Ibf_j2!f"

[+] Synchronized Frame 8 Isolated at Symbol Offset 86080:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE A2 EA 22 1F CB 66 5A 69 F2 B6 22 A6 5F C5
        42 57 04 AD 7C 31 93 0F 19 B7 91 10 EA 51 33 00
        0F 05 A3 3D 30 FF C9 69 53 0F A2 A1 29 80 F6 D5
        18 89 07 CE D9 CC 88 76 28 B8 E8 87 8A C9 86 98
        7E EC B8 68 82 FB 58 D5 C1 3B 6D 2C 64 CB C2 6C
        E4 44 3B 94 5C C6 43 E9 64 C3 45 3F 86 54 74 C8
        F8 E8 6A 60 95 B4 86 22 41 F1 3C A2 22 1D CB 2E
        7A 21 F0 B2 63 A4 9F BB 6E 3A 24 F9 54 31 B0 5E
        D6 4B 11 20 F7 98 79 11 0E A5 17 28 90 F0 59 32
        D1 47 BD B7 15 10 FD AB 7A 98 A7 6B A1 98 98 7D
        CD B9 88 87 52 E9 92 C8 7C AC 98 69 25 EE DB 86
        98 76 65 3D 48 93 B7 D8 C4 4C 3C F4 D4 44 43 B9
        44 DF 44 3E 16 8C 64 C3 F8 6C 47 8C 3D 2A B6 26
        0B FB E8 63 62 1E 52 EF 32 21 FC AA E6 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"fZi"_BW|1Q3=0iS)v(~hX;m,dlD;\CdE?Ttj`"A<".z!cn:$T1^K y(Y2Gzk}R|i%ve=HL<DCDD>dlG=*&cbR2!""

[+] Synchronized Frame 9 Isolated at Symbol Offset 96840:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 ED A0 1F 0B 66 5A 48 F6 B2 72 E6 4F 95
        67 13 45 ED B4 33 11 0F 19 B7 11 30 EA 55 72 C1
        0F 85 B3 0D 14 FF 7B 31 C1 0F E6 B3 2D 82 FE BA
        58 C8 87 8E F3 88 98 76 2A 9A E8 07 82 D9 82 9A
        7F FD 98 75 87 E9 D0 94 C1 6B 3C 0C 44 03 EE 6D
        C7 44 3B 94 5D 62 43 E1 60 CF 49 3F F6 D4 56 C2
        F0 A9 6A 64 35 96 C6 22 61 E5 3A E2 2A 1F 8A 2E
        70 25 E4 B0 62 A4 DF FA 6A 22 61 FA 74 35 B2 4F
        CB C3 31 30 FD 93 51 11 0E BD 55 6D 10 F6 5B 30
        D3 0F AD F7 1D B0 3C 3A 90 98 07 E9 31 88 98 7C
        6D 38 C8 87 6E 8B 92 88 7F 2D 19 A9 07 DF DA 8E
        98 5F B5 AD 4D 17 B3 D0 CC 44 3E 6C 94 44 43 F9
        45 CE 44 3E 16 4C 34 13 FD 6D 45 4C 2F C2 9E A6
        41 DB EC 63 26 5E DF CB 22 21 D0 A2 6A A8 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fZHrOgE30Ur{1-Xv*uk<DmD;]bC`I?Vjd5"a:*.p%bj"at5O10QUm[0<:1|m8n-_MD>lDCED>L4mEL/Ac&^"!j"

[+] Synchronized Frame 10 Isolated at Symbol Offset 107600:
    ├── Extracted APID Subsystem ID : 0x1DA
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DA A2 6F 12 1F 8B 06 3A 69 FF B2 E2 A6 5F C5
        4F 53 00 EC 3C 31 B3 0F 19 B7 11 10 E6 51 72 58
        0F 95 B3 05 34 7A 9B 78 D3 0F C3 A9 AD A0 F6 DE
        79 89 87 CC B9 88 88 7F 68 B9 E0 87 D2 D9 86 98
        3F 3D 98 8D 97 E5 50 D4 C5 2B 4D 0C 4C C3 FA EC
        CE 44 3B 94 5C 54 43 F1 64 CB 45 3F EF DE 7C C3
        F4 AF 6A 62 9F BB 16 62 61 F1 B6 E2 22 1D 9B 2E
        FA 21 E0 B2 21 A6 0F E3 64 3B 60 F8 55 F1 70 0F
        DF 43 19 30 F2 D2 71 91 0F E5 97 1D 10 F9 5B 30
        D3 0F BD B7 0E 78 FE 2A 52 DA 2F 6F B1 88 90 7C
        4C 8C 88 A7 72 A9 BE 00 7D AD 19 E9 A7 EE DB CE
        19 7E 75 AD 5C 03 F7 D2 C4 4C 3F 26 C2 44 42 A9
        74 CC 44 3E 96 4C 54 93 FB FD E3 44 3F 46 C6 2E
        21 FA ED 63 26 5E 32 6F 22 21 DC A2 E4 92 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!o:i_OS<1QrX4zxyh?=P+MLD;\TCdE?|jbba".!!d;`UpC0q[0x*R/o|Lr}~u\L?&DBtD>LTD?F.!c&^2o"!"

[+] Synchronized Frame 11 Isolated at Symbol Offset 118360:
    ├── Extracted APID Subsystem ID : 0x1D5
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D5 A2 E7 22 1F 2B 66 1A 09 FF B6 61 C6 57 95
        6B 13 14 ED F4 B3 13 0F 9D 97 91 10 EF 51 33 D1
        0F 95 93 2D 34 FE C9 79 F2 2F E2 A5 AD 90 76 B2
        18 88 87 FC D3 88 88 77 28 B9 E8 87 C2 D1 82 98
        7F FD B8 E4 85 E0 51 C5 C1 3B 39 0C 44 CB D7 6C
        E4 44 3B 15 5D F4 43 F5 60 C3 48 1B 76 D4 54 C3
        F4 AD 6A 66 3D BC 96 22 45 FF 22 62 22 1D 6A 26
        78 21 F0 B2 67 A2 8F 07 6C 20 25 FA 56 35 B1 5F
        FD CB 11 32 FA D9 79 11 0E E5 17 30 90 EE 5A 31
        51 4F D9 B7 05 B1 F6 4A BA 91 25 EF F1 88 90 7C
        F9 3C CA 87 72 A9 88 80 7E 2D 98 68 A3 F6 CB 86
        98 7E 1D 8D 6C 87 F7 92 C4 4C 3E 7E CC 64 43 F9
        45 C7 40 3E 16 8C 34 C3 F9 65 C7 4C 1F 02 86 A4
        29 FB E0 66 24 1E 3F 8E 22 21 FA A2 E1 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"+faWkQ3-4y/vw(Q;9DlD;]C`HvTjf="E"b"j&x!gl %V5_2y0Z1QOJ%|<r~-h~lL>~dCE@>4eL)f$?"!"

[+] Synchronized Frame 12 Isolated at Symbol Offset 129120:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC 22 61 80 1E 8B 06 0A 69 F3 2E E3 F6 1F E9
        5B 56 04 AD B4 B1 B2 0B B9 B3 11 50 ED 51 73 51
        0B 85 93 0D 34 B1 FF 71 43 0F B2 A1 89 82 FE F3
        18 C9 87 CD A9 C8 88 76 2E BB C8 07 42 D9 8E 98
        7F BF A8 6D 01 E5 51 C4 D5 7B 4E 0C C4 93 D7 71
        E6 44 3B 36 5C A4 43 F1 6C C3 6D 0E 1E 84 74 CB
        B8 A8 6A 48 BF 34 86 26 41 E7 EA 22 26 1D DA 2E
        5B 01 F2 B6 21 A6 9F D3 2E 78 61 F6 54 21 74 4F
        D6 83 39 20 F0 BF 31 11 0E CD 17 3D 00 B0 58 31
        D3 0F D7 91 05 30 DF 7A 1A B9 25 ED 05 18 99 78
        5D B8 C8 87 50 AB 80 C8 5E 2D 89 29 A7 E0 4A 8E
        99 7F 15 1C 5C 93 B7 D2 C4 4C 3E 6C DC 44 43 B9
        45 CE 00 3E 54 CC 14 93 EA 69 65 CC 87 4A 86 36
        0B DA E4 E3 22 17 13 CB A6 21 F9 A6 69 22 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"ai.[VPQsQ4qCv.BmQ{NqD;6\ClmtjH4&A"&.[!.xaT!tO9 1=X10z%x]P^-)J\L>lDCE>TieJ6"!i""

[+] Synchronized Frame 13 Isolated at Symbol Offset 139880:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD A0 E5 A0 5F 0B 66 1A 69 FF BC E2 86 17 C5
        76 53 45 FC 74 31 13 0F 2F 37 91 10 FE 51 73 C1
        0F 15 B3 05 34 7F F9 70 F3 07 C2 A1 2B AA 56 FC
        18 C8 87 6C 91 8C 88 54 0A 99 08 87 D2 C1 86 8A
        7B F7 98 2C 87 63 D8 C6 C1 2B 7D AC 4C 43 E6 6D
        C6 44 3B 1C 45 F0 03 E1 68 47 4D 3F 36 C0 14 42
        F0 AA 62 60 1F B5 86 22 61 F7 76 3A 22 1E 8A A6
        42 21 F6 B6 65 A0 1F 83 2E 2C 69 7C 54 61 30 0B
        D2 4B 31 30 FC 99 51 95 0E E9 17 2D 10 FA 5A 30
        D3 4F F1 9D 1F 30 7D 2B 9A B3 0F 6F 41 8D 98 7E
        1D B8 88 87 66 88 8A 08 78 2D B9 68 27 FA DB 8E
        88 7F 15 1D 4C 83 F4 D4 CE 4C 3C 76 9C E4 C3 FF
        C5 C7 60 3C 96 8C F4 D3 DD 6D 47 AC 8F 4A 84 66
        41 DB 50 63 22 5F 78 66 12 21 D6 AA E4 00 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!_fivSEt1/7Qs4p+VlT{,c+}LCmD;EhGM?6Bb`"av:"B!e.,i|Ta0K10Q-Z0O0}+oA~fx-h'LL<v`<mGJfAPc"_xf!"

[+] Synchronized Frame 14 Isolated at Symbol Offset 150640:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 DD BA ED 96 9E 4B 66 1A 60 FB 9E E3 B6 4F 85
        6B 5A 01 ED F6 B1 31 0F 9D 37 91 10 EE D8 72 D1
        0F 95 93 2D 30 EC 09 19 DB 0F A2 B1 2D A2 76 F7
        19 89 97 BC DB 8C 88 7E A8 99 A4 87 EE C9 86 90
        7D EF FC 78 83 C3 D0 94 C1 3B 6C 2C 64 C3 E6 4D
        C4 44 3A 54 4C D4 03 E9 6C CB 44 3F E7 DC 74 4B
        D4 28 66 60 95 A6 56 22 41 E1 34 B1 22 1D FB 2E
        E9 28 E4 B2 60 24 0F AD E2 3A 61 F8 54 61 24 0E
        8A 43 3B 00 F9 9B 51 91 0F 55 53 09 80 F6 5B 32
        D1 4F CC D7 0F 30 F6 EA 3A 99 A7 65 81 88 99 7D
        DD A8 C8 87 DA AB 96 C0 7C 2D 99 69 83 E7 DB 84
        18 1E C5 0D 29 02 B0 90 C6 48 BE F7 54 64 43 B1
        45 CD 44 3E D7 CC 34 C1 FD 2C C7 CC 3F 2E 94 A6
        29 FB 69 62 26 1F 77 AB 02 21 DA A2 62 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "Kf`OkZ17r-0-v~}x;l,dMD:TLlD?tK(f`V"A4".(`$:aTa$C;QUS[2O0:e}|-i)HTdCED>4,?.)ib&w!b""

[+] Synchronized Frame 15 Isolated at Symbol Offset 161400:
    ├── Extracted APID Subsystem ID : 0x1FA
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FA AA EB B2 9E 0B 66 0A 69 F3 92 20 36 5F A1
        5B 52 04 AC E4 31 12 2F 4D D7 11 10 EB 51 73 79
        0E A5 B3 5D 14 FA 9F 71 57 1F A0 A9 2D 82 D6 F2
        18 88 17 C4 C3 8C 88 77 E8 BB E8 87 8A C0 86 9A
        75 2D 9C 29 97 EB 5A D4 80 6B 7F 0D 44 C3 E6 4D
        24 44 3A 94 5C F4 43 C3 68 C2 4C 0E D6 54 3C 42
        F8 AC 4A 44 9D 97 86 32 21 F7 2E F9 A2 15 FA 2E
        48 21 70 BE 63 A6 9F BF 2A E9 21 FD 54 35 F6 5E
        57 8B 33 32 F9 5B 71 95 0E E5 17 11 10 F0 5B 30
        91 4F F5 B7 9F B0 FC BA 18 D8 27 6F 21 89 98 7A
        EE 78 88 87 72 A9 BC 08 7E 2D 98 69 87 E2 FA 87
        9C 1E F5 B9 70 93 F7 F0 C4 4C BE 27 06 44 43 BB
        45 D8 40 3E 16 CC F4 D3 FF AC E7 4C 3B C2 84 A4
        0B F9 E4 62 66 5F F3 CA 22 21 D8 A2 EA 82 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fi 6_[R1/MQsy]qW-wu-)ZkDM$D:\ChLT<BJD2!..H!pc*!T5^W32[q[0O'o!zxr~-ipL'DCE@>L;bf_"!"

[+] Synchronized Frame 16 Isolated at Symbol Offset 172160:
    ├── Extracted APID Subsystem ID : 0x1D2
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D2 BA E3 8A 1E 0B E6 0A 08 FD 32 A3 86 17 97
        73 57 44 BC FE 31 13 2F FF 03 11 00 EE 59 77 88
        0F 85 B3 2D 14 FD DB 78 53 0E C1 B5 8F 10 7E D2
        18 88 97 D6 DB 89 A8 57 A8 B9 F8 07 C2 D9 A6 88
        3D C4 B8 B5 A7 65 D8 C6 9D 39 59 AC 4C C3 E2 7D
        C4 44 BA 9D 5C F4 43 A1 68 C3 49 1B C6 F4 7E EB
        F9 2F 63 40 95 8C 96 32 41 D7 76 72 22 1D E2 26
        5A 61 E4 B6 60 A0 9D FB 6C 3D 25 FA F4 35 72 5A
        DB 2F 39 20 F4 93 79 D1 0F E5 17 71 92 EC 5B 32
        59 0F A7 81 85 12 BE 2A 3A FB 27 6E 25 88 88 78
        4F BC 88 85 F2 89 9A 88 79 2D 19 68 A7 DC CB 06
        D8 5E 15 DD 49 53 B7 88 C4 88 BE B6 1E 44 43 B9
        44 CB 60 3E 16 0C 94 C3 FF 6D E7 4C 0F 0A CC A6
        4B DA EC 66 66 1F F2 6E 32 21 DA AA E5 02 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!2sWD1/Yw-xS~W=e9YL}D\ChI~/c@2Avr"&Za`l=%5rZ/9 yq[2Y*:'n%xOy-h^ISDCD`>mLKffn2!"

[+] Synchronized Frame 17 Isolated at Symbol Offset 182920:
    ├── Extracted APID Subsystem ID : 0x1D6
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 D6 A2 E7 06 1C 6B 66 2A 49 FA 3A F3 82 0F 87
        43 53 01 ED 2C 31 51 0B 09 B1 93 10 EA 51 73 D9
        0F 85 93 15 34 FA CB 70 DB 07 C3 A9 29 80 F4 D8
        18 C9 07 ED 99 8C 88 77 E8 B9 E8 25 82 C1 96 98
        3D 0D B8 F9 91 E2 58 84 D1 3B 7F 0C 64 C3 DE EC
        44 44 3B 9C 5C F4 43 E1 60 D7 4C 1F AA DC 54 C3
        F0 6D 4A E4 9F 8F 86 2A 61 E3 22 B2 22 1D 5B 26
        7A 01 F2 B4 63 A6 1F 9A EE 3A 65 F9 54 31 11 4A
        DE 4B 19 20 F5 A9 59 11 0E C5 93 29 90 F8 59 32
        53 4F FF B7 5D 30 FC 7B 10 93 2F 6F 81 89 88 7C
        FD A8 88 87 F2 CB 8F 88 79 2C 98 69 87 F5 D9 80
        98 7E 0C 3D 6C 16 B7 D2 C4 CD 3E E6 1E 44 43 B9
        45 CE 24 3C D6 4C B4 D3 FF 6C CF 44 2F 82 96 E4
        8B 5F E8 63 26 77 32 EA 22 21 C5 BA 6F A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "kf*I:CS,1QQs4p)w%=X;dDD;\C`LTmJ*a""[&zc:eT1JK Y)Y2SO]0{/o|y,i~=l>DCE$<LlD/_c&w2"!o"

[+] Synchronized Frame 18 Isolated at Symbol Offset 193680:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC BA EE A0 16 0B 66 2A 68 F7 D6 A3 A6 17 85
        43 13 15 E5 F6 71 33 1F 9B F7 99 10 FE D9 72 C1
        0F D5 83 2D 34 7E EB F0 DB 23 D3 A1 9F 12 76 D2
        18 98 E7 0D E3 88 88 74 68 BB E0 87 E2 D9 86 8B
        7E DC B8 A4 8F E1 D4 D4 C1 6B CD 0C EC CB CE 7D
        60 44 3A D6 1C C2 43 E9 68 C3 49 3F FE 5C 74 C1
        F4 28 6A 60 37 BF C6 72 61 F3 14 F2 22 1D 0A A6
        7A 01 E2 B6 61 A4 8F 79 6E 0A 61 F9 D4 65 A0 5E
        5E C7 31 32 F5 BF 71 91 0F A5 13 15 50 F8 59 33
        D1 47 B6 F2 1D 30 7D BA BA B8 05 69 A5 99 92 7D
        8D 88 88 87 CE 8B 9D 00 7C 2C 99 29 A7 E4 D8 8E
        98 1E C5 4C 4C 12 B1 D0 84 48 3F 36 D6 44 43 F3
        64 CB 42 3E 16 1C A4 D1 FF 3D C3 E4 1F 1A B4 AE
        A9 DB C8 42 66 1F 5B 0F 22 25 FE A2 64 82 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!f*hCq3r-4~#vth~k}`D:ChI?\t(j`7ra"zaynae^^12qPY3G0}i}|,)LLH?6DCdB>=Bf["%d"

[+] Synchronized Frame 19 Isolated at Symbol Offset 204440:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DF AA E7 A2 1F 6B 46 1A 49 FF D6 E3 A6 1F 85
        7B 53 71 ED 7E B1 13 2F D9 B3 11 10 EE 59 72 D0
        0F 05 B3 0D 30 FF D9 51 E3 8F D3 A9 A9 80 F6 F6
        18 D9 97 D4 D9 88 A8 7D 28 BB 60 87 D2 D9 96 9A
        7E EE 98 AD 87 C2 56 C5 C9 2B 7D 08 4C 43 EF 49
        E4 44 3B 94 4C 84 43 F1 6C C3 4C 3F E7 8C 54 C1
        FA A8 6A 60 9F 97 56 22 21 FB 7A A2 22 1F 5A 2E
        32 21 E0 B6 61 A4 8F B3 2F 1B 65 7A B4 F5 73 1A
        D6 23 12 02 F9 DB 71 11 0E FD 17 01 90 F8 59 31
        DB 4B BD F5 15 30 CC 28 5A 18 A5 6F B1 88 98 6A
        E9 B8 89 87 46 8B AE 88 7C 2D 98 E8 07 F7 DB 8F
        98 5E 15 1D 48 03 F7 C8 C4 CC 3E 24 D6 64 C3 A1
        65 DD 44 3F F6 CC F4 D3 F7 6C D7 44 3F 06 DC A6
        01 FB 58 62 62 5F 12 8A 22 21 DB BA ED B4 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!kFI{Sq~/Yr0Q}(`~V+}LCID;LClL?Tj`V"!z"Z.2!a/ezs#qY1K0(ZojF|-^H>$deD?lD?Xbb_"!"

[+] Synchronized Frame 20 Isolated at Symbol Offset 215200:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE BA EF A0 1F 0B 06 5A 69 D9 B6 A7 A6 1F D7
        4A 53 50 ED 34 B1 11 0F F9 B7 11 10 EE 59 31 C1
        0F 45 33 0D 34 FA 9B 51 C3 07 C2 A1 A9 22 7E 3A
        19 99 87 DC C9 88 88 77 2C 99 68 07 C2 D9 9E 92
        3F CD B8 A9 97 E1 52 C4 C4 7B 59 8C 44 4B C7 41
        C4 44 3E 55 4C A0 03 F5 44 CF 4C 3E FF 5C 30 43
        FD ED 6A 40 1D 8F 86 26 41 F7 B6 F0 22 1D 8A 26
        2B 21 F4 B4 60 A6 0F 1B 26 2E 61 7A F6 B5 30 1B
        DF A3 31 30 FD 9B 51 91 0E E5 13 18 10 F0 5A 30
        D3 27 BF F7 8D B2 BC 2A 1A 98 87 E3 E1 8D 88 7C
        C8 98 88 87 72 CB BE C0 7E 2D 19 69 07 F2 E9 86
        99 3E 9D 29 4C 57 BF 90 C4 C4 3E 6E CC 64 43 B5
        44 C8 40 3E 96 CC 74 D1 F7 EC C3 2E 3F AA 84 70
        29 73 C8 66 26 1E 57 62 22 21 F8 BA E0 28 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!ZiJSP4Y1E34Q"~:w,h?R{YDKAD>ULDL>\0Cj@&A"&+!`&.az010QZ0'*|r~-i>)LW>ndCD@>t.?p)sf&Wb"!("

[+] Synchronized Frame 21 Isolated at Symbol Offset 225960:
    ├── Extracted APID Subsystem ID : 0x1D4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D4 A2 E7 B2 1F 0B 66 1A 01 F7 B2 E1 86 0F E5
        63 53 44 FD F4 31 11 2B 1B 25 11 10 ED 51 73 59
        0F 4D A3 0D 04 EB F9 F1 D1 0F E0 A1 AD 80 56 FC
        18 D9 87 CC DB CC 88 7D 2A 99 E8 87 82 D1 96 9A
        7F 4D B8 E9 87 E8 5C D4 C5 2F 59 0C C4 43 F6 CD
        C4 44 3F B4 4C BA C3 E9 68 CB 4C 3F F2 D4 70 43
        F1 28 EB 40 15 BE 86 F2 41 F9 36 F2 22 1D AA 2E
        60 21 F0 B4 61 A6 9D 7B 66 1A 61 79 54 E5 70 4E
        CE 63 39 30 FE 9D 71 91 0E 85 17 1C 10 F9 5B 33
        D3 4F FD B7 34 90 FC 1A 92 93 27 EE 81 88 98 7C
        4D 98 88 87 28 CB 9E 08 7C 2D 98 E9 A3 B4 9B 82
        19 5A 15 0D 5C 53 B7 E0 C5 CC 3F 2E CE 44 43 E3
        45 C7 64 3E 16 8C F4 53 FF 65 47 44 3F 4E B4 A4
        29 DB E8 66 26 1F 33 4E A2 21 FF A2 EB 82 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fcSD1+%QsYMV}*M\/YCD?LhL?pC(@A6".`!a{fayTpNc90q[3O4'|M(|-Z\S?.DCEd>SeGD?N)f&3N!"

[+] Synchronized Frame 22 Isolated at Symbol Offset 236720:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE A0 69 A8 1F 0B 66 1A 69 FF B2 E0 B6 1F F5
        67 52 15 EC E4 B1 33 1F 9B 87 51 10 EE D1 71 D8
        0F 05 B3 0D 34 F9 9B 51 51 0F C7 A9 A9 02 F6 12
        19 89 87 DC D9 88 89 77 A8 BB E8 07 9A D9 9A 82
        7E EF AC B0 93 E9 58 96 CC 7A 4D 0C 44 C3 FA ED
        44 44 3E 14 4C D4 03 A1 68 C3 4C 3F A2 C4 50 EB
        F0 28 6A 6C 3F 9F 84 62 65 FF 34 A2 20 1D 0A AE
        7A 21 F0 B4 65 A6 1F FB EA 38 71 FD 14 35 24 4A
        D7 C3 11 36 FD FA 79 11 0F F5 13 2C 10 FC 53 31
        D1 4F ED F7 85 12 FE 0A D0 D8 07 65 81 88 88 7E
        4D B8 C8 87 76 AB 8C C8 79 2D 19 29 A3 ED DA 87
        98 7E D5 3D 68 93 B6 F0 C4 4C 3E FF 4C 44 43 B1
        65 C7 24 3F 16 CC 74 01 EE AD C5 8C BF 4A C6 AE
        63 DB 48 63 26 56 3B 2E 22 01 FF AA E2 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!ifigR3Qq4QQw~XzMDDD>LhL?P(jl?be4 z!e8q5$J6y,S1Oe~Mvy-)~=hL>LDCe$?tJcHc&V;.""

[+] Synchronized Frame 23 Isolated at Symbol Offset 247480:
    ├── Extracted APID Subsystem ID : 0x1D6
    └── Full Decoded Frame Payload Hex (223 Bytes):
        29 D6 22 EF B2 1F 0B A6 5A 48 FE B2 E3 A6 1F AF
        6A 5B 00 AD F4 35 31 0F B9 25 11 10 EA 11 72 99
        0F 85 A3 05 20 FC 9B 71 43 77 C6 A3 2D 82 F6 FC
        10 81 97 FC 6A DC 90 77 6A B8 E0 07 AA D1 8E 8A
        7F 67 28 ED 97 E9 D0 C6 C1 3F 59 0C 44 C3 C6 6D
        C4 44 3B 95 5D E2 43 C9 68 C3 41 3F 9E DC 74 CB
        F8 A9 CA 64 9D AE 06 66 61 F7 F6 62 22 1D CA AE
        49 21 FE A6 65 A6 9F C3 67 3C 61 F8 56 35 A1 5E
        9F 63 17 30 F0 DB 71 11 0F C5 95 3C 12 EA 5B 34
        51 4F D9 F5 3D B2 FC 3A 58 98 25 E7 81 89 90 5C
        6C 88 89 87 72 CB 9E 88 7E 2D 99 6C A1 E8 DA 8E
        90 7E 95 0C 6D 03 B1 F8 C4 C4 3E 36 56 44 43 B5
        45 C9 44 BD 16 CC 34 D3 E3 A5 C5 0C 1F 2A 84 B6
        4B FB E0 62 26 5F 5B 4C 22 25 DC B2 E7 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ ")"ZHj[51%r qCw-jwjg(?YDmD;]ChA?tdfab"I!eg<aV5^c0q<[4QO=:X%\lr~-l~m>6VDCED4*Kb&_[L"%"

[+] Synchronized Frame 24 Isolated at Symbol Offset 258240:
    ├── Extracted APID Subsystem ID : 0x1FD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FD B2 ED 12 1F 2B 6E 3A 68 FF B6 F3 86 0F F1
        42 53 05 AD F0 31 91 0F 9B 91 95 10 EC D1 71 C0
        0F 95 A3 45 14 FF 2F 51 79 0F CA AD 8D A0 56 7F
        59 D8 07 85 DB 88 88 57 68 BB D8 07 C2 D9 82 9A
        7C BD B8 69 87 F1 58 94 C5 2F 7D 0C 44 83 E6 4C
        C4 44 3F 17 4C B6 C3 E1 68 4B 4D 3F B6 CC 3C C3
        D5 2D EB 6E BD BE C6 62 61 F7 37 E2 22 1D 5A 2A
        5B 21 F0 B2 69 A4 9F BF 48 1B 61 FA 55 35 37 4E
        9E 4B 11 30 F9 FE 51 11 0F 85 17 3D 00 F1 5A 31
        D0 47 B9 B7 8C 32 FC 0A 1A D9 25 67 A1 99 99 7C
        CB 38 88 87 26 8B B0 08 7C 2D 18 49 03 FE F9 8A
        89 5E 25 3D 6C 92 B5 F0 C4 40 3F 66 D4 54 43 B5
        55 CF 00 3E 96 5C 14 C3 F6 7D 45 4C 2F 2A 86 B6
        09 7A 79 66 62 1F 33 CA 62 21 F6 A2 ED 20 9F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+n:hBS1qE/QyVYWh|iX/}DLD?LhKM?<-nba7"Z*[!iHaU57NK0Q=Z1G2%g|8&|-I^%=l@?fTCU>\}EL/*zyfb3b! "

[+] Synchronized Frame 25 Isolated at Symbol Offset 269000:
    ├── Extracted APID Subsystem ID : 0x1FE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FE B2 E7 82 1E 8B A6 2A 68 FA B6 A1 A6 5F B1
        53 50 14 FC F4 31 11 0F 3A 87 11 10 A9 51 72 C1
        0F 85 A3 05 14 FF FE 73 D1 03 C0 B3 A9 A2 76 F2
        18 98 8F CD BB 81 88 76 68 BB 80 87 E2 D1 82 98
        3F 26 B8 E1 37 E1 56 94 CD 7B 1F 0C 44 C3 AF 41
        C6 44 3B 94 5D 74 43 D5 68 CA 65 3D 52 1C 50 EB
        E4 A8 4A 60 9D BE 16 26 03 FD 32 F3 2A 1D 8A A6
        1A 21 F0 A4 63 A2 8F CB 2E 3A 60 FD 35 71 20 5F
        DF 4B 11 30 F3 9D 71 31 0E ED 17 09 10 F9 5B 30
        D3 47 A7 B5 95 30 7E 3B 3A 98 2F EF A1 88 98 7F
        DC BC 88 87 F2 8B BA 00 7D 2D 99 69 A7 FE EA C6
        9A 7E 35 08 2C 43 B2 D8 C4 C4 3E 66 8C 44 43 B9
        65 CF 44 3E 16 0C 74 93 F8 7D 47 2C 0F 22 86 26
        09 F9 EC 6B 62 1E 33 83 02 21 DC A2 E7 82 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!*h_SP1:Qrsvvh?&7V{DAD;]tChe=RPJ`&2*!c.:`5q _K0q1[0G0~;:/}-i~5,C>fDCeD>t}G,"&kb3!"

[+] Synchronized Frame 26 Isolated at Symbol Offset 279760:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        A1 DE A2 E4 80 1F 6B 66 4A 69 F5 D6 F3 86 1F 99
        43 53 70 ED F4 31 13 0F 09 D4 91 30 FD 51 73 90
        0F 45 B3 05 30 FB 9B 5B 5B 0B C2 A9 AF 8A F6 F2
        18 D9 87 CD FB 88 88 7F 2C B9 24 87 92 D1 96 82
        7E 8D B8 A0 87 E1 D1 D4 C1 3F 7D 0C 45 C3 C6 ED
        C4 44 BB 14 4C F4 43 C5 64 C9 49 3E 66 DE 70 C1
        F6 AB 6A 40 95 BE 96 26 61 F2 3E F2 22 1D CA 2E
        79 01 F8 B6 60 A6 8F 93 AF 3B 61 FA 54 65 32 4A
        CF 63 13 20 F9 91 71 11 0A C1 57 1D 10 F8 59 31
        D3 47 F9 E7 15 10 FC 0A 9A C8 A7 61 A1 0C 99 7C
        4D B8 88 87 6A BB BE 88 7E 2D 18 69 87 FE DB 87
        88 06 4D 9C 4C 12 B1 90 C4 CC BE 66 9C 65 43 B9
        44 CA 60 3E 36 CC 74 53 FB 65 C7 4C 1F 0A 84 A6
        01 DB FC 66 66 1F 33 7B 22 21 DA B2 E6 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "kfJiCSp10QsE0[[,$~?}EDLCdI>fpj@&a>".y`;aTe2Jc qWY1Ga|Mj~-iMLfeCD`>6tSeLff3{"!"

[+] Synchronized Frame 27 Isolated at Symbol Offset 290520:
    ├── Extracted APID Subsystem ID : 0x1D8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D8 A2 69 A2 1E 0B 26 1A 69 F5 B2 63 A2 0F A5
        63 17 04 AD F4 F1 13 0F EB 63 11 10 EC D1 53 C0
        0F 1D B3 09 34 77 DB 71 1B 2F DA A9 AB 02 F6 BE
        59 8B 87 EC D3 CC 88 77 28 99 EC 87 BA C9 82 98
        7D AD B8 F8 95 F0 D0 D4 80 3B BD 0C C4 4F C2 19
        C4 45 3B 95 5C F2 43 E1 64 CB 45 3F DA DC 35 C7
        F0 AE 4A 66 9D 9C C6 62 41 F3 76 E2 22 1D 4A 2E
        78 21 F0 B6 63 A0 9F F9 6E 2A 68 F8 16 A1 35 4A
        DA 03 11 30 F5 FE 09 11 0E ED 17 3D 10 F4 5B 32
        50 4F FD 97 15 30 BC AA B2 98 25 4F A1 9C 88 7C
        9F 9C 88 A7 F2 8B 92 40 7A 2D 98 29 27 DB FB CF
        99 7E 05 2C 68 13 F7 F0 C4 4C 3F A6 CC 64 43 F1
        64 CC 44 3E 96 CC 34 D3 EA 6D C5 5C 3F 9E 9E A6
        8B DA F8 66 26 1E 53 0E 62 21 D6 A6 E7 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!i&icccS4wq/Yw(};OE;\CdE?5JfbAv"J.x!cn*h5J0=[2PO0%O|@z-)'~,hL?dCdD>4m\?f&Sb!"

[+] Synchronized Frame 28 Isolated at Symbol Offset 301280:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        29 DC AA 6E 36 1F 0B E6 3A 49 FE 36 A3 A6 46 9F
        43 53 54 ED FC B7 93 0F 89 A7 11 04 FE 59 77 D1
        2F 85 13 0D 02 FA 8B 79 C1 0F FA B1 8D 82 76 98
        58 88 87 44 F3 C8 88 77 A8 B8 E8 87 C2 D9 96 88
        7E ED B8 61 85 E1 51 D4 C5 3F 7F 0C 6C C3 EE 68
        E4 44 3B D6 5C F4 13 C9 64 C3 49 3F B6 D4 60 C0
        D4 AC 6B 20 95 BE 46 62 45 FB 3E F3 22 1D 0A 2E
        3D 21 F8 B2 E3 A6 4F BB 6E 3E 61 FA 76 31 20 4E
        D6 E7 19 00 F5 8E 31 11 0E ED 97 20 10 FF 59 30
        D3 0F 97 B7 1F 10 BD AA 3A 90 07 6B A1 8C 98 7C
        CD 8C 88 87 72 EB 82 88 7A 2D 98 A9 23 EB D3 8E
        18 3E F5 2D 6C 13 B5 B8 C4 48 3A 26 96 C5 C3 B1
        45 CD 04 3B 96 4C 94 D3 FD ED E1 8D BF 4A 84 AE
        21 5B 44 62 22 1F 77 0E 22 29 DE 22 E4 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ ")n6:I6FCSTYw/yvXDw~aQ?lhD;\dI?`k FbE>".=!On>av1 N1 Y0:k|rz-#>-lH:&E;LJ![Db"w")""

[+] Synchronized Frame 29 Isolated at Symbol Offset 312040:
    ├── Extracted APID Subsystem ID : 0x1D8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D8 A2 63 A2 1F 0B 66 5A 68 FD F6 E3 86 1F C7
        72 1B 25 ED 34 B3 30 0F 35 B7 99 10 ED 59 53 C1
        0F 85 03 0D 14 FC 8D 31 51 0F DD B1 AB 20 76 BA
        59 99 07 86 D2 80 88 55 2A 9B 8E 87 A2 CB 9E D0
        7F E5 9C E0 81 E5 59 D4 D1 7F 7D 0C 4C 83 EF CC
        C4 44 3F D4 5C A2 43 C1 60 C3 45 3F 6E 54 76 C3
        F1 2C C2 6A 9D BE 06 22 61 F1 B6 62 22 1D 8E E6
        7A 21 F4 B6 21 A2 9F 1B E2 3A 21 FB 57 65 24 0E
        D6 C3 11 12 F1 BD 79 11 0E BD 97 48 90 F9 5B 32
        D3 4F FD 93 84 30 3D 2A 18 82 25 EF 25 8C 98 7C
        CB 8C 88 97 72 AB 92 88 7E 2D 18 68 87 F8 FA 8E
        98 7E 55 9D 68 53 B7 E1 CC C8 3E 66 CE 44 43 B9
        65 DD 44 3E D6 4C 14 43 E5 2D 47 44 BF 8E E6 26
        89 7B 6D 66 26 5E 53 0F 22 21 DA BA E6 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!cfZhr%405YS1Q vYU*Y}LD?\C`E?nTv,j"ab"z!!:!We$yH[2O0=*%%|r~-h~UhS>fDCeD>LC-GD&{mf&^S"!"

[+] Synchronized Frame 30 Isolated at Symbol Offset 322800:
    ├── Extracted APID Subsystem ID : 0x1F5
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F5 AA E6 8A 9E 0B 26 1A 09 DC 92 E3 F4 5F B9
        43 12 21 ED 74 B3 13 2F 19 C5 11 10 F8 59 77 81
        0F 85 B3 09 34 7E D9 79 D3 2F DD A3 81 20 76 DA
        58 88 97 AC DB 88 88 7F EE 99 AC 07 CA D9 9E 9A
        36 2D B8 E9 87 E7 58 D4 D1 3B 7F 0C 44 43 EE 6F
        C6 54 3B 94 5D F4 43 E1 6C C5 44 1F F7 DC 34 C3
        F0 2D 6A 60 B7 BF 16 22 61 FB B4 E2 22 1F 8A AE
        73 21 F0 B6 62 A4 9F 47 67 39 21 BC 54 31 30 4F
        CF 4B 19 22 F9 98 D1 11 0E 95 57 29 10 FA 59 70
        53 47 CD F7 15 32 FC 2A 18 B8 07 69 B5 0C 88 78
        ED BC 89 85 FE 89 B6 80 7C 2D 98 68 A7 F4 DB CB
        98 7E 35 8D 6D 07 B7 C0 C6 4C 3C 76 DC 64 43 B4
        45 DE 60 3F 96 4C 54 D3 F9 BD CD AC BF 52 EC A6
        89 DB E5 62 26 5F 37 EE 22 21 D8 B2 A7 B2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!&_C!t/Yw4~y/ vX6-X;DCoT;]ClD4-j`"a"s!bGg9!T10OK"W)YpSG2*ix|-h~5mL<vdCE`?LTRb&_7"!"

[+] Synchronized Frame 31 Isolated at Symbol Offset 333560:
    ├── Extracted APID Subsystem ID : 0x1D4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D4 AA EE A2 1F 2B 06 5A 49 F7 B2 B3 82 07 C1
        53 57 01 EC F4 A1 12 2F C9 A7 19 10 EA 51 31 59
        0F B5 B3 1D 24 7F 4B 51 C1 0F C2 A3 A9 02 76 FB
        18 99 87 CD AB 8C 98 76 AA BB E0 87 E2 C9 9E 82
        3E 6D D8 E9 91 F2 50 C5 D1 3F 4A 2C 44 83 E6 E5
        E4 44 3E 97 5D F0 43 F5 68 CB 4D 3F FF 5C 14 43
        F1 28 6A 64 1D B7 86 32 41 FB 36 76 22 1D CA 26
        72 21 F2 B4 61 A6 9F FB EE 38 65 EC 75 31 60 4E
        D6 43 39 30 F8 DE 71 11 0F F5 13 19 30 F9 5B 30
        53 0F 89 B5 1C 32 BE 0B 18 90 25 ED C1 8C 91 79
        C5 B8 C8 87 7A 8B 9E 88 7C 2C 98 A9 27 DE CB 8E
        98 5B 15 7D 6C 46 B7 D0 CE CC 3E E6 94 44 43 A9
        45 CF 44 3D 56 4C 34 C9 F6 FD 47 EE 0F 0E EE AE
        89 FA 78 62 26 1F 36 6A 32 21 DC AA 66 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+ZISW/Q1Y$KQvv>mP?J,DD>]ChM?\C(jd2A6v"&r!a8eu1`NC90q0[0S2%yz|,'[}lF>DCED=VL4Gxb&6j2!f"

[+] Synchronized Frame 32 Isolated at Symbol Offset 344320:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC A2 ED 80 1F 0B 46 0A 68 F5 B6 E3 A6 17 E5
        4B 52 00 ED F8 33 13 0F 99 F7 01 10 EF D1 73 01
        0F A5 33 3D 34 7E EB 79 EB 37 CA A3 8B A8 56 D8
        18 88 85 CC 89 C8 88 72 A8 BA 8C 87 CA D9 86 8A
        7F CD BC 61 95 F0 D8 D4 C1 3B 1F AC 64 C3 C7 55
        C6 44 3B 94 5C E4 43 C1 7C C1 4C BF BE DC 7C CB
        B6 A8 6A E0 BF BF 86 62 81 F7 20 63 20 15 1A 2E
        7A 21 E4 B6 61 A6 8E AF 6E 6B 64 E2 55 35 22 1E
        DF 63 19 30 FD B2 59 15 0E B5 D3 51 00 EC 59 30
        D1 4F F5 B3 04 33 FE 0B 1A E9 07 6F E1 88 99 7C
        CD 38 88 87 FE CB 9A C8 78 AD 98 69 83 82 FA CF
        99 BF 15 A8 7D 07 B4 A0 CE C8 3E FE 56 64 43 B3
        45 C7 60 3E 56 9C 76 53 FF 7D 45 6D 3F 4A C6 96
        0B DA 69 62 26 17 93 EE 22 21 D5 AA E3 02 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!FhKR3s3=4~y7Vra;dUD;\C|L|jb c .z!ankdU5"c0YQY0O3o|8xi}>VdCE`>VvS}Em?Jib&"!"

[+] Synchronized Frame 33 Isolated at Symbol Offset 355080:
    ├── Extracted APID Subsystem ID : 0x1FD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FD A6 E8 92 1F 4B 62 3A 61 E5 3A E7 84 17 81
        53 57 24 FD 76 B1 17 0F 9B 35 91 30 FF 51 31 D1
        0F 25 A3 05 14 7E DB 7D 5B 0B FC A5 89 22 56 F2
        19 99 87 8E AB C8 88 77 28 99 08 87 E2 C1 86 9A
        7F EC BC 28 83 E9 56 D4 85 3B 2D 8C EC 43 EF 64
        E4 44 3B 54 1C F4 53 D1 6C CB 4D 3E 72 CD 30 C1
        FD A8 62 62 35 8F 96 32 41 F1 B0 A3 22 1D CA 26
        FA 21 EE A2 61 A4 1F AB EE 3A 31 F9 54 A5 20 0E
        DB 43 11 12 FA 93 51 11 2E A5 57 1D 10 FC 5B 32
        D1 4E FC 93 0C 70 FC 2A 1A 98 0D 65 91 8C 81 78
        CD 18 88 87 F2 8B BE 48 7F 2D 19 E9 A7 FE DB 8F
        08 7F 35 0D 4D 13 B7 D0 C4 40 3E 76 DC 44 43 B1
        45 C7 04 3F D6 0C B4 93 FA 2D C5 4C 0F EA A4 A6
        49 F9 54 62 66 5F 33 4E 22 21 7C A2 66 32 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!Kb:a:SW$v50Q1%~}["Vw((V;-CdD;TSlM>r0bb52A"&!a:1T CQ.W[2Np*exH-5M@>vDCE?-LITbf_3N"!|f2"

[+] Synchronized Frame 34 Isolated at Symbol Offset 365840:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC B2 6B A2 1F 0B 46 1A 21 FF 16 F1 C2 5F 95
        43 59 34 E5 E4 B3 93 0F B8 97 31 40 E2 D1 72 44
        0F C5 93 3D 14 7E 9B 51 F3 0F C2 A1 0D 9A D6 FA
        18 99 85 CE EC 88 8A 77 EC 99 E8 87 D2 D9 86 9A
        3F D7 88 71 07 E1 50 94 91 3F 7C AC 44 43 E6 ED
        C4 44 3A 15 5C 72 03 E1 68 D3 49 3F F2 CE 76 C3
        F1 2C 6A 60 B5 9E 86 36 61 CD 36 E2 26 1D EA 26
        70 01 C0 B0 61 B6 9D EB AE 3B 60 F9 D6 E5 30 5F
        DC 67 11 30 F3 D7 11 11 0E FD 57 3D 10 FA 5A 30
        51 07 95 B7 95 B0 78 2B 98 9B 27 6F B1 88 90 7C
        E9 B8 88 87 FE AB 92 09 78 2C 98 69 A7 DE DA CB
        98 7E 15 1C 48 03 F3 F0 C4 4C BF A6 DC 44 C3 BD
        75 D3 64 3F 96 0C 34 D3 F7 A5 C5 C4 3F A2 C6 A2
        09 DB FD 63 26 5F 3B 6E 22 21 FF B2 22 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!kF!_CY41@rD=~Qw?qP?|DCD:\rhI?v,j`6a6&&pa;`0_g0W=Z0Qx+'o|x,i~HLDud?4?c&_;n"!""

[+] Synchronized Frame 35 Isolated at Symbol Offset 376600:
    ├── Extracted APID Subsystem ID : 0x1F6
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F6 B2 E7 20 1F 0B 26 4A 69 DD 76 E3 A6 17 A9
        53 53 00 EC 6C 31 33 0F 1D 37 19 10 EE 59 37 D0
        0F 95 B3 0D 14 FA CE 70 F1 03 42 B3 29 A0 56 58
        18 D9 97 A4 F9 88 88 7A 28 B8 C0 87 B2 D9 86 80
        7E 7D 8C F8 97 65 50 97 85 3A F9 AC F4 CB AB 69
        C4 44 3A 96 5C 54 43 D9 6C CB 4D 3F 12 46 16 43
        F8 28 CA 44 3D BE 86 66 61 F5 36 F3 22 1F CA 2E
        CA 21 F4 B6 E4 A2 8F FB 6F 2E 65 FD 52 71 34 4A
        DB CB 19 13 F8 DB 51 15 2E CD 57 2D 10 F8 53 32
        91 47 ED E1 1D B2 3C CA 18 90 27 67 8D 88 98 7C
        CC 98 88 87 66 CB 8C 48 7C 2D 98 E9 87 FE C9 C6
        8D 1E 15 0D 68 83 F4 E0 C4 40 3C 6E DC 44 43 A5
        45 CE 60 2C 36 CC 14 81 EE BD 53 5C 3F 82 96 2A
        0B DF F8 C2 26 1E B3 6E 22 21 D4 A2 67 42 1C
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "! &JivSSl137Y7pB)VXz(~}eP:iD:\TClM?FC(D=fa6".!o.eRq4JQ.W-S2G<'g|fH|-h@<nDCE`,6S\?*&n"!gB"

[+] Synchronized Frame 36 Isolated at Symbol Offset 387360:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD A2 E3 A0 1E EB 66 3A 69 F3 76 E3 D6 1F AF
        43 53 04 ED F4 B1 12 2F 7D 97 91 10 EE 51 73 D9
        0F 05 93 29 30 FE DB 31 DB 2B C2 A1 A9 92 76 FA
        18 89 17 DC CB 8C 98 77 29 99 AC 87 C6 D9 82 9B
        7F 7E AC 21 8D 41 50 94 D5 2B 1D 0C 44 83 F7 F4
        05 44 3B 15 4C 70 43 C9 6C CD 4D 3E 52 54 5C 8B
        F1 28 4A 60 1D BF 46 72 61 F3 72 A3 22 1D DA 2E
        78 21 FC B6 61 A6 9F 75 6E 3E 60 F8 34 B5 30 4E
        CB 4B 13 30 F9 97 71 11 0F D5 17 1D 30 F8 5A 30
        D9 47 FC 97 1C 94 7D 1A 32 B0 07 EF C1 99 98 7C
        CD 98 C8 87 FE CB 9E 08 79 2D 99 29 07 FE DB 8F
        48 7E 75 1D 6D 03 B5 B4 C6 44 3E 37 4C 44 43 BD
        44 D3 44 3A 16 CC 34 93 FF 6C EB 0C BF CE F6 36
        29 7B 4A 66 24 1F 33 EE 32 21 DC AA E5 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!f:ivCS/}Qs)01+vw)~!AP+DD;LpClM>RT\(J`Frar".x!aun>`40NK0q0Z0G}2|y-)H~umD>7LDCDD:4l6){Jf$32!"

[+] Synchronized Frame 37 Isolated at Symbol Offset 398120:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD A2 63 B0 1E 8B 66 1A 49 F5 3E E0 F2 1F 8D
        4E 53 25 FD A4 31 17 0E 49 47 99 10 E8 5D 77 C8
        0F 55 B3 25 20 7F 9B 79 88 07 C1 A1 AB 90 F6 D8
        58 CB 85 CC CA 8A 88 7F 68 B8 E0 87 E2 D9 8E 98
        3F AF B8 A0 87 F5 D0 D6 D1 7B 3F 2C 44 93 E6 4D
        C6 44 3B F7 5C 04 43 F9 6C C1 49 1F E6 CC 74 C0
        F0 AC 6A 48 9D BE 96 22 41 F3 B6 E3 22 1D EA 2A
        F8 41 E8 B6 63 A2 1F F5 7A 39 65 F9 F7 35 20 0A
        DE 6B 17 20 F8 9D 79 11 0E C5 17 2D B0 F8 5A 30
        D2 47 EE B7 9D 92 FC 1A B2 93 27 6B 01 9C 98 7C
        6F 9C 8A 87 76 CB 9A 48 5C 28 18 68 87 FF BF 8F
        99 5E 5D 4D 4D 93 F5 80 C4 40 3E A6 94 44 42 B9
        55 CB 00 3D 96 4C 34 D1 EF AD 47 0C 3E A2 C6 BE
        01 59 E9 66 66 5F A7 2E 22 21 F4 A2 E7 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!cfI>NS%1IG]wU% yXh?{?,DMD;\ClItjH"A"*Acz9e5 k y-Z0G'k|ovH\(h^]MM@>DBU=L4G>Yff_."!""

[+] Synchronized Frame 38 Isolated at Symbol Offset 408880:
    ├── Extracted APID Subsystem ID : 0x151
    └── Full Decoded Frame Payload Hex (223 Bytes):
        A1 51 A2 26 A2 17 4B 66 3A 20 FB 9E E3 86 57 83
        4A 53 04 FD B8 B1 10 0F 19 A7 11 10 EE 5D 37 C1
        0F AD B3 2D 14 FF DB 31 C3 0F EA 9D 09 80 76 BA
        18 E9 87 CC 99 C8 88 76 28 BB FC 87 C2 C8 96 9A
        7F 6D 9C E1 07 E0 50 D4 D1 3B 7D 0C 4C 03 E6 6D
        C4 44 3E 86 5C F4 43 E5 64 CF 4D 0F D6 DC 54 81
        DC A8 E2 60 B7 BE 84 3A 61 F3 3A E2 22 55 4B 2E
        3A 21 FC B6 63 A6 9F 9B E7 3A E1 7A 76 F5 B0 0E
        DB 4B 1B 12 FB 99 39 11 4E A5 17 2D 90 B9 5E 30
        D1 0E ED B7 1D 70 FC 6A 1A 99 2F 67 25 18 98 78
        CF B8 C8 87 52 CB 9E 10 7A AD 98 2D A1 DF 4A 8E
        58 3E E5 4C 4C 03 B2 8A C4 4C 3E E7 7C 44 43 8B
        45 C3 64 3E 76 4C F4 83 F6 6D C7 CC 3B CA 86 E6
        6B 58 88 62 66 5F 12 2E 22 21 FF B6 E7 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "Q&Kf: WJS]7-1vv(mP;}LmD>\CdMT`:a:"UK.:!c:zvK9N-^0pj/g%xRz-JX>LLL>|DCEd>vLm;kXbf_."!"

[+] Synchronized Frame 39 Isolated at Symbol Offset 419640:
    ├── Extracted APID Subsystem ID : 0x16C
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 6C B2 61 B2 1F 4B 66 1A 09 7A 7E E1 D6 1F 8D
        5B 5A 04 E5 A4 31 10 0E 1D F7 19 10 EE 51 73 18
        0F 25 A3 3D 14 F0 DB 78 73 2B DA AB 89 28 F6 FA
        1B 89 A7 A6 8B CC 88 76 2E B9 2C B7 82 D9 82 9B
        7F FD B8 A0 87 E8 D0 D5 85 2B 78 2C 64 D3 E6 E9
        C6 44 3F D4 5C F6 0B E9 6C CF 44 3F E7 DC 56 43
        E1 AC 62 60 9F 9E 4C 72 61 F1 B4 A2 22 1F 4A 26
        F8 21 DC B0 65 A6 9F F1 6E 3A 00 7A 34 35 F2 1A
        EF 43 39 20 FD 93 71 11 0E D5 17 79 80 FD 5B 30
        D3 0F F4 93 9D 90 1E 2B 18 10 87 EF F1 99 99 7C
        C9 28 88 87 5E 89 94 00 5C 2D 98 A8 A7 F2 CB 86
        9C 7D 55 8C 4C 53 F5 D0 C4 C4 3E 2E DC 64 43 C9
        45 C7 64 3F 96 C4 B4 93 FA 6D 43 4C 3F 0A E4 A4
        01 7A 70 62 64 1F 93 EE 02 21 DF A2 A3 22 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "laKfz~[Z1Qs%=xs+(v.,+x,dD?\lD?VCb`Lra"J&!en:z45C9 qy[0+|(^\-}ULS>.dCEd?mCL?zpbd!""

[+] Synchronized Frame 40 Isolated at Symbol Offset 430400:
    ├── Extracted APID Subsystem ID : 0x1D8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D8 AA E7 00 5E 4B 26 5A 21 FF 96 A3 A6 16 EB
        5A 52 04 AD A6 B3 33 0F 29 97 19 10 FA D1 71 D1
        0F 75 B3 1D 30 F9 19 50 CB 2F E6 B5 A9 02 76 B8
        18 99 87 CC 8B CC 88 76 AC A8 68 87 D2 D9 8E 88
        3F B5 B8 E9 93 E9 5A D6 D5 3B 7D 28 C4 C3 B6 41
        C4 44 39 15 5C 24 03 F9 64 C3 4C 2F 77 5C 7E C0
        F8 28 6B 6A 9F BE 06 22 21 E9 22 23 22 5D CB AE
        7A 21 70 B4 61 26 9F FB EF 0A 77 78 17 A5 32 4E
        DF 43 11 30 FA 9B 39 91 0E 3D 57 2D 10 F2 5B 30
        13 47 B9 F7 95 B0 BC 6A 1A FA 27 67 81 B9 89 7A
        E6 08 C8 87 E2 8B 92 40 7C 2C 98 29 A7 F9 D9 8E
        D8 7E 1D 1D 6C 03 B6 D0 C4 44 BF 67 9C 44 42 BB
        65 CE 04 3E 16 0C 14 D3 E2 6D C5 84 3B 26 F6 AE
        69 DB FC 63 66 1F 37 66 12 21 5D A2 E7 26 16
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!^K&Z!ZR3)qu0P/vvh?Z;}(AD9\$dL/w\~(kj"!"#"]z!pa&wx2NC09=W-[0Gj'gz@|,)~lDgDBe>m;&icf7f!]&"

[+] Synchronized Frame 41 Isolated at Symbol Offset 441160:
    ├── Extracted APID Subsystem ID : 0x1FE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FE AA 6E A2 1F AB 66 1A 68 7B B6 B3 F2 17 A7
        53 13 31 ED F4 33 51 0F DB BD 11 10 EE 51 73 38
        0F 95 A3 2D 14 7F 9B 11 53 2F F3 B9 AB 82 56 D2
        18 89 87 CC D9 88 88 74 68 B9 C8 07 D2 D9 8A 8A
        3D 05 AC E8 87 EB D0 94 91 7B 2C 0C 4C 47 F6 6D
        C4 44 3A B4 5D F5 03 E1 6D CD 4D 3F E7 DF 36 C1
        F1 AC 6A 60 15 9E 96 22 61 F1 BE E2 22 1D CB 2E
        39 21 E4 B2 61 A0 8F EB 6F 27 61 F8 16 65 61 4E
        DB E3 33 20 F9 9E 79 11 0E E5 D7 0D 10 F1 58 32
        52 46 CF 93 1D 32 FC 2B 13 98 05 6F 25 89 98 7C
        CD 38 88 87 6A E3 9E 80 58 2D 88 69 A7 CE D2 87
        88 3E 95 48 48 03 B7 D0 C6 4C 3E EF 9E 44 43 A1
        45 CF 60 3C 16 CC F4 D3 C5 6D C7 EC 2F 8A C4 26
        29 DB F0 62 04 1E BB C6 22 21 D8 A2 66 82 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!nfh{S13QQs8-S/Vth={,LGmD:]mM?6j`"a".9!ao'aeaN3 yX2RF2+o%|8jX-i>HHL>DCE`<m/&)b"!f"

[+] Synchronized Frame 42 Isolated at Symbol Offset 451920:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC BA E4 22 1F 2B 26 5A 69 FF F4 E3 F2 1F A5
        7F 46 44 FD 64 B1 32 0E 99 A3 91 10 FE 73 72 C0
        0F B5 B3 3D 10 EB D9 61 73 2B CA A5 A9 AA 52 DA
        58 99 87 DD BB 8A 88 75 28 B9 4C 87 92 C9 96 82
        7B ED BC E1 97 E7 5B 94 C1 6B 7F 0C 44 C3 C6 F9
        E4 44 3F 94 5C 67 03 D9 6C C1 49 1F AF C0 5C C2
        F0 28 6B 48 BD B2 86 22 61 F3 36 72 22 1D CB AE
        7A 21 E8 B6 65 A6 9D AB E6 1A 65 FC D4 A5 A1 4E
        C3 43 11 10 FA E9 50 91 0F F5 17 3D 10 F9 5D 30
        53 4B FD 95 04 30 7D 9A 18 92 27 4F B1 88 90 7C
        49 38 88 87 62 99 8A 80 7C A9 19 69 A7 DA 7B 8E
        98 7E 05 9D 6C 13 B5 F0 C6 4C 3F 66 D4 45 43 F9
        45 C9 48 3E 16 8C 34 93 EF 6D C3 4C 2F 02 A6 2E
        41 F9 CC 62 26 1F 32 92 22 A1 D9 A2 E7 02 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"+&ZiFDd2sr=as+RXu(L{[kDD?\glI\(kH"a6r"z!eeNCP=]0SK0}'O|I8b|i{~lL?fECEH>4mL/.Ab&2""

[+] Synchronized Frame 43 Isolated at Symbol Offset 462680:
    ├── Extracted APID Subsystem ID : 0x1F8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F8 AA E7 A0 1F 0B 66 0A 69 F8 B6 27 A6 1F 85
        47 5B 40 BC 72 33 93 2F A9 37 11 10 EE 51 37 C1
        0F E5 B3 0D 34 F8 69 71 D3 07 C3 A9 89 82 76 D2
        18 89 A7 CC DB 08 88 7F 2C B9 68 87 C2 C9 8A 8A
        3E AD 88 29 87 E0 50 C4 91 2B 39 AC D4 43 E7 69
        64 44 3B 94 4C F6 43 E1 6C CF 4D 3E 92 DC 72 41
        FB EB 6A C0 15 8E 06 22 41 E6 E4 E3 22 1D 4A 26
        AA 21 E0 B4 61 A6 9F ED E6 1C 61 FB 14 35 31 4A
        DF C3 1D 60 F9 13 31 11 2E 85 17 3D 90 B9 5B 33
        51 4F FD F3 8D 30 9C AA 92 9A 8D 6F 9F 98 91 5D
        D9 FC 89 87 5A CB BE C0 7C 2D 98 69 A7 FA DA 8E
        88 3F 35 0C 6C 17 B4 FE C4 4C BC 26 94 64 43 FB
        54 CD 44 3E 56 CD B4 D1 EE 24 E3 44 3D 02 84 B4
        09 D9 74 66 40 1F 33 4B 22 29 FC A2 EF 32 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fi'G[@r3/7Q74iqv,h>)P+9CidD;LClM>rAj"A"J&!aa51J`1.=[3QO0o]Z|-i?5lL&dCTD>V$D=tf@3K")2"

[+] Synchronized Frame 44 Isolated at Symbol Offset 473440:
    ├── Extracted APID Subsystem ID : 0x1D4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D4 A2 ED B0 1F 6B 06 1A 29 FD B6 63 A6 5F 81
        53 12 44 ED 64 73 10 0F BF 81 91 50 EC 59 75 11
        0F 85 B7 2D 14 79 CB 78 F3 87 C2 A1 2D 2A 56 7A
        98 98 07 CC BB 8C 8A 7F 3C BB EC 07 82 D9 8E 92
        7D 8C B8 EF 83 C0 D0 D5 C1 7F 39 0C E4 4B E2 E9
        E4 44 3B 96 5C F4 43 D1 6C C7 4D 3F EF 4E 50 C2
        F8 EE 6A 6A 3D B6 86 22 41 ED 34 F2 2A 1D 4A 26
        4B 41 F0 B6 60 A4 9E F1 6E 3A 28 78 16 A5 35 5A
        DE 6B 13 10 F9 9B 71 11 0E C5 97 7D 10 F4 53 30
        53 47 DD B7 2D 32 3D 9A 38 99 2F 6E C9 98 98 7C
        CF B8 C9 87 FA CB 9E 01 7D 2D B8 68 27 F2 EB 8F
        D9 1A 95 9D 48 13 B1 D0 C4 C4 BE 26 DC 44 43 B9
        7D DF 44 3E 96 CC 94 93 EF 6D 47 4D BF 9A 96 66
        49 58 F8 67 04 1F 32 6F 22 21 D3 E2 EB B2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!k)c_SDdsPYu-yx-*Vz<}9KD;\ClM?NPjj="A4*J&KA`n:(x5Zkq}S0SG-2=8/n|}-h'H&DC}D>mGMfIXg2o"!"

[+] Synchronized Frame 45 Isolated at Symbol Offset 484200:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        61 DC A2 E7 10 1E CB 66 1A 29 FA B2 B7 C6 1E 95
        67 13 44 FC F4 31 B2 0F 39 F5 09 10 FB 59 70 D1
        0F 95 93 05 30 F6 9B 31 C3 2F CA AD 89 02 77 6F
        18 8B 87 CC C2 8C 88 77 68 B8 C8 87 E2 D9 8E 98
        7F EC B8 79 83 E5 50 C4 91 3F 7D 2C C4 CB E6 75
        44 44 3A D4 DC 70 43 C9 68 CB 4D 1F 76 4C 7A C3
        F9 6E 6A E0 B7 B7 86 22 41 7F 22 E2 22 1D AA 26
        F8 E1 E0 B2 60 A2 9F CB EE 3B 61 EA D4 A5 60 0E
        DF 4B 11 12 F8 9A 31 B1 2F E5 97 3F 10 F8 DB 32
        53 4F F9 D7 0D 20 FD 4A 9A EB 8F 67 E1 9B 99 7C
        CF 98 88 87 F6 DB 9A C9 7C 2D 38 69 A7 CD EA 82
        99 76 15 2D 5C 53 B5 CA CC 4C BE 6F 5E 45 43 A9
        65 D3 64 3E 16 4C 24 43 F0 75 C5 64 0F 12 96 AE
        29 DA E1 62 66 1E 1B 6D 32 21 D0 A2 E6 B2 17
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "af)gD19Yp01/wowhyP?},uDD:pChMvLznj"A""&`;a`K1/?2SO Jg||-8iv-\SLo^ECed>L$Cud)bfm2!"

[+] Synchronized Frame 46 Isolated at Symbol Offset 494960:
    ├── Extracted APID Subsystem ID : 0x1FE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FE AA E7 82 1D 6B 46 3A 21 FD BA E3 E6 16 85
        4F 52 15 FC F4 33 30 0F 19 AB 19 10 EA 55 77 CD
        0F 85 83 0D 34 FC C9 75 D3 3B E3 A3 2D AA 56 FB
        58 C9 87 CC D3 C0 88 75 28 99 E8 87 F6 D9 82 9A
        7E E4 A8 2D C5 F9 D3 94 88 3B 69 2C 4C 03 E6 7D
        66 44 3E B5 1C 84 43 E1 64 47 41 3E E6 DC 14 C2
        F4 A8 4B EA 9D BE 86 32 45 EF 3E 42 22 1D 5A 26
        5B 01 F4 B6 61 A4 1F FB 65 BA 61 7C 52 35 B0 0B
        DF 43 31 30 FD 9B 31 51 0E E5 17 6D 10 F9 5B 30
        D3 4F FD F7 0D 30 FC 3A 1A D0 2F 2D B1 88 99 1D
        CD 38 9A A7 42 8B 9A 00 7B 2C 99 69 87 DA CB C7
        98 7E 55 5D 4C 17 B7 B0 C6 44 38 E4 DE 44 43 F9
        45 C3 40 3E 16 CC 74 53 FF 75 E7 8C 3F 4A A6 2E
        C9 D9 C9 E6 22 1F 33 E6 22 21 DC AA EE B0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!kF:!OR30Uw4u;-VXu(~-;i,L}fD>CdGA>K2E>B"Z&[aea|R5C101Qm[0O0:/-8B{,i~U]LD8DCE@>tSu?J."3"!"

[+] Synchronized Frame 47 Isolated at Symbol Offset 505720:
    ├── Extracted APID Subsystem ID : 0x1FD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FD A2 E7 A2 1F 2B 66 3A 68 FF 96 D3 A2 5F A1
        43 5F 00 BD 74 31 81 0F 3F D7 91 10 EE 51 77 90
        0F 85 93 15 24 FF DB 79 73 47 D0 A9 A9 22 7E FB
        18 88 87 CC D3 88 88 76 A8 B9 69 87 96 D9 82 92
        7F DD B8 E1 AB E1 40 D4 85 3F 3D 8C 4C 43 EE 6D
        C4 44 3B D6 4D 64 43 E1 6C C3 49 3F F3 DE 3C C3
        7A AC 62 E8 BD 9E D6 26 65 F3 24 E2 22 1F CA 2E
        4B 01 F0 B6 61 A2 9F BD EE 2E 60 F8 14 F5 70 4F
        CF 4F 11 20 FD BF 51 91 4F D5 13 2C 20 F8 5B 33
        D1 47 EF 97 9F 32 1C AA DA B8 27 67 A1 88 81 78
        CE 18 88 87 7E 89 AA 88 7B AD 98 69 B7 E2 DB 86
        88 7E 15 1C 4C 06 B3 D0 C4 CC 3E EE 5E 44 4B FA
        44 C2 C5 3C 56 8C 14 D3 F0 3D 21 48 3F 2E B6 B6
        23 FA 7D 66 A2 1E 34 67 32 21 DC A2 ED 90 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+f:h_C_t1?Qw$ysG"~vi@?=LCmD;MdClI?<zb&e$".Ka.`pOO QO, [3G2'gx~{i~L>^DKD<V=!H?.#}f4g2!"

[+] Synchronized Frame 48 Isolated at Symbol Offset 516480:
    ├── Extracted APID Subsystem ID : 0x1D9
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D9 A2 6F A2 1F 2B 26 1A 21 FC 76 B0 A7 47 B1
        4A 5B 54 AD AC 33 51 2F 19 B7 09 10 FD D1 15 10
        0F 15 93 1D 14 FF 5B 50 E1 03 C2 B9 AD 92 76 7C
        18 89 87 E5 9B 88 88 76 68 B9 68 87 C2 C9 82 92
        3F F6 BC F1 85 F0 50 D7 81 7B 7D 8C 44 CA D2 ED
        C6 44 3A D4 4C E4 43 F5 6C C3 4D 1B DE DC 70 43
        F1 AC 63 60 1F 9F 06 22 21 63 3A F3 22 1F CA AE
        B8 21 F8 B6 65 A2 0F 6F 6F 3F 61 FA 74 75 23 4E
        DB 63 1B 32 FA 9F 31 11 0F ED B7 7D 10 FB 5B 33
        51 4F B8 B5 1D B2 7C 3B 38 98 8D EB B1 88 A0 78
        C9 BC 88 87 D2 AB A8 80 7D AD 98 69 27 BE 49 CF
        D9 7E 75 0D 6C 82 B7 BA C4 4C 3E 64 4C 64 43 B9
        55 CB 44 3D 56 0C F4 51 FB 7D 47 2C AF 1E 96 AE
        69 F9 FC 62 20 1F 3F EA 32 21 DC A2 E6 22 17
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!o+&!vGJ[T3Q/[Pv|vhh?P{}DD:LClMpCc`"!c:"!eoo?atu#Nc21}[3QO|;8x}i'I~ulL>dLdCUD=VQ}G,ib ?2!""

[+] Synchronized Frame 49 Isolated at Symbol Offset 527240:
    ├── Extracted APID Subsystem ID : 0x1FE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FE A2 6E E2 1E 2B 46 0A 69 EF 7E AB 96 13 E7
        52 57 10 FD 6C B3 12 2F 19 B3 91 10 E6 59 32 41
        6F 95 B3 19 24 FB DB 78 C3 87 FD B1 0B 9A F6 FE
        78 D9 87 D4 F3 8C 88 77 28 9B A8 87 C2 D1 8E 8A
        3F ED 98 BD 97 E2 D5 94 C1 3B 3F 2C EC C3 F7 ED
        C4 44 3B 7D 4D 70 43 C9 68 C1 4D 1F 72 5C 77 C0
        F1 E9 42 68 9D AE C6 62 61 F3 36 E3 22 1D 4A AE
        6A 21 F2 B2 61 A6 8F DB 66 1E 20 B8 56 B5 E0 4E
        CF 43 11 00 F9 BD 71 11 0E A5 D7 39 10 F2 59 31
        D3 2F F5 F7 1C 14 7E 4B 1A 98 27 6F F1 9C 80 78
        6D 3C C8 A7 76 8B 9E 18 7C A9 98 69 A7 FE DA 8A
        58 3F 3D 49 4C 57 E7 92 C6 44 BC 74 94 44 43 BD
        44 CD C0 3C 16 CC 54 83 FB 6D C6 EC 1F 1E BE A6
        A9 EA 69 62 26 5F 17 6E 32 21 FD A2 EC 02 1C
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!n+Fi~RWl/Y2Ao$xxw(?;?,D;}MpChMr\wBhba6"Jj!af VNCq9Y1/~K'oxm<v|iX?=ILWDtDCD<Tmib&_n2!"

[+] Synchronized Frame 50 Isolated at Symbol Offset 538000:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC A2 E5 A2 1E 4B 46 0A 49 D5 F6 33 A2 1D 2D
        42 7A 24 AC 34 B3 92 0F 08 8D 91 10 FF 51 77 90
        0F C5 B3 05 34 FD 79 71 D3 0B C3 B1 29 80 7E 7A
        19 99 07 CE D3 88 88 75 2A 9B 4C 87 D2 B9 96 8A
        7F 6D 9A F9 85 E5 58 D5 DD 3B 7D 8C 44 C3 E6 75
        C4 44 3A 94 5C 66 03 E1 69 C3 4C BF CA 5C 50 43
        F8 AC EA E0 1D B6 06 32 05 F3 B2 E3 2A 1C CE AA
        7A 09 E4 B8 65 A2 CF 7B 6E 3B 29 DE 54 35 76 0E
        DA EB 31 30 F0 93 71 11 0E A5 D7 14 14 F8 59 32
        D3 47 ED 95 44 A0 BF 2A 92 DB 0F 6F BB 1C 99 7E
        AA 28 C8 87 72 8B 9F C8 7C 2C 98 69 A7 F7 DB 8B
        98 7E 05 0D 6C 12 B7 92 85 4D 3D 2E CC 44 43 BD
        45 CA 40 3F 96 CC 36 53 F7 7D 47 4C 3F 0A D4 A6
        49 7A FD 66 22 1F 13 EC 32 21 FD A2 EE B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!KFI3-Bz$4Qw4yq)~zu*LmX;}DuD:\fiL\PC2*ze{n;)T5v10qY2GD*o~(r|,i~lM=.DCE@?6S}GL?Izf"2!"

[+] Synchronized Frame 51 Isolated at Symbol Offset 548760:
    ├── Extracted APID Subsystem ID : 0x1FA
    └── Full Decoded Frame Payload Hex (223 Bytes):
        61 FA A2 EF 22 1F 0B 46 1A 41 FE BA E3 E2 0F E5
        6F 13 00 A5 66 33 83 0F 3D 37 01 10 EF 51 30 D1
        0F 85 A3 3D 14 F9 5F F8 DB 0F C2 B5 A9 8A F6 7E
        59 C9 87 8F F2 88 80 7C 2C B9 E8 87 E2 D1 82 9A
        7D 1E BC E1 97 71 50 D5 C1 3B 0D 2C C0 07 E6 47
        66 44 3D 95 5C 94 43 E1 60 C1 49 3A 6F DC 74 43
        F0 A8 42 66 95 BF 96 64 4D C3 B6 E2 2A 1F EA 26
        3B 29 F0 B6 61 A6 97 DB 62 38 64 E8 55 21 30 4E
        4B 23 31 20 F8 B1 39 91 0E C5 87 05 00 FA 5B 10
        D1 4F FC 31 97 B2 FD 2A 18 D8 25 6F 81 88 90 7D
        CD B8 88 85 FE AB 96 E0 7C AD 99 29 27 F8 4B 83
        98 3E 15 39 4D C3 B3 98 C4 4C 3E E6 54 44 43 A1
        45 CF 04 3E D6 8C 74 83 E3 7D E5 4F 3F 2E 86 26
        0B 5A 5C 62 62 1F 3F 05 22 21 DC E2 E3 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "a"FAof3=7Q0=_~Y|,}qP;,GfD=\C`I:otCBfdM*&;)ab8dU!0NK#1 9[O1*%o}|)'K>9ML>TDCE>t}O?.&Z\bb?"!"

[+] Synchronized Frame 52 Isolated at Symbol Offset 559520:
    ├── Extracted APID Subsystem ID : 0x1D9
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D9 B2 E2 22 1F 0B 66 1A 69 FD B2 F3 D6 1F A3
        43 53 24 ED F2 33 33 5F 0F 37 11 00 ED 55 55 D1
        0F 45 B3 3D 24 7E 89 31 DA 09 C6 AB 29 02 56 D6
        78 A9 87 ED DB 88 80 77 68 B9 E8 07 BA D9 86 9A
        76 5D B8 65 87 F1 44 D5 C1 3B FC 2C 6C CB E2 4D
        66 44 3B D4 5D E5 0B E1 78 C3 4D 3F DE CC 76 E3
        F2 EA 52 EA 3F AE 96 66 61 FB 32 F2 22 1D CA 8E
        FA 01 F4 B4 E3 A2 0F BD EA 3F 25 78 D4 B1 70 0E
        D7 43 19 31 FD BB 51 11 0E B5 53 3D 00 F8 5A 30
        D3 47 F9 F7 1C 34 F8 2A 13 9A 2F 6F A1 8C 88 7C
        CB B0 09 8F 4A 8B B6 80 7C 2D 98 69 A3 FC DB CE
        18 5F 14 6C 58 93 B2 D0 C6 44 BF 7D 14 64 03 A9
        F4 CC 24 3E 16 CC 14 93 EF 6C E7 4C 1F 8E 94 B4
        29 FB E8 62 26 1F 19 6E 32 21 F6 32 E3 2A 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"fiCS$33_7UUE=$~1)Vxwhv]eD;,lMfD;]xM?vR?fa2"?%xpC1QS=Z0G4*/o|J|-i_lXD}d$>lL)b&n2!2*"

[+] Synchronized Frame 53 Isolated at Symbol Offset 570280:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DF A2 E7 02 1F 0B 66 0A 61 FF 16 63 E6 1F ED
        46 53 04 ED FC B3 90 2F 4B B7 91 30 FE 59 33 10
        0F 35 A3 05 34 FB D9 71 D3 2F CF A1 8D 02 76 DB
        18 A9 07 CC 98 88 88 76 EC 99 28 05 F2 C9 96 98
        3F ED BC AD 87 E3 50 C4 C1 3F 2C 1C 64 C3 EB 49
        E6 4C 39 74 4C 56 43 EB 6C C3 4D 3F B6 5C 18 43
        F6 AE 68 4C 9D AE C6 62 21 EB 26 B2 22 1D CB 2E
        EE 21 F3 B4 60 A2 8F FB 2E 1B 41 78 14 65 36 0F
        D6 43 19 30 F9 BB 79 91 0A A5 17 1C 90 F8 5B 32
        D3 4F AD B5 0E 30 FC 2B 1A 98 A7 EF F5 8C 90 7D
        ED 18 8A 07 86 89 9E 08 7C 2D 99 E9 A7 E2 D9 82
        98 1E 75 19 4C 97 B2 D0 D6 44 3E 6E 4E 64 43 B9
        65 C5 20 3E 16 4C 94 C3 EE 64 C7 4C 3C 9A E6 86
        C3 DA 69 63 24 1E 32 6E 22 61 D0 A2 EF 00 1D
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!facFS/K0Y354q/vv(?P?,dIL9tLVClM?\ChLb!&".!`.Axe6C0y[2O0+}|-uLD>nNdCe >LdL<ic$2n"a"

[+] Synchronized Frame 54 Isolated at Symbol Offset 581040:
    ├── Extracted APID Subsystem ID : 0x1D5
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D5 A2 EF A0 1F 0B 46 62 09 7F 92 33 A2 1F 8F
        4A 56 11 AD 76 31 11 0F 9B B7 11 10 BF 51 77 91
        0F 05 83 0D 24 7B DB 71 C3 23 E5 B5 21 CA F4 9D
        18 89 87 5C FA C0 88 75 6A B9 E8 87 E2 D9 A2 8A
        7E ED A9 E5 87 CA 50 94 99 3B 6D 2C 4C C3 C3 48
        CC 4C 39 14 5C 94 43 ED 64 CF 4C 3F FE D0 32 41
        FC E9 62 26 1D B7 86 22 41 EB 30 63 22 1D 82 2E
        FB 01 F0 B6 64 A2 8F 23 6A 3A 21 F8 54 B5 34 5E
        CF 0B 13 12 F5 D7 51 31 0E C5 17 39 62 F8 59 32
        D1 4F F3 B5 1B 10 FC 2A 18 B9 25 61 91 BD 18 7D
        CC A8 08 87 72 8A 9C 88 7D 2D 98 69 A7 FE FB 8F
        D8 5E D5 4D 6C 13 97 A2 C4 4C 3E 76 1C 64 43 B9
        65 4D 40 3E 56 4C 34 D1 F3 6D 41 6C 3F 2A 96 A6
        09 DB A8 63 20 1F 32 EE 32 21 DF A2 E6 A0 17
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!Fb3JVv1Qw${q#!\uj~P;m,LHL9\CdL?2Ab&"A0c".d#j:!T4^Q19bY2O*%a}r}-i^MlL>vdCeM@>VL4mAl?*c 22!"

[+] Synchronized Frame 55 Isolated at Symbol Offset 591800:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC EE EF 22 1F 8B 22 3A 61 FF B2 E3 E6 0F BD
        33 5B 04 FE F6 31 13 0F 99 97 11 12 EC 55 31 91
        0F 95 93 01 00 FF FB 30 D3 07 C3 B1 8F A2 FE 72
        18 89 97 8C 99 A8 88 77 E8 A9 E0 87 AA D9 86 80
        7F BD 88 6D 85 E3 50 D6 C9 3B 3C 2C 44 43 EF 09
        44 44 3B 95 4C D4 43 F1 60 C3 49 3F FE CE 14 C1
        F6 A8 4A 48 BF 85 06 66 61 FB AC A2 22 1D FA 2E
        78 21 E2 B2 65 A4 9F FB AE 39 65 F8 56 B5 F4 4E
        C7 A3 11 20 F9 BA 71 51 0F F5 13 31 10 F2 5B 32
        53 0F D8 B3 1D 30 FD 2A B0 90 A5 EF A1 08 98 7D
        4C 98 88 87 62 8B 9A 08 7C 2D 18 E8 83 D3 DF 8F
        98 3F 15 3D 58 13 B7 D2 C4 4C BC 76 D4 64 43 A9
        65 CB 44 3E 54 CC 74 13 FF 6D E0 68 3F DA A6 A6
        89 DB 69 62 26 5F 73 8F 32 21 DC AA A7 B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"":a3[1U10rwmP;<,DCDD;LC`I?JHfa".x!e9eVN qQ1[2S0*}Lb|-?=XLvdCeD>Ttmh?ib&_s2!"

[+] Synchronized Frame 56 Isolated at Symbol Offset 602560:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 E7 82 1F 0B E2 1A 69 F8 76 E3 E6 4F 81
        73 53 14 E5 AE B5 11 0F 19 B7 11 10 EE 55 73 89
        0F E5 93 05 14 7A 7B 30 F3 2F C1 89 89 92 56 9F
        18 D1 97 FE DB C8 88 76 28 B9 28 87 DA C9 8E 9A
        7F EF A8 EC 87 E6 D8 97 C0 7F 7F 0C E4 4B E7 69
        C4 44 3A 64 5C 75 43 E5 69 CF 44 3F DE D4 54 C3
        F1 A9 6A 48 9F BE 06 32 01 F7 22 E2 22 1D CA 26
        58 05 D0 B6 61 A0 8F AF AE 18 61 7C 54 A5 30 5F
        D3 03 31 20 F1 D1 71 11 0E DD 17 3E 00 F2 5A 30
        D3 4F F1 D7 1D 32 70 2A 1A BA 05 6D A1 98 98 7C
        DE B9 C8 87 C2 89 9C 08 7B 2C 98 69 A7 F6 FB 8E
        19 7E 05 09 4D 53 B3 FA CE 4C 3C A4 AC 64 43 A9
        65 D7 64 3E 56 0C D4 81 F6 6D C7 E4 AF 1A 9E A6
        0B 7E ED 62 20 1E 73 4F 22 21 DE AA EF C2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!ivOsSUsz{0/Vv((KiD:d\uCiD?TjH2""&Xaa|T0_1 q>Z0O2p*m|{,i~MSL<dCed>Vm~b sO"!"

[+] Synchronized Frame 57 Isolated at Symbol Offset 613320:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC BA EF B2 5E 0B E6 4A 09 7D B6 E3 B6 1F D7
        43 57 15 ED F0 31 12 0F 4D B6 11 10 F8 51 73 C1
        0F 85 83 05 34 FB 7F 11 51 4F E2 A3 A9 12 76 B2
        59 99 07 CC FB 88 88 7F AF B9 AC 07 C2 D1 86 92
        3D 7D 98 E1 87 E7 54 D4 C0 2B 3B AC C4 C3 C2 7C
        64 44 3B F7 1C F4 43 E1 6C CB 48 3F B7 C6 74 C1
        F2 AA EB 60 14 BC 96 60 A1 F3 32 E2 22 1F AA AE
        A8 21 F8 B2 60 A6 9F F9 8D 0A 61 B9 35 31 31 5E
        CC 03 13 30 F9 94 79 91 2F F5 17 39 00 FC 58 30
        D1 6F BD F3 9C 10 3D 4A 12 D0 2F 65 A5 8C 98 7C
        4F 3C 88 87 52 AB 8E 88 7C 2D 19 69 27 FE 89 CE
        1B 78 35 88 68 12 B6 80 C4 4C 3E 66 5C 44 43 BD
        C5 CC 04 3C 56 CC 94 51 FE E5 E3 4C 1F 0A 96 A6
        09 DB F1 62 22 9F 33 0E 22 21 DE B2 AD A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!^J}CW1MQs4QOvY=}T+;|dD;ClH?t``2"!`a511^0y/9X0o=J/e|O<R|-i'x5hL>f\DC<VQLb"3"!"

[+] Synchronized Frame 58 Isolated at Symbol Offset 624080:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC B0 E9 A2 1E 8B 66 3A 48 FC F6 F2 A6 1F C7
        43 53 34 ED 70 31 91 0F B9 B1 11 10 AA D9 11 90
        0F 45 B3 0D B4 EF DF 10 F3 05 C0 A5 8E 8A F4 5B
        58 89 95 CC FA 88 89 77 A8 98 C8 87 E2 D9 9A 90
        7E E4 B8 35 95 4D D8 D4 C4 2B 0D 2C E4 43 AE 6D
        E6 44 3B 35 5C D6 43 E1 6C C3 4D 3F E2 5C 74 61
        D8 2E 6A 40 97 8E 86 22 61 F7 42 22 A2 1D FA 26
        7B 21 F0 B6 61 A4 17 F3 AF 2A 65 78 54 35 A1 0E
        CF 43 1A 31 FB 99 31 11 0F 95 17 11 90 F0 5B 33
        D2 47 84 17 0D 30 BE 2B 10 92 27 CD 35 9C 98 79
        FD 98 88 87 72 8B BE C8 7D 2D 98 29 87 FD DB CE
        19 3F 05 2C 68 13 B7 D0 C6 48 BC 24 D5 64 43 FB
        55 CC 44 3E 16 CC 34 D3 BA BD C7 4C AF C6 84 A6
        8B DA E9 62 64 5E B6 2A 22 21 DC AA 63 82 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!f:HCS4p1E[Xw~5M+,CmD;5\ClM?\ta.j@"aB"&{!a*exT5C11[3G0+'5yr}-)?,hH$dCUD>4Lbd^*"!c"

[+] Synchronized Frame 59 Isolated at Symbol Offset 634840:
    ├── Extracted APID Subsystem ID : 0x1D8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D8 BA 27 B0 1F 8B 66 1A 48 FE 76 E3 F6 1F CD
        13 57 04 FD 74 31 13 0F 9B 33 99 10 EA 51 76 C9
        0F 85 83 2D 14 FF DD 71 D3 07 42 A9 A9 A2 D6 FA
        18 88 87 D6 93 C8 88 77 68 B8 40 87 C2 D1 82 9A
        7F AC B8 A1 91 E1 57 94 80 3B 7D 08 64 03 EE 69
        C6 44 3D 97 4D D4 43 E1 68 D3 4D 1F F6 C6 1C 43
        E2 AE 4A 64 9F B6 86 26 61 D3 3F B2 22 1D EA 2E
        6A 01 E6 B2 65 A6 8F BF 3E 3B 21 D9 96 A5 21 4E
        DE 6B 11 30 F8 9B 51 11 0F FD 93 7D 90 F8 5A 32
        D3 4F FF B7 8C B0 FE EB 98 BA A5 CB A1 89 98 78
        EC 18 C8 87 7A 8B 96 20 7F AC 98 E9 23 E6 DB 8A
        98 7E 15 9C 4D 13 F7 80 C4 C0 3E 7D DC 4C 43 9F
        64 C9 60 3C D6 CC 74 03 F7 6D 47 CC 1F 1A A6 36
        E9 5A C4 62 24 1F 2B 46 32 21 D4 A2 E5 B0 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!'fHvWt13Qv-qBwh@W;}diD=MChMCJd&a?".je>;!!Nk0Q}Z2Oxz #~M>}LCd`<tmG6Zb$+F2!"

[+] Synchronized Frame 60 Isolated at Symbol Offset 645600:
    ├── Extracted APID Subsystem ID : 0x154
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 54 A0 67 22 1C 0A 66 4A 61 FF 52 E0 E2 57 87
        43 53 74 ED A4 B1 10 2F F9 F3 19 10 E8 51 73 8B
        4F F5 93 29 14 77 FB 78 D3 0D E4 AF A9 A0 76 BA
        58 C8 07 8D DA C8 88 7F 28 B8 E8 87 C2 D9 92 9A
        3F F5 88 E9 95 E7 59 D4 D1 3F 6E 2C 44 C3 AE 4C
        C4 44 3A 95 4C E2 43 F9 64 C3 4C 3E BB 8C 74 C2
        F0 2F 62 6C 9D A4 C6 72 41 FF B4 A3 2A 1D 2A AE
        82 21 F0 B4 65 A6 9F CB EE 3A 21 F8 56 35 64 5E
        D7 4B 11 30 FE BB 71 91 0F E5 97 11 10 F0 5A 31
        D3 47 D7 97 8F 30 9D 4A 1A 98 2F 67 B5 88 88 7C
        EF A8 C8 87 F2 AB AF C8 7A 2C 99 68 27 FE 49 8B
        D8 7F 3D 5C 48 13 B3 D0 C6 4C 3F 65 9C 54 43 A9
        65 C7 24 3D D6 4C 74 43 F9 A5 C7 64 BB 0A CE 24
        01 FB 60 62 26 1F 1B 6E 22 21 D4 A2 EF B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!Tg"fJaRWCSt/QsO)wxvX(?Y?n,DLD:LCdL>t/blrA**!e:!V5d^K0qZ1G0J/g|z,h'I=\HL?eTCe$=LtCd$`b&n"!"

[+] Synchronized Frame 61 Isolated at Symbol Offset 656360:
    ├── Extracted APID Subsystem ID : 0x1D9
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D9 AA 67 02 1F 6B 66 0A 49 7A D6 63 A6 5F ED
        43 51 44 ED E0 31 13 2F 9B B6 11 10 FF 51 73 51
        0F 05 B3 2D 20 79 DD 71 D3 0F FA BB A9 92 FE 5B
        19 88 87 CC F9 8C 88 74 AC BA 28 87 D2 CB 96 9A
        7D EF B8 E1 A7 EA 50 DC C1 39 7D AD 44 83 EE 4A
        84 44 3B 14 5C F4 43 E5 6C C1 49 3B F2 D6 5E C9
        F2 2C 62 60 BD 9C 86 32 61 F3 26 E3 22 15 DA 26
        D2 21 E8 B6 63 A4 8F C5 60 18 21 FA 76 77 34 4B
        D1 43 11 12 FF 99 11 11 0E E5 17 3D 00 F2 5F 30
        53 0E DD B3 95 30 FD BB 18 91 0F 6D A1 8C 99 7C
        49 BC 88 87 72 8B B0 80 7D AD 98 29 A7 F7 D9 CF
        D9 7F 35 0D 6C 02 B7 C0 C4 CC 3F 6C 7C 44 43 BB
        45 CD 64 3F 96 CC 34 43 F6 ED C5 4D 2F 1A AE 2C
        09 DB CC 67 26 1F 17 62 22 21 DC BA 67 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!gkfIzc_CQD1/QsQ- yq[t(}P9}DJD;\ClI;^,b`2a&"&!c`!vw4KC=_0S0m|Ir})5l?l|DCEd?4CM/,g&b"!g""

[+] Synchronized Frame 62 Isolated at Symbol Offset 667120:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 DE A2 E5 A2 1F 0B 46 1A 69 F5 96 E3 96 1F C7
        43 12 00 ED B4 33 13 2F 59 23 11 30 FF 51 35 D9
        0F 85 93 0D 34 FF CB 51 F3 0F CA B1 29 92 76 DA
        58 C9 87 EE CB C8 88 7D AC B9 E0 87 E2 D1 9E 98
        7D A5 8C E9 83 E8 5A D4 81 2F 7D 8D 44 83 D3 7D
        C6 44 3B 16 5C A1 43 E9 64 C3 4D 3F B7 4E 56 C2
        F0 A8 CA E8 9F 96 86 22 21 F3 BE C6 22 1D 8A 2E
        B2 21 F4 B6 63 A4 9F 7B 2A 22 21 FE 75 35 32 4E
        DF 63 1B 00 F0 8F 71 90 0E E5 93 1D 10 FC 5B 31
        D3 4F FB 95 1C 10 7C 3A 12 B8 07 6D 91 9C 89 78
        C9 A8 88 87 76 AB AF 88 7C 2F 98 69 A7 CF DB 8F
        18 BF 15 0D 4C D2 B3 90 C4 4C 3E 67 DC 64 43 FB
        55 CB 44 3E 16 DC 54 C3 F7 2D E1 2C 1F 26 8E AE
        09 7A E9 62 22 1E 53 EF 2A 21 F8 A2 E7 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "FiC3/Y#0Q54Q)vX}}Z/}D}D;\CdM?NV"!".!c{*"!u52Ncq[1O|:mxv|/iLL>gdCUD>T-,&zb"S*!"

[+] Synchronized Frame 63 Isolated at Symbol Offset 677880:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE A2 EF A2 1E 0B 66 3A 69 FF 96 E3 A6 0D 95
        53 52 01 ED 64 31 17 0F 5D B7 19 10 EA 51 71 41
        0F E5 93 1D 30 73 DF 11 E3 0F DD A1 29 22 76 F1
        18 C9 87 C4 CB C8 A8 77 2C B8 E8 87 E2 F9 92 92
        77 EC B8 BB 92 E1 54 8C C1 3F 6D 8C C4 43 EA 6D
        C6 44 3B B6 5C E4 43 E9 6C CF 4C 1E EE DC 24 41
        F4 A8 6B 60 9D 8C C6 32 41 E1 7C B0 26 1F 4A AE
        6A 61 F4 B6 61 A4 9F 63 6F 38 65 FA D4 35 34 4A
        C7 63 11 21 FD 9B 73 11 0E E5 B3 37 90 F9 5A 30
        93 4F FD B7 3C 30 FD 6A 3A 98 2F EB 21 89 89 7C
        4F 34 08 87 52 C9 8E 80 7D 2C 18 29 A7 E6 D9 CA
        D8 5F 3D 29 4C 12 B7 90 C4 04 3D 66 9C 44 43 E1
        65 CE 64 3E 56 CC 34 C3 FF 64 47 CC EF EA BE A6
        8B 5B EC E6 26 1F B3 EA 32 21 FD A2 E6 12 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!f:iSRd1]QqA0s)"vw,wT?mCmD;\ClL$Ak`2A|&Jjaaco8e54Jc!s7Z0O<0j:/!|O4R},)_=)L=fDCed>V4dG[&2!"

[+] Synchronized Frame 64 Isolated at Symbol Offset 688640:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 E3 A2 1E 0B 46 5A 29 F7 96 73 AA 1F 67
        43 1B 00 EC 30 31 91 0F A9 95 19 10 E8 55 31 F1
        0F D5 B3 05 A4 FB DF 59 62 25 C7 A1 0D 80 FE FA
        18 D9 87 9C DA 88 88 74 28 99 E8 87 BA D9 8E 82
        7D 0D B8 FD 97 EE 53 84 CD 3B 7E 8C 44 82 B6 79
        E6 44 3B B5 4C D5 43 E1 60 C7 4D 3E D6 5E 7E C3
        FA A8 6A 40 35 97 96 32 45 E3 34 62 22 1F EA AE
        1A 21 E6 B4 61 A6 07 EB 66 3A 25 78 54 75 20 4A
        C3 A3 31 12 F8 BD 79 91 0E AD 57 31 00 F9 5B 30
        D3 47 B5 97 15 30 FC 2B 92 98 87 CD A1 88 98 7C
        E9 98 C8 87 72 8B 8A 80 7C 28 98 68 87 CB CA C2
        81 3F 1C 4C 49 13 B0 A4 C4 4C 7E F4 8C 64 43 A9
        45 CE 0C 3D 57 CC 56 03 EF 2D E1 4C 2F 4A 84 B6
        29 58 E8 62 64 1F 16 2A B6 21 D4 BA E7 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!FZ)sgC01U1Yb%t(}S;~DyD;LC`M>^~j@52E4b"!af:%xTu J1yW1[0G0+|r|(h?LIL~dCE=WV-L/J)Xbd*!"

[+] Synchronized Frame 65 Isolated at Symbol Offset 699400:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC AA E7 A0 1E 6B E6 2A 61 F3 36 E2 A2 5F 81
        73 5E 14 FD 62 33 31 2F 1D 97 11 00 EA 5D 71 93
        0F 15 A3 2D 94 7E 0B 71 F7 07 E0 A5 A9 80 F6 38
        18 89 97 8C 9B C8 88 7E 28 BB A0 87 D2 D9 82 92
        7F 8D B8 E9 87 78 54 D6 C0 7B 4F 8C 45 03 EE 7C
        46 44 3B B6 5C D6 43 E1 64 C7 48 3F D6 54 74 C7
        F0 2E 42 68 BF AC 86 26 61 F1 36 E2 22 1D 0E 2E
        6A 25 F8 B0 64 A4 1F D5 EA 3A 61 7A D4 25 74 0A
        DF 63 11 30 F8 99 28 11 0F ED 17 50 10 F8 5A 30
        D3 47 FF D7 1D 30 FC AB 1A D9 07 2F E5 98 91 7C
        EF BC C8 87 D2 AB BC 80 7C 2C 18 69 A3 5B D9 C6
        98 5E 5D 3D 5C 12 F6 F2 CE 4C 3E 9C DC 44 43 FD
        54 CE 04 3F 16 CC B4 51 F5 65 41 A0 2F 8A 8E B2
        4B CA E9 62 22 1F D3 2E 22 01 D4 AA E5 22 16
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!k*a6_s^b31/]q-~q8~(xT{OE|FD;\CdH?Tt.Bh&a6".j%d:az%tc0(PZ0G0/||,i[^]=\L>DCT?QeA/Kb"."""

[+] Synchronized Frame 66 Isolated at Symbol Offset 710160:
    ├── Extracted APID Subsystem ID : 0x1FE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FE AA E3 A2 1E DB 66 1A 08 FF B2 63 A6 1F B7
        52 53 01 AD F6 31 32 2F 9F BF 01 50 F9 51 57 19
        0E 95 B1 15 20 FF 7D 32 73 2F E2 A1 AD 80 5E 7F
        18 D9 87 BC FB C8 88 77 68 B9 60 07 FA C9 96 88
        7D E7 D8 ED 87 E3 59 C5 C9 3B 3D 0C 44 DB C6 E5
        C4 44 3E D4 5C C4 43 E1 6C C3 49 3F B6 5C 74 C3
        F3 E8 4F 60 15 AE 86 62 61 E1 B6 E2 22 5D BB 2E
        FB 01 E8 B6 64 A0 9F BD 7F 2D 64 F8 54 35 31 1B
        D7 43 11 00 F7 BA 71 11 0B E5 97 31 10 F8 5B 32
        D2 4F FD 93 0D 30 B5 2B 38 99 25 E7 B7 8C 90 7C
        4D B8 98 87 52 8A AE C9 78 2D 98 E9 A7 EF DB 8E
        88 3F 15 19 4C 43 B7 D0 C4 CC 3C 7C DE 44 43 BB
        45 CF 44 3E D6 CC 34 D3 FB 25 E5 A4 3B 1A 8E A4
        49 DA B8 62 A6 1E 3A FB 62 21 D5 A2 67 60 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fcRS12/PQW }2s/^wh`}Y;=DD>\ClI?\tO`ba"].d-dT51Cq1[2O0+8%|MRx-?LC<|DCED>4%;Ib:b!g`"

[+] Synchronized Frame 67 Isolated at Symbol Offset 720920:
    ├── Extracted APID Subsystem ID : 0x1F4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 F4 AA E5 B2 1F 2B 46 1A 09 FE B2 A3 B6 3F C5
        73 53 44 AC E4 31 93 6F 1D 17 11 50 EA D5 73 41
        0E B5 A3 0D 30 FB 5F 70 3F 0F F2 A1 09 A8 76 BA
        18 89 97 DE D9 88 88 7F AE B9 68 85 C2 D9 9E 9A
        7C FD BC E0 87 E1 D3 C4 C9 6B 3C 0C 6C C3 C6 EC
        54 C4 3B D4 4C D0 43 CD 6C C3 45 3E E6 CC 70 C2
        F2 2E EA C0 3D B7 86 22 41 F7 3F 33 22 1D DA AE
        FB 21 F3 B6 61 A6 9F F3 2A 3A 24 E8 54 35 B2 4E
        DF C3 11 30 F3 9B 71 11 0F E5 D5 21 90 F6 5B 32
        51 4F F5 D7 0C 30 BD AA 3A F0 0D EF F1 9D 80 7D
        DD B8 C8 87 F6 E9 9E 48 7C 2C 98 29 87 EB DA 87
        08 5E 95 4D 5C 03 B7 80 C4 4C 3E 66 DC 54 43 B5
        54 4B 45 3D 96 CC 34 93 EF 25 C5 44 1B CA 86 64
        29 D9 D8 62 26 5F 53 46 32 21 F9 A0 64 B4 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "+F?sSD1oPsA0_p?vh|k<lT;LClE>p.="A?3"!a*:$T5N0q![2QO0:}H|,)^M\L>fTCTKE=4%Dd)b&_SF2!d"

[+] Synchronized Frame 68 Isolated at Symbol Offset 731680:
    ├── Extracted APID Subsystem ID : 0x1F4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F4 BA 6D 20 1F 4B 46 3A 68 FF 7A A0 A7 4F 83
        53 1B 04 AD A4 31 33 1F DD 3C 15 50 FF 71 73 C0
        0F C5 B3 11 34 3F DB 10 F3 0F C3 B1 09 80 FE 38
        19 C8 9F 85 4D 88 88 56 2A B9 A8 87 C2 D9 96 9A
        7F BD B8 F0 07 E9 50 86 DD 3B 3F 0C 4C 43 EE 7D
        44 44 3B F5 4C F4 03 F1 61 C9 4C 1E D6 5C 10 CB
        F2 AC C3 62 1D BE DE 76 61 E8 36 E3 22 9D DA 2E
        7E 01 F2 B2 60 A2 1F 7B EE 1A 60 FB 57 31 20 5E
        DC 63 11 30 F9 9B 31 11 0E ED 17 1D 90 F2 59 30
        D3 47 F7 93 16 30 BE EA 3A 98 07 6F 51 88 90 7C
        D8 38 88 87 62 89 9E 88 7C AC 99 69 A7 F6 D9 8E
        99 3F 55 0D 7D 17 F7 F0 C4 4C 3E F4 C6 64 43 BB
        44 C5 44 3E 56 4C 54 D3 FF 64 C7 44 3F 9A D6 AE
        8B 79 79 63 66 9F 37 6E 22 29 DB AA 62 32 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!m KF:hzOS13<Pqs4?8MV*P;?LC}DD;LaL\bva6".~`{`W1 ^c01Y0G0:oQ|8b|i?U}L>dCDD>VLTdD?yycf7n")b2"

[+] Synchronized Frame 69 Isolated at Symbol Offset 742440:
    ├── Extracted APID Subsystem ID : 0x1D0
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D0 B2 E3 22 1F 2B 66 1A 21 FF 12 E7 22 5F 8D
        43 13 64 FD F6 31 91 0F B9 E7 91 10 FC D1 70 D1
        2F 15 83 0D 34 FE 1B 79 E3 0F E1 A1 AB A0 76 1A
        18 C9 37 9E DB 8C 88 77 2A BB A4 87 CA D9 B6 82
        3E EE A8 6C 95 E0 53 C5 CD 3B F8 8D 44 43 EA 68
        C0 44 3B 94 5C C4 43 E9 6C C7 49 1F F7 D6 3A 41
        F4 2A 43 E0 9F B5 26 22 21 F3 34 A2 22 1D CA 2E
        62 21 F4 B2 61 A4 9F FB 6F 3A 61 F8 D5 35 20 4E
        DE C3 31 10 A9 BA 50 11 4F A5 17 59 10 FA 5A 30
        93 07 D5 97 17 32 3D 4A B2 D1 A7 A7 A5 9C 98 7C
        DB 18 88 87 5B 8B 9C 48 7E 2D 98 49 A7 D3 D9 E6
        19 BE 15 0D 6C 93 F3 90 C4 44 3F 6E 8C 44 43 F3
        D4 CF 40 3E 16 0C 14 C3 F7 2D C3 44 3F CE 06 A6
        01 6A 29 62 20 1E 13 C2 22 21 DE B0 67 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"+f!"_Cd1p/4yv7w*>lS;DChD;\ClI:A*C&"!4".b!ao:a5 N1POYZ02=J|[H~-IlD?nDC@>-D?j)b "!g"

[+] Synchronized Frame 70 Isolated at Symbol Offset 753200:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 E5 82 1F 8B 06 2A 49 D1 36 E1 BE 1F A5
        0F 53 00 AC FE 31 91 0F D9 B7 91 10 AA 51 71 D1
        0F 95 A7 2D 30 FE B9 30 D3 0F EB BB AB 82 7E DE
        19 89 07 C0 93 88 88 7F 2C 9B 7C 87 D2 C9 82 98
        7F 7C 98 B8 93 E1 50 94 C1 7B 7B 8C 44 C3 C6 6D
        E4 44 3B 94 4C B4 43 F9 68 C3 44 1F F6 DD 7E C9
        F4 AC E2 62 9F B5 84 22 65 65 B6 E2 22 1F CB 2E
        58 21 F0 A6 61 A4 9F 7B 2E 3C 25 78 55 35 32 0A
        DF 83 13 10 F9 92 31 11 0E E5 13 1D 40 F0 5A 30
        50 47 98 B7 15 B0 BC 8A 9A 91 A7 E9 A7 B8 98 7C
        6D 3C E8 87 42 8B 8E 88 70 2D 98 28 87 FE D9 8A
        08 5F F5 4D EC 53 97 9A C4 C8 3E F6 76 44 43 B9
        55 CF 44 3E 56 CC 34 D3 F7 6D E7 4C BF 4A CE AE
        69 D9 F9 63 66 1F BB 67 22 21 D8 A2 66 82 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!*I6S1Qq-00~,||P{{DmD;LChD~b"ee".X!a{.<%xU521@Z0PG|m<Bp-(_MS>vDCUD>V4mLJicfg"!f"

[+] Synchronized Frame 71 Isolated at Symbol Offset 763960:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC B2 66 A0 1F 4B 46 2A 08 FE B6 23 D6 0F D5
        6B 12 74 AD E0 B1 11 0F CB 17 19 10 EE 51 71 91
        0F 85 B3 0D 20 FF DF 79 D3 2F C2 A5 21 02 7E F6
        18 C9 87 EC D9 89 88 77 EA BB 2C 87 C2 C1 92 98
        7F ED 88 E9 83 E2 50 C6 C0 3B 7D 0C 44 CB EA 60
        C4 44 3B 94 5D F4 02 F5 64 CB 45 1F FE D4 74 C8
        F6 AC 4B 66 95 86 46 22 61 E5 72 B2 A2 1D AA 26
        F3 21 F2 B6 61 A6 9F F3 AA 28 61 78 54 B5 32 4E
        FE 43 19 06 FF BE 51 91 0E E5 53 2D 10 F0 59 30
        D2 0E 9E B7 CF 10 BC 3A 1A 99 07 6F D1 9C 99 78
        7D 3C 88 87 72 C9 9A 80 7C 2C 99 69 A3 EE DB 8E
        C9 7E 75 ED 4C 52 B6 F0 C4 4C BE 65 DC 44 43 F5
        45 CF 14 3C 56 CC 34 C3 AF 65 C5 64 3F 4A D6 A6
        89 DA EC 63 26 1F 1F 6F 22 21 FD A2 E2 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fKF*#ktQq y/!~w,P;}D`D;]dEtKfF"ar&!a(axT2NCQS-Y0:ox}<r|,i~uLRLeDCE<V4ed?Jc&o"!"

[+] Synchronized Frame 72 Isolated at Symbol Offset 774720:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD EA EE A2 1F 0B 66 4A 61 F0 B2 F3 A2 1F A5
        4B 56 74 AD 24 33 32 2F 99 95 15 10 FC 59 73 C0
        0F 15 93 0D 34 7F EB 31 DB 2F C2 A9 A9 A0 F6 F9
        18 89 07 DC D2 88 88 7F AA B9 68 87 92 D9 8E 98
        3E EF B8 69 85 E5 53 D4 C1 7F 1F 0C 44 83 E7 7F
        C6 44 3B 95 5C F4 43 E1 6C C9 49 1F F7 D6 54 C3
        B4 2A 4A 64 1D BF 8E 26 41 F9 3C E2 22 1D 8B 26
        3A 21 F0 B6 61 A6 8F B3 EA 3E 60 FA 56 25 71 5F
        D7 43 11 32 F1 98 79 11 0F AD 13 69 30 FA 59 30
        52 4F DD B5 9D B0 FD AA 5A B8 27 6F A1 88 81 7A
        CD A8 88 87 7A 8B 8E 88 7C 2D 99 E9 27 C4 DB 8E
        89 7E 0D 4C 49 06 B6 D0 C4 CC BE EE 94 44 43 BB
        65 CF 44 3E 16 CC 34 D3 FF 7D E7 44 3F 4E B6 B6
        49 D9 ED 62 22 1F 33 03 22 21 DC A2 EF 32 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fJaKVt$32/Ys41/h>iSDD;\ClIT*Jd&A<"&:!a>`V%q_C2yi0Y0ROZ'ozz|-'~LIDCeD>4}D?NIb"3"!2"

[+] Synchronized Frame 73 Isolated at Symbol Offset 785480:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC B2 E5 A2 1F 0B 66 5A 28 FD BE E1 A6 1F 8D
        6E 13 14 F4 F2 B3 31 0F D9 B3 91 10 F8 11 73 81
        4F 45 B3 0D 10 7F DB F0 53 2B ED 91 A9 9A 56 70
        19 D9 87 D4 D3 88 99 75 A8 BA 68 87 E2 D9 86 9A
        7D CF 98 E9 85 E3 54 D4 90 2B 3C CC 44 C3 F2 4C
        E6 44 3B 94 5C F6 43 FD 6C C3 48 1F E6 C6 7C CB
        F2 AA 6A 60 95 BC 86 26 41 FB 72 E2 22 1D EB 26
        0A 01 F8 B6 64 A6 8C FB 2B 3C 61 FC 55 31 B2 4F
        DB 43 33 32 FC 3B 31 51 0F ED 57 3D 10 FC 5A 30
        D3 4F BD B7 1D 30 7D AA 38 B8 05 6B A1 8D 98 7E
        AE 68 88 87 F6 8B 9E 88 78 2D 98 E8 A7 FE F9 86
        98 7F 5D 0C 5C 12 B6 D0 C4 8C 3E F6 DC 44 43 B5
        C5 DF 64 3F 56 CC 34 51 F7 4D C3 2C 0F 96 C6 A6
        61 DB E9 62 26 1F 33 63 32 21 DC A2 67 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fZ(n1sOES+Vpuh}T+<DLD;\ClH|j`&Ar"&d+<aU1OC32;1QW=Z0O0}8k~hx-]\>DCd?V4QM,ab&3c2!g"

[+] Synchronized Frame 74 Isolated at Symbol Offset 796240:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DF B2 EE A0 1F 0B 66 1A 41 FF BA B1 E6 1F D7
        43 53 14 ED 70 31 93 0F 9B 14 11 10 EA 53 72 F8
        0F 35 A3 05 34 FF DB 71 D3 0F 62 A9 AF 82 76 F3
        99 89 87 CC D9 88 88 74 2A B9 AC 87 8A D1 86 82
        7E F4 98 E8 87 E5 50 C4 81 7F 0F 0C C4 43 C6 6D
        C2 44 3B B4 4C E6 43 E5 64 CD 4D 1F FE 5E 52 C9
        F6 61 EA 46 95 BE 86 22 41 FB E2 A2 22 1D DA 26
        DB 21 E0 B4 62 A4 1F FB 2E 3A 61 F8 54 35 20 5F
        C7 6B 19 30 F9 9A 11 11 0E E5 13 04 80 B8 5B 32
        D3 0F CC B5 1C 30 7D 2B 12 B8 27 E5 A1 88 98 7F
        4D BC C8 87 F2 8B 8E 88 7C 2C 18 29 A7 E7 DB 8A
        90 7E 35 EC 4D 17 B7 DA C4 48 3C E4 DC 65 43 A9
        64 CE 65 AF 16 4C 74 C3 F5 E4 C5 4C 1F 1A C6 24
        21 DA 6C 66 22 1F 93 6E 32 21 EC B2 E1 B2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fACSp1Sr54qbvt*~PCmD;LCdM^RaF"A"&!b.:aT5 _k0[20}+'M|,)~5MH<eCdeLtL$!lf"n2!"

[+] Synchronized Frame 75 Isolated at Symbol Offset 807000:
    ├── Extracted APID Subsystem ID : 0x1DA
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DA B2 E2 A2 1F 4B 46 1A 61 FC 12 E2 96 1F B1
        72 57 25 EC F4 31 31 0F 89 F1 11 10 FF 51 33 D1
        0F 05 93 0D 30 F8 4B 11 6B 0F 43 A1 A9 8A FE FA
        19 C9 97 85 F1 88 88 77 2A B8 E4 07 D2 D9 8E 9A
        3F 8D BC E0 83 E1 50 D6 CC 2F 7F 0C C4 82 F6 65
        44 44 3B B4 5C 74 43 E1 64 C7 4D 3F F2 5C 54 C3
        F2 68 6A E0 3D AE 06 62 01 E1 36 A2 22 1D CA AE
        F0 01 F0 B4 61 A6 0F F3 2E 3A 21 F8 D4 25 30 0E
        DF 03 39 32 FB 84 51 11 0F C5 57 3D 00 F8 5A 32
        D2 0F BD F3 9D 30 3C 6A 1A FA 2F 6A A1 8C 90 78
        CD 18 8A 87 62 89 92 C0 7A 2C 18 69 81 EE C8 86
        18 3E 6D 0D 64 17 B4 DA C4 4C BE 26 DC 44 43 BD
        65 D8 44 3F 16 CC 94 D3 E1 EC C3 4C 2F 6E C4 B6
        49 DB EC 62 22 1F 32 5F 22 21 D8 A2 EB A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!KFarW%11Q30KkCw*?P/eDD;\tCdM?\Thj=b6"a.:!%092QW=Z20<j/jxbz,i>mdL&DCeD?L/nIb"2_"!"

[+] Synchronized Frame 76 Isolated at Symbol Offset 817760:
    ├── Extracted APID Subsystem ID : 0x1FE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FE AA EF 32 1F 0B 66 0A 69 F7 BE F3 A6 57 85
        63 53 04 FC F4 31 91 2F 99 E7 91 10 EE 55 31 D3
        0B 65 B3 3D 14 FD DB 51 D3 2F 81 A7 8F 88 7E FA
        18 88 87 CD A3 88 88 76 E8 BB 62 87 8A D1 92 8A
        7F 6D A8 6D 87 F9 D2 C6 84 7F 6D 0C 6C CF C6 E5
        64 4C 3A D6 5C B4 03 C1 64 C1 4C 1F 36 DE 5E C3
        FD A8 6A 42 1D BE 86 26 65 E3 6E F2 22 1D CA A6
        7B A1 F0 B2 64 A4 8F 77 EA 39 61 F8 76 31 B1 4E
        DF 43 10 20 F5 FB 79 11 0E AD 97 0D 10 F9 5B 31
        D3 47 E5 B7 8D 10 3E 3A D0 90 A7 6F 65 88 88 7C
        6D 98 88 87 52 C1 84 C9 7D 2D 99 69 A7 F4 C8 C6
        88 3E 15 2D 4C D7 97 D2 C4 C4 3E 2E D6 44 43 B3
        45 CF 64 3E 56 CC 36 91 FF 2D E7 2C 3F 02 86 AE
        03 DB F0 62 26 1F B7 4E 22 25 D8 B2 E7 B2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!2fiWcS1/U1e=Q/~vbmmmldL:\dL6^jB&en"{dw9av1NC y[1G>:oe|mR}-i>-L>.DCEd>V6-,?b&N"%"

[+] Synchronized Frame 77 Isolated at Symbol Offset 828520:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE AA EE A2 1E 0B 66 1A 61 F9 FE F3 B6 1F 8D
        7A 5B 04 AD F0 B3 12 0B 19 B3 11 10 FE 59 76 D0
        0F A5 93 1D 24 FF E9 F1 D3 0F C4 A9 AD A2 F6 7A
        19 C8 07 DD FB 88 88 7F E8 A9 A0 87 D2 C9 8E 9A
        76 ED 98 E1 07 EB 56 C4 C1 3B 7D 8C 60 83 E6 4C
        46 44 3B 94 5C E4 43 C9 64 CB 4D 3F 16 DF 18 C3
        F0 A8 6B 40 1D BE 06 32 25 E3 B6 A2 22 1F BA 2E
        78 21 E4 B4 63 A4 9F 55 7E 1B 60 F9 55 75 32 1E
        DE 63 33 20 ED 9B 51 11 0E FD 17 19 90 F2 5F 31
        51 0F F8 F7 16 30 FC 2A BA 99 87 6F 41 89 91 7D
        FF A8 C8 87 72 CB AE 88 74 2C 98 68 87 F7 5B 87
        D8 3E 05 5D EC 12 B2 C2 C4 CC 3C 6C 9C 44 C3 AB
        54 CE 44 3F 16 4C 94 93 FB 7D C5 4C 2F 0E 84 AC
        01 FB E9 E6 26 5F 33 26 32 21 FE BA 6E A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!faz[Yv$zvV;}`LFD;\CdM?k@2%".x!cU~`Uu2c3 Q_1Q0*oA}rt,h[>]<lDTD?L}L/&_3&2!n"

[+] Synchronized Frame 78 Isolated at Symbol Offset 839280:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 6F A2 1C AB 22 3A 69 F3 FA E3 A6 1F 9D
        47 1A 04 BF 74 31 13 0F 39 17 11 10 EE 91 71 58
        0F 85 93 05 34 FF 9B 58 DB 0F C3 A3 29 8A 76 FA
        58 89 87 A4 D3 C8 88 76 28 BB 68 87 C2 89 86 DA
        3F 79 1E F8 97 F1 D2 D6 D5 3B 7E 4C 4C 03 E6 1D
        C4 44 2B 96 5D 66 43 E1 64 C3 4D 1E A3 D6 74 E0
        F0 A9 EB 64 9D BE 96 22 61 FF E6 A2 22 1D CB 26
        B3 21 F2 B6 60 A4 9F D9 23 3A 61 F8 54 25 A1 4E
        4B 83 13 12 FD 9B 71 11 0E CD 97 3D 00 FC 59 30
        D2 4F B7 B3 1A 30 FE 1A 9A 92 07 6F A1 A8 98 78
        4D BC C8 87 E2 8B 9A 88 7D 2C 98 68 87 FC 5A CE
        C8 5F 55 09 6D 13 B3 D0 C6 CC BC 26 CC 44 43 E9
        41 CB 40 3E 56 4C B4 D1 F9 6D 47 AC 3F 1A EE BE
        29 DB E9 63 26 1F B3 AA 32 21 D5 A2 67 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!o":iGt19qX4X)vXv(h?y;~LLD+]fCdMtd"a"&!`#:aT%NKq=Y0O0oxM},hZ_Um&DCA@>VLmG?)c&2!g""

[+] Synchronized Frame 79 Isolated at Symbol Offset 850040:
    ├── Extracted APID Subsystem ID : 0x1D8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D8 A2 E7 20 1F 0B 26 5A 28 FF BE F0 A6 1F 09
        43 53 34 ED 70 33 33 0F 39 17 91 10 EE D1 31 59
        0F C5 A3 0D 30 FB DB 71 D1 0F C2 A1 AD 00 76 FA
        18 89 97 CD DB 88 88 7B 28 B9 E8 87 DA D1 86 9A
        7F ED B8 E5 97 FF D0 D5 C8 7F 1F 8C 4C CB EA 6D
        E4 44 3B 97 4C C4 43 C5 70 C1 4D 3E F6 CC 34 42
        E0 A9 6A E2 9C 8E 86 32 61 EB 20 30 22 1F EA AE
        02 21 FA B4 60 A6 9F F3 2E 0A 21 78 14 25 B3 4B
        D7 03 1B 30 F9 9B 11 91 0E ED 17 0D 90 F6 5A 33
        51 0F D5 B5 1D B2 FF 2A 12 98 2F CB 81 89 90 78
        4D 38 C8 87 72 8B 9C 80 7A 6D 98 69 A7 F6 FA 8E
        D0 7F 55 AC 4C 52 F8 83 CE C0 BE 25 D4 6C 4B BD
        45 C3 64 3F 16 4C 14 D3 FF AD C7 2C 3B 4A 86 AE
        09 DA E0 66 2C 57 37 CA 22 25 DC A2 EE A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "! &Z(CS4p3391Y0qv{(LmD;LCpM>4Bj2a 0"!`.!x%K0Z3Q*/xM8rzmiULR%lKEd?L,;Jf,W7"%"

[+] Synchronized Frame 80 Isolated at Symbol Offset 860800:
    ├── Extracted APID Subsystem ID : 0x1FA
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FA B2 EE A0 1E 0B 66 9A 08 FB 36 F3 86 1F DF
        53 03 01 ED EC 31 32 2F 19 F3 11 10 EF 59 35 D1
        4F 85 83 15 34 FF 0B 71 4B 0D 40 A5 AD 82 76 FB
        18 A9 87 FE E9 C0 88 7F 6C B8 E0 07 C2 D9 86 9A
        7F DD BC FD 97 E8 50 D4 C1 3B 2C 5C CC 43 E6 75
        44 44 3A 94 5C E6 43 D5 68 C3 44 3F AF DC 30 C2
        F8 2D EA E0 9F 8E 06 22 21 E3 76 B3 22 1F 8A 2E
        48 01 F0 B4 61 A6 1F 6B 2E 1B 21 38 14 B1 71 4B
        DE 03 13 30 F8 91 71 11 0E ED 13 39 00 FD 59 30
        53 4F B5 93 19 B0 BE 0A 98 B9 A7 6D 61 8C 9B 7C
        CF B8 88 87 7E A8 92 08 7E 6D 98 E9 83 FD 7B D3
        8C 3E 15 09 59 D3 B7 50 CC CC 3F AF DC 64 43 B9
        44 DF 40 3F 16 CC 34 43 FD 3C 45 6C 3F 06 AE AE
        0B DB 50 67 26 1E 3A 63 22 21 D0 A2 66 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!f6S12/Y5O4qK@vlP;,\CuDD:\ChD?0-"!v".Hak.!8qK0q9Y0SOma|~~m{>YP?dCD@?4C<El?Pg&:c"!f"

[+] Synchronized Frame 81 Isolated at Symbol Offset 871560:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE A2 6F 22 9E 0B 26 FA 60 F7 F6 63 A2 0F 8F
        42 17 04 ED B0 33 31 0F A9 81 11 10 EE 59 70 91
        0F A5 93 1D 00 FE 1B 31 D3 0B D3 A9 A9 B2 7E 6A
        19 89 87 E6 D3 88 88 76 2A 99 E4 87 E2 D9 8E 9A
        7F 7F AC BB 93 61 51 D7 C5 3B 3E 8C 64 CB E6 6D
        C6 44 3B 94 5C D4 03 E7 6C C3 4D 3F F6 DC 70 41
        F9 A9 6A 60 95 B4 14 22 21 F9 20 E3 22 1D EA 2E
        B0 01 F8 B6 E0 A4 1F 9B EA 3B 61 F9 54 A1 30 5A
        DA A3 32 32 FE 9F 71 11 0E F5 97 39 10 F8 5B 32
        D3 4E D5 B7 1D 31 FC 2A 12 98 2F 6D 41 8D 98 59
        CC B8 88 87 E2 AB 8E 80 7D 2D 98 A9 A7 E4 CB 8E
        88 7F 05 6D 5D 93 B1 F0 C4 CC 3E 6F 95 44 43 D1
        40 CA 44 3C 96 4C 74 51 F4 AC C1 8C 2F 1A AC A6
        69 F1 E9 62 46 1E 13 EE 22 21 D0 A2 63 82 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!o"&`cB31Yp1~jv*aQ;>dmD;\lM?pAj`"! ".;aT0Z22q9[2N1*/mAY}-m]>oDC@D<LtQ/ibF"!c"

[+] Synchronized Frame 82 Isolated at Symbol Offset 882320:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC EA EE 32 1F EB 46 1A 09 FF 92 E3 B2 1F 9D
        56 13 04 ED 7A 31 13 0F 9D 97 11 10 EC 51 37 51
        0F 65 B3 2D 34 7F 9B 79 D3 0B C0 B1 29 00 7E 7E
        18 C9 87 DC 99 80 88 7F AA 9B 28 97 C2 D9 8E 9A
        7F 4F A8 E9 81 E4 50 D4 C9 3B 4D 8C 4C C3 E6 FD
        C4 4C 3B 16 5D 84 43 F1 6C C3 49 3F 53 5C 74 C5
        F4 E9 6A E0 B5 AE 06 22 25 EB F8 72 22 1D CA AE
        76 21 F8 B6 67 A2 5F 5B 6A 3A 65 F8 56 35 34 4F
        CF 8B 19 00 F1 BA 61 11 0E F5 13 38 80 F8 58 30
        D3 47 68 B3 1C 30 7C 1A 1A F3 07 6B A1 88 90 78
        C9 AC C8 87 5E 8B 9E C8 7C 2D 19 68 07 E8 D9 CE
        18 7E 15 1D 4C 13 B3 D0 CC 4C 3E 26 84 44 C2 B9
        44 C9 44 3C 96 4C 94 D3 FD 6D C5 4C BF 6A D6 3E
        C9 DA E9 62 26 1E B3 E6 2A 25 7C AA 6F 92 16
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!2FVz1Q7Qe-4y)~~(OP;MLL;]ClI?S\tj"%r"v!g_[j:eV54Oa8X0Gh0|kx^|-h~LL>&DDD<LmLj>b&*%|o"

[+] Synchronized Frame 83 Isolated at Symbol Offset 893080:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC A2 65 22 1F EB 66 5A 68 FF F6 73 B6 17 81
        6B 33 14 FD F6 B1 32 0F 19 87 19 10 EF DD 36 10
        0E C5 B3 0D 24 FB AB 71 C3 07 95 A1 AB 0A 76 BA
        18 89 87 87 C9 88 88 72 2E BA E8 87 C2 D9 80 9A
        7F BC A8 E9 83 68 DB D7 DD 6B 48 0C 64 83 E6 6D
        04 44 BF 94 4C F0 43 E1 68 CB 4D 1F FE 5C 74 41
        F1 A8 EA 60 9F FE 06 32 61 F3 B4 A2 22 1D CB 2E
        B3 21 F6 B6 61 A4 9E 77 EF 1A 61 F8 14 A5 30 4E
        DF 63 11 22 F0 9A 39 11 0E F5 17 39 00 B9 5B 30
        52 4F EF F7 1D 30 FD 0A 1A BA 27 67 E1 98 99 78
        CC B8 C8 87 E6 CB BE 08 7E AD 98 E8 A7 F8 F8 8E
        88 5E 55 3D 4C 82 B7 D8 CE 4C 3F 66 1C 44 43 F9
        45 CF 44 3E 16 CC 74 53 EB E5 E5 04 2F EE 8C 22
        09 FB F9 66 64 1F 37 26 22 21 FC AA E1 B2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!e"fZhsk326$qvr.hkHdmDLChM\tA`2a".!awa0Nc"99[0RO0'gx~^U=LL?fDCED>tS/"fd7&"!"

[+] Synchronized Frame 84 Isolated at Symbol Offset 903840:
    ├── Extracted APID Subsystem ID : 0x1F4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F4 A2 69 A2 1E 2B 26 1A 69 FB F6 E2 B6 4F 85
        47 5B 24 AD F4 31 10 2F 89 97 31 10 EA DD 35 C1
        0F C5 B3 0D 94 FD 5B 78 D2 0A C2 A3 AD 80 DE D8
        58 89 07 4E CB 9A 88 74 B8 B9 84 07 82 C9 82 8A
        7A FD 99 E9 83 E5 52 D5 C9 3B 7F BC 4C 43 C6 69
        C4 44 3B 15 5C D4 03 D1 6C C3 45 3E FE D4 52 C3
        F5 EE 6A C0 9D 8E C6 26 21 F3 72 22 22 1F DB 2E
        30 21 F0 B6 61 A2 9F 69 6F 3B 21 78 94 35 A0 4F
        DF 43 31 30 FD 9B 31 11 0E FD 17 7C 10 F4 5B 31
        D1 47 A5 B7 BD 12 EC 0A 72 98 25 6F 81 88 88 7D
        CC B8 88 87 7A A9 9A 88 7F AC 99 69 A7 C6 C8 CE
        18 7E 35 1D 4D 13 B4 E0 CF CC 39 67 DC 44 03 B5
        64 DB 04 3E 16 CC 54 51 F7 2C C7 44 3F B2 A6 A6
        2B F9 F0 66 26 5E B3 EF 32 21 DC B2 AB 02 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!i+&iOG[$1/15[xXNtzR;LCiD;\lE>Rj&!r"".0!aio;!x5OC101|[1Gr%o}zi~5M9gDd>TQ,D?+f&^2!"

[+] Synchronized Frame 85 Isolated at Symbol Offset 914600:
    ├── Extracted APID Subsystem ID : 0x1F8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F8 A2 EF A0 1F EB 46 3A 40 DF 3E A2 E6 17 89
        46 52 14 EC B0 31 93 0F 8B B7 13 10 EC D5 53 91
        0F 95 A3 0D 24 7F FB 50 51 23 C2 B1 8B 20 76 FC
        18 88 97 C4 FB C8 88 76 A8 B9 08 87 52 C9 8E 92
        7B 64 BC B1 97 F1 D0 D4 C9 6B 69 0C C4 C3 E7 84
        C4 44 3B 94 4D 24 43 F1 60 C3 45 3F A6 DC 34 C1
        FB A8 6A E8 9D BE 86 26 21 F3 F3 F2 62 1D FB AE
        6A 21 E8 B6 61 A0 9F FF 6E 3A 24 7A 55 35 34 4F
        5F 23 11 20 B9 D3 38 91 0E C5 17 3D 90 F8 5B 35
        D3 4F F9 B7 15 B8 FF 6A 12 D0 25 47 A5 88 98 7E
        DC 98 C8 87 86 CB 84 09 7F 2C 98 E9 A3 FE DA C2
        98 7E 05 0D 5D 17 A4 C0 C6 CC 3E 66 5C 54 43 F9
        C5 C7 44 3C 94 0C 34 D1 ED 65 C5 0C 9F 0A 84 B6
        A9 7A E8 63 46 1E B7 2A 22 21 D8 A2 E7 92 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!F:@>FR1S$PQ# vvR{dkiD;M$C`E?4j&!bj!an:$zU54O_# 8=[5Oj%G~,~]>f\TCD<4ezcF*"!"

[+] Synchronized Frame 86 Isolated at Symbol Offset 925360:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC AA E6 82 1D 0B 06 7A 69 F7 9E F3 A6 1F A1
        43 5A 60 AD 20 B1 13 2F DD F3 91 20 EC 51 36 59
        0F 15 B3 05 34 FD CB 51 FB 0F C2 B3 AD A2 76 D2
        18 8B 07 C4 DA C8 88 77 AC BB C8 87 EA C9 86 9A
        7F CD AC A1 97 E3 5C C6 8D 3B 3D AC 4C C3 F6 68
        C4 44 3B B5 5C D4 43 ED 48 C3 4D 1D B7 DC 54 C1
        FB A8 63 E8 3D 0E 96 62 61 F7 34 F3 22 1D AA 2E
        32 21 F0 B2 61 A6 1F FB EE 2A 65 F9 54 31 70 4A
        D2 43 11 20 F9 9D 79 11 0E ED 95 1D 00 F7 DB 33
        D3 4F 3E B3 11 10 7D 2A 1A 39 27 6D 45 9C B0 7C
        DC B8 88 87 F2 CB 8F 98 78 AD 18 69 A7 BE DB 83
        08 7E 45 9C 4D 03 B6 D8 CC C8 3B 36 0E 64 43 AF
        45 CD 64 3C D6 CC 96 C1 F7 65 C3 EC 9F 0A 8E AE
        01 5B 3C 62 22 1F 3B 4F 22 21 D4 A2 EB 12 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!ziCZ` / Q6Y4Qvw\;=LhD;\CHMTc=ba4".2!a*eT1pJC y3O>}*9'mE|xi~EM;6dCEd<e[<b";O"!"

[+] Synchronized Frame 87 Isolated at Symbol Offset 936120:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD 22 E5 B6 1E 0B 66 2A 68 FB F6 B3 B2 55 85
        77 59 44 AC B8 B1 22 0F B9 37 11 10 E6 D5 57 C9
        0F A5 B3 2D B4 73 5B 59 F1 0F C6 A9 8B 08 5E F8
        59 99 87 CC FD C8 88 55 2E B9 64 87 E2 D9 86 80
        7B AF 90 6D 91 E7 5E D4 91 7F 1A 8C 4C 8B D6 4D
        E4 44 3B 34 5C F4 43 E1 64 CB 49 3F B7 CC 34 50
        E8 E8 4A 62 9D AE D6 72 21 FF 34 E0 22 1D 0F 2E
        7C 21 F0 B6 61 A0 1F 7D FE 9C 64 D9 97 25 34 5E
        DF CB 31 32 FB DA 79 93 0E B5 53 01 90 BE 5F 30
        53 0F ED B7 0D 10 FC 0A 38 99 27 6F D1 BC 98 78
        DC 38 88 87 72 AB 86 C8 71 2D 98 29 27 FA CA 8B
        98 6F 15 4D 4D 03 91 D0 C4 4C 3C E5 9E 64 43 BA
        75 DF 04 3C 16 0C 74 11 FB 75 C7 04 BF 82 8C E6
        8B F9 CC 67 66 1F F3 EF 32 21 F0 B2 E3 8A 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"f*hUwYD"7W-s[Y^YU.d{m^LMD;4\CdI?4PJbr!4".|!a}d%4^12yS_0S8'ox8rq-)'oMML<dCu<tugf2!"

[+] Synchronized Frame 88 Isolated at Symbol Offset 946880:
    ├── Extracted APID Subsystem ID : 0x1FA
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FA A2 67 82 1F 0B 06 5A 61 FF 3E C3 E6 0F A5
        67 1B 44 EF B4 B1 32 0F FB A5 19 10 E8 3D 71 01
        0F 45 B3 0D 10 7D 3F 51 55 2F C3 A9 A8 02 76 BE
        59 89 15 9E CB CC 80 7F 2A B8 E8 87 CA D1 96 82
        7E ED B8 E9 87 E0 D0 95 C4 7F 18 3C 44 CB ED 4D
        E5 44 3B D4 5D 10 03 E1 64 C1 49 1A EE D4 7C C1
        F1 AD 60 64 9D FE C6 22 09 F2 B1 52 22 1D CA A6
        F8 25 E4 B6 67 A6 9F FF 2F 39 21 F8 55 75 A1 4E
        CB 6B 19 22 FC 9A 11 81 0E FD 13 0D 00 B8 5B 32
        D1 0F B5 17 39 92 FD 2B 7A B8 8D 68 B1 88 98 F5
        CF BC C8 87 C2 EB 94 08 71 AF 99 68 A7 FC 5B 86
        D8 3E AD 58 6C 92 F3 B9 CE 4C 3C 44 9D 64 43 F3
        45 DB 04 3C 16 8C A6 91 EE 2D C5 05 BF 0E 04 B8
        29 D9 F8 63 66 16 93 42 22 21 F8 BA 67 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!gZa>gD2=qE}?QU/vY*~<DMD;]dI|`d"R"%g/9!UuNk"[29+zhqh[>XlL<DdCE<-)cfB"!g"

[+] Synchronized Frame 89 Isolated at Symbol Offset 957640:
    ├── Extracted APID Subsystem ID : 0x1D4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D4 BA 6C 02 1F 0A 66 1A 29 F6 16 E2 D2 2F 8B
        03 53 04 AD F6 21 33 0F 19 A7 11 10 BE 59 73 D9
        0F D5 33 05 24 FE 49 51 DB 0F C2 B1 AB 02 5E FB
        18 D8 05 C4 EB 88 98 74 08 B9 68 07 82 D9 86 9A
        7D E5 B5 25 97 E9 58 D4 CD 3B 6D 3C 44 93 DF F1
        E6 D5 3F 94 5C 30 03 E3 6C C7 4D 1E C6 D4 57 CB
        D8 A8 EA 60 9D 3C 86 32 65 FD 26 F2 22 1D CE 26
        36 21 F0 B6 63 A4 8F F3 E3 3D 60 FA B4 B5 21 4F
        DF C3 19 38 F8 FB 75 11 0E BF 97 2B 94 F5 5B 31
        D3 4F 5D F5 9C 32 7C 6A 1A B8 A7 47 21 88 88 7C
        EF B8 88 A7 F2 89 92 C0 76 2D 19 E8 A7 FB DB 8E
        18 FE 35 AD 4D C3 B7 C1 CD 44 3D 3C 54 44 43 F9
        44 C7 04 3F 16 4C 74 81 FF 6D E5 04 1F 8A AE A4
        29 79 EA 66 64 1F 73 A3 32 21 DC A2 EF A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!lf)/S!3Ys3$IQ^th}%X;m<D?\0lMW`<2e&"&6!c=`!O8u+[1O]2|jG!|v-5MD=<TDCD?Ltm)yfds2!"

[+] Synchronized Frame 90 Isolated at Symbol Offset 968400:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC AE 67 A2 1F 6B 26 0A 21 FB BE A3 E6 07 81
        43 53 40 ED AE 37 33 0F 99 A1 13 10 EF 51 33 C0
        0F 85 B3 0D 10 7E D9 71 C3 0B C6 AD AD 82 76 FA
        19 98 07 F5 F9 98 88 77 E8 B9 C8 07 C2 D9 8A 82
        3F EC B8 E8 85 EB 52 9E D8 3B 7D 8C 44 4B F2 6D
        C4 54 39 B4 4D E4 43 F9 6C CA 4D 3B 77 DC 30 C3
        F7 28 62 60 B5 AE D6 22 25 F3 74 F2 22 1D CA 2E
        82 61 F0 B6 67 A6 9F 39 6F 2A 60 F8 94 35 B6 0E
        DF C3 39 30 FE 9A 79 11 0F FD 13 5D 90 EA 5B 33
        D3 4F FC F5 1D 10 BD 2A 12 B9 A7 6D A1 88 80 7C
        EF 88 C8 87 46 AB BE 88 7C 2D 98 69 A7 FE DA 8E
        58 7E 0D 4D 48 13 B6 D2 C4 C8 BE 7E DC 44 43 B9
        45 C7 64 3F 16 CC 34 92 EB 65 45 9E 3E DA 96 94
        09 CF E8 62 26 1F 32 2E 22 21 DA A2 E5 00 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!gk&!CS@73Q3~qvw?R;}DKmT9MClM;w0(b`"%t".ag9o*`590y][3O*m|F|-iX~MH~DCEd?4eE>b&2."!"

[+] Synchronized Frame 91 Isolated at Symbol Offset 979160:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC B2 E5 80 1F 4B 26 3B 60 FB B6 69 A2 1F 85
        53 57 44 ED E4 B1 13 0F 5B B3 11 00 E8 59 70 71
        0F B5 93 0D 34 FC DE 71 FB 0F C2 A5 AD 88 DE DA
        18 D9 A7 CC D0 CC 88 7E 68 B8 E0 87 C2 C9 86 9A
        3C 75 98 69 87 E5 58 DE C1 3B 4C AC 44 CB C6 CD
        C4 44 3B 34 5C 64 43 E1 68 CF 4C 3F 47 D4 74 C1
        F3 68 62 62 BD 9E 86 26 21 F1 20 E3 22 1D 6B 2E
        7A 21 F2 B2 61 A6 9F F5 2E 38 65 78 57 21 B0 4E
        CE 43 11 00 FD 9B 71 15 0E B5 53 7C 10 F9 59 30
        53 4F B9 93 CD 32 7D AA 12 98 27 67 A5 88 88 78
        D1 BC C8 87 72 CB BE 88 7D AD 99 69 A3 C0 DB 8F
        C8 7F 05 8D 2C 13 F6 B0 CC 40 3F B4 54 64 43 FF
        61 C6 04 3C 16 8C B4 51 FC 6C C7 AC 1F 0A 9C A6
        21 7B 60 43 24 5E 73 6B 02 21 D0 B2 67 82 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!K&;`iSWD[Ypq4q~h<uiX;LDD;4\dChL?Gthbb&! "k.z!a.8exW!NCqS|Y0SO2}'gxr}i,@?TdCa<Ql!{`C$^sk!g"

[+] Synchronized Frame 92 Isolated at Symbol Offset 989920:
    ├── Extracted APID Subsystem ID : 0x1F8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F8 EA 66 82 1F 8B E6 5A 28 F2 36 E2 82 1F 8B
        5B 12 14 ED FE 33 33 1F 8B 33 11 10 FE 55 37 D0
        0F B5 B3 05 24 FB E9 58 F3 2F D2 A3 AD 08 F6 FB
        51 C8 87 CD DB 8C 88 76 28 B9 C8 87 82 D9 82 9A
        7D F4 B8 3C 85 E1 51 84 C5 3F 3D 0C 44 C3 FD AD
        E4 4C 3B 54 5C E6 43 E5 64 C1 45 3F D2 DC 70 C2
        F8 AE 62 64 95 BE 06 32 61 EB 36 62 26 1D AB 2E
        5C 21 F0 B2 65 A6 9F DB EF 0E 61 FA D7 F1 A0 5F
        DB 0B 31 32 B9 9F 71 11 0E E5 17 39 10 FC 5B 10
        D3 47 FD F5 9F 94 FC 2A 10 BB 05 65 31 88 88 7C
        5D 9C 88 87 52 88 BA 80 58 AD 98 29 23 D1 EB 87
        89 7F 25 8D 18 17 B5 92 C4 C0 BE 66 DC 54 43 B9
        45 CD 60 3E 16 CC 34 83 FE 6C E3 6C 1F 86 86 AE
        81 FB C8 63 24 1F BA 8E 62 21 D8 A0 67 02 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fZ(6[333U7$X/Qv(}<Q?=DL;T\CdE?pbd2a6b&.\!ea_12q9[G*e1|]RX)#%fTCE`>4llc$b!g"

[+] Synchronized Frame 93 Isolated at Symbol Offset 1000680:
    ├── Extracted APID Subsystem ID : 0x5D2
    └── Full Decoded Frame Payload Hex (223 Bytes):
        25 D2 AA E5 A2 1F 2B 66 1A 49 FC B6 A1 92 17 8F
        4B 56 14 EC B4 B1 93 2F BD F7 19 10 EE 51 72 D1
        0F 85 B3 0D 34 7D 7A 51 D3 0F E6 A1 8B 82 F6 B2
        18 C9 87 CC F3 8C 88 7D AC BB 68 97 C2 C9 9E 9A
        7D ED 3C 39 95 F3 D0 84 C0 3B 2D 0C 4C D3 F6 7D
        E4 4C 3F 94 5D 94 43 E1 6C CD 4D 3F E6 F6 70 C8
        78 E8 EA 60 95 BE 86 62 65 E3 74 60 22 1F CA 26
        89 01 F4 B2 61 A2 9F FF 66 3A 64 78 D6 B5 B0 4E
        CF 2B 11 02 ED 9B F1 11 0F CD 13 34 90 FE 5B 30
        D1 4F A9 37 1E 30 7E 0A 38 90 2F EF 01 9C 99 7B
        ED B8 88 87 4E CB 9E 88 7C 2D 99 69 87 FF DB 8A
        19 5E 55 0D 6C 93 B7 D4 C4 4C 3C 26 DA 44 43 BF
        45 CF 64 3F 16 CC 34 51 FE 7D C7 0C 3E 62 86 B6
        09 59 D8 67 24 1F BB 6E 32 61 D8 A2 67 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "%+fIKV/Qr4}zQ}h}<9;-L}L?]ClM?px`bet`"&af:dxN+4[0O70~8/{N|-i^UlL<&DCEd?4Q}>bYg$n2ag""

[+] Synchronized Frame 94 Isolated at Symbol Offset 1011440:
    ├── Extracted APID Subsystem ID : 0x1F8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F8 A2 65 BA 1E 0A 66 2B 0C FF F2 23 A6 1F CB
        43 5B 14 ED F4 31 11 0F 89 A7 11 10 E6 55 31 C1
        0F ED A3 0D 34 7E 8B 71 C3 03 CA A1 0B 8A F6 BA
        18 8B 07 FF AB 88 88 7F 2E B8 E8 87 C2 D9 82 92
        38 ED A8 68 87 E7 50 D4 D5 6B 7D 0C C4 CB F6 4C
        C6 44 3B 96 5C F0 43 C5 68 C3 4D BF 76 DE 5C 41
        F6 EA 6A 40 3D BE 86 22 61 F1 B6 E2 22 1C 2A 26
        DA 21 F0 B4 65 A4 0F BB 6A 33 60 F8 D6 A5 20 5A
        DB C3 31 20 F9 BD 31 11 0F F5 97 3D 90 FA 58 32
        D1 0F 9E F3 9D 00 DD 3B 52 90 27 EF F5 89 98 78
        7F B8 18 87 62 8B B9 08 7C 2D 98 69 07 67 DB 0F
        C8 3E 05 0D 7C D2 B7 D0 D4 CC BD 66 8C E4 43 AA
        65 DB 60 3E 16 CC 14 C1 FB A9 C7 4C 1F 26 A6 2E
        E1 DA 48 6E 20 1F 3A AA 22 21 F0 A2 22 82 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!ef+#C[1U14~q.8hPk}LD;\ChMv\Aj@="a"*&!ej3` Z1 1=X2;R'xb|-ig>|fCe`>L&.Hn :"!""

[+] Synchronized Frame 95 Isolated at Symbol Offset 1022200:
    ├── Extracted APID Subsystem ID : 0x1D7
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D7 A2 E8 92 17 0B 06 1A 68 FF 76 E3 D6 4F CD
        72 52 04 ED E4 31 33 0F C8 B7 19 10 FB D1 73 D1
        0F 95 B3 3D 14 7F 79 51 F3 0F C0 A1 2B 08 56 FA
        18 98 87 EF D8 84 88 7F 28 B8 E0 07 FA C1 86 90
        7E 24 B8 69 85 E7 50 C4 D1 2F 7D 0C E4 5B EF 7D
        E4 4C 3F 94 5C F4 43 D1 64 C3 48 0E 7A DE 74 C3
        F6 AA 63 44 9F 9E 96 22 21 F1 A7 6A 22 1D CA AE
        5B 21 E0 B6 61 A0 9F B9 EE 49 21 F8 B4 B1 F2 4F
        DE 63 11 32 FB D8 31 11 0E C5 97 2C 90 F3 5B 30
        D3 0F F5 97 9D 32 FC 2A 50 B8 25 6F 21 98 88 7C
        4B 88 C8 87 4A CB 98 80 7C 2D 99 E9 A7 E6 DB 84
        98 5F 35 19 4C 93 B7 DA CC C4 7E 76 DC 44 43 B1
        75 CF 64 3C 16 4C 34 93 FE 6D 47 E4 B7 0E AE 26
        01 DB 60 62 60 1F 33 23 22 21 D9 AA E3 A2 17
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!hvOrR13s=yQ+V(~$iP/}[}L?\CdHztcD"!j"[!aI!Oc21,[02*P%o!|KJ|-_5L~vDCud<L4mG&`b`3#"!"

[+] Synchronized Frame 96 Isolated at Symbol Offset 1032960:
    ├── Extracted APID Subsystem ID : 0x1F4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F4 A2 6F A2 1E AB 66 1B 09 FF 36 A0 A6 17 8D
        4B 13 00 FD F4 B3 22 2F CF B7 95 12 FE 59 76 90
        0F 15 B3 1D 24 FF FB 71 FB 2B C1 A1 AB 02 76 6A
        18 99 87 CC DB CA 88 75 2C B9 E4 87 C2 D1 82 92
        7F 77 98 F9 87 FD 52 C4 C1 3B D8 2C 44 C3 E7 74
        C6 44 3B D4 4C FD 43 F9 68 CF 6D 3E 1F 54 7A 4A
        F9 AD EB EC 9D 86 06 66 61 FF 3A E2 22 1D 8A AE
        38 21 F0 B0 61 A0 0F AF AF 29 21 F8 D4 75 B0 4F
        DF 43 11 12 FD 90 31 11 0E BD 97 4D 00 FC 59 33
        D3 0F E4 B5 9C 10 3C 6A 5A D8 27 E8 61 88 81 7D
        DD 38 C8 87 D2 89 BE 88 7D 2D 98 69 27 7C CB 8B
        59 7F 95 29 7C 57 B7 DA CC 4C BE 74 86 64 43 B5
        45 CE 00 3C D6 CC 34 D1 FD 6C E7 CC 3F 82 8E A4
        A9 DB E8 62 6E 1F B2 6A 22 21 DB AA 65 92 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!of6K"/Yv$q+vju,wR;,DtD;LChm>TzJfa:"8!a)!uOC1MY3<jZ'a}8}-i'|Y)|WLtdCE<4l?bnj"!e"

[+] Synchronized Frame 97 Isolated at Symbol Offset 1043720:
    ├── Extracted APID Subsystem ID : 0x1D8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        29 D8 AA EF A2 9E 8B 46 5A 20 FD B2 B3 C6 5F 8F
        4A 53 04 FD F8 31 01 4F 3D B1 19 12 FA 75 71 11
        0F 85 A3 25 34 FC FB 39 6B 2F E2 A1 AD 82 FE 52
        18 91 07 9D BA 8C 88 76 AE BB E8 87 C2 D9 96 82
        7D 0D A8 F9 97 A2 D9 D4 C1 3F 7D 8C 64 43 F7 7D
        64 44 3E 96 5C 74 03 E1 6C 43 45 3F 37 4C 1C CA
        F4 2A 62 48 15 BF 86 62 61 F9 7C A2 22 1D CA AE
        6A 01 FE B4 61 A6 8F FF 2E 2A 65 FC 14 B5 B5 5E
        D2 8B 31 30 F0 B7 59 91 0E E5 17 35 10 F8 59 30
        53 47 FD F7 9D 32 FC 6A 7A D8 A7 6F 81 89 98 7E
        C8 70 88 87 42 CB 9A A0 7A 2D 98 E8 27 F6 49 CE
        1C 7E 4D 89 49 12 B5 D0 C4 40 BE EC DC 44 42 BF
        45 DF 24 3A 56 4C 34 DB FE 64 C7 6C FE 0A 86 A6
        89 D8 C0 63 22 1F 72 0E 22 21 DC A2 E4 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ ")FZ _JS1O=uq%49k/Rv}?}dC}dD>\tlCE?7L*bHba|"ja.*e^10Y5Y0SG2jzo~pBz-'I~MI@DBE$:VL4dlc"r"!"

[+] Synchronized Frame 98 Isolated at Symbol Offset 1054480:
    ├── Extracted APID Subsystem ID : 0x1D0
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D0 A2 E9 A2 1F 2B 46 7A 61 FD BE 73 90 1F AD
        53 59 14 AD F1 31 90 2F BB 37 99 10 ED 51 73 51
        0F 45 B3 09 04 FF 4B 11 51 23 42 B1 0F 30 D6 79
        18 C8 87 8C DB CC 88 76 68 BB 00 A7 82 D1 86 9A
        77 EC B8 A7 86 E1 50 97 C0 2F 5D 0C 44 C3 CE E1
        E4 44 3A C4 5D F0 43 C1 6C C1 4D 1F F6 DE 74 C1
        F2 A8 6A 44 1D B6 86 2E 41 73 FE E2 22 1D 4A 2E
        22 25 F2 B6 61 A2 8F 7B 62 3E 61 F8 95 35 10 4E
        DB E3 31 30 AB 99 51 11 0E E5 D7 3D 00 FA 5B 30
        D1 47 7B B7 14 30 7C AA 52 9A 27 26 A1 88 80 7C
        4E FA C8 87 DE CB B4 88 7C 2D 98 69 A3 BE C8 8F
        89 7F 15 BD 5C 53 F5 DA C4 4C BE 3E 86 44 43 B9
        45 CB 44 3F 16 0C 94 D3 FE FC C5 E4 1F 06 94 AC
        49 5B 68 43 22 5F 73 6E 32 61 DC B2 E4 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+FzasSY1/7QsQEKQ#B0yvhwP/]DD:]ClMtjD.As"J."%a{b>a5N10Q=[0G{0|R'&|N|-i\SL>DCED?I[hC"_sn2a"

[+] Synchronized Frame 99 Isolated at Symbol Offset 1065240:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        61 DF A2 E6 00 1F AB 66 9A 68 FC B6 21 46 2E 85
        6F 57 20 ED 64 31 77 4F F9 B3 11 10 FE 5D 73 D1
        0F 95 B3 0D 24 FF FB 71 7B 0B D9 A5 8B 32 F6 FB
        58 D8 87 FC DB 88 88 76 68 B9 28 87 C2 D1 9A 92
        7D EC BC 60 97 E7 54 C4 85 7B 4F 0C 44 CB E6 65
        44 44 3A C6 5C F0 43 C1 64 C5 4C 3F F2 D4 74 CB
        F0 A9 62 E2 9D BE 56 62 21 F1 26 E3 22 1D FA 2E
        38 21 FE B6 62 A6 9F F1 6A 3E 60 6A 55 25 33 4A
        DF 63 31 32 FE 98 71 91 0E CD 57 04 10 F2 5B 30
        D3 0F 75 B7 9D 30 FE BA 32 9A 87 21 A1 9C 98 7E
        CD B8 C8 87 52 C9 8C 88 78 2D 19 E9 27 F2 CB 8F
        C9 5E 1D 0D 4C 52 B7 C2 C6 4C 7A E6 9C 64 43 BB
        45 C1 00 3F 16 8C 74 53 FE 6D E7 9C 9F 06 84 AC
        EB D3 EC 67 26 1F 3F 2F 22 21 DC A2 67 A0 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "afh!F.oW d1wO]s$q{2Xvh(}`T{ODeDD:\CdL?tbVb!&".8!bj>`jU%3Jc12qW[0u02!~Rx-'^LRLzdCE?tSmg&?/"!g"

[+] Synchronized Frame 100 Isolated at Symbol Offset 1076000:
    ├── Extracted APID Subsystem ID : 0x1FF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FF B2 E9 82 1F EB 46 1A 28 FF F6 23 A6 5F 93
        56 5B 04 AD FC 31 12 0F 39 37 99 30 EF 7D 73 91
        0F 05 B3 2D 20 79 8D 31 DB 06 D7 81 89 80 F6 3A
        18 88 87 F2 DA 88 88 76 28 BB 60 87 F2 D9 9E 92
        7E FD B8 29 87 E1 52 D4 99 7B 7D 8C 64 C3 D7 E5
        C6 44 3B 94 DC B4 43 F9 68 C3 4D 3F 95 DC 74 43
        BA 28 E2 42 9F AA 86 62 25 F1 3E E3 22 1D CA 2E
        E2 21 F6 B6 6D A4 1F EE 2E 7A 61 FB 57 B5 30 5A
        CE E3 11 30 FC DB 59 13 0F E5 17 34 90 F8 59 72
        53 0F 91 F5 95 10 EC 3A 5A B0 27 6D A5 9C 98 7C
        EC 3C 89 87 FA 89 B6 C8 7C 2D 98 69 27 CD DB CE
        88 7E 15 4D 68 02 97 D0 C4 CC 3C 62 D6 44 43 F3
        44 DF 64 3C D6 CC 94 C1 F1 6D E1 4C 1E AE 86 A6
        41 F9 6B 63 26 5E 74 6A 62 21 DC A2 E7 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!F(#_V[1970}s- y1:v(`~)R{}dD;ChM?tC(Bb%>".!m.zaW0Z0Y4YrS:Z'm|<|-i'~Mh<bDCDd<mLAkc&^tjb!"

[+] Synchronized Frame 101 Isolated at Symbol Offset 1086760:
    ├── Extracted APID Subsystem ID : 0x5F0
    └── Full Decoded Frame Payload Hex (223 Bytes):
        25 F0 B0 E7 A2 1F CB 26 0A 69 FF B6 A1 C6 1F 87
        56 72 25 EC F0 31 00 0F FF B5 01 10 EE 51 70 D1
        0F C5 A3 3D 24 F7 8B 31 D1 0F C3 A1 A9 98 76 7A
        1A 89 87 C4 D9 4C 88 75 28 38 EE 87 CA D9 8A 8A
        7C F4 A8 E1 A1 E3 D0 D5 C1 3B 39 0C CC 03 F9 CD
        C4 44 3B 17 5D F4 03 D1 6C C3 40 3E 66 DC F6 63
        F0 6C E2 E2 9D 87 96 32 65 F3 66 B2 22 1F CA 2E
        3A 01 FC B6 61 A2 9D B3 EF 3A 21 EA 54 35 27 4E
        DE 43 11 32 F0 BB 31 11 0E DD 57 69 10 F8 5F 30
        D1 67 BE 95 0D 10 BC 2B B8 91 07 6D E1 88 99 7F
        4C 18 88 87 C2 8B B6 40 7A 2D 88 29 A7 EE 99 CB
        98 7E 1D DC 48 52 F7 D0 C4 44 7F 6F 8E 44 4B B1
        45 C9 40 3E D6 0C 14 D3 FC 64 E5 48 3F 0E D6 26
        C3 F8 C0 62 26 1E 33 2B 22 21 DD EA E6 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "%&iVr%1Qp=$1vzLu(8|;9D;]l@>fcl2ef".:a:!T5'NC21Wi_0g+mL@z-)~HRDoDKE@>dH?&b&3+"!"

[+] Synchronized Frame 102 Isolated at Symbol Offset 1097520:
    ├── Extracted APID Subsystem ID : 0x1D6
    └── Full Decoded Frame Payload Hex (223 Bytes):
        61 D6 A2 E6 A2 1F 4B 66 4A 61 F0 52 A1 E6 1F C5
        42 13 64 FD 7C B1 B3 0F 18 37 01 50 EC D1 73 A1
        0F 05 93 0D 34 7D DD 30 99 0F CE BD A9 02 F6 F9
        18 89 07 8C D9 88 88 74 2A 99 CC 87 D6 D9 82 9B
        7D E9 A0 6D 87 E0 DC DC DD 2B 4F 2C 44 83 F6 E9
        C6 44 3F 14 5C 84 43 F1 68 C1 44 3E 76 44 60 43
        F9 E8 69 E4 9D BC 26 62 61 F1 36 C3 20 1D 4B AE
        5B 21 F0 B6 61 A6 1F FD EE 3A 65 D8 F5 75 34 4A
        C7 4B 13 70 FB F7 79 11 0E B5 53 79 10 F5 5B 30
        D3 4F BC B7 1D B0 FE 3A 5A 9A 8D 6F A5 88 98 7D
        CD BC 88 07 72 CB A8 80 7D AD 19 A9 27 FF 5B 8E
        08 1F 15 09 4C 16 B5 F2 C4 00 3F 2C 1E 44 43 BB
        65 CF 04 3E 17 4C 14 03 FF ED C5 0E 1F C6 D6 A6
        49 FF D8 62 2A 1E 75 6E 32 21 DC F2 E7 A0 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "aKfJaRBd|7Ps4}0t*}m+O,DD?\ChD>vD`Ci&ba6 K[!a:eu4JKpySy[0O:Zo}r}'[L?,DCe>LIb*un2!"

[+] Synchronized Frame 103 Isolated at Symbol Offset 1108280:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        A1 DD AA E6 B2 5F AB 06 1A 28 FF B6 A3 A6 0F D5
        63 57 05 FD BE 31 32 0F 99 B7 91 10 FC 55 10 18
        0F B5 A3 0D 30 FE 9B 11 DB 2F D2 B5 A9 B0 76 DF
        18 C8 07 CC FB 8C 88 76 AA B9 8C 87 82 D1 86 92
        7C 7D B8 E9 81 E3 58 D6 C1 3E 7D 0C 44 C3 EE 68
        44 44 3F 94 4C D4 43 D9 60 C3 4D 1E FF DE 7C 43
        F0 E8 E2 62 B5 9E 86 36 61 FF 62 62 22 1D 8A 2E
        D2 25 F6 B4 61 A2 9E 7A 67 38 26 FC D4 F5 71 5F
        D3 4F 1B 30 F3 BB 79 11 0F B5 13 18 90 F8 5B 31
        53 47 EC D7 0C B0 7C 2A 1A D9 A7 61 A1 89 00 FC
        6D 2C 88 87 76 CB BC C0 7C AC 98 69 07 F6 DB 8E
        D8 7E 15 4D 48 07 F7 90 84 44 BC 64 9C 44 43 B9
        64 CF 64 3E F6 8C 74 C3 F7 E1 61 8C 7F D6 86 BE
        21 FB 6C 62 66 5F BB 76 22 21 D4 A2 E3 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "_(cW12U0/vv|}X>}DhDD?LC`M|Cb6abb".%azg8&q_O0y[1SG|*am,v|i~MHDdDCdd>ta!lbf_v"!"

[+] Synchronized Frame 104 Isolated at Symbol Offset 1119040:
    ├── Extracted APID Subsystem ID : 0x1FF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        A1 FF A2 E6 A2 1F 1B 26 5A 69 FB 52 69 92 1F 8D
        43 1B 64 BC 52 B1 10 0F CB D7 91 10 FE 59 77 D1
        0F E5 33 05 80 7F 5F 19 D3 0F E7 A1 A9 18 70 58
        18 D9 87 C5 CA C8 88 75 AA B8 D9 87 DA D9 82 9A
        3F ED 38 E9 87 E9 50 D6 C1 7A 79 0C CC D3 CB E5
        C4 40 39 94 4C DC 43 E9 68 CC 4D 3F F6 5C 76 C2
        F2 AE 6B E0 9F 9E 86 32 61 E6 36 F2 22 1D 0A 2E
        FB 01 F6 B6 65 A6 9F 7B 27 3A 69 7E 54 35 30 4F
        87 03 33 31 FD BB 19 11 0E FD 97 3D 10 F1 5A 30
        D3 47 DA F7 9F 91 36 4A 9B 99 8D 6D D5 88 80 71
        FD BC 98 87 62 EB AA C8 79 AC 98 69 A7 C4 4B 8B
        09 4E 5D 9C 4D 12 B5 C0 C6 4C BF 06 D4 64 43 BB
        55 CD 44 3F 56 8C B4 DB FF 6D D7 CC 3F 2A A6 A6
        A9 FA E8 62 66 1F 12 EA 22 21 DE B6 E5 10 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "&ZiRiCdRYw3_pXu?8Pzy@9LChM?\vk2a6".e{':i~T50O31=Z0G6JmqbyiKN]MLdCUD?Vm?*bf"!"

[+] Synchronized Frame 105 Isolated at Symbol Offset 1129800:
    ├── Extracted APID Subsystem ID : 0x1F9
    └── Full Decoded Frame Payload Hex (223 Bytes):
        29 F9 B2 E7 92 1F 1B 66 1A 2D F5 9E 63 F6 1F 9D
        4B 32 45 ED BC B1 23 0F F9 A7 09 10 EE 99 33 D0
        0F 85 A3 0D 24 68 19 79 F1 2F A1 A5 AD 30 76 B1
        58 98 07 84 C4 88 88 7D 3E B8 C8 87 C2 D1 A4 90
        7F ED AC A1 87 EF D2 C4 C4 3B D5 0C CC CB CE 79
        C4 C4 3B B4 5C F4 43 C1 60 C3 4D 1F F7 DC 34 C9
        F6 6C 6B 60 9D 9F 86 22 65 E1 BC E3 26 1F 0B 26
        7B 21 E0 B4 61 A2 1F 59 6B 32 27 F9 D4 75 71 46
        DF 23 13 30 F9 DB 71 93 0E C5 57 3D 90 FA 5B 30
        93 0F BB B7 1D 32 FD 5B 5A B9 25 6F E1 AC 98 7E
        F9 28 88 85 72 A9 9E 88 7E 2D 98 28 83 DD 5B 8A
        59 5E 55 0C 6C 03 B3 D8 C4 4D BC E6 9C 64 43 A1
        75 DE 60 3E 16 4C 34 53 ED 6D 43 6C 1F 22 A4 AE
        01 DB E1 62 66 5F 33 06 12 01 D1 A2 E7 F2 1D
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ ")f-cK2E#3$hy/0vX}>;y;\C`M4lk`"e&&{!aYk2'uqF#0qW=[02[Z%o~(r~-([Y^UlMdCu`>L4SmCl"bf_3"

[+] Synchronized Frame 106 Isolated at Symbol Offset 1140560:
    ├── Extracted APID Subsystem ID : 0x155
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 55 A2 EE B0 1E 6B 66 3A 29 FD B2 F3 86 7F 97
        52 1B 25 FD EC B1 91 2F 89 16 13 10 EF D1 36 C1
        0F 95 83 2D 14 7F 5B 11 71 2F 5A A1 A9 92 76 9A
        18 98 07 CE BB 88 A8 76 2C B9 68 87 82 DB 96 98
        3F A5 B8 A9 81 E8 50 97 C5 3B 5D 4C E4 CB C6 6C
        74 54 3B D4 5C 66 03 CB 68 C7 4D 1E F2 DC 54 CB
        F9 AA 42 64 95 B6 86 22 61 E9 60 A2 22 1D CA 2E
        39 21 F2 B2 67 A2 9F 59 67 2A 60 75 74 35 B1 5E
        9F 43 11 30 FB BA 71 11 4F A7 17 4C 10 F5 59 34
        D3 4F BC B7 1F 90 FD 4A DA 98 2D 6B E5 88 98 7E
        EF 9A 88 87 72 8B 8E C8 5D 2C 98 29 A3 FA FB 82
        58 5E 25 3C C9 96 F5 80 C6 4C 3D 16 4E 45 C3 B9
        E5 CE 44 3E B6 CC 34 D1 FF ED CB 44 3D 0A E6 26
        C9 5B 68 66 20 1E 7F 26 22 21 D8 A8 E0 B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "Ukf:)R%/6-[q/Zvv,h?P;]LltT;\fhMTBd"a`".9!gYg*`ut5^C0qOLY4OJ-k~r],)X^%<L=NED>4D=&[hf &"!"

[+] Synchronized Frame 107 Isolated at Symbol Offset 1151320:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 EF 80 1E 6B 66 1A 29 79 B2 73 A6 5F 89
        66 36 14 FD E4 31 12 0B 99 B6 91 12 FF 59 74 C8
        0F 05 B3 3D 24 FC 9F 39 DD A3 E2 BF 39 0A 76 3A
        18 88 07 8C 9B 8C 88 75 68 9B 88 A7 EA C1 86 9A
        7B EF 88 24 83 F5 50 C4 C5 3B 6D 8C 44 4B FE EC
        E4 44 3E 14 4D 74 42 E5 68 C3 4D 3F E6 54 64 C1
        F2 A9 4A 6C 9F BE 06 22 25 F7 F2 E3 22 1D 47 26
        17 21 F4 B2 61 A6 1F 75 EF 0A 26 F2 54 F5 72 4E
        CF 4B 19 30 FF F9 39 13 0B AD D7 25 10 F2 5A 31
        D2 4F E9 87 3E 30 7C A8 12 39 85 7F 21 BC 91 7C
        CC 3E 88 87 E2 89 B6 80 7C AD 18 29 87 FA F9 82
        98 76 0D C8 70 12 FF D0 C4 44 3E 6E CC 44 43 FB
        C5 CE 54 3C 96 4C 34 93 F3 64 C7 5C BF 66 86 F4
        09 DB F1 E6 66 1E BD 6E 22 21 DC BA 63 80 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!kf)ys_f61Yt=$99v:uh{$P;mDKD>MtBhM?TdJl"%"G&!au&TrNK09%Z1O>0|9!|>|)vpD>nDCT<L4d\ffn"!c"

[+] Synchronized Frame 108 Isolated at Symbol Offset 1162080:
    ├── Extracted APID Subsystem ID : 0x1DB
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DB A2 E2 02 16 AB 06 5A 21 FF B6 E3 A6 0F C5
        5A 5A 40 ED B4 71 93 0E 4A 11 19 10 EB DB 73 15
        4E E5 B3 15 24 BD 4D 71 D3 B3 CB A1 A9 82 F6 50
        18 D9 07 CF CA E8 88 7F 68 B9 E4 A7 D2 F9 86 9B
        7E 7D B8 FD 87 A0 D3 94 C1 3B 3F 0C C4 83 E2 49
        F4 4C 2B BE 4D E4 43 CD 68 C3 45 3B C2 D6 1E C1
        F2 AD E2 C0 9D 97 C6 32 61 F9 C0 62 26 1D EB 2E
        08 21 F2 B6 61 A2 1F EF A6 3A 21 F8 34 25 37 4E
        CF E3 33 32 FB 99 79 11 0E DD 17 77 10 E0 59 33
        D3 4B BB D7 17 30 FC 2B 1A 98 0F 67 95 88 90 7C
        EF B8 88 87 E2 8B 98 88 77 AD 98 48 A7 B6 CB 8F
        89 7F D4 0D 4C 53 B7 D0 CC 40 3E 66 DC 44 43 B9
        45 CE 44 3E 16 8C 34 83 F9 7D E3 2C 1F 12 8E A4
        8B DB D8 62 46 1F 77 6F 32 21 DA AA E8 82 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!Z!ZZ@qJsN$MqPh~};?IL+MChE;2ab&.!a:!4%7N32ywY3K0+g|wHLS@>fDCED>4},bFwo2!"

[+] Synchronized Frame 109 Isolated at Symbol Offset 1172840:
    ├── Extracted APID Subsystem ID : 0x1DB
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DB A0 EF 92 1E AB 66 CA 01 F6 EE A3 E2 4F C7
        4A 53 10 EC E2 B1 12 2F BF F7 11 10 ED 59 35 C1
        0F A5 93 0D 20 FE 9D 71 79 2F E8 A5 8D BA D2 F8
        58 89 97 9F D3 CC 88 7C 68 98 E0 87 C2 99 82 9A
        1D E5 B8 81 A7 E5 D3 CF D1 3F 2D 0C 40 D2 E3 6C
        45 45 3F 94 44 F0 42 A1 64 C5 4C 3F 97 CC 38 4A
        F0 2A 6A 62 9D BF 86 26 61 F7 82 F2 22 5D 3A 2E
        6A 01 E0 AA 68 A6 8F 93 2E 2E 61 FC 54 35 36 4A
        C7 43 31 30 FD FB 31 11 4B F5 17 61 10 F9 5A 34
        D1 46 F2 B3 1D 92 FD EA 58 90 AF E7 C1 88 98 7E
        FC B8 08 87 66 9B B6 88 75 2C 98 28 A7 FE 9B C7
        99 1B 75 BC 4C 02 B2 D9 C6 4C 3F 20 DC 44 43 B1
        45 DF 4C 3E 16 CC 74 D1 FF 7D C7 4C 0F 1A A6 BE
        01 FB E8 66 22 9F 53 46 22 21 F5 A2 6D B2 9F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fOJS/Y5 qy/X|h?-@lEE?DBdL?8J*jb&a"]:.jh..aT56JC101KaZ4FX~fu,(uLL? DCEL>t}Lf"SF"!m"

[+] Synchronized Frame 110 Isolated at Symbol Offset 1183600:
    ├── Extracted APID Subsystem ID : 0x1D6
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D6 B2 6E A2 1F 0B 4E DA 61 FA F6 61 86 4F D7
        66 53 04 E4 B4 33 93 0B B9 B5 11 10 EC 51 51 91
        0F B5 93 0D 34 EC 8B 10 F3 2F E2 B3 8B 22 56 B3
        38 C9 87 EE 8B 88 88 57 2E B8 CC 87 AA C9 96 C0
        3F 8C B9 A0 91 E1 58 D1 D0 2B 3E 2C 44 C3 FE 58
        E4 44 3F B6 4C F2 43 C9 60 C0 49 1F DE DE 30 C8
        F0 A9 6B 60 9F BE 86 72 41 F7 32 E2 A2 1D 2B 2E
        BA 21 C0 B6 62 A6 8F 23 6E 52 25 7D 55 75 A0 1A
        DE 23 31 32 F9 9F 71 11 0F B5 13 35 90 FD 58 31
        50 47 CD D3 0E 30 BD 9B 32 B8 0F EF A1 88 99 5C
        CE 2A C8 87 72 99 96 88 7C 2D 18 69 A7 F4 DA 92
        58 7E 5D 18 4D 03 B7 F4 C6 4C 3F E6 C6 64 43 B9
        44 DB 0C 3F 16 CC 34 D3 FD 3D F3 EC 2F 4A 84 BE
        0B DB D5 66 26 1F 32 8A 32 21 DC FA 6D A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!nNaaOfS3QQ4/"V8W.?X+>,DXD?LC`I0k`rA2+.!b#nR%}Uu#12q5X1PG02\*r|-iX~]ML?dCD?4=/Jf&22!m"

[+] Synchronized Frame 111 Isolated at Symbol Offset 1194360:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC BA 66 30 1D 0B 06 5A 09 F4 9E E2 16 5F E5
        42 17 04 AE B9 31 93 0F 5B B5 11 10 EE 51 73 41
        0F A5 B3 0D 24 FB D9 70 D3 07 52 A9 0F 88 76 D0
        13 89 87 FD F0 80 8A 7E 28 98 6C 87 DA D9 9A 9B
        79 CE 98 E1 93 F5 D0 D6 C1 3F 7F 0C C4 C3 EA 75
        E4 44 3B B6 5C 36 C3 E1 6C C7 4D 3F 96 CE 54 4B
        F0 A8 6B EA 1D AA 86 22 61 F4 26 E9 22 1D 6A 26
        CB 21 F0 B6 65 B0 9E FF 6E 3E 61 F8 90 35 30 0F
        CF 62 33 20 F3 B3 51 91 0E E5 17 7C 90 F0 5B 32
        D3 4F F5 B5 1F B8 7D 2B 9A B8 27 6F A1 88 9A 78
        4D 38 99 87 02 8B 98 88 7E ED 99 69 03 CF E9 8E
        C8 7E 05 0C 58 87 B1 F0 C4 4C 3C F7 CE 64 43 B3
        44 CE 44 3E 96 0C 34 D3 FE FD C7 4C 37 1A A6 B4
        01 5B C8 62 64 1F 1F 2E 72 21 D0 B2 E0 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!f0Z_B1[QsA$pRv~(ly?uD;\6lM?TKk"a&"j&!en>a50b3 Q|[2O}+'oxM8~i~XL<dCDD>4L7[bd.r!"

[+] Synchronized Frame 112 Isolated at Symbol Offset 1205120:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD A2 62 A2 1F 0B 46 2A 6D D7 36 63 C6 1F 8F
        6B 1B 01 ED F8 B1 93 4F 99 B5 51 10 EA 53 32 51
        0F 05 97 1D 34 F3 D3 51 53 26 F0 A1 AB A0 76 FA
        18 99 87 C4 DA C9 88 77 0A B9 60 87 D2 D9 86 9A
        3F E5 A8 F9 87 E2 D0 D4 81 3B 0F 8C E4 C3 EE 79
        C0 54 3B 14 4D F4 03 D9 6C C3 49 1F B6 DC 72 CA
        F0 ED 6A 60 1F 9C 86 72 69 E7 70 E2 22 1D 6A 2E
        22 21 EC B2 63 A6 9F E7 2A 2A 65 FA 57 B1 32 5F
        DF 03 11 32 F1 BF F1 11 6A C5 13 3C 90 FC 59 36
        D3 4F B5 D3 0E 32 BD 0B 32 98 07 7B A1 8C 89 7E
        78 1C A8 A7 72 8B BE 08 7B 2D 18 E9 A7 7E 62 86
        5A 7E 05 8D 4C 17 B4 D8 CC 44 3E E6 CC 44 4B B9
        E5 CC 44 3E 16 CC 14 43 F9 6D 43 6C AF 46 C4 A6
        49 D9 68 62 24 1F 36 6E 22 21 DA A2 E7 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!bF*m6ckOQS2Q4QS&vw`?;yT;MlIrj`rip"j."!c**eW2_2j<Y6O22{~xr{-~bZ~LD>DKD>CmClFIhb$6n"!"

[+] Synchronized Frame 113 Isolated at Symbol Offset 1215880:
    ├── Extracted APID Subsystem ID : 0x1CE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 CE A2 E7 92 1F 3B 66 1A 28 FF AE E1 F6 1F C5
        6F 16 44 AD F4 31 92 0F 19 33 1D 70 EA 51 72 99
        0F 95 A3 0D 34 FE B9 40 52 2F C8 A1 A9 90 76 FB
        18 9A 17 DE C3 88 A8 7E 28 B9 48 07 C2 C1 9A 9A
        7F D7 98 E0 87 E5 D4 C4 D1 3F 28 AC 4C C3 DA 69
        E6 44 3B 96 5C F6 03 C9 68 C1 49 3F E2 56 B0 C3
        F8 28 6A E4 3F BE C6 22 A1 E3 BE 22 2A 1D CA 2E
        70 09 F8 B6 61 A2 8F 33 6E 0A 60 D8 75 31 30 5A
        DE 63 19 32 F1 9F 70 11 0E E5 17 18 94 F8 5B 32
        53 4F 8E B7 1F B0 FD AB FA 98 A7 67 A1 A8 89 7C
        DC 28 C8 87 FA 8B 9A 88 7C AC 99 E8 A7 D8 D9 4A
        9D 5E 3D 09 59 03 F3 B0 CE 4C 2C 67 DC 45 C3 CD
        44 CE 64 3C 17 CC 34 D3 E9 E4 C7 4C 27 0A 8E AE
        0B DB 60 62 26 1E 33 C7 02 21 DC A2 EE 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!;f(oD13pQr4@R/v~(H?(LiD;\hI?V(j?""*.pa3n`u10Zc2p[2SOg|(|J^=YL,gEDd<4L'`b&3!""

[+] Synchronized Frame 114 Isolated at Symbol Offset 1226640:
    ├── Extracted APID Subsystem ID : 0x1D4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D4 A2 E1 02 5F EB 26 1A 69 FF 3E 71 A6 1B A3
        43 56 15 FC E6 23 13 0F A9 31 11 10 EA 51 71 D3
        0F A5 A3 05 14 EF 19 20 63 0F C6 A3 8D 8A 76 98
        18 99 97 FE B3 80 89 76 28 9B C8 87 C2 F9 96 92
        7F 0D 88 E8 85 E5 55 C5 C5 2B 6D 0C E4 C3 E6 64
        44 44 3A 14 5C F6 43 E1 64 C3 4D 3F D6 D4 7A 41
        F2 E9 6B C2 9D AD 86 26 05 F7 A4 22 22 1F C2 2E
        5A 21 D0 B0 60 A4 9F 71 6E 3A 61 DF 34 35 32 5E
        C3 03 31 10 FD 9B 71 91 0E 85 17 19 10 F8 59 30
        D3 47 99 D3 94 10 FA 0A 30 B8 27 61 C1 88 98 7E
        FD 88 8A A7 52 A9 9E 80 7A 2C 99 E9 87 FB F8 87
        9C 7F 25 6D 5C 17 F2 B8 C4 5C BC EC 94 4C 43 B3
        44 CF 40 3E 96 C4 B4 D3 D9 65 63 05 3F 52 C4 24
        AB D3 48 63 66 1E 13 66 22 21 DC A2 62 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!_&i>qCV#1Qq cvv(U+mdDD:\CdM?zAk&"".Z!`qn:a452^1qY0G0'a~Rz,%m\\LCD@>ec?R$Hcff"!b"

[+] Synchronized Frame 115 Isolated at Symbol Offset 1237400:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        81 DC A2 E7 82 1F 8B 46 1A 69 F3 92 A3 C6 1F E7
        2F 5B 35 E9 F6 B1 13 0F 29 95 11 10 EE 55 75 D0
        0F BD B3 0D B4 FD DB 71 53 0F D2 B3 8B A2 76 DA
        58 99 87 EC D3 8C 8A 7F 2A B9 68 87 CA C1 86 98
        7E CC B4 AC 85 F1 57 C4 C1 3F 58 2C 6C 4B EE 4C
        C4 44 BF 14 4C 92 43 C1 68 CB 4D 3B F2 74 14 C3
        F1 2C EA 40 97 BE 8C 22 61 FB 2F 72 22 15 0A 26
        7B 21 F0 B6 61 A6 97 69 AE 2E 60 5E 56 A5 30 4E
        DC C3 18 02 FD 99 31 11 4E CD 17 0D 80 F8 5B 72
        D1 4F FC F6 9E B0 BC 08 1A 9A 25 CB E5 89 99 7C
        39 2C 88 87 5A AB B0 40 7C AC 98 E9 A3 FF 69 83
        D8 7E 35 2D 4C 47 B2 90 C4 C4 3E 45 DC 44 4B FD
        45 CB 20 3E 16 8C 34 11 BC 64 C1 4C AF 2E A4 AC
        2B D9 CC 67 26 1F B2 E3 62 A1 FD E2 67 80 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "Fi/[5)UuqSvX*h~W?X,lKLDLChM;t,@"a/r"&{!ai.`^V0N1N[rO%|9,Z@|i~5-LG>EDKE >4dL.+g&bg"

[+] Synchronized Frame 116 Isolated at Symbol Offset 1248160:
    ├── Extracted APID Subsystem ID : 0x1D0
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D0 A6 E3 82 9E CB 06 1A 48 FC 9E 63 E6 1F A5
        57 13 15 EC F0 B1 11 2F 89 97 11 10 EE 55 73 40
        0F 45 B3 05 14 FB FB 71 63 2F E0 B9 AB 0A 76 57
        18 89 97 AC C9 8C 88 7D 28 9B C8 87 DA D9 86 9A
        3F 6C B8 A9 87 EB D3 D4 91 3B 7D 0C 44 CB E6 E1
        44 44 3A 16 4C FC 43 E5 6C C3 4D 3F F6 CC 74 03
        F0 A8 EA 6A 1D AE 0E 22 29 F5 2A A2 22 1D CA 2E
        79 21 F4 B6 67 A6 9F DB 6E 36 64 F8 D4 25 E0 4E
        DF 03 11 32 F8 9C 31 91 0F A5 53 3D 92 FA 59 31
        D3 0F FD B7 1D 30 FC 6A BA D0 27 EF 85 8D 98 7C
        49 38 88 87 72 CB 8C 88 78 2D 99 69 87 FC FA 8F
        98 7E 95 0D 6C 92 B3 D0 CC 48 BE E5 D4 44 43 B9
        65 CC 44 3E D6 CC B4 C3 FA 69 C5 4C 9D 8A A6 2E
        01 DA E9 62 26 5F 33 2E 22 21 DE E2 EF A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!HcW/Us@Eqc/vW}(?l;}DDD:LClM?tj")*".y!gn6d%N21S=Y10j'|I8rx-i~lHDCeD>iL.b&_3."!"

[+] Synchronized Frame 117 Isolated at Symbol Offset 1258920:
    ├── Extracted APID Subsystem ID : 0x1F4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F4 AA EF A0 1F 8B 66 2A 28 F7 96 E1 A6 5F 81
        46 53 05 ED EE 31 53 0F DF A3 11 10 EE D1 77 41
        0F C5 B3 0D 30 FF 8B 30 43 0F EB A5 A9 32 7E F2
        18 89 87 ED 92 88 88 77 28 B8 EC 87 D2 C9 86 82
        7C ED AC E9 97 E9 D8 86 59 3B 79 2C 6C 83 E6 FD
        C6 4C 3F 95 4C 96 43 C1 6C C1 4D 3F F6 DC 3C C1
        F0 28 6A 60 9F BE 86 76 41 F3 30 E3 22 1D FB 2E
        2A 21 F0 B4 61 A2 1F F9 EA 1A 61 FC 55 35 E3 5F
        CF CB 19 30 F1 DB 71 11 0E FD 57 39 00 FC 5B 32
        D3 4F D0 D3 1D 30 BE 3A 1A 18 AF 69 B1 88 98 7E
        CB 08 88 87 F2 AB 92 88 74 A9 19 2D 87 FE 7B CF
        D8 3F 15 0D 48 12 B6 F0 CE 4C BF 64 DC 44 43 F9
        45 CD 44 3E 16 8C B4 D3 FF 6C 47 04 3F B2 86 BE
        69 7B D8 62 22 1E 2F 2F 22 21 DC A2 E6 B2 1C
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!f*(_FS1SwA00C2~w(|Y;y,lL?LClM?<(j`vA0".*!aaU5_0qW9[2O0:i~t-{?HLdDCED>lG?i{b"//"!"

[+] Synchronized Frame 118 Isolated at Symbol Offset 1269680:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE A2 E6 A2 1F CB 66 1A 69 FB B6 23 B6 5F A5
        43 53 04 ED B0 B7 31 0F 49 97 11 30 EF D1 75 91
        0E 05 B3 05 14 F9 1B 31 CB 0B F0 AD 89 8A 76 FE
        18 88 17 9E 9A 8C 88 7E AC BB C8 87 0A C1 86 80
        7F 75 AC 69 87 E1 D6 D4 C5 3B 7E 0C 44 83 E6 7C
        C4 44 3B 94 4C C4 43 E1 60 CB 45 1F 7E D4 70 C3
        F4 AA 6A C0 9D BE 86 22 E1 F7 BE F2 22 1D 4A AE
        5A 21 C2 B6 61 A6 1F EF EE 3A 61 F9 D5 31 75 0F
        DF 63 13 22 FB 9B 71 11 0E AD 97 35 94 F8 5B 32
        D2 4F ED B5 0D B0 BC 4A 5A B8 25 6D 21 89 99 7C
        FE B8 C8 87 FA 8B 9E C8 78 AD 99 A9 27 CE EB 86
        89 5E 05 0D 68 17 B7 D2 C4 4C 3C FC 56 44 43 B9
        65 DD 44 3E 16 CC 34 43 FF FC C1 44 1F 5A C6 26
        8B 5B F8 63 22 1F 93 CF 32 21 FC A2 66 B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fi#_CS1I0u1v~ui;~D|D;LC`E~pj""JZ!a:a1uc"q5[2OJZ%m!|x'^hL<VDCeD>4CDZ&[c"2!f"

[+] Synchronized Frame 119 Isolated at Symbol Offset 1280440:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        61 DC A2 64 B2 1F 2B 66 7A 69 FF DA 62 86 17 95
        67 13 11 ED 28 31 13 0F B9 35 91 10 EE 55 73 D1
        0F 95 A3 0D 34 FE FB 71 C3 2F C1 B1 29 A2 FE F2
        58 89 87 C4 F1 8C 88 7F 28 B8 A0 87 42 D9 96 9A
        7C FD 98 E9 83 E9 5A D4 D1 3A 5F 1C 4C 43 E6 E4
        C4 44 3F 96 5C 3C 03 C5 68 C2 4D 1F E4 DE 3C CB
        D0 A9 E2 64 9F AE 96 F2 09 E7 64 A6 22 1D CB 2E
        DA 01 E4 B6 6D A6 9F AB 62 38 E0 FD 54 E5 30 4A
        DF 43 11 30 F2 9B 69 11 4E E5 17 35 10 FA 5B 32
        D3 0F 94 B7 0E 32 FC 6A D8 D8 2F 69 C1 88 98 78
        DD 38 88 07 72 8B 96 C8 7F AD 98 69 A3 F8 4B C0
        D8 7A 55 AC 68 03 B7 A0 C6 44 3F 6F DE 84 C3 B9
        45 C7 04 3E 17 CC D4 01 FF AD C7 44 3F 4A B4 BE
        2B FB D8 47 22 1F 73 4A 22 21 DF A2 EF 22 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "ad+fzibg(15Us4q/)X(B|Z:_LCD?\<hM<dd".mb8T0JC0iN5[22j/ix8riKzUhD?oE>D?J+G"sJ"!""

[+] Synchronized Frame 120 Isolated at Symbol Offset 1291200:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD A2 EB 00 1F 2B 26 7A 69 EF 36 70 A6 5F 93
        57 13 25 E3 B4 31 10 0F 1B A7 09 10 FE 51 71 50
        0F 95 B3 0D 14 FF CF 51 79 07 C8 A9 A9 8A 5E 7F
        58 89 97 C4 CA 8C 88 71 2C BB EC 97 92 D1 96 90
        7F 2D B8 E7 87 EB 52 D4 C1 7B 7D 8C 45 C3 DE 7F
        4C 44 39 B5 4C E4 43 F5 6C C3 41 3F B2 DC 30 83
        F1 A8 68 C0 15 BE 46 6E 65 F3 3A B2 22 1F 8A 26
        52 21 D2 B2 65 A4 8F 4B E6 3A 60 7A 14 61 61 4E
        DB E3 31 30 FD 97 71 11 0F 85 D7 1C 10 F8 58 30
        D1 4F AD B7 1E B0 3E 3A 18 DA 25 69 B1 0C 98 79
        4D B8 88 87 76 8B 9E 88 76 2D 98 69 A7 CE C3 8A
        58 1E 75 0C 4C 13 97 D8 DC 44 3E E2 5E 4C 43 BC
        45 C8 04 3E 56 CC D4 C3 FF 74 C1 44 1F 2A EE A6
        89 FA 68 63 26 1F 36 3E 22 61 D8 A2 E4 C2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+&zi6p_W%1QqPQy^Xq,-R{}ELD9LClA?0hFne:"&R!eK:`zaaN10qX0O>:%iyMvv-iXuLD>^LCE>VtD*hc&6>"a"

[+] Synchronized Frame 121 Isolated at Symbol Offset 1301960:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD A2 E1 A2 1D 2B 62 5A 28 FE FA 3B A6 17 CF
        07 52 24 FC E4 31 32 0F 99 11 D9 10 FF 53 33 99
        0F B5 B3 4D 14 FB 59 71 EB 0A F2 B3 8B 3A 56 FE
        D8 89 87 C4 E9 88 88 76 AC 99 A8 87 E2 D1 8E 9A
        7C CF A8 F9 87 C2 55 D4 D0 3F 6D 0C C4 43 E6 65
        64 44 3B D6 5C 7E 43 C9 64 43 4D 1F FE D4 50 4E
        F0 AF CF E0 1F 9F D6 36 21 E9 32 B2 22 1D EB 6E
        50 21 EF B0 65 A6 9F 83 EE 1A 71 FA 56 25 10 1A
        DE 43 13 22 B8 97 71 15 0E E5 13 3D 90 B8 D9 32
        D2 4F 6D 95 1E 30 7C 5B 1A 98 0D EB 21 9C 88 7D
        CA B8 88 87 6E 89 AC D8 7A AC 98 2D 03 EF 59 CE
        81 7F 85 79 7C 12 B6 D0 C4 4C 3E 2E D4 44 43 BC
        65 CF 64 3E 16 8C 54 C3 E8 A5 C5 04 1E 8A 86 0E
        6B DA E8 62 22 5E 13 2F 22 21 F4 A2 E7 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+bZ(;R$12S3MYq:Vv|U?mCedD;\~CdCMPN6!2"nP!eqV%C"q=2Om0|[!}nz-Yy|L>.DCed>Tkb"^/"!"

[+] Synchronized Frame 122 Isolated at Symbol Offset 1312720:
    ├── Extracted APID Subsystem ID : 0x1D4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D4 A2 E2 02 17 CB 62 1A 28 F9 36 23 E6 5F 9D
        43 1A 04 BD F0 35 93 2F 19 A7 91 10 EC D1 73 93
        0F 85 B3 0D 24 FD 9F 70 D3 0B E9 B5 2D 92 7E FA
        18 C9 87 8C D1 98 98 77 AC 99 E8 87 BA D1 86 8A
        74 8D 8C E8 87 E5 D0 95 C1 6B 6D 0C D4 C3 E7 EC
        E6 44 2B B5 4C B4 C3 E1 64 CD 4D 3F F6 DC 36 CA
        D0 2B 4A C0 B5 BF 86 22 61 F7 72 E2 22 1D CA 26
        18 01 E0 B6 61 A6 9F BB 2E 2E 61 F8 F4 25 60 4F
        57 63 11 20 FD BD 59 91 0F E5 07 0D 10 F6 59 31
        D1 4F EC 91 9D B0 DC 6B 9A B0 87 F5 F5 8C 18 7F
        6F 9C 8A 27 F6 E3 B2 00 7A 2D 98 69 A7 F6 EB 8E
        58 5E 1D 5D 7D 13 B3 C2 C6 C8 3A 6F CC C4 43 F5
        54 CF 04 3C 16 CC 54 C0 FD 6D 41 6C 7F 9A A6 A6
        61 59 E5 66 20 1F 3F 6F 22 21 DC A2 EF 32 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!b(6#_C5/s$p-~wtkmD+LdM?6+J"ar"&a..a%`OWc YY1Oko'z-iX^]}:oCT<TmAlaYf ?o"!2"

[+] Synchronized Frame 123 Isolated at Symbol Offset 1323480:
    ├── Extracted APID Subsystem ID : 0x1F9
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F9 B0 63 A0 1F 0B 26 5A 41 FD B2 B3 E2 5F CF
        4A 17 04 EC F6 31 71 2E 99 11 91 10 ED 51 30 D0
        0F B5 A7 1D 24 FE DF F0 D3 2B C2 A3 2B 00 5E FB
        11 88 17 F9 DA 88 8A 7F AA B9 E6 87 92 D9 92 88
        3F AF 3A 64 87 E3 D8 84 D5 3B 3D 0D 64 4B DE CD
        44 44 3F 97 5C F4 43 C1 6C C3 4D 39 8A 5E 74 C3
        F1 AB 4A 48 95 24 D6 60 45 FB 32 A3 22 1D CB 2E
        6C 21 C2 B6 60 A0 1D F9 EF 2C 65 F8 94 65 B0 4E
        DF 63 13 32 F8 93 31 91 0E AD 13 7D 90 F2 5B 30
        D3 47 8D 95 9C 30 7D 0A 38 FA 27 6F A1 8D 88 7C
        6D B8 89 87 FE AB 8E C0 79 AC 9A 29 87 F8 DB 8E
        78 3E 8C 0C 5C 12 B7 D1 CC 4C BE 6B DE 44 42 B5
        51 CF 40 2F 16 0C F4 D1 FF 3F C3 4C 2D 0E A4 AE
        41 7B E0 66 66 5F 77 EE 22 21 F8 A2 66 82 1C
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!c&ZA_J1q.Q0$++^?:d;=dKDD?\ClM9^tJH$`E2".l!`,eeNc21}[0G0}8'o|my)x>\LkDBQ@/?L-A{ff_w"!f"

[+] Synchronized Frame 124 Isolated at Symbol Offset 1334240:
    ├── Extracted APID Subsystem ID : 0x1C4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 C4 B2 E6 26 1F 8B 46 0A 69 FE B6 63 E6 3F A5
        63 53 05 FD F4 31 33 2F BB A3 99 10 FF 99 37 19
        0F 65 B3 19 74 7E DB 38 E3 0B C0 A7 AD 02 7E 76
        19 89 27 24 FB 88 88 7F 68 B8 C6 87 AA C1 92 9A
        7E 6D B8 B1 83 F0 50 D4 C1 2B 7F 8C 54 83 C7 6D
        C6 44 3A B4 4D A0 43 E1 6C C3 4D 1F 6E 5C 58 C3
        F8 E8 EB 68 95 9E 96 6A 61 F3 36 E6 22 1D FA AE
        EA 21 F6 B6 6A A6 8F 3D EE 28 61 F1 D7 B5 34 4E
        D2 8B 30 30 F0 AB 51 11 2E A5 13 65 10 F4 59 32
        D2 4F D9 91 1F B0 BD AA 5A 98 27 69 C5 88 98 7C
        4E 98 88 87 76 C9 8C 80 7C 2C 99 69 A3 FE 42 87
        99 7E F5 19 4C 13 B3 A0 C7 4C 3E 76 5E 44 43 BF
        7D CF 44 3D D6 8C B4 C3 EA 24 C7 6C 3F 72 DE A6
        89 DB 65 62 06 5F 1B 66 22 21 DC A2 E7 82 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!&Fic?cS13/7et~8~v'$h~mP+TmD:MClMn\Xhja6"!j=(a4N00Q.eY2OZ'i|Nv|,iB~LL>v^DC}D=$l?reb_f"!"

[+] Synchronized Frame 125 Isolated at Symbol Offset 1345000:
    ├── Extracted APID Subsystem ID : 0x1CD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 CD A2 E6 32 1F 4B 66 1A 69 F6 BA 61 B6 57 87
        43 52 04 EC 44 31 93 2F D9 F7 17 10 EF 51 70 D1
        0F A5 B3 3D 14 FC FB 70 D3 0F D2 B1 A9 0A FE 9F
        18 D8 87 DC BB 8C 88 77 2C BA CC 87 C2 C9 8A 90
        5E 2D B8 B9 87 E7 52 D5 C5 2B 7D 0C 44 0B C2 68
        C4 44 3E 15 5C E4 42 D1 68 CB 4D 1E 32 CC 3C 41
        F3 AD EA 46 3D BC 16 22 23 F0 3A C3 62 5F CB A6
        7A 21 F4 B6 65 A6 9F FB AE 0A 65 B8 55 25 30 4A
        C3 63 11 30 FB D3 71 91 0E E5 17 65 00 F8 59 10
        93 4F B0 F7 1D 10 3C 9B 12 99 25 67 E1 99 88 F5
        F9 AC 88 87 62 AB BE 89 7F 2C 99 69 A7 DA DB CE
        98 7E 15 0D 7D 97 B7 C2 C4 4C 3E 6E DC 64 43 B9
        45 D1 40 3F 96 4C 34 D1 FE FD 47 0C 3F 06 8C B4
        03 DA F8 62 A6 1F 33 4E 22 21 DD BA E3 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!2KfiaWCRD1/Qp=pw,^-R+}DhD>\BhM2<AF="#:b_z!eeU%0Jc0qeYO<%gb,i~}L>ndCE@?L4G?b3N"!"

[+] Synchronized Frame 126 Isolated at Symbol Offset 1355760:
    ├── Extracted APID Subsystem ID : 0x1D5
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D5 AA E1 20 1F 0B 26 4A 60 FF B6 BA C6 5D A5
        63 13 14 ED F6 21 11 2F BD D7 91 50 ED 55 73 81
        0F 85 B3 2D 34 FF DB 70 E9 2F 50 B1 0D A0 76 FE
        10 D8 97 8D 19 8C 88 7E E8 B8 A8 87 C2 D9 82 8A
        7F AE B8 61 87 F9 58 D6 C0 2B 7D 0C 44 03 E6 4D
        64 44 3F 34 4D 54 43 C5 6C C7 45 1F B6 1C 14 43
        F9 A9 69 64 9D 86 86 22 41 F3 B7 E3 22 1D DE 2E
        38 01 F0 B0 61 A6 8F 3B 66 7B 20 FA 74 35 34 4E
        DE 43 39 32 F3 DA 31 11 0E E5 13 29 00 F9 5B 33
        D3 0F BF D1 9D B2 7C 1B DA A1 27 6F A1 89 98 7D
        FB B8 88 87 62 EB 8C C8 7F AC 18 29 A7 FA DF 85
        89 7E 85 08 4C 13 B3 D8 C6 4C BE 77 DC 4C 43 B5
        44 D7 44 3F D6 8C B4 D3 D7 75 63 44 AF 02 86 A2
        49 FB D4 62 20 9E 73 CE 22 21 DE 22 E7 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "! &J`]c!/PUs-4p/Pv~aX+}DMdD?4MTClECid"A".8a;f{ t54NC921)[3|'o}b)~LLwLCDD?ucDIb s"!""

[+] Synchronized Frame 127 Isolated at Symbol Offset 1366520:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 FC A2 ED B2 1F 2B 66 1A 29 FF 7A 61 E6 07 A7
        47 73 44 ED 7C 31 31 0F F9 97 19 10 FA D1 37 38
        0F 95 B3 1D 14 79 DB 79 61 0F CA A5 AD 88 76 DA
        18 D8 87 64 43 C8 88 77 A8 89 44 87 E2 D1 86 8A
        3B A4 A8 E9 83 67 50 85 D0 6B 6D 0C C4 C3 E2 7D
        C4 4C 3A A4 54 F6 43 ED 6C CF 4D 1E E7 DC 34 C8
        F0 A1 6B 6A 9D 94 86 66 65 E3 32 A3 22 1D AA AE
        2A 01 F6 B6 64 A0 9F D3 6E 39 65 FB 14 65 21 0E
        DE 43 19 30 F9 B1 11 31 0E 85 17 19 00 F6 59 30
        D0 4F C7 B7 1D F2 7E BA 12 9A AF 63 81 88 99 78
        CD BC C8 87 72 8B 8E 48 78 2C 98 69 27 FA EA 8A
        D8 7E 65 2D 48 D6 B3 D0 C4 44 BE 67 9C C4 43 B3
        55 CB 49 28 16 8C 74 D2 EE 2D C7 EC 3F 02 A6 AE
        E3 F8 78 62 42 1F 33 6E 22 21 D1 B2 67 20 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "+f)zaGsD|1178yyavdCwD;gPkm}L:TClM4kjfe2"*dn9ee!C01Y0O~cxrHx,i'~e-HDgCUI(t-?xbB3n"!g "

[+] Synchronized Frame 128 Isolated at Symbol Offset 1377280:
    ├── Extracted APID Subsystem ID : 0x1FA
    └── Full Decoded Frame Payload Hex (223 Bytes):
        A1 FA A2 E7 A2 1F 8B 06 DA 61 FE B2 60 E2 1F 9F
        43 5E 21 E1 B0 B1 52 0F BB D5 1D 10 EA 51 77 D8
        4F C5 A3 15 14 FE 89 19 DB 0F D3 B1 A3 12 5E BF
        59 88 17 8C 8A 88 88 75 6E B9 A8 87 F2 D9 96 9A
        7E 9F 98 B1 95 ED 54 D4 C1 2B 6B 0C 54 43 C2 45
        C4 44 3B 96 5D B5 03 E5 64 C7 40 2F 4A 5E 10 42
        F9 68 4A E4 9D 3F 04 72 41 E7 32 73 22 1D CA 2E
        73 21 E2 B6 61 A2 8F EF 6A 3A 61 F9 57 75 10 5E
        D7 C3 71 30 FA BB 59 B1 0F E5 93 15 90 A9 5B 30
        D1 0B BC F7 15 70 FC 0B 1A F8 87 61 B1 A8 88 78
        5D 38 88 87 62 CB 8C 88 7C 2D 19 28 A7 F2 DB 8E
        18 7E 15 5D 4C 13 B6 C2 C5 40 BE 27 5C 44 43 F1
        45 CB 64 2E 96 4C F4 C1 F7 7D 61 48 3F CA C6 B6
        2B 5B 89 63 26 1F 73 26 02 21 DA A2 6E 82 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "a`C^!RQwO^Yun~T+kTCED;]d@/J^BhJ?rA2s".s!aj:aWu^q0Y[0pax]8b|-(~]L@'\DCEd.L}aH?+[c&s&!n"

[+] Synchronized Frame 129 Isolated at Symbol Offset 1388040:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD A2 E6 A2 1F 8B 66 5A 29 F3 36 70 82 4F AD
        43 57 04 F4 F0 33 13 2F 99 B5 99 10 EF 59 73 D1
        0F 85 B3 0D 34 FF D9 71 F2 07 F2 B7 A9 12 FC F9
        19 89 87 CD DB 88 81 7F 7E BA E8 07 9E D1 86 90
        7F 3D FD F1 87 E9 C8 85 C4 3B 6D AC EC C3 EF 6D
        E4 44 3B B6 5C E4 43 E5 6C C7 45 2E EF DC 1E 43
        E1 A8 CB E0 9D AE 86 22 01 F3 36 73 22 1D 3A 2E
        62 01 F0 B8 61 A4 8F CB E7 3F 21 FD 54 35 F0 4A
        D2 83 19 30 F9 D3 33 11 0E ED F7 3C D0 F8 5A 30
        D2 0F E9 97 1D 42 FD EB 32 99 27 65 A5 89 90 7B
        58 B8 88 87 72 C3 BE 40 79 2D 98 E9 87 7F CA 82
        98 7A 05 29 58 17 B7 C0 C6 CC 3C 65 44 44 43 B3
        44 DF 00 3E 56 44 B6 C3 FD ED E5 CC 1E 56 84 AC
        4B 7B 79 62 66 1F 77 EF 22 21 DC B2 E7 B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fZ)6pOCW3/Ys4q~=;mmD;\ClE.C"6s":.ba?!T5J03<Z0B2'e{Xr@y-z)X<eDDCD>VDVK{ybfw"!"

[+] Synchronized Frame 130 Isolated at Symbol Offset 1398800:
    ├── Extracted APID Subsystem ID : 0x15D
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 5D B2 E6 A0 1E 0B 66 8A 41 F8 F6 63 A6 0F A5
        43 1B 45 BD F0 B1 13 0F 19 23 91 14 FE 58 31 55
        0F 85 A3 3D 22 FF DD 79 CB 07 D8 A5 AD 02 FE DA
        18 88 17 8C D3 C9 88 74 28 B8 E8 87 C6 D9 82 90
        5F EC B8 E1 81 F4 D4 95 D4 7B 44 2C C4 C3 E6 CC
        E4 44 3A B5 4C E0 43 C5 64 C7 4D 2F FA 4E 16 8B
        F0 AD 63 C0 9C AA 16 66 41 EB 36 E2 62 1D 0A 6E
        FA 01 7C B4 65 B2 8F F3 E6 3D 60 F9 75 71 E0 4F
        9F 43 1B 11 FF 99 71 11 0E FD 97 3D 10 F8 5A 30
        50 0F DC 97 1D B0 3C AA BA 98 07 65 A1 9D 81 75
        68 F8 88 87 F2 8B B0 20 7C AC 18 69 A3 F0 C2 8E
        18 6A A5 AD 58 07 F3 80 C4 4C 7E E6 CC 44 43 A9
        44 C5 04 3F 16 0C 94 13 FF AD C7 EC 1D 1A 86 A6
        09 DB 60 66 06 1E 33 EE A2 21 EC A2 6F 6A 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!]fAcCE#X1U="yt(_{D,D:LCdM/NcfA6bn|e=`uqOCq=Z0P<euh |ijXL~DCD?`f3!oj"

[+] Synchronized Frame 131 Isolated at Symbol Offset 1409560:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        A1 DE 32 E7 92 1F EB 26 4A 21 D5 F2 E3 AE 1F C3
        42 52 00 EC F4 33 13 0B 0F 07 91 10 FF 51 72 19
        0F 45 83 35 34 ED D9 70 DB 2F DA B9 3B 02 5E F8
        D0 D9 87 CC DB 8C 88 75 28 99 60 07 A2 D9 86 8B
        3D 75 98 B1 93 C9 D8 D4 81 2B 7D 0C CD C3 E6 6D
        C6 54 3A D4 5D 34 43 F1 6C CF 4C 1F E7 DC 34 C0
        E3 AD 6B 6A 15 96 86 72 29 E2 FE 62 62 1F 52 2E
        71 01 F2 B0 61 A6 9F 7F AC 3F E5 FF 15 31 36 5B
        DF 0B 31 20 E3 BA 7B 11 0E C5 57 3D 50 F9 59 70
        11 46 9D B3 85 34 FC AA 5A BA 07 6B F1 98 88 7C
        DD 88 88 87 C2 8B 94 88 7F AC 99 E9 A7 FE EA C7
        C9 5A 5D 0C 68 56 D4 D8 C4 C4 3C 25 1C 64 43 A5
        55 CF 60 3E 16 4C 94 91 C3 65 61 8C 2F 0E 86 AE
        01 FB 55 63 26 1E 73 E6 32 21 FC A2 E5 B2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "2&J!BR3QrE54p/;^u(`=u+}mT:]4ClL4kjr)bbR.qa?16[1 {W=PYpF4Zk|Z]hV<%dCU`>Lea/Uc&s2!"

[+] Synchronized Frame 132 Isolated at Symbol Offset 1420320:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE B2 E7 A2 1F 2B 6E 1A 69 FF B2 F0 A6 0F 91
        5B 56 45 ED F2 31 12 0F 9F D7 11 30 FE 55 71 D0
        0F 95 83 0D 34 7B FA 30 D3 0B DA B9 A9 82 76 FA
        98 89 07 CE C8 8C 88 75 2E 99 C4 07 C2 C9 9A 98
        7F AD B8 E9 04 E4 51 D4 D5 6B 3B 8C F4 8B E2 59
        64 44 3B 94 4C F4 43 E1 6C 41 45 1F FB DE 36 42
        78 E8 67 E0 1D 2C 86 66 61 F3 35 32 22 1D FB 2E
        2A 85 F2 B6 60 26 9F CB 22 3A 28 B9 34 25 34 4A
        DF 63 11 00 FB B9 31 15 0E A5 97 1D 10 FB 5A 31
        52 03 A9 37 9D 10 3C 0A 1A F8 05 EF E1 89 88 5A
        F9 38 E8 87 72 EB 9C 88 7D 2D 98 29 27 D2 5D 88
        99 37 15 2C 4C 07 B3 D8 CC 44 3B 26 9E D4 43 B1
        75 CF 20 3E 57 CC 34 53 FD 2D 43 6C 8E 6A 86 8C
        6B DA 70 62 66 17 1E 27 32 21 D0 A2 E5 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+ni[VE10Uq4{0vu.Qk;YdD;LClAE6Bxg,fa52".*`&":(4%4Jc1Z1R7<Z8r}-)']7,LD;&Cu >W4S-Cljkpbf'2!""

[+] Synchronized Frame 133 Isolated at Symbol Offset 1431080:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 67 20 1E FB 46 5A 68 D8 BE E0 82 5F B1
        57 12 44 AD 66 31 73 2F CD F7 11 10 FE 55 32 C1
        0F 05 93 1D 10 FE DB 71 D3 0F C2 B9 29 A0 76 78
        18 88 87 CD D1 88 89 75 2C B9 A9 87 EA C9 A6 92
        77 25 A8 AD 87 F2 D0 D4 88 3F 33 4C 4C CB E2 74
        C4 44 3F 54 5C C0 C3 E1 6C C1 4D 1F EA 54 50 C3
        F5 EA 62 60 1D BF D6 72 61 E3 B4 E2 22 1F 9B 2E
        7A 01 FE B6 61 A6 97 DB 6A 28 65 7A 16 75 21 4E
        CF 43 1B 32 F9 98 71 90 0E DD 17 0C 10 F5 5B 31
        51 4E B5 B7 1D 32 FC 1A 9A 98 27 EF A5 99 98 7F
        CC 98 88 87 7A A9 9E 08 7F AC 98 69 A7 74 7B C6
        09 1B 95 4C 48 17 B7 CA C6 4C 3E 66 CC 44 43 B9
        65 DC 40 3E 96 CC 74 D3 F7 AC CB 6C 07 8A CC AE
        E9 5B E8 63 26 5F F2 0C 22 21 D1 B2 E6 12 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!g FZh_WDf1s/U2q)vxu,w%?3LLtD?T\lMTPb`ra".zaj(ezu!NC2q[1QN2'zit{LHL>fDCe@>tl[c&_"!"

[+] Synchronized Frame 134 Isolated at Symbol Offset 1441840:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 E6 32 1D 0B 46 4A 69 FE BE B3 86 0F A3
        47 12 10 AD 14 31 03 0F C9 95 11 10 EB 59 73 91
        0F A5 B3 2D 24 FF EF F9 DB 87 F7 A3 AD 82 76 73
        19 89 87 EC C3 CC 88 77 68 BB E0 87 2A B1 8E 9A
        7E 2F B8 F9 97 E9 46 D7 C0 2B 3B 0C 4C CB EE 69
        C4 44 38 57 4D F6 43 E1 6C CB 68 3F FE D4 30 C3
        E2 AC 4A 60 BD BE 06 72 61 E1 20 62 22 1D EA A6
        09 01 F0 B6 61 A4 9F 2B 6F 1B 61 78 55 35 24 5A
        DF 43 31 22 FB DB 71 91 0A A5 53 7D 10 F8 5B 32
        51 6F F8 D5 8C 90 7C 0B DA 9B 27 ED A1 0C 98 7C
        CF B8 88 87 72 8B 8E 48 7C 2C 99 69 A7 CF 4B C7
        9C 5C 85 ED 58 17 B7 D2 C6 4C 3E FE 1C 24 43 B5
        44 47 44 3E 16 CC 54 91 FF 3D C7 CC 3F 02 CC AC
        0B DB 58 66 26 1F 33 0F 02 21 FC A2 E7 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!2FJiG1Ys-$vswh*~/F+;LiD8WMClh?0J`ra b"a+oaxU5$ZC1"qS}[2Qo|'|rH|,iK\XL>$CDGD>T=?Xf&3!"

[+] Synchronized Frame 135 Isolated at Symbol Offset 1452600:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 E9 A6 1E 2A 66 6A 49 FF 96 A2 82 57 A5
        63 13 44 F5 78 21 91 0F 8D 7F 91 10 AE 59 33 D9
        0F 85 B3 0D 34 F8 8F 30 D2 0F C0 AD AD 8A FE FA
        58 89 87 8C F3 E8 88 7F 2E B9 C8 87 C2 C9 86 8A
        7D ED B8 A9 87 F5 58 96 C9 7B 5B 0C 44 83 F7 ED
        46 44 3F 94 5C 94 0B E5 6C C3 49 3E 42 CC 56 C1
        F6 E8 6A 68 9F 96 96 32 61 E7 3A 72 22 1D 6A 2E
        09 21 F8 B6 61 A6 1F 91 6B 38 63 FC 54 35 34 0A
        D7 0B 32 30 F8 9D 71 11 2E E5 17 5D 10 FA 51 30
        93 0F DF F5 9F 30 7E 2B DA D8 27 C3 F1 88 98 7F
        4D 18 88 87 72 8B 90 E8 78 2D 98 E9 A3 DC EA 0A
        58 FE 15 88 6C 13 B0 C2 C4 CC BE E4 1C 44 43 AD
        45 CD 04 3E 16 CC 54 C3 FD 2D 47 04 3F 82 A6 BC
        A1 DB 18 E2 22 1E B7 EE 22 21 D6 3A E5 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!*fjIWcDx!Y340X.}X{[DFD?\lI>BVjh2a:r"j.!ak8cT5420q.]Q00~+'Mrx-XlDCE>T-G?""!:"

[+] Synchronized Frame 136 Isolated at Symbol Offset 1463360:
    ├── Extracted APID Subsystem ID : 0x1D6
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D6 B2 E7 A2 1E 6B 46 0A 49 EF B6 61 8E 1F 0F
        5B 52 05 EE 24 B1 32 0F 7D 83 11 10 E8 59 70 D1
        0F 85 83 0D 30 78 DB 70 F3 0F C2 A1 29 8A DE 7B
        18 C8 15 ED 18 CA 88 77 6C B9 E0 87 CA D9 86 9A
        3F 5D 99 A9 81 ED 54 C6 C1 3B 7C 8C 4C 83 D2 59
        C6 44 3A 94 5C B4 03 F1 6C C1 4D 1E FA DC 74 43
        F6 A9 4A 64 95 BC 46 62 61 F5 36 63 22 1E 5E AE
        FA 01 E8 B2 62 A2 9F EB 6A 3E 05 78 55 25 20 5F
        CA 6B 11 32 FB BB 11 13 0E F5 97 1D 00 F1 5A 33
        53 47 E9 F7 8D 10 7E 2A 90 93 87 6F 61 88 98 79
        4D 98 C8 87 66 AB 9E A8 7A AD 99 29 87 6D D9 8B
        09 7E 25 2D 5C C7 B7 D0 C4 4C 3F E6 DC 54 43 A9
        75 C6 40 3F 16 CC D4 92 B2 7D C6 24 BE 6E BC A6
        41 FB C0 62 26 1E 93 CE 22 21 DC A2 E6 22 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!kFIa[R$2}Yp0xp){wl?]T;|LYD:\lMtCJdFba6c"^bj>xU% _k2Z3SG~*oayMfz)m~%-\L?TCu@?}$nAb&"!""

[+] Synchronized Frame 137 Isolated at Symbol Offset 1474120:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE AA E7 22 1F 0B 66 1A 69 FF BE 30 96 5D C1
        46 3B 44 ED BB 33 13 0F 9D F5 91 12 EE 5D 72 C9
        0F 15 B3 1D 24 F2 9B 71 D3 0B E7 AD A9 A8 76 B9
        18 C9 87 8D CB 88 8A 5C AC 9A E8 87 E2 D1 86 90
        7C EF FC E1 93 E7 54 96 CC 3B 2D 2C 6C 8B F7 49
        C6 4C 3A 55 5C D4 43 E1 68 C5 4D 1F 72 D6 54 43
        F2 A8 E2 60 97 AE 86 76 05 E3 32 A2 22 1D EA 2E
        7B 21 F0 B4 61 A4 9F B7 2E 2E 61 F2 95 B5 26 4F
        DF C3 19 20 F8 93 71 91 0F ED 17 20 00 F8 5B 30
        D1 4F FF B1 2C 34 BC 0A F2 DA A7 6D 91 98 90 7C
        EC B8 88 87 72 8B 9E 80 7D 2D 98 68 A3 FA DA CA
        F8 7E 95 29 6C 17 C6 F2 C4 CC BF 25 DC 64 43 A1
        45 CF 00 3C D6 CC F4 81 FF 25 47 C8 9F 02 86 AE
        89 DB D0 E2 66 1F D7 8E 22 21 DC AA E7 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"fi0]F;D3]r$qv\|T;-,lIL:U\ChMrTC`v2".{!a..a&O q [0O,4m|r}-h~)l%dCE<%Gf"!"

[+] Synchronized Frame 138 Isolated at Symbol Offset 1484880:
    ├── Extracted APID Subsystem ID : 0x1FE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FE A2 E7 B2 1E 0B 06 0A 29 FF F6 F2 A2 17 E1
        63 5D 64 AD 64 B1 93 0E 0D A1 11 10 FE D1 73 D9
        0F 95 A3 0D 34 7F 3B 78 F3 4F C6 B3 2F 90 76 F2
        59 81 0F B4 DB 88 88 7F 2A 99 C4 87 C2 C1 96 9A
        3C 20 BC E5 95 F5 53 D7 9D 6B 3A 8C 6C C2 E9 4D
        44 44 3A B4 5C B4 03 ED 6C C3 49 0D EB 56 75 E9
        F8 E9 CA C8 B5 AC D4 22 05 F3 E6 A3 22 17 8A 2E
        73 21 E6 B6 67 A4 1D C9 66 2A 69 F9 F2 B4 F5 1A
        DA C3 31 22 F9 B1 39 11 0E AD 07 39 00 F8 5A 30
        53 07 B9 B5 14 30 FC 2A 3A 98 07 EB 41 88 98 78
        DF 3C 88 87 72 C9 B4 A8 7D 6D 99 29 87 FA DB 1A
        D8 7E 75 09 48 03 B4 D8 CE 4C BD E7 CC 44 43 89
        44 59 44 3E 16 CC 34 D3 F7 3D E5 4C 3F 26 C4 A6
        89 DB 70 6A 2A 1F 33 4B B2 21 D4 B2 EA A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!)c]dds4;xO/vY*< Sk:lMDD:\lIVu"".s!gf*i1"99Z0S0*:Ax<r}m)~uHLDCDYD>4=L?&pj*3K!"

[+] Synchronized Frame 139 Isolated at Symbol Offset 1495640:
    ├── Extracted APID Subsystem ID : 0x5DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        25 DF A2 EF A2 1F 0B 46 1A 69 FE B6 73 86 0F CD
        42 53 00 AD F9 F3 13 0F 99 A5 95 10 FA 51 72 41
        0F CD B3 15 22 F9 DD 35 F3 02 82 AB 8D 88 D6 F6
        19 C1 07 94 99 88 88 76 AC BA E4 07 C6 C8 96 9A
        7E E7 A8 B1 87 C1 52 96 C5 3B 39 AC CC 43 EE E8
        56 44 3B 94 5D 34 43 E1 6C CF 49 3F F2 CC 7D 42
        FC 60 4A 4C 9D 8E 86 26 01 F3 F6 62 26 1F 4A 26
        5A 21 FE B4 61 A2 1F DB 21 19 61 FD 15 35 38 5E
        9A 0B 3D 31 FB FF 71 11 0E E5 17 19 10 F9 5A 30
        92 4F 5C B5 0D 10 B1 AB 3A B9 A7 69 C3 89 98 78
        F9 38 C8 87 D6 CB 95 88 78 2D 98 69 87 CE DA 82
        98 5C E5 8C 4C 03 B2 A8 CC C0 7F 6A CC 44 43 B5
        65 C7 04 3C 16 CC F4 9B FF 2D C3 0C BF 3E 84 26
        69 DB E8 62 22 1E BB CA 22 21 DD AA 67 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "%FisBSQrA"5v~R;9CVD;]4ClI?}B`JL&b&J&Z!a!a58^=1qZ0O\:ix8x-i\LjDCe<->&ib""!g"

[+] Synchronized Frame 140 Isolated at Symbol Offset 1506400:
    ├── Extracted APID Subsystem ID : 0x1CC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 CC A2 6B 82 1F 4B 26 0A 21 FC B6 E1 F6 1F A5
        73 52 54 ED F6 A3 11 0F 9D B5 11 10 EC 51 71 89
        0F A5 B3 0D 30 FE 5B 79 D1 0F CF B1 AB 28 76 B6
        19 90 97 EC D9 C8 88 7F 2A 9B C8 87 E2 D9 8A 82
        3F AD 88 A9 87 E3 D4 D5 90 2F 7D 0C 44 8E EB 4D
        C4 44 3F D4 5D 72 43 E9 6C CB 4D 3F A6 DC 50 CB
        B8 A8 66 60 BD AD 86 72 65 F7 36 E2 22 1F CA 0E
        52 29 E4 B2 61 A2 1F F9 6F 18 40 F9 77 31 30 0F
        DF 6B 51 30 F1 92 59 91 0E AD 17 14 00 FC 5B 30
        D2 47 F2 97 15 B2 BC 6A 12 F8 A7 6F 71 98 90 7E
        9D B8 88 07 64 89 96 00 7C AC 98 29 87 FE E9 8A
        9C 7E 25 7D 4D D2 B5 98 CC 40 BC 26 DC 04 43 B1
        65 4B 4C 3E 96 CC B4 93 AF 64 C5 8C 1B 0A CE 26
        0B FA 6C 62 24 1F 70 EA 2A 21 C4 B2 AB B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!kK&!sRTQq0[y(v*?/}DMD?]rClM?Pf`re6"R)ao@w10kQ0Y[0Gjoq~d|)~%}M@&CeKL>d&lb$p*!"

[+] Synchronized Frame 141 Isolated at Symbol Offset 1517160:
    ├── Extracted APID Subsystem ID : 0x1FF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        29 FF A2 E6 12 1E AB 4E 0A 29 EB DA 63 A6 1F 97
        43 57 54 BD E8 33 13 2F B9 B7 91 10 EE DD 37 59
        0E 35 33 3D 30 FF DB 31 CF 27 CD B5 AF 32 FE F8
        18 99 97 84 C0 8C 88 75 BC 99 E8 A7 42 D1 8A 89
        5F 6D 98 E4 87 E0 50 D5 C5 3B B9 28 44 C3 E7 49
        C4 44 3A 74 4D E1 42 B5 6C D3 4C 3F DE 44 76 C3
        F8 AE 6B 64 95 8C D6 66 61 F3 2C F2 22 17 CB 2E
        38 21 D7 B6 67 A6 97 3B 6E 3F E1 F8 75 35 70 0E
        DF 43 31 22 F3 93 79 11 0E 85 17 5C 10 F0 59 30
        D3 47 BF B1 0D 10 F6 AB 12 B9 27 77 A1 8D 99 7D
        D8 BC 88 85 52 89 BE 80 7E AD 19 69 A7 F5 DE CE
        D8 7F 1D 09 59 02 B4 D1 C6 4C 3E EC C4 64 43 ED
        45 CF 04 3C 16 4C 74 D3 F3 F4 C7 4C 9F 42 86 26
        09 DA E0 67 26 1F 33 46 02 21 D7 A2 E7 A6 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ ")N)cCWT3/7Y53=01'2uB_mP;(DID:tMBlL?Dvkdfa,".8!g;n?u5pC1"y\Y0G'w}R~iYL>dCE<LtLB&g&3F!"

[+] Synchronized Frame 142 Isolated at Symbol Offset 1527920:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC A2 E1 20 16 2B 66 8A 29 FF B6 A2 A6 0D 8D
        4F 53 50 AD B4 31 93 0F D9 D5 91 10 ED D1 32 D0
        0F C5 A3 1D 34 BF B9 31 FB 27 C2 B5 A9 8A 76 7E
        18 88 07 E5 D1 88 90 77 A8 99 C8 87 E2 C9 86 9A
        7E E5 BC FC 83 E9 51 D4 88 39 DD 0C 64 43 E7 65
        85 44 3B 95 4D 70 43 E1 69 C1 49 3F 56 44 F0 43
        F2 A0 4A 40 B5 BE 86 32 61 D7 34 E2 22 1F AA A6
        77 21 F0 B4 67 A4 DF BD E4 3A 61 7B 14 75 31 4F
        D2 43 59 20 F7 D3 6B 11 0E B5 17 2C 10 F8 5B 30
        D1 4F DA 95 25 92 FF 6B 92 98 87 6D A1 89 98 7C
        CC 98 8B 87 7B 8B A2 C8 7E 2D 18 A9 23 DC C3 8E
        99 5E 2D 8C 7D 16 B1 D8 D4 4C 3E 66 D6 44 42 FD
        45 DA 48 3E 96 4C 34 93 EF 7D C7 4C 3F 8A 44 A6
        09 DB CC 62 A6 1F 92 2E 2A 21 D4 A2 ED 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "! +f)OSP1241'v~w~Q9dCeD;MpCiI?VDCJ@2a4"w!g:a{u1OCY k,[0O%km|{~-#^-}L>fDBEH>L4}L?Db.*!""

[+] Synchronized Frame 143 Isolated at Symbol Offset 1538680:
    ├── Extracted APID Subsystem ID : 0x1FD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FD A2 E7 A0 1E 2B 66 5A 69 FF B6 A0 A2 2F 8F
        43 12 25 ED FA B1 11 0F F9 B5 91 10 EE 11 73 C1
        0E 95 83 3D 10 FE DB 71 33 2F C2 A5 89 2A 76 DB
        58 89 87 EC D9 8C 8A 75 2E 99 62 07 C2 D0 8A 9A
        39 EF B8 E4 95 F1 51 D4 C1 3B 5D 9C 5C 8B C7 08
        CE C4 3A 96 5C 84 43 F1 6C C3 45 3E 5A DC 74 48
        FB E8 CA CC 9F BC D6 32 41 F7 E6 A3 22 1D BA 26
        5B 21 E8 B2 60 22 8F F3 6E 30 60 F0 56 65 B4 1E
        C5 CB 11 72 F1 35 59 91 0F E5 D3 7A 92 F8 58 31
        52 47 AC 91 3F 90 38 0A 58 B8 A7 EF 95 88 90 78
        F9 9C 88 87 52 8B 9F 00 7D 6D 19 E8 A3 DB DB 8E
        98 1F 1D 29 4C 92 BF 90 CE 4C BE 24 9C 64 43 B1
        45 CA 64 3C 16 0C 34 43 F3 24 47 6C 3B 0A CE EE
        2B DB 49 62 66 1E B3 62 22 21 DE AA E5 B0 1D
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+fZi/C%s=q3/*vXu.b9Q;]\:\ClE>ZtH2A"&[!`"n0`Ver5YzX1RG?8XxR}m)LL$dCEd<4C$Gl;+Ibfb"!"

[+] Synchronized Frame 144 Isolated at Symbol Offset 1549440:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DF A2 E3 A2 1F 2B 66 5A 41 FD 9E A6 E6 37 87
        4B 57 64 EC F0 B1 13 2F 0B F1 19 30 EC 55 73 59
        0F 85 B3 2D B4 FF DF 78 EB 0F C2 B7 AB 82 F6 FA
        19 81 97 EE DA CC 88 75 2A B9 E4 87 E2 E9 92 8A
        3F 8D A8 70 87 E8 50 D4 C9 3F 1F 2C 44 43 F6 ED
        44 44 3B 96 4C 34 83 F1 64 C3 4D 3F 82 CC 78 CB
        F9 A0 6A 68 1F BE 86 62 21 F3 22 E0 20 1D 92 2E
        5A 21 E8 A6 61 A4 9F 6B 6E 0F 69 78 D4 65 E2 0E
        DF 47 36 02 F0 9D 71 91 2F E5 93 2D 90 FC DB 32
        D2 07 6D B7 1D F2 B4 8B 1A 9B AF ED D5 98 80 7C
        DC 98 C8 87 66 8B 8C 88 5C 2D 98 29 83 F6 F9 8E
        98 9F D5 0C 4C 13 B2 D8 D4 48 3F 36 4C 64 43 B3
        55 D3 44 3E 16 4C 74 D3 FF 84 46 0C 8F 0A A6 26
        09 DB C8 67 60 1F 93 4E 32 21 DC A2 E7 22 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+fZA7KWd/0UsY-xu*?pP?,DCDD;L4dM?xjhb!" .Z!aknixeG6q/-2m|f\-)LH?6LdCUD>LtF&g`N2!""

[+] Synchronized Frame 145 Isolated at Symbol Offset 1560200:
    ├── Extracted APID Subsystem ID : 0x1DB
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DB A2 E3 60 1F 8B 66 AA 29 FB F2 E3 84 57 95
        67 5B 25 EC E0 31 31 0F C9 F7 11 10 FE 51 33 90
        2F C5 B3 2D 14 7F CB 79 D1 07 CD 89 29 AA 76 F2
        19 89 1F E4 99 CD 88 76 EC B8 C8 07 E2 D9 86 8A
        7E F7 98 E9 AD E0 5E 84 81 7B 2B 0C 44 82 E7 65
        C6 44 3B 05 4C 60 43 E1 64 C9 6D 3F FF D4 56 42
        F0 EF E2 60 9D BE 86 F6 61 DD 36 E2 22 1D 5A A6
        F3 21 F8 B2 67 A6 DF FB 6A 38 61 E8 54 35 E2 5E
        C6 6F 31 20 AD 9B 11 91 4E C5 D3 30 90 F8 59 31
        D3 2F B9 97 1F 90 3C EA 92 9B 2F E5 95 98 88 74
        4B B8 89 87 62 CB BE 88 7C AD 98 68 83 DC 7B AE
        98 56 3D 0C 6C 13 F3 D8 C4 48 BE E6 84 64 43 E1
        65 C4 44 3E 16 4C 34 83 FF 3C 43 D4 1F 0A 96 A4
        0B DB F8 66 22 1E 1A 6A 22 21 DC A2 EF 20 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!`f)Wg[%11Q3/-y)vv~^{+DeD;L`Cdm?VB`a6"Z!gj8aT5^o1 N0Y1/</tKb|h{V=lHdCeD>L4<Cf"j"! "

[+] Synchronized Frame 146 Isolated at Symbol Offset 1570960:
    ├── Extracted APID Subsystem ID : 0x1CC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 CC A2 E7 18 1E 0B 62 3B 49 FB B2 63 E6 07 D5
        56 57 05 E9 7C B3 33 2F B9 A7 15 10 EF 59 76 D8
        0F B5 31 39 14 7F C3 50 FB 0F C3 A9 09 AA 7E 72
        58 88 87 8E D8 A8 88 7D 28 B9 2C 87 C2 C9 82 92
        3F AD B8 F4 91 C1 56 85 C5 2B 1D 0C 44 C3 CB DD
        44 45 3B 95 5C 84 C3 E5 6C C3 49 0F F6 CC 51 C1
        F0 6C 6B E0 15 96 86 66 61 F7 BE E6 22 1F 8B 2E
        6A 21 66 B6 65 A2 1F FD 6A 0B 21 F9 54 34 67 5E
        D6 03 31 10 F8 AB 31 11 2E D5 17 05 10 F8 5B 32
        53 4F 96 F7 1D 10 7E AA 30 CA 2F E1 D5 99 90 78
        5F AC 89 87 D2 8B 8E 08 7E 2C 19 E9 A7 D2 EB 8F
        88 7E 15 9D 58 53 B7 D0 C4 4C 3C E7 F4 44 43 ED
        45 DF 60 3F 57 4C F4 81 FF 6D E7 24 8F 4A 86 B2
        8B 59 DC 62 26 1F 33 66 22 21 D8 B2 EB A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!b;IcVW|3/Yv19P~rX}(,?V+DDE;\lIQlkfa".j!fej!T4g^11.[2SO~0/x_~,~XSL<DCE`?WLm$JYb&3f"!"

[+] Synchronized Frame 147 Isolated at Symbol Offset 1581720:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE E2 61 B2 5F 1B 46 1A 40 F3 B6 E3 96 1F B5
        63 17 04 BD F9 37 13 0F 6D B5 91 10 F9 D5 72 48
        0F 05 B3 2D 00 79 DF 59 11 07 7D B5 2B 98 D6 79
        59 D8 85 F2 89 8C 88 76 E8 B9 A1 97 C2 D9 86 9A
        77 BC B0 AB 97 E9 5C C4 C5 3B 7B 2C E4 43 E6 24
        44 44 38 35 5D D4 43 C1 60 C3 49 3A F2 DC 14 C2
        FD 2C E8 E0 95 B6 86 66 65 F1 36 F2 2A 1F AB 2E
        78 01 E0 A6 65 B2 9F CF EF 2A 61 F8 16 35 75 4B
        D9 4B 13 32 FC D5 39 91 2E E5 17 74 10 FE 5B 70
        D2 4F FD 93 0D 92 7C 2A 98 91 07 63 E1 88 98 7E
        C9 39 C8 87 58 88 B4 88 7B AC 18 69 A7 FC E9 86
        D9 3E 05 0C 4D 13 B7 90 84 48 3C EE C6 44 43 F3
        45 C7 44 3D 16 CC 54 D3 E6 75 67 4C A7 EA 66 B4
        0B FB E4 62 64 1F 3B 8E 32 21 DF AA E7 B2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!a_F@c7mrH-yY}+yYvw\;{,C$DD85]C`I:,fe6*.xe*a5uKK29.t[pO|*c~9X{i>MH<DCED=TugLfbd;2!"

[+] Synchronized Frame 148 Isolated at Symbol Offset 1592480:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A2 E3 B0 5F 2B 66 1A 21 FE 56 E3 A6 0F E5
        53 53 65 AD B4 31 12 0F 18 A7 11 10 F1 55 72 89
        0F C5 B3 05 10 7A 69 70 D6 0F C3 B3 AB 8A F6 76
        19 E9 07 ED 5B C8 88 76 EE B8 0C 87 E2 D1 9E 92
        7D DF 98 F9 D5 E1 5C D6 C5 7B 6E 0C 64 C3 8E 65
        4E 44 3B 34 5D D6 43 F5 6C C7 41 3E 72 DC 7C 43
        B0 AF C3 E4 9F BE 06 74 21 F3 30 E2 22 1F CB A6
        CB 01 E0 B4 69 A6 8F F5 26 1A 61 F8 B6 75 64 4F
        CA 43 11 40 F9 BA 71 11 0E ED 97 75 92 F0 59 32
        D3 0F 95 B7 9D 32 FC 2A 3A 59 A7 67 21 88 89 7C
        7D 18 C8 87 7A CB 96 88 78 2D 98 EC A3 CE D9 9E
        B8 7E 35 4C 7C 42 B0 F8 C4 44 BC 65 9C 44 43 AF
        45 CB 20 3E 16 CC 94 93 FF 6D 83 40 3F 12 8C AE
        09 58 C8 66 26 5F 93 6A 22 21 C4 A2 E5 32 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!_+f!VSSe1Urzipv[v}\{ndeND;4]ClA>r|Ct!0"i&audOC@quY22*:Yg!|}zx-~5L|BDeDCE >m@?Xf&_j"!2"

[+] Synchronized Frame 149 Isolated at Symbol Offset 1603240:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        61 DC B2 E9 30 1E 0B 46 5A 28 FF B2 F1 AE 57 97
        62 73 04 ED E4 B1 11 0F 9B A7 1B 10 FE D5 72 C9
        0F F5 93 0D 30 71 89 D0 5B 0F D0 A7 AB 02 7E BA
        18 C9 87 C5 F9 88 88 77 28 B8 C8 87 E2 C9 92 D0
        7D 8F B8 75 91 FA 58 D5 C0 7F 7D 2C 60 CB E3 41
        C4 4C 3F F6 5C F4 03 F9 6C C5 49 3F D6 D4 74 C3
        F0 EB 62 68 9D BF 86 36 C1 FB EE A2 22 1F 0A 26
        0B 01 F8 B6 63 A6 9F FC 67 38 64 FB 55 31 33 4B
        C2 03 3B 34 F9 9E 31 91 0E CD 93 35 80 FB 5B 30
        D1 4F C4 F3 9F 70 FC 6A BA BB A5 6F 81 9C 98 7E
        4D BC 88 87 72 8B 9E 88 7D 2D 88 AD A7 CE CB 8F
        19 7E 35 8D 48 86 F7 C2 C6 4C AD 66 D4 64 43 E9
        5D CD 44 3C 96 CC 34 83 EB 65 C7 C5 3F 02 8E AC
        A3 59 F8 62 22 1F 3F 68 22 21 F4 A2 67 30 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "a0FZ(Wbsr0q[~w(}uX},`AL?\lI?tbh6"&cg8dU13K;415[0Opjo~Mr}-~5HLfdC]D<4e?Yb"?h"!g0"

[+] Synchronized Frame 150 Isolated at Symbol Offset 1614000:
    ├── Extracted APID Subsystem ID : 0x1F1
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F1 A2 EA A0 1F 4B 26 3A 45 D9 DE 71 A3 17 81
        43 53 54 EC 74 21 92 2F 19 75 19 10 EF 53 73 C0
        0F 45 B7 2D 00 FF 8B 70 C3 0F CA B9 A9 82 F6 FE
        18 99 8F 44 1B AC 88 76 AC BB 88 87 D2 D3 82 D2
        7F D5 B8 A1 97 E1 54 D5 D5 3A 7E 0C 4C CB E6 6D
        C6 44 3A 14 CD E0 43 E5 44 C1 49 1F 7F CE 7A CA
        F8 AA 6A 68 9D BD 06 22 6D E7 64 E3 22 1F 0A 2E
        D8 21 FC B2 60 B4 0F 13 6A 1A 21 F8 75 75 31 5E
        DF C3 13 32 F5 9A B3 91 0F E5 53 3C 14 FF 5B 33
        D2 4F 8D F7 5F 30 6F 8A FA F8 AF 6F A5 8C 89 7C
        C9 98 88 A7 C6 8B BC 88 7C 2D 18 29 A7 C6 DB 8F
        99 3E 15 4C 59 92 F7 B0 C6 CC 2F 6E 5C 64 43 BA
        45 C7 40 3F 96 4C 34 13 DF 65 4B E4 2B 3A A6 36
        2B FB F0 62 66 17 37 CA 12 21 DF A2 62 F2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!K&:EqCSTt!/uSsE-pDvT:~LmD:CDIzjh"md".!`j!uu1^2S<[3O_0oo||-)>LY/n\dCE@?L4eK+:6+bf7!b"

[+] Synchronized Frame 151 Isolated at Symbol Offset 1624760:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD BA E3 A0 1F 4B 46 6A 69 F9 96 01 C6 0B ED
        4A 53 55 AD A0 31 33 0F 89 B7 19 10 FB 19 72 40
        0F 05 B3 0D 30 FF EF 41 E3 37 C1 A5 2F 82 76 DA
        18 C9 97 BD DF 8E 88 7E 68 B8 80 87 E2 C1 82 9A
        7F D4 9C 69 81 F8 D0 C6 95 3B 1F 2C 44 83 C7 49
        C4 44 3A 16 5C 74 03 E1 6D C3 49 1F EB DC 54 C3
        F0 28 6B 40 95 BE 86 22 01 D3 66 E2 26 1D CB 6E
        58 01 F8 B6 63 A2 8F F1 2A 3A 25 78 D4 35 B0 5B
        C7 03 11 22 F5 FA 51 11 0E E5 17 74 10 FA 5B 32
        D3 47 98 F5 9C 30 FC 6A 9A DB 0F 41 51 8C 98 78
        DD 18 C8 87 F2 AB 9C C8 7E AC 98 E9 A3 F7 5B 82
        B9 7E BD 0D 4C 13 B7 90 DC 44 3E 67 DC 64 03 B9
        5D 46 C4 BF 96 CC 96 91 FB E5 C5 44 3F F6 84 84
        09 FA 68 62 06 1F FB 6F 22 21 DC F2 E3 E2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!KFjiJSU13r@0A7/v~hi;,DID:\tmIT(k@"f&nXc*:%x5["Qt[2G0jAQx~[~LD>gd]FD?hbo"!"

[+] Synchronized Frame 152 Isolated at Symbol Offset 1635520:
    ├── Extracted APID Subsystem ID : 0x1D2
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D2 A2 67 86 1F 4B 4E 9A 48 FF 36 A1 A6 6F CB
        4F 53 01 AD B0 31 21 0F A9 27 91 10 EA 55 14 D1
        0F 05 B3 15 14 FE BA 71 F3 2B C2 A3 89 AA 76 5A
        18 89 17 8C DA 88 88 7D 28 99 60 07 C2 C9 86 90
        7D 35 A8 61 97 E5 D4 D4 C9 7B 6D 0C 4C CB E2 6D
        E7 44 3A B7 5D B4 43 E1 64 C3 4C 2F F2 46 7C C1
        E0 EB 6A E8 1F BD 06 32 65 E3 36 B3 A2 1D 0A 2E
        7A 25 F6 B6 61 A2 1F 63 26 3C 20 FA 94 61 B1 5F
        CF 43 31 30 FC BB 79 11 0E E5 57 0C 80 F1 59 37
        D2 4F FE F7 0F 10 FD 38 1A 99 27 67 A5 88 98 7E
        EF BC 89 87 52 EB AE 80 7E AD 98 29 A7 CE DB 8A
        99 76 3D 78 4C 53 F3 D0 C4 8C BF 66 DC C4 43 AD
        54 DB 44 3E 16 CC 34 D3 E6 A5 E5 C4 BF CA E6 A6
        C1 DB E8 62 26 57 97 0E 22 21 DC 22 EC A2 9F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!gKNH6oOS1!'Uq+vZ}(`}5a{mLmD:]CdL/F|j2e6.z%ac&< a_C10yWY7O8'g~R~)v=xLSfCTD>4b&W"!""

[+] Synchronized Frame 153 Isolated at Symbol Offset 1646280:
    ├── Extracted APID Subsystem ID : 0x1D9
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D9 BA 65 22 1E 2B 66 5A 28 F7 76 E3 96 4F C1
        4B 1A 40 ED 76 33 33 0F 9B B3 51 10 FF 59 73 D0
        0F 85 93 0D 24 FF 9F 71 D3 23 C2 81 AD B2 F6 DC
        18 89 B7 EC 8B 8C 98 54 28 BB ED 87 82 D9 8E 80
        7F F4 B8 A3 97 E3 54 94 81 3B 59 0C 4C C3 EA 68
        C4 44 3B 36 5D B4 43 C1 64 CB 49 1F 37 CC 14 4A
        FA EB 4A E4 BF B5 16 22 65 F1 B6 E2 22 1D 5A A6
        C3 01 F8 B6 61 A2 9F 3B 6F 3A 64 F8 54 72 36 4F
        DF 83 11 32 FB 9B 39 91 0E ED 17 5D 10 FE 5B 30
        D3 0F DD 97 0D 10 EC 0A 18 98 07 EF A1 88 90 7C
        FD 38 88 87 66 8B 8A 08 78 AD 19 A9 A7 E2 C9 87
        18 7E 15 6D 7D 13 B4 A2 C4 4C 3C 26 DC 44 42 E1
        61 CF 44 3E 56 DC 14 51 B5 7D 6F AC BF 82 BC FE
        0B FE F0 62 64 1F B3 EE 32 21 DA A2 E7 B0 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!e"+fZ(vOK@v33QYs$q#T(T;YLhD;6]CdI7JJ"e"Za;o:dTr6O29][0|8fx~m}L<&DBaD>VQ}obd2!"

[+] Synchronized Frame 154 Isolated at Symbol Offset 1657040:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC B2 E7 96 1F 2B 66 7A 69 F9 96 E3 D6 1F 85
        43 53 00 ED F4 31 03 0F B9 B7 19 10 EE 51 73 C0
        0F C5 93 2D 14 FF 99 71 D3 2B C0 8D 8B 9A 76 FA
        18 98 95 CF DA 88 89 77 2C B9 CE 87 C2 D9 86 9A
        77 C6 B8 B9 83 E4 D1 D4 D0 7F 0D 6C C4 CB EB 7D
        C6 44 3B D4 54 4C 43 F5 68 C3 4D 3F F6 CE 54 43
        7D A2 6A 68 BD 9F 06 32 C5 F3 30 E2 22 1D C3 26
        B2 25 F0 B6 E0 A6 1F FB 6E 2D 65 F9 D5 60 20 4E
        CF 03 39 00 FD BF 71 11 0E 71 57 0D 10 F8 59 33
        D0 0F F5 DD 37 32 FE 9A 30 99 A7 67 01 98 98 78
        58 BA C8 87 62 CB 9E C0 7F AD 98 28 87 FF 4B 8F
        68 5E 0D 2C 6C 92 B3 C0 CE 48 3C A4 DC 64 43 B1
        4C CF 64 3C 56 0C 74 D3 FF 6D C7 4C 1F 0A E6 A6
        01 5B E8 62 06 5F 32 CF 22 21 FC A2 6D 22 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+fziCS1Qs-q+vw,wl}D;TLChM?TC}jh20"&%n-e` N9qqWY3720gxXb(Kh^,lH<dCLd<VtmL[b_2"!m""

[+] Synchronized Frame 155 Isolated at Symbol Offset 1667800:
    ├── Extracted APID Subsystem ID : 0x1D8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D8 AA EF 26 1F 0B 26 2A 68 FF 52 D3 E6 5F AD
        43 34 20 EE EA B1 22 0B 69 B4 93 10 EA 91 73 50
        0F D5 B3 5D 34 FF 5B 51 D3 0F C2 B3 8B A0 56 B8
        18 89 97 CC A9 49 80 76 2A B9 E0 07 C2 F1 8E 98
        7F DD 88 FD 87 E5 50 C5 D5 3B 4D AC 64 CB EE 6D
        46 40 3F 95 5C B0 03 E9 6C CB 49 3F 96 DE 54 41
        F2 2C 6A 4C 1D BE 86 22 65 F3 32 62 22 1D 4A 22
        1B 21 F0 B6 67 A0 8F 8F E6 2C 61 F8 D7 75 30 4A
        CB CB 1D 10 F8 B7 71 11 0E A9 57 29 10 FE 5A 33
        D3 47 BC B4 0E 30 7C 3A 58 F8 27 EF F5 08 91 7E
        DD 18 88 87 72 8B 9E 88 7C 2C 98 69 27 D3 DB 86
        59 DE 15 1C 5D 57 B5 F2 C4 CC 3F 68 DC 64 43 BD
        44 C6 44 3C 16 8C 14 D3 F8 68 67 4C 1F 0A C6 B4
        AB 53 DD 42 26 1E 17 67 A2 21 D6 AA 67 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!&&*hR_C4 "isP]4[QVIv*P;MdmF@?\lI?TA,jL"e2b"J"!g,au0JqW)Z3G0|:X'~r|,i'Y]W?hdCDD<hgLSB&g!g"

[+] Synchronized Frame 156 Isolated at Symbol Offset 1678560:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC BA E1 B0 1F 2B 06 4A 49 C7 BE 60 A6 5E 85
        52 57 04 AC 30 31 13 2F 99 F5 31 10 FA 51 70 82
        0B 05 83 0D 00 F9 99 71 51 0F F5 A5 0B AA 76 FA
        19 89 07 8C FA C8 8A 7D 28 98 EC 87 42 D1 86 CA
        7E 24 A8 E9 05 E1 52 CE 91 2B 2C 0C 44 43 E2 49
        C4 44 3B 94 5C F6 43 D9 6C C7 4C 1F E2 DC 74 C3
        F1 AB EA 6C B7 BE 16 62 65 EB 34 B2 22 15 9A 2E
        7A 01 FC B4 65 A4 0F 73 6E 3A 21 FA 54 74 30 0E
        DF 63 31 24 F8 9D 71 11 0E DD 53 3D 04 F8 5B 32
        D2 0F BD 91 8D 12 7C 2B 1A 98 07 6F E1 AD 09 7A
        6B 2C 88 87 44 8B 9E C8 7D 2D 98 89 A7 F8 79 CE
        89 6E 15 69 6C 12 91 90 CC CC 3E 14 FE 44 43 F9
        75 C7 44 3E 16 4C B4 D1 F9 65 C5 4C BF 0A C6 AC
        A9 D8 D0 63 26 1F 92 2E 22 21 FD A2 E7 A2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+JI`^RW01/1QpqQv}(B~$R+,DCID;\ClLtlbe4".zesn:!Tt0c1$qS=[2|+ozk,D}-ynil>DCuD>LeLc&."!"

[+] Synchronized Frame 157 Isolated at Symbol Offset 1689320:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC B2 E7 B2 9F 2B 26 1A 69 FB 12 63 92 0F 85
        52 53 64 EC 72 B1 13 0F D8 77 91 10 F8 51 73 D4
        0A C5 B3 0D 14 79 FF 71 D3 0F F5 A3 99 9A F6 7B
        18 C8 07 86 C3 9C 88 76 28 B9 68 07 C6 D9 86 9A
        7F 27 BC 39 87 F9 D0 D7 C0 3B 68 0C CC C3 D6 6C
        C4 44 2F 34 5C 52 43 F1 78 C7 49 3F 22 DC 3C 43
        F9 E9 4A C0 9F BC C4 24 45 D9 B6 BE 22 1F 63 A6
        58 21 E4 B2 63 A6 9F 51 AA 3B 65 F8 D4 35 31 4A
        CE 43 31 30 F9 FA 51 11 0F F5 F7 5C 50 F9 5B 30
        D3 47 98 D7 94 10 1D 2A 5A B9 A7 47 E5 88 98 7F
        CD 18 C8 87 F2 A3 BE 00 7E 2D 99 69 A3 E7 DB 8C
        B8 5F 2C 1D 6C 57 A5 D0 C4 4C 3E 66 DC 54 43 B5
        45 D7 44 3F D6 CC 14 D3 F7 AC C3 44 2F 0A 86 36
        03 DA E4 67 26 1E 1B 43 22 21 D4 A2 E3 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+&icRSdrwQsyq{v(h'9;hlD/4\RCxI?"<CJ$E"cX!cQ;e51JC10Q\P[0G*ZG~-i_,lWL>fTCED?D/6g&C"!"

[+] Synchronized Frame 158 Isolated at Symbol Offset 1700080:
    ├── Extracted APID Subsystem ID : 0x1DD
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DD A2 ED A2 9E 8B 06 5A 61 E5 52 F0 AE 4F 8B
        53 13 24 AD 78 33 12 4F 89 F3 95 10 E0 D1 73 D3
        0F A5 B3 1D 24 F3 DB F1 B3 0F E2 A1 AF 9A DE FA
        10 89 17 C4 F9 84 80 7F 6C 89 EC 07 82 D9 96 92
        39 15 BC E1 83 FB 50 D4 D1 6B 5F 8C 64 C3 F3 5D
        E4 44 3A D5 5C 70 43 E9 6C C7 41 3F D3 DE 74 C3
        F3 AC 4A 60 1F AC 86 36 61 E0 84 22 20 1F AA A6
        52 21 F2 B4 E3 A6 9F DB 6F 3D 21 7E D6 35 70 4F
        DB 1B 11 30 F5 18 31 11 0F E5 93 38 00 F0 5A 32
        52 07 9D B5 15 30 7C 6B 9B 9A A7 69 DD 8C 98 7E
        E5 98 C8 87 62 8B 9F C8 78 AD 99 68 27 DC 4A 8E
        D8 16 5D AC 4C 47 B6 D8 CE 44 3F 2D DC 44 42 BF
        40 C8 64 3C 56 CC F4 83 FF FD C3 CD 3F 6A C6 A6
        49 DB A8 62 26 3F 7B 66 32 21 DE A2 E8 00 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!ZaROS$x3Os$l9Pk_d]D:\pClA?tJ`6a" R!o=!~5pO018Z2R0|ki~bxh'J]LGD?-DB@d<V?jIb&?{f2!"

[+] Synchronized Frame 159 Isolated at Symbol Offset 1710840:
    ├── Extracted APID Subsystem ID : 0x1F8
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F8 A2 EA B2 9F AB 66 5A 65 F3 92 B2 96 1F 81
        66 16 24 BD F4 B1 33 0F 5D E7 11 10 EC 59 73 49
        0F F5 B3 0D 36 FB C9 11 D5 07 F7 A3 2E 30 7E 75
        18 89 97 CE D3 88 88 7F 28 B8 68 85 B2 D9 8E 98
        7F ED 38 E1 97 E5 50 D7 C0 7B 7B 0C 44 4B E2 7D
        C0 4C 3F B4 4D F4 03 C1 68 CA 49 1F DB 4C 3A 03
        F5 AC 6A 6C 9F 8E 86 22 61 E3 AE 32 22 1D 7A 2E
        18 21 E0 B2 60 A6 1F BB 6E 3A 60 78 56 61 B0 1A
        D7 6B 1B 30 F1 D1 31 11 0E A5 57 2D 00 FC 5B 33
        D1 07 DC BF 1D 90 FC CB 1A D8 AF 63 A1 88 88 7E
        4D 38 88 87 7A 89 AE 88 7C 2D 18 69 A7 C8 DA 87
        58 7D 55 78 0D 03 B5 E8 C6 4C BC 7D 8C 64 43 FB
        44 CF 44 3E 16 CC 14 D1 FD 65 C7 6C 3B 6A DE BE
        01 5B 49 66 24 1E 73 6F 32 21 F8 BA 67 B0 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fZef$3]YsI6.0~u(h8P{{DK}L?MhIL:jl"a2"z.!`n:`xVak01W-[3c~M8z|-iX}UxL}dCDD>el;j[If$so2!g"

[+] Synchronized Frame 160 Isolated at Symbol Offset 1721600:
    ├── Extracted APID Subsystem ID : 0x15E
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 5E A2 A3 82 1C 0B 4E 7A 69 FB B3 E1 B6 D7 C5
        67 4D 10 FD F4 B1 93 0F 2B 97 11 10 EF D5 77 D9
        0F 85 F3 0D 20 7F 8B 51 69 07 C0 B3 89 A0 5E DB
        19 C9 87 CC DB 8C 88 77 2A 99 C8 87 82 C9 9E 9A
        7E B5 88 E8 87 B3 50 D1 D4 3F 3D 2C 64 C3 E7 E9
        E4 44 3B 15 5C 54 03 C1 6C C3 48 1F B6 DC 74 C2
        F0 ED 6B 64 9F 9E 16 62 05 F3 B6 E2 22 1D EA AE
        23 21 E8 B4 65 A6 8F FB E7 0F 64 F8 16 35 B0 4E
        D7 AB 11 22 F8 9B 51 11 0E BD 17 1D 50 F1 5B 30
        D1 0F EB BD 15 30 3C FB 38 B8 05 2F 31 88 88 7E
        49 B8 98 87 72 89 9E C8 7E 29 98 69 83 ED DA 83
        18 56 25 08 6C D7 B7 CA CE CC 3E EC DC 44 43 A9
        64 CB 04 3E 96 8C 34 C1 E7 2E 45 6C 3F 02 A6 B4
        4B DF 68 62 64 1F 53 7E 02 61 DC A2 EB 02 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!^NzigM+w Qi^w*~P?=,dD;\TlHtkdb"#!ed5N"QP[00<8/1~Ir~)iV%l>DCd>4.El?KhbdS~a"

[+] Synchronized Frame 161 Isolated at Symbol Offset 1732360:
    ├── Extracted APID Subsystem ID : 0x1EE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 EE B2 64 02 1F CB 26 1A 25 E3 B3 63 A2 1F 87
        66 42 04 FD 7D B3 33 0F DD 93 91 10 EC 51 72 51
        0F 05 13 05 30 FF 59 51 43 27 C3 A1 A9 9A 56 FA
        18 8B 07 8E D7 88 88 79 28 B9 61 87 CA D9 96 9A
        7F EF A8 29 85 E2 D4 D4 C5 3F 1D 8C 44 C3 E7 4D
        D4 44 3B B4 5D 70 03 E9 64 C1 4D 2E F2 CC 7C 41
        F0 AE 62 46 BD B2 16 26 61 E7 3E E3 22 1F DA AE
        09 21 F5 BC 61 A4 9F 6B 6A 3E 61 FB 54 75 30 4A
        C7 2B 11 32 F8 9F 21 91 0E FD 57 3D 90 FD 5B 32
        D1 4F B9 B3 9D 92 FE 1A 1A 9B 27 63 A1 88 99 7C
        CD 98 A8 87 6A 8B B3 80 7F 2D 99 E9 A3 DC 98 CE
        18 77 35 1C 4C 13 BF D0 C4 CC 38 FE 86 44 43 B5
        55 D9 04 3E 16 CC 34 53 E7 75 63 4C 3F 9A 8E 36
        09 D9 EC 42 22 1F 3F 6A 22 21 FC B2 E6 30 9F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!d&%cfB}3QrQ0YQC'Vy(a)?DMD;]pdM.|AbF&a>"!akj>aTu0J+2!W=[2O'c|j-w5L8DCU>4SucL?6B"?j"!0"

[+] Synchronized Frame 162 Isolated at Symbol Offset 1743120:
    ├── Extracted APID Subsystem ID : 0x1D9
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D9 AA E7 80 1F 2B 66 1A 68 F7 36 E7 E6 5F C7
        53 52 21 F4 BA B3 B1 2E AD F5 91 10 EE 51 73 D1
        0F 85 B3 0D 24 FF 7B 51 77 2B CB A3 2B 02 D2 FA
        58 88 87 C4 D7 88 88 7B 2C B8 28 87 C2 C1 8E 92
        7D CD A8 F9 A1 E5 58 D5 C1 7B 39 AC C4 C3 F6 6F
        E4 44 3F D4 4D 72 03 E9 64 C1 4D 1E FA DC 32 C1
        FA AC EA 60 1D 2E 46 32 21 E7 B6 62 22 15 1B 2E
        7D 21 E2 B0 63 A4 1F 1B 6A 98 61 F8 D0 35 21 0E
        DF 43 3B 20 F9 F1 70 31 0F F5 13 3D 10 F8 5B 31
        D3 47 FD B7 9D 38 3C BA 98 B8 A7 6B 61 89 80 78
        CE BC C8 87 DE 89 AA 0A 7D 2D 18 69 03 E6 6A CE
        DA 3E 95 0D 4D 17 B0 40 C4 48 3E EE 9C 64 53 AF
        75 C3 40 3C D6 8C 14 53 EB 6D C6 4C B7 46 CC A6
        A9 F3 D9 62 26 5F 73 6A A2 21 DC AA E7 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+fh6_SR!.Qs${Qw++X{,(}X{9oD?MrdM2`.F2!b".}!cja5!C; p1=[1G8<kax}-ij>M@H>dSu@<SmLFb&_sj!"

[+] Synchronized Frame 163 Isolated at Symbol Offset 1753880:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DF A2 EF 22 1F 9B 0E FA 60 E4 BE E3 66 1F CD
        47 1A 44 ED BC 31 31 0F 09 93 81 10 B9 55 73 10
        0F 65 B3 0D 34 F4 8F 51 CB 07 C7 A1 AB 92 76 F9
        18 99 87 F6 EB 8C 88 7F AC B8 CA 87 82 D9 82 98
        7D 4F B8 A9 83 E1 D8 94 99 2F 4D 2C 4C 8B D6 7D
        54 44 3A D4 5C F4 03 F1 6C C1 45 3F F6 5C 70 43
        F1 E8 6B 64 95 B7 D6 66 61 E5 36 E2 22 1D CA 2E
        7A 21 F0 B6 E1 A6 9F AB 6E 1E 61 FC 57 25 61 4F
        CF 63 13 30 F1 9A 71 51 0F B5 F1 3D 10 F0 59 30
        D2 07 A6 F0 0D 11 FC EB 3A 98 25 E5 ED 1D 80 7D
        E9 90 88 87 DA EA 8E 08 78 AD 98 69 83 DE F9 8F
        99 3E 7D 0D 68 07 B7 D8 C4 40 3C 6F FC 44 43 BF
        65 CF 44 3E 56 8C 34 D3 FC 6D E5 8C 3F CA 96 B6
        49 D9 70 66 24 1E 7B 6E 32 21 D5 A2 67 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!"`fGD11Use4Qv}O/M,L}TD:\lE?\pCkdfa6".z!naW%aOc0qQ=Y0:%}xi>}h@<oDCeD>V4m?Ipf${n2!g"

[+] Synchronized Frame 164 Isolated at Symbol Offset 1764640:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE BA E7 90 1E 0B 06 5A 65 FD 3E F1 C6 17 87
        57 5B 14 ED 7A 31 32 2F 99 85 19 10 ED 59 77 D1
        4F 05 A3 0D 10 FD EB 70 D3 07 C6 A7 8B 82 76 B2
        50 99 97 EC C9 8C 88 7E 68 B8 49 07 E2 D9 96 8A
        5D 6D A8 A9 82 E5 52 D6 D1 3B 79 0C 44 0B F7 7C
        C4 40 3F 94 5D 9C 03 CD 68 C1 65 3E F3 DC 30 C0
        F2 AA 6B 60 9D BE 86 32 65 E3 68 F2 22 1F DA 26
        5A 21 F0 B4 64 A6 1F 71 6E 39 E9 FC D4 27 71 4A
        D2 43 11 12 F8 9F 71 11 0E D5 17 3F 00 FE 5B 30
        D3 4F BD 97 1C 32 FC EA 10 D9 A5 27 81 88 80 79
        48 9A 88 87 52 8B 9A 00 7D AD 98 69 A3 FF 58 06
        18 3A 0D 29 4C 43 F4 D0 C4 48 3E 26 C8 44 42 B9
        65 C7 40 BC D6 1C 34 D3 EC 6D C3 0E 3F 12 94 A4
        03 DB E1 62 26 1F 37 2F 26 21 D4 AA 67 B6 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!Ze>W[z12/YwOpvP~hI]mR;yD|@?]he>0k`2eh"&Z!dqn9'qJCq?[0O2'yHR}iX:)LCH>&DBe@4m?b&7/&!g"

[+] Synchronized Frame 165 Isolated at Symbol Offset 1775400:
    ├── Extracted APID Subsystem ID : 0x1DA
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DA A2 67 A0 1E 4B 66 1A 48 F9 52 E7 A2 5E 91
        43 53 44 FD B4 33 12 2F 11 B3 11 10 FA D1 33 C1
        4F 85 93 05 A4 FF DF 21 59 0F D2 A1 8D 9A D6 FA
        58 98 87 A4 C1 C8 88 76 AA 99 60 07 92 D1 86 92
        3F BC B8 69 83 ED 5B 94 C1 2B 6F 0C 64 4B CE EC
        C4 44 3C 54 54 F6 43 C1 68 C3 4D 1F 4A 5C 10 CA
        F0 28 6B 62 9D AC 86 72 61 F3 36 62 22 1D 8A 2E
        F5 21 E0 B6 63 A6 9F FF 6E 1E 20 72 15 25 30 4E
        DB 53 17 24 F3 9E 71 91 0E C5 57 3D 10 FE 5A 30
        D2 4F FD D7 18 B0 BC EA B2 F0 87 E7 B1 08 80 7E
        CD B8 88 A7 72 8B 9E 88 7D AD 98 E9 A7 D6 5B C6
        90 7E 05 0D 6D 03 B4 D0 C6 C8 BE C4 44 64 43 B9
        45 4F 64 3E 17 0C 34 D3 FE FD ED 4C 9F 7A 84 B8
        0B DA 78 67 22 1F 17 4F 22 21 DC BA E3 B2 9E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!gKfHR^CSD3/3O!YXv`?i[+odKD<TTChMJ\(kbra6b".!cn r%0NS$qW=Z0O~r}[~mDdCEOd>4Lzxg"O"!"

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

[+] Synchronized Frame 167 Isolated at Symbol Offset 1796920:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC A2 E1 A2 9F 0B 66 72 61 FF D2 E1 26 1F 9D
        67 53 15 EC 74 73 33 0F 11 35 99 10 EA 15 33 D5
        0F 85 A1 0D 04 FF EB 71 CB 0F D8 B9 AD 28 76 8F
        38 89 17 C4 FB 88 88 77 AA BA EC 87 8A D9 82 98
        3D 64 88 F9 87 E9 D0 D7 81 6F 7F 2C 64 4B C6 61
        C6 CC 3B D4 5C 72 53 E1 6C C5 4D 3F F2 D4 70 43
        F0 E8 EB 68 BF 9A 86 22 45 FB 16 F2 22 1D AA A6
        3B 21 E0 B6 63 A4 9F F3 2E 0A 65 79 55 35 27 5B
        CF 43 13 20 F8 9B 51 11 0F A5 17 6C 10 F8 5B 33
        53 4F F9 C7 1D B2 FC EB 18 B8 25 63 31 88 99 7C
        ED AC C8 87 52 A9 9E C8 7E 2C 99 69 87 FD CA 8B
        58 7D 1D 1D 48 42 F7 F8 C6 44 3E 66 46 44 43 BB
        65 C7 04 3F 16 8C B4 D3 F9 6D E5 0C 7F 0A 9E 34
        09 DB EC 63 26 9F 1B 2A 22 21 D5 B2 63 00 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!fra&gSts353q(v8w=do,dKa;\rSlM?pCh"E";!c.eyU5'[C Ql[3SO%c1|R~,iX}HBD>fFDCe?m4c&*"!c"

[+] Synchronized Frame 168 Isolated at Symbol Offset 1807680:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 DF B2 EA B2 1F 0B 46 2A 28 F7 B7 60 B6 0F 8D
        4B 1F 05 ED 68 31 11 0F 39 A4 19 10 FA D1 73 51
        0F C5 A3 0D 34 7B DB 79 D1 0F CF B1 29 8A 74 DA
        58 C9 97 CC EB 98 88 7D 28 B9 AC 87 C2 D1 8E 9A
        5E 84 E8 AD 87 E5 51 C4 95 2B 1C 0C E4 03 E6 69
        E4 44 3A D4 1D D0 03 C5 6C C3 49 3F F6 4C 7C C3
        F3 28 C2 E0 3F B7 D6 26 65 F1 34 F3 22 1D CB AE
        78 21 F0 B4 63 B2 8E F3 6D 3A 61 7B D7 24 B0 5B
        D7 0B 11 30 FA B7 19 11 0E C7 D3 7D 80 FC 5B 32
        D2 4F FD B7 05 30 FC 2B D2 98 87 6E E1 88 98 7C
        C9 28 88 87 5A 89 86 80 7F 2D 98 68 87 E7 DB CA
        59 36 4D 29 4C 16 B3 D0 CE C8 3E 27 9C 44 43 A1
        55 CF 44 BF 17 4C 94 43 FA 7D 47 4C 3F 9A 96 A6
        29 DA 6C 67 20 5F B3 A6 A2 01 D8 A2 EF 92 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "F*(`Kh19sQ4{y)tX}(^Q+iD:lI?L|(?&e4"x!cm:a{$[0}[2O0+n|(Z-hY6M)L>'DCUDLC}GL?)lg _"

[+] Synchronized Frame 169 Isolated at Symbol Offset 1818440:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A0 6D 22 1F 4B 46 3A 69 FF AE 23 E6 4F A5
        67 5B 55 AC FC 71 32 2F 8B B7 11 10 EC 51 72 90
        0F 85 B3 0D 36 FD DB 50 F3 0B C0 A5 2D 20 76 9B
        18 89 87 9D DB 0C 88 7F 28 9B A8 87 9A D9 80 DA
        5F BB 98 58 80 E3 D8 C4 C9 29 7D 2C 4C 8B E3 6D
        C4 44 3B 96 5C 96 43 F9 64 C3 4D 3F 3E DC 58 C2
        F1 2C CA 48 BD AE 96 66 41 E5 B2 62 22 1F DB AE
        6B 21 FB B6 60 24 4F 33 EE 28 01 FA 30 31 23 5A
        C7 4B 11 22 F2 AB 69 91 0E 81 17 3F 10 FE 59 30
        D1 47 8E B7 1C 92 3C 2A 1A D9 A7 6F BD 88 98 5C
        6F B8 89 87 76 A9 AC 09 7C 2D 98 29 83 EE F9 8E
        58 7E 15 CD 48 42 B3 DA C4 CC 3F 6E C8 64 43 F1
        45 CB 44 3E 56 CC 14 52 EC 2D E2 4C 1F 26 E4 26
        29 DF CD 62 66 1F 33 6F 32 21 F8 B2 EE A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!m"KF:i#Og[Uq2/Qr6P- v(_X)},LmD;\CdM?>X,HfAb"k!`$O3(01#ZK"i?Y0G<*o\ov|-)X~HB?ndCED>VR-L&&)bf3o2!"

[+] Synchronized Frame 170 Isolated at Symbol Offset 1829200:
    ├── Extracted APID Subsystem ID : 0x1D4
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D4 A2 EB AA 1F 0B 46 3A 28 F8 96 23 F6 0B E5
        43 12 70 ED 74 B3 33 0E 9D B3 11 10 ED 59 72 D1
        0F 85 B3 0D 34 7F 9B 39 D0 07 E3 A1 8B 82 76 FA
        18 C9 87 94 C9 88 88 76 6A B9 EA 87 C2 D9 8A 89
        1F EC 98 E0 83 F9 51 86 C5 7F 7D 4C C4 CB FB 65
        64 44 3F B4 5D C4 03 E5 64 C7 4D 3E 3C 9C 34 C2
        F5 E0 4A 48 9D BA A6 22 61 E1 E6 E2 22 1D AA 26
        6A 21 F0 B6 61 A6 8E 3B 4F 3E 65 BD 54 25 31 4E
        D2 43 39 12 F3 F7 31 11 0E C5 17 3D 90 FB 5A 31
        D3 0F FB B7 0E 90 BC 6A 38 DB AF E5 A1 98 80 7C
        CD FC D8 87 72 C9 9C 08 7D 2D 98 69 A7 F9 DB CE
        98 7E 15 5D 4C 03 B6 CA C4 08 3F 26 4C C4 43 AB
        55 CA 44 3E 16 CC 34 C3 F1 ED E7 4C 1F 0A 96 A6
        29 5A E8 62 22 1F B2 27 22 A1 DC B2 E3 A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!F:(#Cpt3Yr49vvjQ}LedD?]dM><4JH"a"&j!a;O>eT%1NC91=Z1j8|r}-i~]L?&LCUD>4L)Zb"'""

[+] Synchronized Frame 171 Isolated at Symbol Offset 1839960:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC BA EF 82 1F AB 26 3A 29 FD 56 73 E6 0F 97
        4A 57 14 FC E8 31 33 0F B9 07 19 10 FC 59 72 51
        0F 05 B3 29 34 FE 19 71 51 3F D2 B9 09 82 7E F8
        18 99 87 CC DA 88 80 75 AE 38 A8 97 CA C9 92 99
        7E E4 B8 20 87 EB 52 84 80 3B 2F AC 44 D3 E7 6D
        40 40 3E 1C 4C F4 43 F1 68 CB 4D 3F E3 DC 78 C4
        70 E8 6A E0 BF BE 86 22 41 FF 3A F3 22 1F 5B 26
        72 21 E0 B4 66 A6 1F BD A4 2A 41 FE 74 21 20 4F
        9F 43 39 30 F9 99 79 11 0F E5 97 35 90 FC 59 31
        93 4E FD 93 1D 12 FD AA 9A D9 07 4B B1 88 88 7C
        C9 28 88 87 72 AB 9E A8 7E 2D 98 68 A7 FD CA EE
        98 7F 6D 28 48 02 B4 C2 C4 CC 3C E5 94 44 5B B9
        44 CF 44 3C 16 CC 74 D3 FC 7D C1 2C BF 2E C4 A6
        41 58 F8 63 24 5F 37 6B 22 21 DE AA E1 90 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!&:)VsJW13YrQ)4qQ?~u8~ R;/Dm@@>LChM?xpj"A:"[&r!f*At! OC90y5Y1NK|(r~-hm(H<D[DD<t},.AXc$_7k"!"

[+] Synchronized Frame 172 Isolated at Symbol Offset 1850720:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC A8 EE A2 1F 0B 66 BA 28 FF B6 A2 E6 0F 55
        5B 1A 24 ED E0 B3 12 0F DD B7 95 50 FF 5D 31 D5
        0F 85 A3 0D 34 7D E9 79 4B 0F E6 A3 AD 82 76 9F
        18 8B 87 8D F9 88 88 7F AA BA A8 07 B2 D9 8E 9A
        3F 1D F8 AC 87 E1 50 D4 C5 3B 7D 2C C4 4B E6 68
        C4 44 3F 94 5C B5 43 C9 48 C2 4C 1E F6 DE 56 CB
        F4 28 6A 40 9D B4 86 66 61 F7 30 A2 22 1D FA 2E
        F2 01 F0 B6 66 A6 9F F1 62 3E 21 FC 55 35 B6 0A
        DF 6B 11 10 F2 DA 79 91 0F A5 17 2D 80 FA 5B 30
        D3 4F EF F1 16 70 FC 6A 12 90 0F 67 C5 88 98 7E
        69 8C 89 87 52 AB 9E 88 7C 2C 98 69 A7 FE CB 8E
        89 3E 0D 8D 6D 17 D4 90 C6 40 3E 6E CC 44 43 FF
        41 CA 04 3A 56 CC 64 11 F6 AD 47 8C 3E 06 C4 B6
        41 DB DD 42 20 5F B3 D6 32 21 D5 AA E1 A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!f(U[$P]14}yKv?P;},KhD?\CHLV(j@fa0".fb>!U5ky-[0Opjg~iR|,i>m@>nDCA:VdG>AB _2!"

[+] Synchronized Frame 173 Isolated at Symbol Offset 1861480:
    ├── Extracted APID Subsystem ID : 0x1F0
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 F0 A2 6B B2 1F CB 66 1A 60 FA BE A0 D2 43 8D
        6B 56 14 AD BC F3 13 2F 99 35 B1 10 EA 55 33 40
        0F A5 B3 15 30 7F DB 5D C1 07 C0 B5 8B 8A 7A F2
        19 98 97 CC F1 88 88 76 2C B9 28 87 F2 C9 86 88
        7E 2D BC 71 87 61 D4 D4 C5 3B 79 8C 6C 8B F6 6D
        C4 44 3B 17 5C A4 43 F9 64 CB 4D 3E D7 56 B6 CB
        F7 E8 4B E8 9D B7 16 22 61 F3 32 A2 22 1D DA 2E
        23 21 F0 B6 62 A6 9F C3 EE 39 61 FB D7 F5 30 0E
        45 07 11 32 FD 79 59 91 0E F5 17 3C 10 FD 59 30
        53 4F DF D5 9C B0 7C EA D0 5B 07 65 E9 18 98 79
        DD BC 18 87 B2 EB B6 C8 7C 2D 19 E9 27 FE CB 8E
        89 7F FD CD 6D 17 F7 D0 CD 4D 3E 24 6C 6C 43 AD
        45 CF 24 3E 56 8C 34 53 E7 6D C7 8C 3F 0A 8C B6
        01 5B E9 63 20 1F 13 ED 32 25 FC A2 EC A0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!kf`CkV/5U3@0]zv,(~-qa;ylmD;\CdM>VK"a2".#!b9a0E2yY<Y0SO|[ey|-'mM>$llCE$>V4Sm?[c 2%"

[+] Synchronized Frame 174 Isolated at Symbol Offset 1872240:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        01 DE B2 E7 A2 1E CB 06 1A 48 FF BA E2 A6 5F A5
        4F 57 10 FD F4 31 12 2F 99 B1 11 10 ED DD 77 18
        0F 05 91 0D 34 7F DB 79 4B 2F DD B3 3B 82 76 BF
        18 88 07 CF B3 08 88 77 2A 9B 68 87 C2 89 A6 9A
        3F E6 A0 E9 83 E3 58 D5 CD 3B 5A 8C C4 83 F6 7C
        E4 44 3B 14 1C E0 43 C9 6C C7 49 1E 66 5E 74 41
        F4 AC 6B 4C 3D BE 06 62 61 F3 14 60 22 1D CA 2E
        39 29 F2 B6 61 A2 9F BA 6E 38 E1 F9 14 61 33 4E
        F2 43 31 32 F8 B2 31 91 0E 85 17 65 80 F9 5A 30
        D3 47 FF 93 1F B0 7C 2A 92 98 25 6B A5 98 80 79
        CE AC 88 85 56 8B 9C 88 7C 2D 99 A9 A7 DA DA CE
        09 7E 15 8D 7C 93 B7 D0 CE 4C 3F 7E D4 64 43 E1
        45 CF 04 3F 16 CC 94 43 F3 25 43 04 BF 4E 54 B6
        29 DA C9 62 44 1E B3 EE 32 01 F6 AA E7 A0 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "H_OW1/w4yK/;vw*h?X;Z|D;ClIf^tAkL=ba`".9)an8a3NC121eZ0G|*%kyV|-~|L?~dCE?C%CNT)bD2"

[+] Synchronized Frame 175 Isolated at Symbol Offset 1883000:
    ├── Extracted APID Subsystem ID : 0x1DC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DC B2 EE 00 1F 8B 26 7A 29 F9 36 63 A2 1F 85
        46 53 11 EC F4 31 33 2F 3B B7 91 12 EE 59 76 D1
        0F 95 93 0D 34 FF 1B 78 D9 2F C9 B5 A9 A0 76 9A
        18 89 17 8C DB CC 88 7F A8 88 A8 A7 A2 C9 86 9A
        7C ED AC 61 81 E1 58 96 C0 7B 79 0C CC 03 CE AD
        E5 44 3E 96 5C B0 43 F5 64 C7 4C 3F F6 DC 38 C3
        F0 A6 CB 44 95 BF D6 32 05 E1 F6 E2 22 1D CA AE
        6E 21 D0 B6 61 A2 8F BF 6F 3A 70 DA 96 35 71 0E
        D3 63 33 30 FD 1B F3 11 0E AD D7 0D 16 F9 5B 31
        D2 0F 9B 95 1C B0 FC 2A 7A B8 A7 6F A1 8C 98 7C
        EE B8 88 87 FE 8B 9E 08 78 AD 98 E9 A7 FE 5B 87
        C9 7E 0D 08 5C 43 B2 F8 C6 4C 3E A6 DC 44 43 F5
        65 C5 44 3F 16 CC B4 D3 FE 6D E7 4C 3F 0A 86 36
        2B F9 F4 62 26 1F 33 CE 22 21 DC B0 ED A2 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!&z)6cFS13/;Yv4x/v|aX{yD>\CdL?8D2"n!ao:p5qc30[1*zo|x[~\CL>DCeD?mL?6+b&3"!"

[+] Synchronized Frame 176 Isolated at Symbol Offset 1893760:
    ├── Extracted APID Subsystem ID : 0x1FC
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 FC A2 ED 30 1F 4B 46 1A 28 FB A6 61 A6 5F 8F
        6B 5F 54 BD FC 31 11 2F 99 95 01 10 EE 51 74 51
        0F 85 B3 1D 14 7E DB 71 F3 2F C3 B1 2B 82 DE FA
        58 C9 87 CC DA 88 8A 77 28 BB E0 07 D2 D9 82 9A
        77 ED BC 79 81 F7 50 D7 D9 3F 2D 0C 4D 0B CA E8
        C0 44 3D B4 1C D4 43 C5 68 C3 4D 1E 76 CC 16 C0
        D0 AA 4A E8 95 86 86 22 65 EB A4 F2 22 1D 4A 2E
        68 21 E0 B6 60 A2 9F 7F EF 3D 61 7A 35 35 31 4F
        DF EB 31 10 FF 9F 71 11 0E E5 57 16 10 F0 5B 30
        D3 0F E1 B7 15 10 FC 6B 18 D9 0D 6F A5 09 88 7C
        AD B8 88 87 5E C9 98 88 78 2C 98 AD 83 F2 DF 8F
        58 5E 15 0D 48 13 F7 92 CE 4C 3F 6A DC 44 43 F9
        65 C7 64 3E 16 CC 34 C1 FC AD C7 2C 2F CA 84 A4
        81 DB E8 67 24 7E 32 66 32 21 F8 B2 67 8A 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!0KF(a_k_T1/QtQ~q/+Xw(wyP?-MD=ChMvJ"e"J.h!`=az551O1qW[0ko|^x,X^HL?jDCed>4,/g$~2f2!g"

[+] Synchronized Frame 177 Isolated at Symbol Offset 1904520:
    ├── Extracted APID Subsystem ID : 0x1D2
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 D2 B2 E7 A0 1F 0B 06 1B 29 F7 BE E3 84 55 DF
        5F 53 14 AD 44 31 12 0F CD B5 11 10 ED D1 34 D1
        0F C5 83 25 34 FA 5B 35 F9 2F C2 B1 29 92 76 3A
        18 89 87 E5 8A C8 88 76 28 B9 E8 85 8A D9 96 92
        7D 8D B9 2C 87 E1 D0 D4 D5 7F 2D 8C 6C 4B C2 A4
        C4 44 3F 34 5C 50 43 C1 64 C3 45 3D D7 DC 7D 49
        E0 AA E2 E0 BD 3E CE 66 61 F1 B6 62 22 1D 2A 2E
        22 21 F0 B0 65 A6 1F E9 46 1B 21 7D 55 35 33 5E
        DF E3 13 30 F7 FA 31 91 0E A5 17 31 10 F9 5B 33
        51 47 9F 9B 9D 10 FC 2A 58 98 05 6E A9 88 81 71
        4D B8 88 87 EA E9 9C 00 7E 2C 18 29 A7 E7 DB 86
        D8 6E 15 89 68 53 B7 18 CC C4 3C AD 5C 4C 03 B9
        44 DF 4C 3C 16 8C F4 51 EF FC 47 4C BF 0A 86 A6
        09 DA 6C 67 E4 1E 1B 4B 22 21 FC A2 E5 B0 1F
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!)U_SD14%4[5/)v:v(},-lKD?4\PCdE=}I>fab"*."!eF!}U53^011[3QG*XnqM~,)nhS<\LDL<QGLlgK"!"

[+] Synchronized Frame 178 Isolated at Symbol Offset 1915280:
    ├── Extracted APID Subsystem ID : 0x1DF
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DF AA E3 A2 1F 8B 26 7A 61 FF D3 62 86 5F B3
        53 5A 64 ED F4 B1 17 0F BD 2B 91 12 EE D9 33 F1
        0F 95 93 05 34 FF 9B 11 E9 2A C3 B1 A9 8A 76 F3
        99 C9 97 9C FB 88 98 75 AE B9 E8 97 D2 D9 86 92
        7F ED 98 61 83 D1 58 86 C8 3A 69 AC 4C C7 E2 F5
        E5 C4 3B 15 5D B4 43 DD 64 C1 45 3F D3 DC 74 C7
        F1 A8 4A 68 BD 86 16 26 03 E1 28 E3 22 1D CE AE
        5A 21 EC BA 61 A4 0F 7B EE 2A 60 F8 74 35 50 5E
        CF 2B 11 20 FD DB 71 11 0E A5 17 01 80 F9 5B 31
        D3 4F C4 B7 1F 10 FC 0A 9A DB 05 6F 01 8C 88 7C
        CC A8 98 87 F2 A9 9E A0 7C 2D 98 69 A7 D8 DA 8E
        1A 5C 45 4D 58 56 B7 90 CC 48 BE 6E 96 64 43 BD
        45 CC 64 2F D6 8C 34 C3 EF 3C E3 4C 3F 16 AC 26
        03 DB CE E2 66 1E 13 6F 22 21 FC B2 E4 B2 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!&zab_SZd+34*vuaX:iL;]CdE?tJh&("Z!a{*`t5P^+ q[1Oo||-i\EMXVHndCEd/4<L?&fo"!"

[+] Synchronized Frame 179 Isolated at Symbol Offset 1926040:
    ├── Extracted APID Subsystem ID : 0x1DE
    └── Full Decoded Frame Payload Hex (223 Bytes):
        21 DE B2 E3 A2 1F 2B 66 2A 69 F8 AE E3 F7 7F AD
        63 5B 04 EC F6 31 93 0F 9F 17 11 10 EE D8 13 D1
        0F 85 B3 25 34 F9 DF 51 D3 0E E1 B1 AB A2 76 1C
        18 C9 87 9C DE C8 88 77 28 BB 68 07 D2 D1 86 8A
        3D F5 9C EB 87 E1 D0 C5 C1 7F 6C 0C 64 8B E7 6C
        E6 44 3B 16 DD F4 03 E1 64 CF 45 1F 7E D4 77 C3
        F1 AD 6A C8 9D AC 96 62 61 FF B2 E2 22 1D 8B 2E
        52 21 F8 B6 61 A6 8F DB 6E 39 26 F9 D6 31 B0 4A
        DB 83 73 10 F9 7A 71 11 0E F5 53 2C 10 FC 5B 30
        D0 4F F9 F3 15 12 BD AA 73 BA 8F 44 A1 0C 90 79
        ED B8 C8 87 76 CB 9E 89 7C 2D 98 69 A3 CC FB 86
        98 BF D5 99 5C 16 F3 F2 CC 4C 3E E4 8C 44 C3 B9
        75 D7 44 3C 17 CC B4 4B EF 2D 4F 2C 3F 02 86 84
        69 D9 DC 66 20 1F D3 6F 22 21 DC A2 E2 32 1E
        -------------------------------------------------
    └── Extracted ASCII Strings (Skipping Non-Printable):
        └─ "!+f*ic[1%4Qvw(h=ldlD;dE~wjba".R!an9&1JszqS,[0OsDyv|-i\L>DuD<K-O,?if o"!2"

[*] ===============================================
[*] Pipeline processing complete. Parsed 180 frames safely.
[*] ===============================================
