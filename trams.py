# -*- coding: UTF-8 -*-

trams = {'ŽST Vinohrady': (48.1857811, 17.1331615),
         'Odborárska': (48.1767018, 17.1462562),
         'Zlaté piesky': (48.1894747, 17.1832841),
         'Hlavná stanica': (48.1580612, 17.1069616),
         'Slovanet': (48.1559227, 17.1423346),
         'Saleziáni': (48.1551391, 17.133958),
         'STU': (48.1523201, 17.1157568),
         'Nám. Biely kríž': (48.1821751, 17.1297673),
         'Vozovňa Krasňany': (48.1888511, 17.1362371),
         'Černockého': (48.1996659, 17.1475656),
         'Kamenné nám.': (48.1455395, 17.113559),
         'ŽST Nové Mesto': (48.1715369, 17.1454668),
         'Trnavské mýto': (48.1578266, 17.1274982),
         'Vysoká': (48.1484611, 17.1123005),
         'Americké nám.': (48.151106, 17.1179506),
         'Kapucínska': (48.1449449, 17.1049719),
         'ŽST Nové Mesto': (48.1719398, 17.1454366),
         'Detvianska': (48.2111984, 17.1548265),
         'Žilinská': (48.1545357, 17.1103665),
         'Most SNP': (48.1397672, 17.1056993),
         'Molecova': (48.1493614, 17.0631736),
         'Jurigovo námestie': (48.1520959, 17.0613428),
         'Segnerova': (48.153643, 17.0578354),
         'Nad lúčkami': (48.1560222, 17.0535376),
         'Borská': (48.1621051, 17.0485989),
         'Karlova Ves': (48.1644645, 17.0468962),
         'Drobného': (48.1878915, 17.036662),
         'Americké nám.': (48.1508408, 17.1181852),
         'STU': (48.1512188, 17.1160848),
         'Jesenského': (48.142166, 17.1102847),
         'Astronomická': (48.1585697, 17.1771889),
         'Zátišie': (48.1719608, 17.1413853),
         'Ursínyho': (48.1619737, 17.1238219),
         'Pionierska': (48.1679236, 17.1274638),
         'Riazanská': (48.1731517, 17.1271935),
         'ŽST Vinohrady': (48.1859131, 17.1336572),
         'Pekná cesta': (48.1957361, 17.143841),
         'Hečkova': (48.2029016, 17.1494608),
         'Herlianska-OC Retro': (48.1570213, 17.1563639),
         'Malé Krasňany': (48.1910693, 17.1388367),
         'Poštová-Martinus': (48.1467137, 17.1087702),
         'Švantnerova': (48.1816487, 17.0407981),
         'Alexyho': (48.1845828, 17.0379879),
         'Dolné Krčace': (48.1703978, 17.0495328),
         'Horné Krčace': (48.1736765, 17.0492079),
         'Damborského': (48.178941, 17.0442784),
         'Lafranconi': (48.1452174, 17.0780548),
         'Mariánska': (48.1473993, 17.1155267),
         'Park kultúry': (48.1427052, 17.0858182),
         'Botanická záhrada': (48.1481357, 17.0717803),
         'Legionárska': (48.1547027, 17.1236619),
         'MiÚ Karlova Ves': (48.158733, 17.0516049),
         'Nová doba': (48.1650134, 17.1347081),
         'Odbojárov': (48.1620361, 17.1318194),
         'Polus City Center': (48.1685817, 17.1381315),
         'Shopping Palace': (48.1884508, 17.1777535),
         'Chatam Sófer': (48.1408687, 17.0930282),
         'Jurajov dvor': (48.1830088, 17.1637702),
         'Magnetová': (48.1798468, 17.1544115),
         'PPA Controll': (48.1854625, 17.1706942),
         'Šafárikovo námestie': (48.1417026, 17.1157112),
         'Nemocnica Ružinov': (48.1567037, 17.1520925),
         'Blumentál': (48.1535948, 17.1187979),
         'Hybešova': (48.2076722, 17.1503896),
         'Komisárky': (48.216186, 17.1662226),
         'Komisárky': (48.2162855, 17.1665144),
         'Mladá garda': (48.1773678, 17.1280017),
         'Púchovská': (48.2153654, 17.1645903),
         'Račianske mýto': (48.1579549, 17.1205274),
         'Záhumenice-Drevona': (48.2122916, 17.159269),
         'OD Saratov': (48.1916648, 17.0351364),
         'Pri kríži': (48.194736, 17.0339237),
         'Tomášikova': (48.1574257, 17.1618369),
         'Chlumeckého': (48.1584158, 17.1750981),
         'Súmračná': (48.1579795, 17.1692868),
         'Záhumenice-Drevona': (48.2116062, 17.15835),
         'Hečkova': (48.2031217, 17.1495403),
         'Černockého': (48.199315, 17.1471856),
         'Pekná cesta': (48.1952965, 17.1433805),
         'Malé Krasňany': (48.1912896, 17.1390342),
         'Vozovňa Krasňany': (48.1883502, 17.1355642),
         'Pionierska': (48.1693975, 17.1272851),
         'Račianske mýto': (48.1584725, 17.1210004),
         'Blumentál': (48.1538751, 17.1189611),
         'Trnavské mýto': (48.157623, 17.1271676),
         'Vysoká': (48.1487558, 17.1129474),
         'Kapucínska': (48.1451591, 17.1055581),
         'Zlaté piesky': (48.1894759, 17.1826885),
         'Nám. Ľ. Štúra': (48.140209, 17.1096039),
         'Jurigovo námestie': (48.1523141, 17.0612493),
         'Saleziáni': (48.1555414, 17.1335261),
         'Slovanet': (48.1557406, 17.1407091),
         'Púchovská': (48.2147824, 17.1632955),
         'Detvianska': (48.2110892, 17.1546191),
         'ŽST Vinohrady': (48.1857128, 17.1333867),
         'Nám. Biely kríž': (48.1825954, 17.1302837),
         'Mladá garda': (48.1779006, 17.1281805),
         'Riazanská': (48.1743883, 17.127483),
         'Ursínyho': (48.1624693, 17.1242352),
         'Hlavná stanica': (48.1577105, 17.1067752),
         'Námestie Franza Liszta': (48.156049, 17.1073582),
         'Poštová-Martinus': (48.1471841, 17.1097765),
         'Námestie SNP': (48.1451993, 17.1116367),
         'Jesenského': (48.1429334, 17.1120069),
         'Most SNP': (48.1397937, 17.1051969),
         'Chatam Sófer': (48.141198, 17.0924593),
         'Park kultúry': (48.1430645, 17.0840806),
         'Lafranconi': (48.1451568, 17.0782391),
         'Botanická záhrada': (48.1481265, 17.0724726),
         'Molecova': (48.149832, 17.0629251),
         'Segnerova': (48.1538512, 17.0571133),
         'Nad lúčkami': (48.1564879, 17.0532684),
         'MiÚ Karlova Ves': (48.1592601, 17.0512874),
         'Borská': (48.1626165, 17.0482856),
         'Karlova Ves': (48.1646427, 17.0468161),
         'Dolné Krčace': (48.1709178, 17.0495359),
         'Horné Krčace': (48.174194, 17.0491125),
         'Damborského': (48.1796779, 17.0434042),
         'Švantnerova': (48.1824495, 17.0398173),
         'Alexyho': (48.1860176, 17.0374407),
         'Drobného': (48.1886922, 17.0363959),
         'OD Saratov': (48.1922471, 17.0349543),
         'Pri kríži': (48.1950498, 17.0338404),
         'Mariánska': (48.1483509, 17.1164788),
         'Americké nám.': (48.1515864, 17.1180952),
         'Odborárske nám.': (48.1520063, 17.1201636),
         'Legionárska': (48.1549227, 17.1240066),
         'Trnavské mýto': (48.1577873, 17.1275749),
         'Odbojárov': (48.1616436, 17.1314024),
         'Nová doba': (48.1646412, 17.1342885),
         'Polus City Center': (48.1689435, 17.1384329),
         'Zátišie': (48.1714473, 17.1408367),
         'Odborárska': (48.1764233, 17.145792),
         'Magnetová': (48.1793259, 17.1527756),
         'Jurajov dvor': (48.1824684, 17.1620987),
         'PPA Controll': (48.1849801, 17.1692388),
         'Shopping Palace': (48.1878657, 17.1764562),
         'Astronomická': (48.1585376, 17.1763494),
         'Chlumeckého': (48.1583171, 17.1733694),
         'Súmračná': (48.1578894, 17.1676052),
         'Tomášikova': (48.1573261, 17.1600777),
         'Herlianska-OC Retro': (48.1569417, 17.1549158),
         'Hybešova': (48.208242, 17.1509866),
         'Nemocnica Ružinov': (48.1566815, 17.1513983),
         'Žilinská': (48.1543071, 17.1108053),
         'Farského': (48.1276018, 17.1169015),
         'Farského': (48.1272404, 17.1168363),
         'Námestie Franza Liszta': (48.1560226, 17.1074169),
         'Jungmannova': (48.1244875, 17.1149539),
         'Jungmannova': (48.1248177, 17.1154067),
         'Sad Janka Kráľa': (48.1353448, 17.1169879),
         'Sad Janka Kráľa': (48.1358072, 17.1170409),
         'Šafárikovo nám.': (48.1413427, 17.1161809),
         'Vozovňa Jurajov dvor': (48.1813353, 17.1614439),
         'Vozovňa Jurajov dvor': (48.1815265, 17.1613635)
}

