I added a nhdemod4.py that descrambles the frames (using the standard CCSDS descrambler) and turbo (1/6) decodes them.

python bpsk2.py | tee ccsds.log

creates a file called telemetry_output.bin from the webcam

then type, as new bytes are added to the file, 

python3 nhdemod12.py telemetry_output.bin out.frames # turbo version 1

or

python script3.py telemetry_output.bin frames.out # turbo code version 2

or

cat ccsds.log | tail -n 1000 | python3 space.py > telem3.bin

or

cat ccsds.log | tail -n 1000 | python3 space.py -k 7 -r 2 -p "79,5B" -i "0,1" > telem3.bin # for the voyager code

it doesn't have to be pointed directly at the planets/spacecraft to work.

----------------------------
you get frames like: 


        00000010  2A 5A 01 68 31 AF D4 45 DB 55 70 72 67 35 52 D7  |*Z.h1..E.Uprg5R.|
        00000020  6F 4B 88 88 4E 8D 4F 14 66 6D 2B A3 1E F6 AC 1F  |oK..N.O.fm+.....|

from ESCAPADE-Blue:

[+] Frame 05142 [Offset 00005142]: REPAIRED (1-Bit Corrected)

    ├── Layer 2 Format  : AOS (V2)
    
    ├── Spacecraft ID   : 9
    
    └── Virtual Channel : 56
    
    └── Uncorrupted Frame Panel Data:
    
        00000000  42 78 15 0D DD 86 EB 77 FF 96 55 67 34 D8 51 97  |Bx.....w..Ug4.Q.|
        
        00000010  69 6F 90 AF 69 04 17 F1 7B C0 7A B8 CE 1D 34 76  |io..i...{.z...4v|
        
        00000020  62 0A 37 FD BB D5 E1 07 04 C4 4F 91 CE 0F 43 99  |b.7.......O...C.|
        
        00000030  09 35 03 60 7B 91 18 5F 07 21 51 92 21 94 A2 2D  |.5.`{.._.!Q.!..-|
        
        00000040  5D 3B 73 C8 70 99 C7 D0 07 A6 50 7C 22 E3 C2 66  |];s.p.....P|"..f|
        00000050  0C F4 73 63 62 75 51 24 09 06 2F C4 1A AD D8 FF  |..scbuQ$../.....|
        
        00000060  92 41 D6 62 F1 F6 0A 64 03 CE 11 5A F1 CA E2 7C  |.A.b...d...Z...||
        
        00000070  F3 BF 64 2C D3 8D 92 4D 1A E8 24 47 E4 4B 45 02  |..d,...M..$G.KE.|
        
        00000080  92 8F 88 E0 80 C1 56 2B 6A F2 55 E0 49 79 AD 6B  |......V+j.U.Iy.k|
        
        00000090  03 D4 EB 44 34 5A 3B CD 18 5F A2 3A 88 17 38 D4  |...D4Z;.._.:..8.|
        
        000000A0  3F 9A 25 6F AD 9D A6 7F E4 78 78 DC D3 3C 32 51  |?.%o.....xx..<2Q|
        
        000000B0  93 7A B1 08 08 B7 5C A4 4F 0C 51 6F 99 16 4D 82  |.z....\.O.Qo..M.|
        
        000000C0  6A CA C5 58 C1 C0 65 98 E1 B6 09 0A EB 5C 3A 17  |j..X..e......\:.|
        
        000000D0  EF 6E 57 C1 95 0E 54 94 33 45 B7 39 53 46 A0     |.nW...T.3E.9SF.|
        
        -----------------------------------------------------------------------


from LCROSS Shepherd:

[+] Frame 00530 [Offset 00000530]: REPAIRED (1-Bit Corrected)

    ├── Layer 2 Format  : AOS (V2)
    
    ├── Spacecraft ID   : 18
    
    └── Virtual Channel : 40
    
    └── Uncorrupted Frame Panel Data:
    
        00000000  44 A8 53 06 01 51 6F 06 77 C6 17 38 31 41 89 32  |D.S..Qo.w..81A.2|
        
        00000010  38 11 30 C1 2D 26 22 1B 15 61 B1 00 F6 3D A6 82  |8.0.-&"..a...=..|
        
        00000020  DF 2B DE 1A 66 06 A1 A2 E0 14 5F 60 9D 5D 11 01  |.+..f....._`.]..|
        
        00000030  90 56 BF D6 7B D4 55 36 8B 71 81 B0 BD AB 11 A6  |.V..{.U6.q......|
        
        00000040  54 50 90 76 90 24 F5 06 6F 05 9E 11 5D 96 F4 9A  |TP.v.$..o...]...|
        
        00000050  5D C4 22 43 01 31 27 3D E3 7A 29 6D BA 5E C7 CC  |]."C.1'=.z)m.^..|
        
        00000060  13 28 91 7A 61 7D CC C5 6E 9C 30 70 36 48 B1 BF  |.(.za}..n.0p6H..|
        
        00000070  D8 94 BF 25 BD 0C 0E 4F 9A FA AE 42 6C 4C 98 EF  |...%...O...BlL..|
        
        00000080  8E 9F BB CC 9C 16 70 DC A4 CD D3 5D 30 E0 4A 28  |......p....]0.J(|
        
        00000090  5C 98 23 6F BE 39 69 A8 A4 97 00 AA A5 73 80 EF  |\.#o.9i......s..|
        
        000000A0  8E 2C 9C 28 EF 14 9B B3 94 4F F0 B3 1A 02 D0 25  |.,.(.....O.....%|
        
        000000B0  6D CD B1 0F 33 63 90 B9 11 3E C5 19 7B D3 21 4B  |m...3c...>..{.!K|
        
        000000C0  2A 3E 55 28 22 94 A2 63 AE EC 1E 1B F9 1D FD FF  |*>U("..c........|
        
        000000D0  78 12 8D 00 D0 A8 D4 A1 26 19 A1 3F A9 43 15     |x.......&..?.C.|

        
        -----------------------------------------------------------------------





or with an earlier attempt :

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

