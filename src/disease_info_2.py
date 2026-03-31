"""
Disease Info — Part 2 of 3
Classes 31–61: chilli_whitefly → potato_late_blight
Source: ICAR & PAU Ludhiana guidelines
"""

DISEASE_INFO_2 = {

    # ── 31 ────────────────────────────────────────────────────────────────────
    "chilli_whitefly": {
        "name_en": "Chilli Whitefly Infestation",
        "name_hi": "मिर्च की सफेद मक्खी",
        "cause_en": "Silverleaf whitefly Bemisia tabaci (Biotype B). "
                    "Sucks phloem sap and transmits viruses (ChiLCV, TYLCV).",
        "cause_hi": "बेमिसिया टेबेसी (बायोटाइप B) सफेद मक्खी। फ्लोएम रस चूसती है "
                    "और वायरस (ChiLCV, TYLCV) फैलाती है।",
        "symptoms_en": "Yellowing and upward curling of leaves; sticky honeydew; "
                       "sooty mold; reduced plant vigor; viral disease symptoms if vector.",
        "symptoms_hi": "पत्तियों का पीलापन और ऊपर की ओर मुड़ना; चिपचिपा मधुरस; "
                       "काली फफूंद; पौधे की कमजोरी; वाहक होने पर वायरस लक्षण।",
        "cure_en": "Spray systemic neonicotinoid insecticide. Use yellow sticky traps "
                   "(one per 25 sq m). Remove heavily infested leaves.",
        "cure_hi": "प्रणालीगत नियोनिकोटिनॉइड कीटनाशक छिड़काव करें। पीले चिपचिपे जाल "
                   "(25 वर्ग मीटर पर एक) लगाएँ। अत्यधिक संक्रमित पत्तियाँ हटाएँ।",
        "prevention_en": "Install yellow sticky traps before planting. Reflective silver mulch "
                         "repels whitefly. Avoid planting near tomato/tobacco. "
                         "Release Encarsia formosa (parasitoid) for biocontrol.",
        "prevention_hi": "रोपण से पहले पीले चिपचिपे जाल लगाएँ। परावर्तक चाँदी मल्च सफेद मक्खी भगाती है। "
                         "टमाटर/तंबाकू के पास न लगाएँ। जैव नियंत्रण के लिए एन्कार्सिया फॉर्मोसा छोड़ें।",
        "pesticide_en": "Imidacloprid 17.8 SL @ 0.5 mL/L OR Spiromesifen 22.9 SC @ 1.0 mL/L "
                        "OR Diafenthiuron 50 WP @ 1.0 g/L. Spray undersides of leaves. "
                        "Rotate groups every 2 sprays.",
        "pesticide_hi": "इमिडाक्लोप्रिड 17.8 SL @ 0.5 मिली/ली अथवा स्पाइरोमेसीफेन 22.9 SC @ 1.0 मिली/ली "
                        "अथवा डायफेनथियूरॉन 50 WP @ 1.0 ग्राम/ली। पत्तियों की निचली सतह पर छिड़काव। "
                        "हर 2 छिड़काव पर समूह बदलें।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 32 ────────────────────────────────────────────────────────────────────
    "chilli_yellowish": {
        "name_en": "Chilli Yellowing (Nutrient Deficiency / Viral)",
        "name_hi": "मिर्च का पीलापन (पोषक तत्व कमी / वायरल)",
        "cause_en": "Multiple causes: nitrogen or iron deficiency, magnesium deficiency, "
                    "or mild viral infection (CMV, TSWV). Root-related stress also causes yellowing.",
        "cause_hi": "अनेक कारण: नाइट्रोजन या लोहे की कमी, मैग्नीशियम की कमी, "
                    "या हल्का वायरल संक्रमण (CMV, TSWV)। जड़ तनाव भी पीलापन करता है।",
        "symptoms_en": "Interveinal yellowing (Mg deficiency); uniform pale yellow plant (N deficiency); "
                       "mosaic yellowing with stunting (viral); no lesions in deficiency cases.",
        "symptoms_hi": "नसों के बीच पीलापन (Mg कमी); पूरा पौधा हल्का पीला (N कमी); "
                       "अवरुद्ध विकास के साथ मोज़ेक पीलापन (वायरल); कमी में कोई घाव नहीं।",
        "cure_en": "For nutrient deficiency: foliar spray of 2% urea (N) or "
                   "0.5% ferrous sulfate (Fe) or 1% magnesium sulfate (Mg). "
                   "For viral: manage vectors and remove infected plants.",
        "cure_hi": "पोषक कमी के लिए: 2% यूरिया (N) या 0.5% फेरस सल्फेट (Fe) या "
                   "1% मैग्नीशियम सल्फेट (Mg) का पत्ती पर छिड़काव। वायरल के लिए: वाहक प्रबंधन।",
        "prevention_en": "Soil testing before planting. Apply balanced NPK + micronutrients. "
                         "Maintain pH 6.0–6.8. Control aphid/whitefly vectors.",
        "prevention_hi": "रोपण से पहले मिट्टी परीक्षण। संतुलित NPK + सूक्ष्म पोषक तत्व दें। "
                         "pH 6.0–6.8 बनाए रखें। माहू/सफेद मक्खी वाहक नियंत्रित करें।",
        "pesticide_en": "Nutrient spray: Ferrous sulfate 0.5% OR MgSO4 1% foliar. "
                        "Vector control: Imidacloprid 17.8 SL @ 0.5 mL/L. "
                        "No fungicide needed for yellowing alone.",
        "pesticide_hi": "पोषक छिड़काव: फेरस सल्फेट 0.5% या MgSO4 1% पत्ती पर। "
                        "वाहक नियंत्रण: इमिडाक्लोप्रिड 17.8 SL @ 0.5 मिली/ली। "
                        "केवल पीलेपन के लिए फफूंदनाशक नहीं।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 33 ────────────────────────────────────────────────────────────────────
    "common_root_rot": {
        "name_en": "Wheat Common Root Rot",
        "name_hi": "गेहूँ का सामान्य जड़ सड़न रोग",
        "cause_en": "Fungi Bipolaris sorokiniana and Fusarium culmorum / F. graminearum. "
                    "Soil-borne; favored by dry, warm soils and crop stress.",
        "cause_hi": "बाइपोलारिस सोरोकिनियाना और फ्यूजेरियम कल्मोरम फफूंद। "
                    "मृदाजनित; शुष्क, गर्म मिट्टी और फसल तनाव में अधिक।",
        "symptoms_en": "Brown to black discoloration of subcrown internode and roots; "
                       "premature ripening of tillers (whiteheads); poor root system; reduced yield.",
        "symptoms_hi": "उप-ताज संधि और जड़ों का भूरा से काला रंग परिवर्तन; "
                       "कल्लों का समय से पहले पकना (सफेद बालियाँ); खराब जड़ तंत्र; उपज में कमी।",
        "cure_en": "No curative chemical once established. Apply foliar nitrogen "
                   "to compensate early losses. Ensure adequate irrigation at crown-root stage.",
        "cure_hi": "एक बार स्थापित होने पर कोई उपचारात्मक रसायन नहीं। "
                   "प्रारंभिक हानि पूरी करने के लिए पत्ती पर नाइट्रोजन दें। ताज-जड़ अवस्था पर पर्याप्त सिंचाई।",
        "prevention_en": "Seed treatment with Carbendazim + Thiram. Crop rotation with non-host crops. "
                         "Avoid drought stress. Deep plowing to expose and kill soil inoculum.",
        "prevention_hi": "कार्बेन्डाज़िम + थीरम से बीज उपचार। गैर-पोषक फसलों के साथ फसल चक्र। "
                         "सूखे तनाव से बचें। मिट्टी के टीके को उजागर करने के लिए गहरी जुताई।",
        "pesticide_en": "Seed treatment: Carbendazim 50 WP @ 2.0 g/kg + Thiram 75 WS @ 2.5 g/kg. "
                        "OR Tebuconazole 2% DS @ 1.5 g/kg seed. Apply before sowing.",
        "pesticide_hi": "बीज उपचार: कार्बेन्डाज़िम 50 WP @ 2.0 ग्राम/किग्रा + थीरम 75 WS @ 2.5 ग्राम/किग्रा। "
                        "अथवा टेब्युकोनाज़ोल 2% DS @ 1.5 ग्राम/किग्रा बीज। बुवाई से पहले लगाएँ।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 34 ────────────────────────────────────────────────────────────────────
    "corn_maize_cercospora_leaf_spot_gray_leaf_spot": {
        "name_en": "Maize Gray Leaf Spot (Cercospora Leaf Spot)",
        "name_hi": "मक्का का सेर्कोस्पोरा पत्ती धब्बा (ग्रे लीफ स्पॉट)",
        "cause_en": "Fungus Cercospora zeae-maydis. Favored by prolonged leaf wetness, "
                    "high humidity, and warm temperatures (25–30°C).",
        "cause_hi": "सेर्कोस्पोरा ज़ी-मेडिस फफूंद। लंबे समय तक पत्ती की नमी, "
                    "उच्च आर्द्रता और गर्म तापमान (25–30°C) में अधिक।",
        "symptoms_en": "Rectangular grayish-tan lesions limited by leaf veins; "
                       "lesions run parallel to veins giving streaky appearance; "
                       "severe infection causes blight and lodging.",
        "symptoms_hi": "पत्ती नसों से सीमित आयताकार भूरे-पीले घाव; "
                       "घाव नसों के समानांतर चलते हैं जिससे धारीदार दिखता है; "
                       "गंभीर संक्रमण से झुलसा और आलोढ़न।",
        "cure_en": "Apply foliar fungicide at tasseling stage. "
                   "One spray at VT (tasseling) stage provides best economic return.",
        "cure_hi": "टेसलिंग अवस्था पर पत्ती फफूंदनाशक लगाएँ। "
                   "VT (टेसलिंग) अवस्था पर एक छिड़काव सबसे अच्छा आर्थिक लाभ देता है।",
        "prevention_en": "Plant resistant hybrids. Crop rotation with non-maize crops. "
                         "Tillage to bury infected residues. Avoid dense planting.",
        "prevention_hi": "प्रतिरोधी संकर किस्में लगाएँ। गैर-मक्का फसलों के साथ फसल चक्र। "
                         "संक्रमित अवशेष दबाने के लिए जुताई। सघन रोपण से बचें।",
        "pesticide_en": "Propiconazole 25 EC @ 1.0 mL/L OR Azoxystrobin 23 SC @ 1.0 mL/L "
                        "OR Tebuconazole 25.9 EC @ 1.0 mL/L. Apply at 10–14 day intervals.",
        "pesticide_hi": "प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली अथवा अज़ोक्सीस्ट्रोबिन 23 SC @ 1.0 मिली/ली "
                        "अथवा टेब्युकोनाज़ोल 25.9 EC @ 1.0 मिली/ली। 10–14 दिन के अंतराल पर।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 35 ────────────────────────────────────────────────────────────────────
    "corn_maize_common_rust": {
        "name_en": "Maize Common Rust",
        "name_hi": "मक्का का सामान्य रतुआ",
        "cause_en": "Fungus Puccinia sorghi. Spreads by wind-borne uredospores; "
                    "favored by cool temperatures (16–23°C) and high humidity.",
        "cause_hi": "पक्सिनिया सोर्घी फफूंद। हवा से फैलने वाले यूरेडोस्पोर; "
                    "ठंडा तापमान (16–23°C) और उच्च आर्द्रता अनुकूल।",
        "symptoms_en": "Brick-red to dark brown elongated pustules (uredinia) scattered on both "
                       "leaf surfaces; later turn black (telia); reduces photosynthesis.",
        "symptoms_hi": "दोनों पत्ती सतहों पर बिखरी ईंट-लाल से गहरे भूरे लंबी फुंसियाँ; "
                       "बाद में काली (टेलिया) हो जाती हैं; प्रकाश संश्लेषण कम होता है।",
        "cure_en": "Spray triazole or strobilurin fungicide at early pustule stage. "
                   "Generally one spray suffices if applied timely.",
        "cure_hi": "शुरुआती फुंसी अवस्था पर ट्राइएज़ोल या स्ट्रोबिलुरिन फफूंदनाशक छिड़काव। "
                   "समय पर किया एक छिड़काव सामान्यतः पर्याप्त है।",
        "prevention_en": "Use rust-resistant hybrids. Early planting avoids peak infection. "
                         "Balanced potassium nutrition reduces severity.",
        "prevention_hi": "रतुआ-प्रतिरोधी संकर किस्में उपयोग करें। जल्दी रोपण से चरम संक्रमण से बचाव। "
                         "संतुलित पोटेशियम पोषण गंभीरता कम करता है।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Propiconazole 25 EC @ 1.0 mL/L "
                        "OR Zineb 75 WP @ 2.0 g/L. Spray 500 L solution per ha.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली "
                        "अथवा ज़ाइनेब 75 WP @ 2.0 ग्राम/ली। 500 ली घोल प्रति हेक्टेयर।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 36 ────────────────────────────────────────────────────────────────────
    "corn_maize_healthy": {
        "name_en": "Maize — Healthy",
        "name_hi": "मक्का — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Use certified hybrid seed. Adequate NPK and zinc supplementation. "
                         "Timely sowing and proper plant spacing.",
        "prevention_hi": "प्रमाणित संकर बीज उपयोग करें। पर्याप्त NPK और जिंक पूरकता। "
                         "समय पर बुवाई और उचित पौध अंतराल।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 37 ────────────────────────────────────────────────────────────────────
    "corn_maize_northern_leaf_blight": {
        "name_en": "Maize Northern Leaf Blight (Turcicum Blight)",
        "name_hi": "मक्का का उत्तरी पत्ती झुलसा रोग",
        "cause_en": "Fungus Exserohilum turcicum (syn. Helminthosporium turcicum). "
                    "Favored by moderate temperatures (18–27°C) and wet weather.",
        "cause_hi": "एक्सेरोहिलम टर्सिकम फफूंद। मध्यम तापमान (18–27°C) "
                    "और नम मौसम में अधिक।",
        "symptoms_en": "Long cigar-shaped grayish-green to tan lesions (5–15 cm) on leaves; "
                       "dark sporulation visible in lesions; premature death of leaves.",
        "symptoms_hi": "पत्तियों पर लंबे सिगार के आकार के भूरे-हरे से पीले घाव (5–15 सेमी); "
                       "घावों में गहरे बीजाणु दिखते हैं; पत्तियों की समय से पहले मृत्यु।",
        "cure_en": "Apply fungicide at first appearance of lesions. "
                   "Best results when applied before tasseling.",
        "cure_hi": "घाव के पहले लक्षण पर फफूंदनाशक लगाएँ। "
                   "टेसलिंग से पहले लगाने पर सर्वोत्तम परिणाम।",
        "prevention_en": "Resistant hybrids are most effective. Crop rotation. "
                         "Deep tillage of infected stubble. Avoid overhead irrigation.",
        "prevention_hi": "प्रतिरोधी संकर किस्में सबसे प्रभावी। फसल चक्र। "
                         "संक्रमित ठूँठ की गहरी जुताई। ऊपरी सिंचाई से बचें।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Zineb 75 WP @ 2.0 g/L "
                        "OR Propiconazole 25 EC @ 1.0 mL/L. Spray 2 times at 10-day intervals.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा ज़ाइनेब 75 WP @ 2.0 ग्राम/ली "
                        "अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली। 10 दिन के अंतराल पर 2 छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 38 ────────────────────────────────────────────────────────────────────
    "fusarium_head_blight": {
        "name_en": "Wheat Fusarium Head Blight (Scab)",
        "name_hi": "गेहूँ का फ्यूजेरियम बाली झुलसा (स्कैब)",
        "cause_en": "Fungi Fusarium graminearum and F. culmorum. "
                    "Spreads by wind and rain during anthesis. "
                    "Produces mycotoxin DON (deoxynivalenol) — unsafe for humans and animals.",
        "cause_hi": "फ्यूजेरियम ग्रैमिनेरम और F. कल्मोरम फफूंद। "
                    "परागण के दौरान हवा और वर्षा से फैलती है। "
                    "माइकोटॉक्सिन DON पैदा करती है — मनुष्यों और पशुओं के लिए असुरक्षित।",
        "symptoms_en": "Premature bleaching of spikelets ('white heads'); "
                       "pink-orange spore masses at spikelet base; "
                       "shriveled, chalky infected grains (tombstone kernels).",
        "symptoms_hi": "स्पाइकलेट का समय से पहले सफेद होना ('सफेद बालियाँ'); "
                       "स्पाइकलेट आधार पर गुलाबी-नारंगी बीजाणु पुंज; "
                       "सिकुड़े, खड़िया-रंग के संक्रमित दाने।",
        "cure_en": "Apply triazole fungicide at early anthesis (50% heads flowering). "
                   "Do not feed contaminated grain to livestock without testing.",
        "cure_hi": "प्रारंभिक परागण (50% बालियाँ फूलने पर) ट्राइएज़ोल फफूंदनाशक लगाएँ। "
                   "परीक्षण किए बिना दूषित अनाज पशुओं को न खिलाएँ।",
        "prevention_en": "Grow resistant varieties. Crop rotation with non-cereal crops. "
                         "Avoid late sowing. Plow under infected residues.",
        "prevention_hi": "प्रतिरोधी किस्में उगाएँ। गैर-अनाज फसलों के साथ फसल चक्र। "
                         "देर से बुवाई न करें। संक्रमित अवशेष जुताई से दबाएँ।",
        "pesticide_en": "Tebuconazole 25.9 EC @ 1.0 mL/L OR Propiconazole 25 EC @ 1.0 mL/L "
                        "OR Metconazole 9% + 6% SC @ 1.0 mL/L. "
                        "Spray at 50% anthesis; repeat after 5–7 days if wet.",
        "pesticide_hi": "टेब्युकोनाज़ोल 25.9 EC @ 1.0 मिली/ली अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली। "
                        "50% परागण पर छिड़काव; नम रहने पर 5–7 दिन बाद दोहराएँ।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 39 ────────────────────────────────────────────────────────────────────
    "grape_black_rot": {
        "name_en": "Grape Black Rot",
        "name_hi": "अंगूर का काला सड़न रोग",
        "cause_en": "Fungus Guignardia bidwellii. Overwinters in mummified berries. "
                    "Spreads by rain; infects young tissue within 6–24 hours of wetting.",
        "cause_hi": "गुइग्नार्डिया बिडवेलिई फफूंद। सूखे दानों में सर्दी बिताती है। "
                    "वर्षा से फैलती है; 6–24 घंटे नमी में युवा ऊतक को संक्रमित करती है।",
        "symptoms_en": "Reddish-brown circular lesions on leaves with dark borders; "
                       "infected berries shrivel to black mummies attached to cluster; "
                       "shoot and tendril lesions.",
        "symptoms_hi": "पत्तियों पर गहरे हाशिए वाले लाल-भूरे गोल घाव; "
                       "संक्रमित दाने काले सूखे दानों में बदल गुच्छे से लटके रहते हैं; "
                       "प्ररोह और टेंड्रिल पर घाव।",
        "cure_en": "Remove and destroy mummified berries before budbreak. "
                   "Apply protective fungicide from pre-bloom through veraison.",
        "cure_hi": "कली फूटने से पहले सूखे दाने हटाकर नष्ट करें। "
                   "प्री-ब्लूम से वेरेसन तक सुरक्षात्मक फफूंदनाशक लगाएँ।",
        "prevention_en": "Remove all mummies and infected debris in winter. "
                         "Ensure good air circulation through pruning. "
                         "Begin fungicide program at budbreak.",
        "prevention_hi": "सर्दियों में सभी सूखे दाने और संक्रमित अवशेष हटाएँ। "
                         "छंटाई द्वारा अच्छा वायु संचार सुनिश्चित करें। "
                         "कली फूटने पर फफूंदनाशक कार्यक्रम शुरू करें।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Captan 50 WP @ 2.5 g/L "
                        "OR Myclobutanil 24.5 EC @ 1.0 mL/L. "
                        "Apply every 10–14 days from budbreak to harvest.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा कैप्टन 50 WP @ 2.5 ग्राम/ली "
                        "अथवा माइक्लोब्युटेनिल 24.5 EC @ 1.0 मिली/ली। "
                        "कली फूटने से कटाई तक हर 10–14 दिन पर।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 40 ────────────────────────────────────────────────────────────────────
    "grape_esca_black_measles": {
        "name_en": "Grape Esca / Black Measles (Grapevine Trunk Disease)",
        "name_hi": "अंगूर का एस्का / काला खसरा (तना रोग)",
        "cause_en": "Fungal complex: Phaeomoniella chlamydospora, Phaeoacremonium spp., "
                    "and Fomitiporia mediterranea. Enter through pruning wounds.",
        "cause_hi": "फफूंद समूह: फेओमोनिएला क्लैमाइडोस्पोरा, फेओएक्रेमोनियम प्रजातियाँ "
                    "और फोमिटिपोरिया मेडिटेरेनिया। छंटाई घावों से प्रवेश करती हैं।",
        "symptoms_en": "Tiger-stripe pattern (interveinal chlorosis/necrosis) on leaves; "
                       "berry skin cracks with chocolate-brown internal discoloration ('measles'); "
                       "sudden vine collapse in summer ('apoplexy').",
        "symptoms_hi": "पत्तियों पर टाइगर-धारी पैटर्न; दाने की खाल फटना और "
                       "चॉकलेट-भूरे आंतरिक रंग परिवर्तन ('खसरा'); "
                       "गर्मियों में बेल का अचानक गिरना ('एपोप्लेक्सी')।",
        "cure_en": "No complete cure. Surgically remove infected wood to healthy tissue. "
                   "Protect wounds immediately with fungicidal paste.",
        "cure_hi": "कोई पूर्ण उपचार नहीं। संक्रमित लकड़ी को स्वस्थ ऊतक तक शल्य-चिकित्सा से हटाएँ। "
                   "घावों को तुरंत फफूंदनाशक पेस्ट से सुरक्षित करें।",
        "prevention_en": "Prune in dry weather. Apply wound protectant immediately after pruning. "
                         "Disinfect pruning tools between vines. Remove and burn infected wood.",
        "prevention_hi": "शुष्क मौसम में छंटाई करें। छंटाई के तुरंत बाद घाव रक्षक लगाएँ। "
                         "बेलों के बीच छंटाई औजार कीटाणुरहित करें। संक्रमित लकड़ी जलाएँ।",
        "pesticide_en": "Wound protection: Thiophanate-methyl 70 WP paste OR "
                        "Copper-based wound sealant. "
                        "No systemic fungicide is effective once internal.",
        "pesticide_hi": "घाव सुरक्षा: थायोफनेट-मिथाइल 70 WP पेस्ट अथवा "
                        "तांबा-आधारित घाव सीलेंट। "
                        "आंतरिक संक्रमण होने पर कोई प्रणालीगत फफूंदनाशक प्रभावी नहीं।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 41 ────────────────────────────────────────────────────────────────────
    "grape_healthy": {
        "name_en": "Grape — Healthy",
        "name_hi": "अंगूर — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Dormant pruning, annual copper spray, adequate potassium, "
                         "and good canopy management maintain vine health.",
        "prevention_hi": "सुप्त छंटाई, वार्षिक तांबा छिड़काव, पर्याप्त पोटेशियम "
                         "और अच्छी छतरी प्रबंधन बेल को स्वस्थ रखती है।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 42 ────────────────────────────────────────────────────────────────────
    "grape_leaf_blight_isariopsis_leaf_spot": {
        "name_en": "Grape Leaf Blight (Isariopsis Leaf Spot)",
        "name_hi": "अंगूर का पत्ती झुलसा (इसेरिओप्सिस पत्ती धब्बा)",
        "cause_en": "Fungus Pseudocercospora vitis (syn. Isariopsis clavispora). "
                    "Favored by warm, humid conditions late in growing season.",
        "cause_hi": "स्यूडोसेर्कोस्पोरा विटिस फफूंद। उगाई के मौसम के अंत में "
                    "गर्म, नम परिस्थितियाँ अनुकूल।",
        "symptoms_en": "Irregular dark brown spots on upper leaf surface; "
                       "gray-white sporulation on lower surface; "
                       "early leaf drop reduces photosynthesis and fruit quality.",
        "symptoms_hi": "पत्तियों की ऊपरी सतह पर अनियमित गहरे भूरे धब्बे; "
                       "निचली सतह पर भूरे-सफेद बीजाणु वृद्धि; "
                       "जल्दी पत्ती झड़ने से प्रकाश संश्लेषण और फल गुणवत्ता कम।",
        "cure_en": "Apply fungicide spray at first sign of disease. "
                   "Remove fallen infected leaves from vineyard floor.",
        "cure_hi": "रोग के पहले लक्षण पर फफूंदनाशक छिड़काव। "
                   "अंगूर बाग की ज़मीन से गिरी संक्रमित पत्तियाँ हटाएँ।",
        "prevention_en": "Maintain good canopy airflow. Avoid excessive irrigation. "
                         "Apply copper spray before rainy periods.",
        "prevention_hi": "अच्छा छतरी वायु संचार बनाए रखें। अधिक सिंचाई से बचें। "
                         "वर्षा अवधि से पहले तांबा छिड़काव करें।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Carbendazim 50 WP @ 1.0 g/L "
                        "OR Copper oxychloride 50 WP @ 3.0 g/L. "
                        "Spray at 10-day intervals from veraison.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली "
                        "अथवा कॉपर ऑक्सीक्लोराइड 50 WP @ 3.0 ग्राम/ली। "
                        "वेरेसन से 10 दिन के अंतराल पर।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 43 ────────────────────────────────────────────────────────────────────
    "groundnut_early_leaf_spot": {
        "name_en": "Groundnut Early Leaf Spot",
        "name_hi": "मूँगफली का अगेती पत्ती धब्बा",
        "cause_en": "Fungus Cercospora arachidicola. Appears 30–40 days after sowing. "
                    "Spreads by rain splash and wind.",
        "cause_hi": "सेर्कोस्पोरा अराकिडिकोला फफूंद। बुवाई के 30–40 दिन बाद दिखती है। "
                    "वर्षा छींटों और हवा से फैलती है।",
        "symptoms_en": "Circular dark brown spots with yellow halos on upper leaf surface; "
                       "gray sporulation on lower surface; premature defoliation reduces pod filling.",
        "symptoms_hi": "पत्तियों की ऊपरी सतह पर पीले घेरे वाले गोल गहरे भूरे धब्बे; "
                       "निचली सतह पर भूरे बीजाणु; समय से पहले पत्ती झड़ने से फली भराव कम।",
        "cure_en": "First spray at 30 DAS (days after sowing) at first symptom. "
                   "Repeat at 10–14 day intervals. 3 sprays provide good control.",
        "cure_hi": "पहला छिड़काव 30 DAS पर (बुवाई के दिनों बाद) पहले लक्षण पर। "
                   "10–14 दिन के अंतराल पर दोहराएँ। 3 छिड़काव अच्छा नियंत्रण देते हैं।",
        "prevention_en": "Use tolerant varieties (ICGS-76, ICGS-44). "
                         "Crop rotation. Treat seed with Thiram @ 3 g/kg. "
                         "Remove infected crop debris after harvest.",
        "prevention_hi": "सहनशील किस्में (ICGS-76, ICGS-44) उगाएँ। "
                         "फसल चक्र। बीज को थीरम @ 3 ग्राम/किग्रा से उपचारित करें। "
                         "कटाई के बाद संक्रमित फसल अवशेष हटाएँ।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Chlorothalonil 75 WP @ 2.0 g/L "
                        "OR Carbendazim 50 WP @ 1.0 g/L. Spray at 30, 45, and 60 DAS.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा क्लोरोथैलोनिल 75 WP @ 2.0 ग्राम/ली "
                        "अथवा कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली। 30, 45 और 60 DAS पर छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 44 ────────────────────────────────────────────────────────────────────
    "groundnut_early_rust": {
        "name_en": "Groundnut Early Rust",
        "name_hi": "मूँगफली का अगेती रतुआ",
        "cause_en": "Fungus Puccinia arachidis. Monocyclic rust; one cycle per season. "
                    "Spreads by wind. Favored by temperatures of 20–25°C.",
        "cause_hi": "पक्सिनिया अराकिडिस फफूंद। मोनोसाइक्लिक रतुआ; प्रति मौसम एक चक्र। "
                    "हवा से फैलती है। 20–25°C तापमान अनुकूल।",
        "symptoms_en": "Small orange-brown uredia on undersides of leaves; "
                       "corresponding yellow spots on upper surface; "
                       "early severe infection causes premature leaf drop.",
        "symptoms_hi": "पत्तियों की निचली सतह पर छोटे नारंगी-भूरे यूरेडिया; "
                       "ऊपरी सतह पर संगत पीले धब्बे; "
                       "जल्दी गंभीर संक्रमण से पत्तियाँ जल्दी गिरती हैं।",
        "cure_en": "Spray fungicide at first pustule appearance. "
                   "Do not delay — rust spreads fast in favorable weather.",
        "cure_hi": "पहली फुंसी दिखने पर फफूंदनाशक छिड़काव करें। "
                   "देरी न करें — अनुकूल मौसम में रतुआ तेजी से फैलता है।",
        "prevention_en": "Use resistant varieties (JL-24, TAG-24). "
                         "Early sowing. Monitor from 30 DAS. Avoid excess humidity.",
        "prevention_hi": "प्रतिरोधी किस्में (JL-24, TAG-24) उपयोग करें। "
                         "जल्दी बुवाई। 30 DAS से निगरानी। अधिक आर्द्रता से बचें।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Propiconazole 25 EC @ 1.0 mL/L "
                        "OR Hexaconazole 5 EC @ 1.0 mL/L. "
                        "Spray 2–3 times at 10-day intervals.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली "
                        "अथवा हेक्साकोनाज़ोल 5 EC @ 1.0 मिली/ली। "
                        "10 दिन के अंतराल पर 2–3 छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 45 ────────────────────────────────────────────────────────────────────
    "groundnut_healthy": {
        "name_en": "Groundnut — Healthy",
        "name_hi": "मूँगफली — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Use certified seed. Rhizobium inoculation for nitrogen fixation. "
                         "Adequate calcium for pod development. Monitor from 30 DAS.",
        "prevention_hi": "प्रमाणित बीज उपयोग करें। नाइट्रोजन स्थिरीकरण के लिए राइज़ोबियम टीका। "
                         "फली विकास के लिए पर्याप्त कैल्शियम। 30 DAS से निगरानी।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 46 ────────────────────────────────────────────────────────────────────
    "groundnut_late_leaf_spot": {
        "name_en": "Groundnut Late Leaf Spot",
        "name_hi": "मूँगफली का पछेती पत्ती धब्बा",
        "cause_en": "Fungus Phaeoisariopsis personata (syn. Cercosporidium personatum). "
                    "More damaging than early leaf spot; appears 50–70 DAS.",
        "cause_hi": "फेओइसेरियोप्सिस पर्सोनेटा फफूंद। अगेती पत्ती धब्बे से अधिक हानिकारक; "
                    "50–70 DAS पर दिखता है।",
        "symptoms_en": "Dark brown to black circular spots on lower leaf surface; "
                       "less prominent yellow halo compared to early spot; "
                       "heavy sporulation; can cause 50% yield loss if uncontrolled.",
        "symptoms_hi": "पत्तियों की निचली सतह पर गहरे भूरे से काले गोल धब्बे; "
                       "अगेती धब्बे की तुलना में कम प्रमुख पीला घेरा; "
                       "भारी बीजाणु वृद्धि; अनियंत्रित रहने पर 50% उपज हानि।",
        "cure_en": "Apply fungicide at first sign (50 DAS onward). "
                   "3 sprays at 10-day intervals from first detection.",
        "cure_hi": "पहले लक्षण पर (50 DAS से) फफूंदनाशक लगाएँ। "
                   "पहली पहचान से 10 दिन के अंतराल पर 3 छिड़काव।",
        "prevention_en": "Early sowing to escape late-season humid conditions. "
                         "Tolerant varieties. Remove infected debris. Crop rotation.",
        "prevention_hi": "देर-मौसम नम परिस्थितियों से बचने के लिए जल्दी बुवाई। "
                         "सहनशील किस्में। संक्रमित अवशेष हटाएँ। फसल चक्र।",
        "pesticide_en": "Chlorothalonil 75 WP @ 2.0 g/L OR Carbendazim 50 WP @ 1.0 g/L "
                        "OR Propiconazole 25 EC @ 1.0 mL/L. "
                        "Spray at 50, 60 and 70 DAS.",
        "pesticide_hi": "क्लोरोथैलोनिल 75 WP @ 2.0 ग्राम/ली अथवा कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली "
                        "अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली। "
                        "50, 60 और 70 DAS पर छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 47 ────────────────────────────────────────────────────────────────────
    "groundnut_nutrition_deficiency": {
        "name_en": "Groundnut Nutritional Deficiency",
        "name_hi": "मूँगफली में पोषक तत्व की कमी",
        "cause_en": "Deficiencies of iron (Fe), zinc (Zn), calcium (Ca), or boron (B). "
                    "Iron deficiency (chlorosis) is most common in alkaline soils.",
        "cause_hi": "लोहे (Fe), जिंक (Zn), कैल्शियम (Ca), या बोरॉन (B) की कमी। "
                    "क्षारीय मिट्टी में लोहे की कमी (क्लोरोसिस) सबसे आम है।",
        "symptoms_en": "Fe deficiency: interveinal yellowing of young leaves. "
                       "Zn: small leaves, stunted growth. "
                       "Ca: empty pods, peg death. "
                       "B: hollow hearts in kernel.",
        "symptoms_hi": "Fe कमी: युवा पत्तियों की नसों के बीच पीलापन। "
                       "Zn: छोटी पत्तियाँ, अवरुद्ध वृद्धि। "
                       "Ca: खाली फलियाँ, पेग मृत्यु। "
                       "B: दाने में खोखला हृदय।",
        "cure_en": "Foliar spray with deficient nutrient solution. "
                   "Ferrous sulfate 0.5% for Fe; ZnSO4 0.5% for Zn; "
                   "CaSO4 soil application for Ca; Borax 0.1% for B.",
        "cure_hi": "कमी वाले पोषक घोल का पत्ती पर छिड़काव। "
                   "Fe के लिए फेरस सल्फेट 0.5%; Zn के लिए ZnSO4 0.5%; "
                   "Ca के लिए मिट्टी में CaSO4; B के लिए बोरेक्स 0.1%।",
        "prevention_en": "Soil test before sowing. Apply gypsum (CaSO4 @ 400 kg/ha) "
                         "at peg formation. Maintain pH 6.0–6.5. "
                         "Use micronutrient mixtures at sowing.",
        "prevention_hi": "बुवाई से पहले मिट्टी परीक्षण। पेग बनने पर जिप्सम (CaSO4 @ 400 किग्रा/हेक्टेयर) दें। "
                         "pH 6.0–6.5 बनाए रखें। बुवाई पर सूक्ष्म पोषक मिश्रण उपयोग करें।",
        "pesticide_en": "No pesticide needed. "
                        "Nutrient sprays: FeSO4 0.5% OR ZnSO4 0.5% OR Borax 0.1%. "
                        "Apply 2–3 times at 10-day intervals during vegetative stage.",
        "pesticide_hi": "कोई कीटनाशक नहीं। "
                        "पोषक छिड़काव: FeSO4 0.5% अथवा ZnSO4 0.5% अथवा बोरेक्स 0.1%। "
                        "वानस्पतिक अवस्था में 10 दिन के अंतराल पर 2–3 बार।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 48 ────────────────────────────────────────────────────────────────────
    "groundnut_rust": {
        "name_en": "Groundnut Rust",
        "name_hi": "मूँगफली का रतुआ",
        "cause_en": "Fungus Puccinia arachidis. Can cause up to 70% yield loss "
                    "if it appears early. Spreads rapidly by wind.",
        "cause_hi": "पक्सिनिया अराकिडिस फफूंद। जल्दी दिखने पर 70% तक उपज हानि। "
                    "हवा से तेजी से फैलती है।",
        "symptoms_en": "Orange-brown uredinia primarily on lower leaf surface; "
                       "yellow flecks on upper surface; severe defoliation; "
                       "infected plants ripen prematurely.",
        "symptoms_hi": "मुख्यतः पत्तियों की निचली सतह पर नारंगी-भूरे यूरेडिनिया; "
                       "ऊपरी सतह पर पीले धब्बे; गंभीर पत्ती झड़ना; "
                       "संक्रमित पौधे समय से पहले पकते हैं।",
        "cure_en": "Apply fungicide at first pustule appearance; do not delay. "
                   "Two sprays at 10-day intervals are usually sufficient.",
        "cure_hi": "पहली फुंसी दिखने पर तुरंत फफूंदनाशक लगाएँ; देरी न करें। "
                   "10 दिन के अंतराल पर दो छिड़काव सामान्यतः पर्याप्त हैं।",
        "prevention_en": "Grow resistant varieties (ICGV-86031, TG-37A). "
                         "Early sowing. Regular monitoring from 35 DAS.",
        "prevention_hi": "प्रतिरोधी किस्में (ICGV-86031, TG-37A) उगाएँ। "
                         "जल्दी बुवाई। 35 DAS से नियमित निगरानी।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Tebuconazole 25.9 EC @ 1.0 mL/L "
                        "OR Propiconazole 25 EC @ 1.0 mL/L. "
                        "Spray at 10-day intervals; 3 sprays from first detection.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा टेब्युकोनाज़ोल 25.9 EC @ 1.0 मिली/ली "
                        "अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली। "
                        "10 दिन के अंतराल पर; पहली पहचान से 3 छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 49 ────────────────────────────────────────────────────────────────────
    "healthy": {
        "name_en": "Wheat — Healthy",
        "name_hi": "गेहूँ — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Timely sowing of certified seed treated with fungicide. "
                         "Balanced NPK. Weekly monitoring from tillering to grain fill.",
        "prevention_hi": "फफूंदनाशक से उपचारित प्रमाणित बीज की समय पर बुवाई। "
                         "संतुलित NPK। कल्ले से दाना भरने तक साप्ताहिक निगरानी।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 50 ────────────────────────────────────────────────────────────────────
    "leaf_blight": {
        "name_en": "Wheat Leaf Blight (Helminthosporium Blight)",
        "name_hi": "गेहूँ का पत्ती झुलसा रोग",
        "cause_en": "Fungus Bipolaris sorokiniana (syn. Helminthosporium sativum). "
                    "Favored by warm temperatures (20–30°C), high humidity, and heavy dew.",
        "cause_hi": "बाइपोलारिस सोरोकिनियाना फफूंद। गर्म तापमान (20–30°C), "
                    "उच्च आर्द्रता और भारी ओस में अधिक।",
        "symptoms_en": "Oval to elongated brown lesions on leaves; dark brown border; "
                       "lesions may coalesce causing extensive blighting; "
                       "glume blotch reduces grain quality.",
        "symptoms_hi": "पत्तियों पर अंडाकार से लंबे भूरे घाव; गहरे भूरे हाशिए; "
                       "घाव मिलकर व्यापक झुलसा बनाते हैं; "
                       "ग्लूम ब्लॉच से दाने की गुणवत्ता कम।",
        "cure_en": "Spray triazole fungicide at flag leaf stage. "
                   "One to two sprays at 10-day interval from symptom onset.",
        "cure_hi": "ध्वज पत्ती अवस्था पर ट्राइएज़ोल फफूंदनाशक छिड़काव। "
                   "लक्षण दिखने से 10 दिन के अंतराल पर एक-दो छिड़काव।",
        "prevention_en": "Seed treatment with Carboxin + Thiram. Balanced nitrogen. "
                         "Grow resistant varieties. Crop rotation.",
        "prevention_hi": "कार्बोक्सिन + थीरम से बीज उपचार। संतुलित नाइट्रोजन। "
                         "प्रतिरोधी किस्में उगाएँ। फसल चक्र।",
        "pesticide_en": "Propiconazole 25 EC @ 1.0 mL/L OR Tebuconazole 25.9 EC @ 1.0 mL/L "
                        "OR Mancozeb 75 WP @ 2.5 g/L. Apply 500 L spray solution per ha.",
        "pesticide_hi": "प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली अथवा टेब्युकोनाज़ोल 25.9 EC @ 1.0 मिली/ली "
                        "अथवा मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली। 500 ली छिड़काव घोल प्रति हेक्टेयर।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 51 ────────────────────────────────────────────────────────────────────
    "leaf_smut": {
        "name_en": "Rice Leaf Smut",
        "name_hi": "धान का पत्ती कांगियारी रोग",
        "cause_en": "Fungus Entyloma oryzae. Spreads by spores in soil and water. "
                    "Generally a minor disease; becomes significant under wet conditions.",
        "cause_hi": "एंटाइलोमा ओराइज़ी फफूंद। मिट्टी और पानी में बीजाणुओं से फैलती है। "
                    "सामान्यतः मामूली रोग; नम परिस्थितियों में महत्त्वपूर्ण हो जाती है।",
        "symptoms_en": "Small black angular spots (sori) on leaves and leaf sheaths; "
                       "spots do not cause severe defoliation; "
                       "in heavy infection, leaves show extensive black discoloration.",
        "symptoms_hi": "पत्तियों और पत्ती आवरण पर छोटे काले कोणीय धब्बे (सोरी); "
                       "धब्बे गंभीर पत्ती झड़ना नहीं करते; "
                       "भारी संक्रमण में पत्तियाँ व्यापक कालापन दिखाती हैं।",
        "cure_en": "Generally, no chemical treatment required for mild cases. "
                   "For severe infection, apply systemic fungicide.",
        "cure_hi": "सामान्यतः हल्के मामलों के लिए कोई रासायनिक उपचार आवश्यक नहीं। "
                   "गंभीर संक्रमण के लिए प्रणालीगत फफूंदनाशक लगाएँ।",
        "prevention_en": "Use healthy certified seed. Seed treatment with Carbendazim @ 2 g/kg. "
                         "Good field drainage. Crop rotation.",
        "prevention_hi": "स्वस्थ प्रमाणित बीज उपयोग करें। बीज को कार्बेन्डाज़िम @ 2 ग्राम/किग्रा से उपचारित करें। "
                         "अच्छी खेत जल निकासी। फसल चक्र।",
        "pesticide_en": "Carbendazim 50 WP @ 1.0 g/L OR Propiconazole 25 EC @ 1.0 mL/L. "
                        "Spray only if disease is severe (>10 spots per leaf).",
        "pesticide_hi": "कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली। "
                        "केवल गंभीर रोग (प्रति पत्ती >10 धब्बे) होने पर छिड़काव करें।",
        "severity": "low",
        "is_healthy": False,
    },

    # ── 52 ────────────────────────────────────────────────────────────────────
    "mildew": {
        "name_en": "Wheat Powdery Mildew",
        "name_hi": "गेहूँ का चूर्णिल आसिता (पाउडरी मिल्ड्यू)",
        "cause_en": "Obligate parasite fungus Blumeria graminis f.sp. tritici. "
                    "Favored by cool temperatures (15–22°C), high humidity but dry leaf surface.",
        "cause_hi": "ब्लूमेरिया ग्रैमिनिस f.sp. ट्रिटिसी अनिवार्य परजीवी फफूंद। "
                    "ठंडा तापमान (15–22°C), उच्च आर्द्रता लेकिन सूखी पत्ती सतह अनुकूल।",
        "symptoms_en": "White to gray powdery colonies on upper leaf and sheath surfaces; "
                       "colonies turn brown at maturity; yellow patches beneath colonies; "
                       "severe infection reduces tillering and grain weight.",
        "symptoms_hi": "पत्तियों और आवरण की ऊपरी सतह पर सफेद से भूरे पाउडरयुक्त उपनिवेश; "
                       "परिपक्वता पर भूरे होते हैं; उपनिवेशों के नीचे पीले धब्बे; "
                       "गंभीर संक्रमण से कल्ला और दाना भार कम।",
        "cure_en": "Spray systemic triazole fungicide at first sign of disease. "
                   "One spray at flag leaf emergence is most critical.",
        "cure_hi": "रोग के पहले लक्षण पर प्रणालीगत ट्राइएज़ोल फफूंदनाशक छिड़काव। "
                   "ध्वज पत्ती निकलने पर एक छिड़काव सबसे महत्त्वपूर्ण।",
        "prevention_en": "Grow resistant varieties (K-307, HD-2781). "
                         "Avoid high nitrogen doses. Timely sowing.",
        "prevention_hi": "प्रतिरोधी किस्में (K-307, HD-2781) उगाएँ। "
                         "नाइट्रोजन की अधिक मात्रा न दें। समय पर बुवाई।",
        "pesticide_en": "Propiconazole 25 EC @ 1.0 mL/L OR Hexaconazole 5 EC @ 2.0 mL/L "
                        "OR Triadimefon 25 WP @ 1.0 g/L. Apply 500 L/ha.",
        "pesticide_hi": "प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली अथवा हेक्साकोनाज़ोल 5 EC @ 2.0 मिली/ली "
                        "अथवा ट्राइडाइमिफॉन 25 WP @ 1.0 ग्राम/ली। 500 ली/हेक्टेयर।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 53 ────────────────────────────────────────────────────────────────────
    "mite": {
        "name_en": "Wheat Mite Infestation",
        "name_hi": "गेहूँ का घुन / माइट",
        "cause_en": "Mites: Aceria tosichella (wheat curl mite) and Petrobia latens (brown wheat mite). "
                    "A. tosichella also vectors Wheat streak mosaic virus.",
        "cause_hi": "घुन: एसेरिया टोसिचेला (गेहूँ कर्ल माइट) और पेट्रोबिया लेटेंस (भूरा गेहूँ माइट)। "
                    "A. टोसिचेला गेहूँ स्ट्रीक मोज़ेक वायरस भी फैलाता है।",
        "symptoms_en": "Brown wheat mite: bronzing or yellowing of leaves; silvery stippling. "
                       "Wheat curl mite: leaf rolling; yellowing; stunting; "
                       "mosaic virus symptoms if vectoring.",
        "symptoms_hi": "भूरा गेहूँ माइट: पत्तियों का काँसा या पीलापन; चाँदी जैसी बिंदी। "
                       "गेहूँ कर्ल माइट: पत्ती मुड़ना; पीलापन; अवरुद्ध विकास; "
                       "वाहक होने पर मोज़ेक वायरस लक्षण।",
        "cure_en": "Spray miticide at first sign of mite infestation. "
                   "Do not use pyrethroid insecticides — they worsen mite outbreaks.",
        "cure_hi": "घुन के पहले लक्षण पर माइटिसाइड छिड़काव। "
                   "पायरेथ्रॉइड कीटनाशक न उपयोग करें — वे घुन प्रकोप बढ़ाते हैं।",
        "prevention_en": "Destroy volunteer wheat before planting. "
                         "Avoid late planting near maturing wheat. "
                         "Eliminate grassy weeds that host mites.",
        "prevention_hi": "रोपण से पहले अनायास उगे गेहूँ को नष्ट करें। "
                         "परिपक्व होते गेहूँ के पास देर से रोपण से बचें। "
                         "घुन पोषक घास के खरपतवार हटाएँ।",
        "pesticide_en": "Dicofol 18.5 EC @ 2.5 mL/L OR Abamectin 1.9 EC @ 0.5 mL/L "
                        "OR Propargite 57 EC @ 2.0 mL/L. Spray undersides of leaves. "
                        "Repeat after 7–10 days if needed.",
        "pesticide_hi": "डाइकोफॉल 18.5 EC @ 2.5 मिली/ली अथवा एबेमेक्टिन 1.9 EC @ 0.5 मिली/ली "
                        "अथवा प्रोपार्जाइट 57 EC @ 2.0 मिली/ली। पत्तियों की निचली सतह पर छिड़काव। "
                        "आवश्यकता पर 7–10 दिन बाद दोहराएँ।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 54 ────────────────────────────────────────────────────────────────────
    "orange_haunglongbing_citrus_greening": {
        "name_en": "Citrus Greening Disease (Huanglongbing / HLB)",
        "name_hi": "संतरे का हुआंगलोंगबिंग / साइट्रस ग्रीनिंग रोग",
        "cause_en": "Bacterium Candidatus Liberibacter asiaticus (CLas). "
                    "Transmitted by citrus psyllid Diaphorina citri. "
                    "Phloem-limited; no cure once infected.",
        "cause_hi": "कैंडिडेटस लिबरीबैक्टर एशियेटिकस (CLas) जीवाणु। "
                    "साइट्रस सिल्लिड डायफोरिना सिट्री द्वारा फैलाया जाता है। "
                    "फ्लोएम-सीमित; एक बार संक्रमित होने पर कोई उपचार नहीं।",
        "symptoms_en": "Asymmetric yellow mottling on leaves (blotchy mottle); "
                       "small, lopsided, bitter fruit with green color at stylar end; "
                       "twig dieback; tree decline over years.",
        "symptoms_hi": "पत्तियों पर असममित पीला धब्बेदार रंग; "
                       "स्टाइलर सिरे पर हरे रंग के साथ छोटे, एकतरफा, कड़वे फल; "
                       "शाखा पीछे से मरना; वर्षों में पेड़ का पतन।",
        "cure_en": "No cure available. Remove and destroy infected trees immediately "
                   "to prevent spread to healthy trees. "
                   "Report to state horticulture department.",
        "cure_hi": "कोई उपचार उपलब्ध नहीं। स्वस्थ पेड़ों में फैलाव रोकने के लिए "
                   "संक्रमित पेड़ तुरंत हटाकर नष्ट करें। "
                   "राज्य बागवानी विभाग को सूचित करें।",
        "prevention_en": "Plant certified disease-free nursery trees. "
                         "Strictly control psyllid population. "
                         "Inspect orchards monthly. Quarantine new planting material.",
        "prevention_hi": "प्रमाणित रोगमुक्त नर्सरी पेड़ लगाएँ। "
                         "सिल्लिड आबादी का कड़ा नियंत्रण। "
                         "मासिक बाग निरीक्षण। नई रोपण सामग्री को अलग रखें।",
        "pesticide_en": "Psyllid vector control: Imidacloprid 17.8 SL @ 0.5 mL/L "
                        "OR Thiamethoxam 25 WG @ 0.3 g/L OR Dimethoate 30 EC @ 2.0 mL/L. "
                        "Spray new flushes every 15–21 days.",
        "pesticide_hi": "सिल्लिड वाहक नियंत्रण: इमिडाक्लोप्रिड 17.8 SL @ 0.5 मिली/ली "
                        "अथवा थायमेथोक्सम 25 WG @ 0.3 ग्राम/ली अथवा डाइमिथोएट 30 EC @ 2.0 मिली/ली। "
                        "नई कोपलों पर हर 15–21 दिन छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 55 ────────────────────────────────────────────────────────────────────
    "peach_bacterial_spot": {
        "name_en": "Peach Bacterial Spot",
        "name_hi": "आड़ू का जीवाणु धब्बा रोग",
        "cause_en": "Bacterium Xanthomonas arboricola pv. pruni. "
                    "Spreads by rain splash; enters through stomata and wounds.",
        "cause_hi": "जैन्थोमोनास आर्बोरिकोला pv. प्रूनी जीवाणु। "
                    "वर्षा छींटों से फैलता है; रंध्र और घावों से प्रवेश करता है।",
        "symptoms_en": "Small water-soaked spots on leaves turning brown with yellow halo; "
                       "shot-hole appearance when lesions drop out; "
                       "sunken dark spots on fruit; twig cankers.",
        "symptoms_hi": "पत्तियों पर छोटे जलसिक्त धब्बे जो पीले घेरे के साथ भूरे होते हैं; "
                       "धब्बे गिरने पर शॉट-होल दिखता है; "
                       "फल पर धँसे गहरे धब्बे; शाखा कैंकर।",
        "cure_en": "Apply copper-based bactericide at petal fall and repeat every 7–10 days "
                   "during wet weather. Avoid overhead irrigation.",
        "cure_hi": "फूल झड़ने पर तांबा-आधारित जीवाणुनाशक लगाएँ और नम मौसम में "
                   "हर 7–10 दिन दोहराएँ। ऊपरी सिंचाई से बचें।",
        "prevention_en": "Plant resistant peach varieties. Prune infected branches. "
                         "Apply copper spray before fall rains and at bud swell.",
        "prevention_hi": "प्रतिरोधी आड़ू किस्में लगाएँ। संक्रमित शाखाएँ काटें। "
                         "पतझड़ की वर्षा से पहले और कली फूलने पर तांबा छिड़काव।",
        "pesticide_en": "Copper oxychloride 50 WP @ 3.0 g/L + Streptomycin sulfate @ 0.2 g/L "
                        "OR Kasugamycin 3 SL @ 2.0 mL/L. "
                        "Spray every 7–10 days during leaf expansion.",
        "pesticide_hi": "कॉपर ऑक्सीक्लोराइड 50 WP @ 3.0 ग्राम/ली + स्ट्रेप्टोमाइसिन सल्फेट @ 0.2 ग्राम/ली "
                        "अथवा कसुगामाइसिन 3 SL @ 2.0 मिली/ली। "
                        "पत्ती फैलाव के दौरान हर 7–10 दिन पर।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 56 ────────────────────────────────────────────────────────────────────
    "peach_healthy": {
        "name_en": "Peach — Healthy",
        "name_hi": "आड़ू — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Annual dormant copper spray. Proper pruning for airflow. "
                         "Balanced fertilization and timely irrigation.",
        "prevention_hi": "वार्षिक सुप्त तांबा छिड़काव। वायु संचार के लिए उचित छंटाई। "
                         "संतुलित उर्वरक और समय पर सिंचाई।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 57 ────────────────────────────────────────────────────────────────────
    "pepper_bell_bacterial_spot": {
        "name_en": "Bell Pepper Bacterial Spot",
        "name_hi": "शिमला मिर्च का जीवाणु धब्बा",
        "cause_en": "Bacterium Xanthomonas campestris pv. vesicatoria. "
                    "Seed-borne; spreads by rain and irrigation. "
                    "Favored by warm, wet weather (24–30°C).",
        "cause_hi": "जैन्थोमोनास कैम्पेस्ट्रिस pv. वेसिकेटोरिया जीवाणु। "
                    "बीजजनित; वर्षा और सिंचाई से फैलता है। "
                    "गर्म, नम मौसम (24–30°C) अनुकूल।",
        "symptoms_en": "Small water-soaked spots on leaves turning dark brown; "
                       "scab-like raised lesions on fruit surface; "
                       "defoliation in severe cases reduces fruit quality.",
        "symptoms_hi": "पत्तियों पर छोटे जलसिक्त धब्बे जो गहरे भूरे होते हैं; "
                       "फल की सतह पर पपड़ी जैसे उभरे घाव; "
                       "गंभीर मामलों में पत्ती झड़ने से फल गुणवत्ता कम।",
        "cure_en": "Apply copper bactericide + streptomycin spray. "
                   "Remove badly infected leaves and fruit.",
        "cure_hi": "तांबा जीवाणुनाशक + स्ट्रेप्टोमाइसिन छिड़काव। "
                   "बुरी तरह संक्रमित पत्तियाँ और फल हटाएँ।",
        "prevention_en": "Use disease-free certified seed. Hot water seed treatment (52°C, 30 min). "
                         "Drip irrigation instead of overhead. Crop rotation.",
        "prevention_hi": "रोगमुक्त प्रमाणित बीज उपयोग करें। गर्म पानी बीज उपचार (52°C, 30 मिनट)। "
                         "ऊपरी के बजाय ड्रिप सिंचाई। फसल चक्र।",
        "pesticide_en": "Copper oxychloride 50 WP @ 3.0 g/L + Streptomycin sulfate @ 0.2 g/L "
                        "OR Kasugamycin 3 SL @ 2.0 mL/L. Spray every 7 days during wet weather.",
        "pesticide_hi": "कॉपर ऑक्सीक्लोराइड 50 WP @ 3.0 ग्राम/ली + स्ट्रेप्टोमाइसिन सल्फेट @ 0.2 ग्राम/ली "
                        "अथवा कसुगामाइसिन 3 SL @ 2.0 मिली/ली। नम मौसम में हर 7 दिन।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 58 ────────────────────────────────────────────────────────────────────
    "pepper_bell_healthy": {
        "name_en": "Bell Pepper — Healthy",
        "name_hi": "शिमला मिर्च — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Certified disease-free seed. Adequate calcium and boron. "
                         "Drip irrigation. Regular scouting.",
        "prevention_hi": "प्रमाणित रोगमुक्त बीज। पर्याप्त कैल्शियम और बोरॉन। "
                         "ड्रिप सिंचाई। नियमित निगरानी।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 59 ────────────────────────────────────────────────────────────────────
    "potato_early_blight": {
        "name_en": "Potato Early Blight",
        "name_hi": "आलू का अगेती झुलसा रोग",
        "cause_en": "Fungus Alternaria solani. Favored by warm days (24–29°C), "
                    "cool nights, and leaf wetness. Infects older/stressed leaves first.",
        "cause_hi": "अल्टरनेरिया सोलेनी फफूंद। गर्म दिन (24–29°C), "
                    "ठंडी रात और पत्ती नमी में अधिक। पुरानी/तनावग्रस्त पत्तियाँ पहले संक्रमित।",
        "symptoms_en": "Circular dark brown lesions with concentric rings (target-board pattern) "
                       "on older leaves; yellow halo around lesion; defoliation causes tuber sunscald.",
        "symptoms_hi": "पुरानी पत्तियों पर संकेंद्रित वलयों के साथ गोल गहरे भूरे घाव "
                       "(निशाना बोर्ड पैटर्न); घाव के चारों ओर पीला घेरा; "
                       "पत्ती झड़ने से कंद धूप से जलता है।",
        "cure_en": "Apply protective fungicide at first sign of disease. "
                   "Start spraying when lower leaves show first spots. "
                   "Ensure good leaf coverage.",
        "cure_hi": "रोग के पहले लक्षण पर सुरक्षात्मक फफूंदनाशक लगाएँ। "
                   "निचली पत्तियों पर पहले धब्बे दिखने पर छिड़काव शुरू करें। "
                   "अच्छी पत्ती आवरण सुनिश्चित करें।",
        "prevention_en": "Use healthy certified seed tubers. Balanced NPK — avoid nitrogen excess. "
                         "Adequate potassium and calcium reduce susceptibility. "
                         "Avoid prolonged leaf wetness.",
        "prevention_hi": "स्वस्थ प्रमाणित बीज कंद उपयोग करें। संतुलित NPK — नाइट्रोजन की अधिकता न हो। "
                         "पर्याप्त पोटेशियम और कैल्शियम संवेदनशीलता कम करते हैं। "
                         "लंबे समय तक पत्ती नमी से बचें।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Chlorothalonil 75 WP @ 2.0 g/L "
                        "OR Iprodione 50 WP @ 1.5 g/L. "
                        "Spray every 7–10 days from symptom onset.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा क्लोरोथैलोनिल 75 WP @ 2.0 ग्राम/ली "
                        "अथवा इप्रोडिओन 50 WP @ 1.5 ग्राम/ली। "
                        "लक्षण से हर 7–10 दिन पर छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 60 ────────────────────────────────────────────────────────────────────
    "potato_healthy": {
        "name_en": "Potato — Healthy",
        "name_hi": "आलू — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Use certified disease-free seed tubers. "
                         "Treat seed with Mancozeb before storage. "
                         "Balanced NPK and adequate irrigation.",
        "prevention_hi": "प्रमाणित रोगमुक्त बीज कंद उपयोग करें। "
                         "भंडारण से पहले बीज को मैनकोज़ेब से उपचारित करें। "
                         "संतुलित NPK और पर्याप्त सिंचाई।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 61 ────────────────────────────────────────────────────────────────────
    "potato_late_blight": {
        "name_en": "Potato Late Blight",
        "name_hi": "आलू का पछेती झुलसा रोग",
        "cause_en": "Oomycete Phytophthora infestans. The pathogen responsible for the "
                    "1840s Irish Famine. Spreads extremely rapidly in cool, wet weather (10–24°C).",
        "cause_hi": "फाइटोफ्थोरा इन्फेस्टेंस ओओमाइसीट। 1840 के आयरिश अकाल के लिए जिम्मेदार रोगज़नक। "
                    "ठंडे, नम मौसम (10–24°C) में अत्यंत तेजी से फैलता है।",
        "symptoms_en": "Water-soaked pale green to brown lesions at leaf margins/tips; "
                       "white sporulation on underside in humid conditions; "
                       "dark brown rot of tubers; entire field can be destroyed within days.",
        "symptoms_hi": "पत्ती किनारों/नोक पर जलसिक्त हल्के हरे से भूरे घाव; "
                       "नम परिस्थितियों में निचली सतह पर सफेद बीजाणु वृद्धि; "
                       "कंदों का गहरा भूरा सड़न; पूरा खेत कुछ दिनों में नष्ट हो सकता है।",
        "cure_en": "Apply systemic fungicide immediately at first sign. "
                   "Spray every 5–7 days during cool, wet periods. "
                   "Destroy infected haulms before harvest.",
        "cure_hi": "पहले लक्षण पर तुरंत प्रणालीगत फफूंदनाशक लगाएँ। "
                   "ठंडे, नम समय में हर 5–7 दिन छिड़काव। "
                   "कटाई से पहले संक्रमित पौधों को नष्ट करें।",
        "prevention_en": "Use blight-resistant varieties (Kufri Jyoti, Kufri Bahar). "
                         "Prophylactic spray at 45 DAS in high-risk areas. "
                         "Avoid excess irrigation. Good drainage.",
        "prevention_hi": "झुलसा-प्रतिरोधी किस्में (कुफरी ज्योति, कुफरी बहार) उगाएँ। "
                         "उच्च जोखिम क्षेत्रों में 45 DAS पर निवारक छिड़काव। "
                         "अधिक सिंचाई से बचें। अच्छी जल निकासी।",
        "pesticide_en": "Metalaxyl-M 4% + Mancozeb 64% WP @ 2.5 g/L "
                        "OR Cymoxanil 8% + Mancozeb 64% WP @ 3.0 g/L "
                        "OR Fenamidone 10% + Mancozeb 50% WDG @ 3.0 g/L. "
                        "Spray every 5–7 days in wet weather.",
        "pesticide_hi": "मेटालैक्सिल-M 4% + मैनकोज़ेब 64% WP @ 2.5 ग्राम/ली "
                        "अथवा साइमोक्सेनिल 8% + मैनकोज़ेब 64% WP @ 3.0 ग्राम/ली "
                        "अथवा फेनेमिडोन 10% + मैनकोज़ेब 50% WDG @ 3.0 ग्राम/ली। "
                        "नम मौसम में हर 5–7 दिन छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },
}
