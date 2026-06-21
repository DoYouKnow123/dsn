
I tested this latest version in ubuntu linux stonking as of june 20/21 th/st (2026) or so.

Most webcams are sensitive to visible light these days, but they have some capability for x-band radio science.

the array read from the file mapping2 should work over nyquist since it's topologically compact in the frequency domain

python3 bpsk.py | tee -a xband.log

then in another window (there might be some error saying it can't find a valid CCSDS frame, but just ignore it
the format is different)


cat xband.log | tail -n 1000 | python3 space.py > telem.bin 

xxd telem.bin | python iceye.py

xxd -p -c 0 iceeye_recovered.bin | grep -o -E '[0-9a-fA-F]{36}0000' | python3 scid3.py

SCID's are approximate, example new horizons frame in iceeye_recovered.bin
```diff
  00000050: 0000 0590 4b0d 55d6 19fe 8155 2fc6 ff4d  ....K.U....U/..M
+ 00000060: 7cad ec25 0000 0670 7ceb 1d75 ff90 7440  |..%...p|..u..t@
+ 00000070: 0e33 7adc 5472 5a2b 0000 0700 c77c 23da  .3z.TrZ+.....|#.
  00000080: dba9 491c edeb 8f8c a8d3 ff1e 0000 0730  ..I............0
  00000090: 2855 96d3 357c f122 bcfc ae58 f731 42ac  (U..5|."...X.1B.
```

example output of scid3.py for new horizons frame:

06707ceb1d75ff9074400e337adc54725a2b0000, apid = 1648, apid_hex = 0x670, scid = -103, SCLK = 4287657024
