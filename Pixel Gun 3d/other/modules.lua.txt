gg.toast("Updated by never | orginally made by kyh")
gg.searchNumber("h F3 0F 1E F8 FD 7B 01 A9 FD 43 00 91 33 4D 02 B0 68 D2 6A 39 E8 00 00 37 68 19 02 D0 08 15 45 F9", gg.TYPE_BYTE)
--[[ found: 0 ]]
gg.alert("execute twice!!")
--[[ return: 1 ]]
gg.clearResults()
gg.setRanges(gg.REGION_CODE_APP)
gg.setVisible(false)
gg.searchNumber("h 60 00 00 B4 E2 03 1F AA EB 09 03 14 C0 03 5F D6 F5 53 BE A9 F3 7B 01 A9 35 22 02 B0 A8 32 47 39 F3 03 01 AA F4 03 00 AA C8 00 00 37 C0 FB 01 90", gg.TYPE_BYTE)
--found - 2308C70
--[[ found: 64 ]]
gg.getResults(8)
--[[ count: 8 ]]
gg.editAll("h 20 00 80 D2 C0 03 5F D6", gg.TYPE_BYTE)
gg.clearResults()
gg.setVisible(false)





gg.searchNumber("h F4 0F 1E F8 F3 7B 01 A9 60 02 00 B4 E1 03 1F AA F3 03 00 AA F3 60 F2 97 60 01 00 36 E0 03 13 AA E1 03 1F AA 68 60 F2 97 F4 03 00 2A E0 03 13 AA", gg.TYPE_BYTE)
--found - 2310E00
--[[ found: 64 ]]
gg.getResults(8)
--[[ count: 8 ]]
gg.editAll("h 20 00 80 D2 C0 03 5F D6", gg.TYPE_BYTE)
gg.clearResults()
gg.setVisible(false)




gg.searchNumber("h FF 43 01 D1 F5 53 03 A9 F3 7B 04 A9 35 22 02 B0 A8 2A 47 39 F3 03 01 AA F4 03 00 AA C8 00 00 37 40 FE 01 F0 00 EC 46 F9 16 E3 A9 97 28 00 80 52", gg.TYPE_BYTE)
--found - 2308B70
--[[ found: 64 ]]
gg.getResults(8)
--[[ count: 8 ]]
gg.editAll("h 20 00 80 D2 C0 03 5F D6", gg.TYPE_BYTE)
gg.clearResults()


gg.searchNumber("h F4 0F 1E F8 F3 7B 01 A9 74 6E 02 F0 88 26 6F 39 F3 03 00 AA C8 00 00 37 C0 48 02 D0 00 F8 41 F9 33 51 D2 97 28 00 80 52 88 26 2F 39 33 02 00 B4 C8 48 02 D0 08 F9 41 F9 00 01 40 F9 08 E0 40 B9", gg.TYPE_BYTE)
--[[ found: 0 ]]
gg.searchNumber("h F5 53 BE A9 F3 7B 01 A9 74 6E 02 F0 F5 46 02 90 88 2A 6F 39 B5 FA 47 F9 F3 03 00 AA 28 01 00 37 60 4A 02 B0 00 DC 46 F9 B5 50 D2 97 E0 46 02 90 00 F8 47 F9 B2 50 D2 97 28 00 80 52 88 2A 2F 39", gg.TYPE_BYTE)
--[[ found: 0 ]]
gg.clearResults()
gg.alert("done! now you can upgrade your modules (you will need a lot of coins) | if it doesn't work, run the script again.")
--[[ return: 0 ]]
