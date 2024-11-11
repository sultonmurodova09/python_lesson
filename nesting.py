allomalar={
'alloma1':{
    'ism':'Abu Abdulloh Muhammad Ibn Ismoil',
    'yil':810,
    'qayerda':'Buxoro',
    'umr':60
},
'alloma2':{
    'ism':'Abdulla Qodiriy',
    'yil':1894,
    'qayerda':'Toshkent',
    'umr':44,
},
'alloma3':{
    'ism':'Erkin Vohidova',
    'yil':1936,
    'qayerda':'Farg\'ona',
    'umr':80,
},
'alloma4':{
    'ism':'Alisher Navoiy',
    'yil':1441,
    'qayerda':'Xirot',
    'umr':60,  
},
}
for alloma,info in allomalar.items():
    print(f"{info['ism'].title()},"
          f"{info['yil']}-yilda,"
          f"{info['qayerda']}da tug'ilgan."
          f"{info['umr']} yil umr ko'rgan.")
    

allomalar={
'alloma1':{
    'ism':'Abu Abdulloh Muhammad Ibn Ismoil',
    'asarlari':'Al-jome as-ashih , Al-adab al-mufrad , At-tarix al-kabir , At-tarix as-sag\'ir'
},
'alloma2':{
    'ism':'Abdulla Qodiriy',
   'asarlari':'O\'tgan kunlar , Mexrobdan chayon , Obid ketmon'
},
'alloma3':{
    'ism':'Erkin Vohidova',
   'asarlari':'Tong nafasi , Qo\'shiqlarim sizga , O\'zbegim , Qiziquvchan Matmusa'
},
'alloma4':{
    'ism':'Alisher Navoiy',
    'asarlari':'Xamsa , Lison ut-tayr , Mahbub Al-Qulub , Munojot'
},
}
for ism , info in allomalar.items():
    print(
        f"{info['ism']}ning mashxur asarlari:"
        f"{info['asarlari']}"
)
    
kinolar={
'ism1':{
    'ism':'shirinoy',
    'kinolar':'lanatlangan rohiba , sirli uy , ilonlar o\'rmoni'
},
'ism2':{
    'ism':'oysulton',
    'kinolar':'asl  go\'zallik , mening iblisim , biz o\'likmiz ,'
},
'ism3':{
    'ism':'guli',
    'kinolar':'shaytanat , meros , baxt ovchisi , jurnalist'
},
}
for ism , info in kinolar.items():
    print(
        f"{info['ism'].title()}ning sevimli kinolari:"
        f"{info['kinolar']}"
    )