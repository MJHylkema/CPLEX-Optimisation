Minimize
     r
Subject to
     demandflow11:   x111 + x121 = 2
     demandflow12:   x112 + x122 = 3
     demandflow13:   x113 + x123 = 4
     demandflow14:   x114 + x124 = 5
     demandflow21:   x211 + x221 = 3
     demandflow22:   x212 + x222 = 4
     demandflow23:   x213 + x223 = 5
     demandflow24:   x214 + x224 = 6
     demandflow31:   x311 + x321 = 4
     demandflow32:   x312 + x322 = 5
     demandflow33:   x313 + x323 = 6
     demandflow34:   x314 + x324 = 7
     cap11X:         x111 + x112 + x113 + x114 - c11 <= 0
     cap12X:         x121 + x122 + x123 + x124 - c12 <= 0
     cap21X:         x211 + x212 + x213 + x214 - c21 <= 0
     cap22X:         x221 + x222 + x223 + x224 - c22 <= 0
     cap31X:         x311 + x312 + x313 + x314 - c31 <= 0
     cap32X:         x321 + x322 + x323 + x324 - c32 <= 0
     capX11:         x111 + x211 + x311 - d11 <= 0
     capX12:         x112 + x212 + x312 - d12 <= 0
     capX13:         x113 + x213 + x313 - d13 <= 0
     capX14:         x114 + x214 + x314 - d14 <= 0
     capX21:         x121 + x221 + x321 - d21 <= 0
     capX22:         x122 + x222 + x322 - d22 <= 0
     capX23:         x123 + x223 + x323 - d23 <= 0
     capX24:         x124 + x224 + x324 - d24 <= 0
     flow111:        3 x111 - 2 U111 = 0
     flow121:        3 x121 - 2 U121 = 0
     flow112:        3 x112 - 3 U112 = 0
     flow122:        3 x122 - 3 U122 = 0
     flow113:        3 x113 - 4 U113 = 0
     flow123:        3 x123 - 4 U123 = 0
     flow114:        3 x114 - 5 U114 = 0
     flow124:        3 x124 - 5 U124 = 0
     flow211:        3 x211 - 3 U211 = 0
     flow221:        3 x221 - 3 U221 = 0
     flow212:        3 x212 - 4 U212 = 0
     flow222:        3 x222 - 4 U222 = 0
     flow213:        3 x213 - 5 U213 = 0
     flow223:        3 x223 - 5 U223 = 0
     flow214:        3 x214 - 6 U214 = 0
     flow224:        3 x224 - 6 U224 = 0
     flow311:        3 x311 - 4 U311 = 0
     flow321:        3 x321 - 4 U321 = 0
     flow312:        3 x312 - 5 U312 = 0
     flow322:        3 x322 - 5 U322 = 0
     flow313:        3 x313 - 6 U313 = 0
     flow323:        3 x323 - 6 U323 = 0
     flow314:        3 x314 - 7 U314 = 0
     flow324:        3 x324 - 7 U324 = 0
     nbFlows11:      U111 + U121 = 3
     nbFlows12:      U112 + U122 = 3
     nbFlows13:      U113 + U123 = 3
     nbFlows14:      U114 + U124 = 3
     nbFlows21:      U211 + U221 = 3
     nbFlows22:      U212 + U222 = 3
     nbFlows23:      U213 + U223 = 3
     nbFlows24:      U214 + U224 = 3
     nbFlows31:      U311 + U321 = 3
     nbFlows32:      U312 + U322 = 3
     nbFlows33:      U313 + U323 = 3
     nbFlows34:      U314 + U324 = 3
     TRANSIT1:        x111 +  x112 +  x113 +  x114 +  x211 +  x212 +  x213 +  x214 +  x311 +  x312 +  x313 +  x314 - r <= 0
     TRANSIT2:        x121 +  x122 +  x123 +  x124 +  x221 +  x222 +  x223 +  x224 +  x321 +  x322 +  x323 +  x324 - r <= 0
Bounds
     0 <= r
     0 <= x111
     0 <= x112
     0 <= x113
     0 <= x114
     0 <= x121
     0 <= x122
     0 <= x123
     0 <= x124
     0 <= x211
     0 <= x212
     0 <= x213
     0 <= x214
     0 <= x221
     0 <= x222
     0 <= x223
     0 <= x224
     0 <= x311
     0 <= x312
     0 <= x313
     0 <= x314
     0 <= x321
     0 <= x322
     0 <= x323
     0 <= x324
Binary
     U111
     U121
     U112
     U122
     U113
     U123
     U114
     U124
     U211
     U221
     U212
     U222
     U213
     U223
     U214
     U224
     U311
     U321
     U312
     U322
     U313
     U323
     U314
     U324
End