trams_rev = {(48.1857811, 17.1331615): 'ŽST Vinohrady',
             (48.1767018, 17.1462562): 'Odborárska',
             (48.1894747, 17.1832841): 'Zlaté piesky',
             (48.1580612, 17.1069616): 'Hlavná stanica',
             (48.1559227, 17.1423346): 'Slovanet',
             (48.1551391, 17.133958): 'Saleziáni',
             (48.1523201, 17.1157568): 'STU',
             (48.1821751, 17.1297673): 'Nám. Biely kríž',
             (48.1888511, 17.1362371): 'Vozovňa Krasňany',
             (48.1996659, 17.1475656): 'Černockého',
             (48.1455395, 17.113559): 'Kamenné nám.',
             (48.1715369, 17.1454668): 'ŽST Nové Mesto',
             (48.1578266, 17.1274982): 'Trnavské mýto',
             (48.1484611, 17.1123005): 'Vysoká',
             (48.151106, 17.1179506): 'Americké nám.',
             (48.1449449, 17.1049719): 'Kapucínska',
             (48.1719398, 17.1454366): 'ŽST Nové Mesto',
             (48.2111984, 17.1548265): 'Detvianska',
             (48.1545357, 17.1103665): 'Žilinská',
             (48.1397672, 17.1056993): 'Most SNP',
             (48.1493614, 17.0631736): 'Molecova',
             (48.1520959, 17.0613428): 'Jurigovo námestie',
             (48.153643, 17.0578354): 'Segnerova',
             (48.1560222, 17.0535376): 'Nad lúčkami',
             (48.1621051, 17.0485989): 'Borská',
             (48.1644645, 17.0468962): 'Karlova Ves',
             (48.1878915, 17.036662): 'Drobného',
             (48.1508408, 17.1181852): 'Americké nám.',
             (48.1512188, 17.1160848): 'STU',
             (48.142166, 17.1102847): 'Jesenského',
             (48.1585697, 17.1771889): 'Astronomická',
             (48.1719608, 17.1413853): 'Zátišie',
             (48.1619737, 17.1238219): 'Ursínyho',
             (48.1679236, 17.1274638): 'Pionierska',
             (48.1731517, 17.1271935): 'Riazanská',
             (48.1859131, 17.1336572): 'ŽST Vinohrady',
             (48.1957361, 17.143841): 'Pekná cesta',
             (48.2029016, 17.1494608): 'Hečkova',
             (48.1570213, 17.1563639): 'Herlianska-OC Retro',
             (48.1910693, 17.1388367): 'Malé Krasňany',
             (48.1467137, 17.1087702): 'Poštová-Martinus',
             (48.1816487, 17.0407981): 'Švantnerova',
             (48.1845828, 17.0379879): 'Alexyho',
             (48.1703978, 17.0495328): 'Dolné Krčace',
             (48.1736765, 17.0492079): 'Horné Krčace',
             (48.178941, 17.0442784): 'Damborského',
             (48.1452174, 17.0780548): 'Lafranconi',
             (48.1473993, 17.1155267): 'Mariánska',
             (48.1427052, 17.0858182): 'Park kultúry',
             (48.1481357, 17.0717803): 'Botanická záhrada',
             (48.1547027, 17.1236619): 'Legionárska',
             (48.158733, 17.0516049): 'MiÚ Karlova Ves',
             (48.1650134, 17.1347081): 'Nová doba',
             (48.1620361, 17.1318194): 'Odbojárov',
             (48.1685817, 17.1381315): 'Polus City Center',
             (48.1884508, 17.1777535): 'Shopping Palace',
             (48.1408687, 17.0930282): 'Chatam Sófer',
             (48.1830088, 17.1637702): 'Jurajov dvor',
             (48.1798468, 17.1544115): 'Magnetová',
             (48.1854625, 17.1706942): 'PPA Controll',
             (48.1417026, 17.1157112): 'Šafárikovo námestie',
             (48.1567037, 17.1520925): 'Nemocnica Ružinov',
             (48.1535948, 17.1187979): 'Blumentál',
             (48.2076722, 17.1503896): 'Hybešova',
             (48.216186, 17.1662226): 'Komisárky',
             (48.2162855, 17.1665144): 'Komisárky',
             (48.1773678, 17.1280017): 'Mladá garda',
             (48.2153654, 17.1645903): 'Púchovská',
             (48.1579549, 17.1205274): 'Račianske mýto',
             (48.2122916, 17.159269): 'Záhumenice-Drevona',
             (48.1916648, 17.0351364): 'OD Saratov',
             (48.194736, 17.0339237): 'Pri kríži',
             (48.1574257, 17.1618369): 'Tomášikova',
             (48.1584158, 17.1750981): 'Chlumeckého',
             (48.1579795, 17.1692868): 'Súmračná',
             (48.2116062, 17.15835): 'Záhumenice-Drevona',
             (48.2031217, 17.1495403): 'Hečkova',
             (48.199315, 17.1471856): 'Černockého',
             (48.1952965, 17.1433805): 'Pekná cesta',
             (48.1912896, 17.1390342): 'Malé Krasňany',
             (48.1883502, 17.1355642): 'Vozovňa Krasňany',
             (48.1693975, 17.1272851): 'Pionierska',
             (48.1584725, 17.1210004): 'Račianske mýto',
             (48.1538751, 17.1189611): 'Blumentál',
             (48.157623, 17.1271676): 'Trnavské mýto',
             (48.1487558, 17.1129474): 'Vysoká',
             (48.1451591, 17.1055581): 'Kapucínska',
             (48.1894759, 17.1826885): 'Zlaté piesky',
             (48.140209, 17.1096039): 'Nám. Ľ. Štúra',
             (48.1523141, 17.0612493): 'Jurigovo námestie',
             (48.1555414, 17.1335261): 'Saleziáni',
             (48.1557406, 17.1407091): 'Slovanet',
             (48.2147824, 17.1632955): 'Púchovská',
             (48.2110892, 17.1546191): 'Detvianska',
             (48.1857128, 17.1333867): 'ŽST Vinohrady',
             (48.1825954, 17.1302837): 'Nám. Biely kríž',
             (48.1779006, 17.1281805): 'Mladá garda',
             (48.1743883, 17.127483): 'Riazanská',
             (48.1624693, 17.1242352): 'Ursínyho',
             (48.1577105, 17.1067752): 'Hlavná stanica',
             (48.156049, 17.1073582): 'Námestie Franza Liszta',
             (48.1471841, 17.1097765): 'Poštová-Martinus',
             (48.1451993, 17.1116367): 'Námestie SNP',
             (48.1429334, 17.1120069): 'Jesenského',
             (48.1397937, 17.1051969): 'Most SNP',
             (48.141198, 17.0924593): 'Chatam Sófer',
             (48.1430645, 17.0840806): 'Park kultúry',
             (48.1451568, 17.0782391): 'Lafranconi',
             (48.1481265, 17.0724726): 'Botanická záhrada',
             (48.149832, 17.0629251): 'Molecova',
             (48.1538512, 17.0571133): 'Segnerova',
             (48.1564879, 17.0532684): 'Nad lúčkami',
             (48.1592601, 17.0512874): 'MiÚ Karlova Ves',
             (48.1626165, 17.0482856): 'Borská',
             (48.1646427, 17.0468161): 'Karlova Ves',
             (48.1709178, 17.0495359): 'Dolné Krčace',
             (48.174194, 17.0491125): 'Horné Krčace',
             (48.1796779, 17.0434042): 'Damborského',
             (48.1824495, 17.0398173): 'Švantnerova',
             (48.1860176, 17.0374407): 'Alexyho',
             (48.1886922, 17.0363959): 'Drobného',
             (48.1922471, 17.0349543): 'OD Saratov',
             (48.1950498, 17.0338404): 'Pri kríži',
             (48.1483509, 17.1164788): 'Mariánska',
             (48.1515864, 17.1180952): 'Americké nám.',
             (48.1520063, 17.1201636): 'Odborárske nám.',
             (48.1549227, 17.1240066): 'Legionárska',
             (48.1577873, 17.1275749): 'Trnavské mýto',
             (48.1616436, 17.1314024): 'Odbojárov',
             (48.1646412, 17.1342885): 'Nová doba',
             (48.1689435, 17.1384329): 'Polus City Center',
             (48.1714473, 17.1408367): 'Zátišie',
             (48.1764233, 17.145792): 'Odborárska',
             (48.1793259, 17.1527756): 'Magnetová',
             (48.1824684, 17.1620987): 'Jurajov dvor',
             (48.1849801, 17.1692388): 'PPA Controll',
             (48.1878657, 17.1764562): 'Shopping Palace',
             (48.1585376, 17.1763494): 'Astronomická',
             (48.1583171, 17.1733694): 'Chlumeckého',
             (48.1578894, 17.1676052): 'Súmračná',
             (48.1573261, 17.1600777): 'Tomášikova',
             (48.1569417, 17.1549158): 'Herlianska-OC Retro',
             (48.208242, 17.1509866): 'Hybešova',
             (48.1566815, 17.1513983): 'Nemocnica Ružinov',
             (48.1543071, 17.1108053): 'Žilinská',
             (48.1276018, 17.1169015): 'Farského',
             (48.1272404, 17.1168363): 'Farského',
             (48.1560226, 17.1074169): 'Námestie Franza Liszta',
             (48.1244875, 17.1149539): 'Jungmannova',
             (48.1248177, 17.1154067): 'Jungmannova',
             (48.1353448, 17.1169879): 'Sad Janka Kráľa',
             (48.1358072, 17.1170409): 'Sad Janka Kráľa',
             (48.1413427, 17.1161809): 'Šafárikovo nám.',
             (48.1813353, 17.1614439): 'Vozovňa Jurajov dvor',
             (48.1815265, 17.1613635): 'Vozovňa Jurajov dvor'
}
