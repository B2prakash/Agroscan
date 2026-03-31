"""
Disease Info — Part 1 of 3
Classes 1–30: aphid → chilli_leafspot
Source: ICAR (Indian Council of Agricultural Research) & PAU Ludhiana guidelines
Structure per class:
    name_en / name_hi
    cause_en / cause_hi
    symptoms_en / symptoms_hi
    cure_en / cure_hi
    prevention_en / prevention_hi
    pesticide_en / pesticide_hi   (name + dose)
    severity: "low" | "medium" | "high"
    is_healthy: bool
"""

DISEASE_INFO_1 = {

    # ── 1 ─────────────────────────────────────────────────────────────────────
    "aphid": {
        "name_en": "Wheat Aphid",
        "name_hi": "गेहूँ का माहू / चेपा",
        "cause_en": "Soft-bodied insects: Schizaphis graminum (green bug) and "
                    "Rhopalosiphum padi (bird-cherry oat aphid).",
        "cause_hi": "कोमल शरीर वाले कीट: स्किज़ाफिस ग्रैमिनम और रोपालोसिफम पादी "
                    "नामक माहू कीट फसल को नुकसान पहुँचाते हैं।",
        "symptoms_en": "Yellowing and curling of leaves; sticky honeydew on plant surface; "
                       "sooty mold growth; stunted tillers; reduced grain filling.",
        "symptoms_hi": "पत्तियों का पीला पड़ना व मुड़ना; पौधे पर चिपचिपा मधुरस; "
                       "काली फफूंद; कल्ले का अवरुद्ध विकास; दाने का खराब भराव।",
        "cure_en": "Spray systemic insecticide at first sign of infestation. "
                   "Natural predators like ladybird beetles help reduce population.",
        "cure_hi": "प्रकोप के पहले संकेत पर प्रणालीगत कीटनाशक का छिड़काव करें। "
                   "लेडीबर्ड बीटल जैसे प्राकृतिक शत्रु आबादी कम करने में सहायक हैं।",
        "prevention_en": "Use resistant wheat varieties. Avoid excess nitrogenous fertilizer. "
                         "Monitor crop weekly from tillering stage. Remove weed hosts.",
        "prevention_hi": "प्रतिरोधी गेहूँ किस्मों का उपयोग करें। अत्यधिक नाइट्रोजन उर्वरक से बचें। "
                         "कल्ले निकलने से प्रति सप्ताह फसल की निगरानी करें। खरपतवार हटाएँ।",
        "pesticide_en": "Imidacloprid 17.8 SL @ 250 mL/ha OR Dimethoate 30 EC @ 1.0 L/ha "
                        "OR Thiamethoxam 25 WG @ 100 g/ha dissolved in 500 L water.",
        "pesticide_hi": "इमिडाक्लोप्रिड 17.8 SL @ 250 मिली/हेक्टेयर अथवा डाइमिथोएट 30 EC @ 1.0 ली/हेक्टेयर "
                        "अथवा थायमेथोक्सम 25 WG @ 100 ग्राम/हेक्टेयर — 500 ली पानी में मिलाकर छिड़काव करें।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 2 ─────────────────────────────────────────────────────────────────────
    "apple_apple_scab": {
        "name_en": "Apple Scab",
        "name_hi": "सेब की पपड़ी / स्कैब रोग",
        "cause_en": "Fungus Venturia inaequalis. Spores spread through rain splash "
                    "and wind during cool, wet spring weather.",
        "cause_hi": "वेंचुरिया इनेक्वालिस नामक फफूंद। ठंडे व नम मौसम में वर्षा जल "
                    "और हवा द्वारा बीजाणु फैलते हैं।",
        "symptoms_en": "Olive-green to brown velvety spots on leaves and fruit; "
                       "leaves may yellow and drop early; scabby, cracked fruit skin.",
        "symptoms_hi": "पत्तियों और फलों पर जैतून-हरे से भूरे मखमली धब्बे; "
                       "पत्तियाँ पीली होकर जल्दी गिरती हैं; फल की खाल पपड़ीदार व दरारयुक्त।",
        "cure_en": "Apply fungicide at bud break and repeat every 7–10 days during wet periods. "
                   "Remove and destroy fallen infected leaves.",
        "cure_hi": "कली खुलते समय फफूंदनाशक लगाएँ और नम मौसम में हर 7–10 दिन दोहराएँ। "
                   "गिरी हुई संक्रमित पत्तियाँ हटाकर नष्ट करें।",
        "prevention_en": "Plant scab-resistant varieties. Prune for good airflow. "
                         "Apply protective sprays before rainfall. Rake and compost fallen leaves.",
        "prevention_hi": "पपड़ी-प्रतिरोधी किस्में लगाएँ। अच्छे वायु संचार के लिए छंटाई करें। "
                         "वर्षा से पहले सुरक्षात्मक छिड़काव करें। गिरी पत्तियाँ इकट्ठी कर खाद बनाएँ।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L water OR Captan 50 WP @ 3.0 g/L water "
                        "OR Carbendazim 50 WP @ 1.0 g/L. Spray at 7–10 day intervals.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली पानी अथवा कैप्टन 50 WP @ 3.0 ग्राम/ली पानी "
                        "अथवा कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली। 7–10 दिन के अंतराल पर छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 3 ─────────────────────────────────────────────────────────────────────
    "apple_black_rot": {
        "name_en": "Apple Black Rot",
        "name_hi": "सेब का काला सड़न रोग",
        "cause_en": "Fungus Botryosphaeria obtusa. Overwinters in dead bark and mummified fruit.",
        "cause_hi": "बोट्रियोस्फेरिया ओब्टूसा फफूंद। मृत छाल और सूखे फलों में सर्दी बिताती है।",
        "symptoms_en": "Circular purple spots on leaves turning brown with yellow halo; "
                       "fruit shows black rot from the calyx end; cankers on branches.",
        "symptoms_hi": "पत्तियों पर गोल बैंगनी धब्बे जो भूरे होते हैं; फूल वाले सिरे से "
                       "काला सड़न; शाखाओं पर कैंकर।",
        "cure_en": "Remove and destroy infected fruit and cankers. Apply fungicide during "
                   "growing season starting at pink bud stage.",
        "cure_hi": "संक्रमित फल और कैंकर हटाकर नष्ट करें। गुलाबी कली अवस्था से "
                   "बढ़ते मौसम में फफूंदनाशक लगाएँ।",
        "prevention_en": "Prune out dead wood annually. Avoid wounding trees. "
                         "Remove mummified fruit. Maintain tree vigor with balanced fertilization.",
        "prevention_hi": "हर साल मृत लकड़ी की छंटाई करें। पेड़ को चोट से बचाएँ। "
                         "सूखे फल हटाएँ। संतुलित उर्वरक से पेड़ की ताकत बनाए रखें।",
        "pesticide_en": "Captan 50 WP @ 3.0 g/L OR Thiophanate-methyl 70 WP @ 1.0 g/L "
                        "OR Mancozeb 75 WP @ 2.5 g/L. Begin at pink bud; repeat every 10–14 days.",
        "pesticide_hi": "कैप्टन 50 WP @ 3.0 ग्राम/ली अथवा थायोफनेट-मिथाइल 70 WP @ 1.0 ग्राम/ली "
                        "अथवा मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली। गुलाबी कली से शुरू करें; 10–14 दिन पर दोहराएँ।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 4 ─────────────────────────────────────────────────────────────────────
    "apple_cedar_apple_rust": {
        "name_en": "Apple Cedar Rust",
        "name_hi": "सेब-देवदार रतुआ रोग",
        "cause_en": "Fungus Gymnosporangium juniperi-virginianae. Requires two hosts: "
                    "apple/crabapple and eastern red cedar (juniper).",
        "cause_hi": "जिम्नोस्पोरेंजियम जुनिपेरी-वर्जिनियाना फफूंद। इसे दो पोषक पौधे "
                    "चाहिए: सेब और देवदार/जुनिपर।",
        "symptoms_en": "Bright orange-yellow spots on upper leaf surface in spring; "
                       "tube-like spore structures on leaf undersides; fruit and twig infections.",
        "symptoms_hi": "वसंत में पत्तियों की ऊपरी सतह पर चमकीले नारंगी-पीले धब्बे; "
                       "पत्तियों की निचली सतह पर नलिकाकार बीजाणु संरचनाएँ।",
        "cure_en": "Fungicides applied at bud break and during wet spring weather give good control. "
                   "Removing nearby juniper trees breaks the disease cycle.",
        "cure_hi": "कली खुलने पर और नम वसंत मौसम में फफूंदनाशक का प्रयोग अच्छा नियंत्रण देता है। "
                   "पास के जुनिपर पेड़ हटाने से रोग चक्र टूट जाता है।",
        "prevention_en": "Plant rust-resistant apple varieties. Remove junipers within 1 km if possible. "
                         "Apply protective fungicide at 10-day intervals from bud break.",
        "prevention_hi": "रतुआ-प्रतिरोधी सेब किस्में लगाएँ। संभव हो तो 1 किमी के भीतर जुनिपर हटाएँ। "
                         "कली खुलने से 10-दिन के अंतराल पर सुरक्षात्मक फफूंदनाशक लगाएँ।",
        "pesticide_en": "Myclobutanil 24.5 EC @ 1.0 mL/L OR Propiconazole 25 EC @ 1.0 mL/L "
                        "OR Trifloxystrobin + Tebuconazole @ 0.5 g/L. Apply 3–4 times in spring.",
        "pesticide_hi": "माइक्लोब्युटेनिल 24.5 EC @ 1.0 मिली/ली अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली "
                        "अथवा ट्राइफ्लोक्सीस्ट्रोबिन + टेब्युकोनाज़ोल @ 0.5 ग्राम/ली। वसंत में 3–4 बार छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 5 ─────────────────────────────────────────────────────────────────────
    "apple_healthy": {
        "name_en": "Apple — Healthy",
        "name_hi": "सेब — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed. Continue good agronomic practices.",
        "cure_hi": "उपचार की आवश्यकता नहीं। अच्छी कृषि पद्धतियाँ जारी रखें।",
        "prevention_en": "Regular monitoring, balanced fertilization, proper pruning, "
                         "and timely irrigation keep apple trees healthy.",
        "prevention_hi": "नियमित निगरानी, संतुलित उर्वरक, उचित छंटाई और समय पर सिंचाई "
                         "सेब के पेड़ों को स्वस्थ रखती है।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 6 ─────────────────────────────────────────────────────────────────────
    "bacterial_leaf_blight": {
        "name_en": "Rice Bacterial Leaf Blight",
        "name_hi": "धान का जीवाणु पत्ती झुलसा (BLB)",
        "cause_en": "Bacterium Xanthomonas oryzae pv. oryzae. Spreads through irrigation water, "
                    "rain splash, and infected seed.",
        "cause_hi": "जैन्थोमोनास ओराइज़ी नामक जीवाणु। सिंचाई जल, वर्षा छींटों और "
                    "संक्रमित बीज से फैलता है।",
        "symptoms_en": "Water-soaked lesions on leaf margins turning yellow then straw-colored; "
                       "wilting of entire leaf (kresek phase in seedlings); milky bacterial ooze.",
        "symptoms_hi": "पत्ती के किनारों पर जलसिक्त घाव जो पीले फिर पुआल रंग के होते हैं; "
                       "पूरी पत्ती का मुरझाना (पौधे में क्रेसेक अवस्था); दूधिया जीवाणु स्राव।",
        "cure_en": "Drain fields and reduce nitrogen. Spray copper-based bactericide. "
                   "No curative chemical available — management is preventive.",
        "cure_hi": "खेत से पानी निकालें और नाइट्रोजन कम करें। तांबा-आधारित जीवाणुनाशक का छिड़काव करें। "
                   "कोई उपचारात्मक रसायन उपलब्ध नहीं — प्रबंधन निवारक है।",
        "prevention_en": "Use resistant varieties (IR-20, Pusa Basmati 1). Treat seed with "
                         "Streptomycin @ 0.5 g/L. Avoid excess nitrogen. Maintain clean irrigation.",
        "prevention_hi": "प्रतिरोधी किस्में (IR-20, पूसा बासमती 1) उगाएँ। बीज को "
                         "स्ट्रेप्टोमाइसिन @ 0.5 ग्राम/ली से उपचारित करें। नाइट्रोजन अधिक न दें। स्वच्छ सिंचाई बनाए रखें।",
        "pesticide_en": "Copper oxychloride 50 WP @ 3.0 g/L + Streptomycin sulfate 90% SP @ 0.2 g/L. "
                        "Spray 2–3 times at 10-day intervals after disease appearance.",
        "pesticide_hi": "कॉपर ऑक्सीक्लोराइड 50 WP @ 3.0 ग्राम/ली + स्ट्रेप्टोमाइसिन सल्फेट 90% SP @ 0.2 ग्राम/ली। "
                        "रोग दिखने के बाद 10 दिन के अंतराल पर 2–3 बार छिड़काव करें।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 7 ─────────────────────────────────────────────────────────────────────
    "banana_bract_mosaic_virus": {
        "name_en": "Banana Bract Mosaic Virus Disease",
        "name_hi": "केले का ब्रैक्ट मोज़ेक वायरस रोग",
        "cause_en": "Banana bract mosaic virus (BBrMV), a Potyvirus, transmitted by aphids "
                    "(Pentalonia nigronervosa).",
        "cause_hi": "केले का ब्रैक्ट मोज़ेक वायरस (BBrMV), एक पोटीवायरस, जो माहू "
                    "(पेन्टालोनिया निग्रोनर्वोसा) द्वारा फैलाया जाता है।",
        "symptoms_en": "Spindle-shaped chlorotic streaks on bracts and pseudostem; "
                       "mosaic patterns on leaves; distorted bunches; reduced yield.",
        "symptoms_hi": "ब्रैक्ट और छद्मतने पर धुरीदार पीली धारियाँ; पत्तियों पर मोज़ेक पैटर्न; "
                       "विकृत गुच्छे; उपज में कमी।",
        "cure_en": "No chemical cure. Remove and destroy infected plants promptly. "
                   "Control aphid vectors to limit spread.",
        "cure_hi": "कोई रासायनिक उपचार नहीं। संक्रमित पौधों को तुरंत हटाकर नष्ट करें। "
                   "फैलाव सीमित करने के लिए माहू वाहकों को नियंत्रित करें।",
        "prevention_en": "Use virus-free tissue-cultured planting material. Rogue out infected suckers. "
                         "Control aphids with systemic insecticide. Do not replant in infected fields.",
        "prevention_hi": "वायरस-मुक्त ऊतक संवर्धित पौध सामग्री उपयोग करें। संक्रमित सकर हटाएँ। "
                         "प्रणालीगत कीटनाशक से माहू नियंत्रित करें। संक्रमित खेत में पुनः रोपण न करें।",
        "pesticide_en": "To control aphid vector: Imidacloprid 17.8 SL @ 0.5 mL/L "
                        "OR Thiamethoxam 25 WG @ 0.3 g/L. Spray every 15 days.",
        "pesticide_hi": "माहू वाहक नियंत्रण हेतु: इमिडाक्लोप्रिड 17.8 SL @ 0.5 मिली/ली "
                        "अथवा थायमेथोक्सम 25 WG @ 0.3 ग्राम/ली। हर 15 दिन पर छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 8 ─────────────────────────────────────────────────────────────────────
    "banana_cordana": {
        "name_en": "Banana Cordana Leaf Spot",
        "name_hi": "केले का कॉर्डाना पत्ती धब्बा रोग",
        "cause_en": "Fungus Cordana musae (Helminthosporium torulosum). Favored by high humidity.",
        "cause_hi": "कॉर्डाना म्यूज़ी फफूंद। उच्च आर्द्रता में यह रोग अधिक होता है।",
        "symptoms_en": "Small oval brown spots with pale centers and dark brown margins on older leaves; "
                       "spots coalesce causing leaf blight in severe cases.",
        "symptoms_hi": "पुरानी पत्तियों पर हल्के केंद्र और गहरे भूरे हाशिए वाले छोटे अंडाकार भूरे धब्बे; "
                       "धब्बे मिलकर पत्ती झुलसा बनाते हैं।",
        "cure_en": "Remove and destroy severely infected leaves. Apply systemic fungicide "
                   "at first appearance of disease.",
        "cure_hi": "गंभीर रूप से संक्रमित पत्तियाँ हटाकर नष्ट करें। रोग के पहले लक्षण पर "
                   "प्रणालीगत फफूंदनाशक लगाएँ।",
        "prevention_en": "Avoid overhead irrigation. Maintain proper plant spacing for airflow. "
                         "Remove dead and dying leaves regularly.",
        "prevention_hi": "ऊपरी सिंचाई से बचें। वायु संचार के लिए उचित पौध अंतराल रखें। "
                         "मृत और सूखती पत्तियाँ नियमित हटाएँ।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Carbendazim 50 WP @ 1.0 g/L "
                        "OR Propiconazole 25 EC @ 1.0 mL/L. 2–3 sprays at 15-day intervals.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली "
                        "अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली। 15 दिन के अंतराल पर 2–3 छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 9 ─────────────────────────────────────────────────────────────────────
    "banana_healthy": {
        "name_en": "Banana — Healthy",
        "name_hi": "केला — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Use certified disease-free suckers or tissue-culture plants. "
                         "Ensure proper drainage and balanced nutrition.",
        "prevention_hi": "प्रमाणित रोगमुक्त सकर या ऊतक संवर्धन पौध उपयोग करें। "
                         "उचित जल निकासी और संतुलित पोषण सुनिश्चित करें।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 10 ────────────────────────────────────────────────────────────────────
    "banana_insectpest": {
        "name_en": "Banana Insect Pest",
        "name_hi": "केले के कीट",
        "cause_en": "Various insects including banana stem weevil (Cosmopolites sordidus), "
                    "thrips (Thrips hawaiiensis), and banana aphid.",
        "cause_hi": "केले का तना घुन (कॉस्मोपोलाइट्स सॉर्डिडस), थ्रिप्स "
                    "(थ्रिप्स हवाईएंसिस) और केले का माहू।",
        "symptoms_en": "Weevil: tunneling in corm/stem, yellowing, toppling. "
                       "Thrips: silvery streaks on leaves. Aphids: leaf curling, virus spread.",
        "symptoms_hi": "घुन: कंद/तने में सुरंग, पीलापन, पौधे का गिरना। "
                       "थ्रिप्स: पत्तियों पर चाँदी जैसी धारियाँ। माहू: पत्तियाँ मुड़ना, वायरस प्रसार।",
        "cure_en": "For weevils: apply chlorpyrifos granules around corm. "
                   "For thrips: spray insecticide under leaves. For aphids: systemic spray.",
        "cure_hi": "घुन के लिए: कंद के चारों ओर क्लोरपाइरीफॉस दाने डालें। "
                   "थ्रिप्स के लिए: पत्तियों के नीचे कीटनाशक छिड़कें। माहू के लिए: प्रणालीगत छिड़काव।",
        "prevention_en": "Use clean planting material. Destroy crop residues. "
                         "Trap weevils with cut pseudostem pieces. Regular field monitoring.",
        "prevention_hi": "स्वच्छ रोपण सामग्री उपयोग करें। फसल अवशेष नष्ट करें। "
                         "कटे हुए छद्मतने के टुकड़ों से घुन पकड़ें। नियमित खेत निगरानी।",
        "pesticide_en": "Chlorpyrifos 20 EC @ 2.5 mL/L (stem weevil) OR "
                        "Imidacloprid 17.8 SL @ 0.5 mL/L (aphids/thrips). "
                        "Spray 2–3 times at 15-day intervals.",
        "pesticide_hi": "क्लोरपाइरीफॉस 20 EC @ 2.5 मिली/ली (तना घुन) अथवा "
                        "इमिडाक्लोप्रिड 17.8 SL @ 0.5 मिली/ली (माहू/थ्रिप्स)। "
                        "15 दिन के अंतराल पर 2–3 बार छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 11 ────────────────────────────────────────────────────────────────────
    "banana_moko": {
        "name_en": "Banana Moko Disease (Bacterial Wilt)",
        "name_hi": "केले का मोको रोग (जीवाणु उकठा)",
        "cause_en": "Bacterium Ralstonia solanacearum race 2. Spreads through infected soil, "
                    "tools, and contaminated planting material.",
        "cause_hi": "राल्स्टोनिया सोलानेसेरम रेस 2 जीवाणु। संक्रमित मिट्टी, औजारों और "
                    "दूषित रोपण सामग्री से फैलता है।",
        "symptoms_en": "Internal browning of vascular tissue; premature ripening of fingers; "
                       "wilting and collapse of entire plant; bacterial ooze from cut stem.",
        "symptoms_hi": "संवहनी ऊतक का आंतरिक भूरापन; केलों का समय से पहले पकना; "
                       "पूरे पौधे का मुरझाकर गिरना; कटे तने से जीवाणु स्राव।",
        "cure_en": "No chemical cure available. Uproot and destroy infected plants by burning. "
                   "Disinfect tools with 10% bleach solution.",
        "cure_hi": "कोई रासायनिक उपचार उपलब्ध नहीं। संक्रमित पौधे उखाड़कर जलाकर नष्ट करें। "
                   "औजारों को 10% ब्लीच घोल से कीटाणुरहित करें।",
        "prevention_en": "Use disease-free tissue-culture plants. Do not replant in infested soil for 2–3 years. "
                         "Practice strict field sanitation. Disinfect cutting tools.",
        "prevention_hi": "रोगमुक्त ऊतक संवर्धन पौध उपयोग करें। 2–3 साल तक संक्रमित मिट्टी में पुनः रोपण न करें। "
                         "खेत में कड़ी स्वच्छता बनाएँ। काटने के औजार कीटाणुरहित करें।",
        "pesticide_en": "No effective bactericide. Preventive: drench soil with Copper oxychloride "
                        "@ 3 g/L around healthy plants as a barrier. Quarantine infected area.",
        "pesticide_hi": "कोई प्रभावी जीवाणुनाशक नहीं। निवारण: स्वस्थ पौधों के चारों ओर "
                        "कॉपर ऑक्सीक्लोराइड @ 3 ग्राम/ली से मिट्टी भिगोएँ। संक्रमित क्षेत्र को अलग करें।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 12 ────────────────────────────────────────────────────────────────────
    "banana_panama": {
        "name_en": "Banana Panama Wilt (Fusarium Wilt)",
        "name_hi": "केले का पनामा उकठा रोग",
        "cause_en": "Soil-borne fungus Fusarium oxysporum f.sp. cubense (Foc). "
                    "Persists in soil for decades.",
        "cause_hi": "मृदाजनित फफूंद फ्यूजेरियम ऑक्सीस्पोरम f.sp. क्यूबेंस (Foc)। "
                    "मिट्टी में दशकों तक जीवित रहती है।",
        "symptoms_en": "Yellowing of lower leaves progressing upward; splitting of pseudostem base; "
                       "reddish-brown internal discoloration; plant collapse.",
        "symptoms_hi": "निचली पत्तियों का पीलापन जो ऊपर की ओर बढ़ता है; छद्मतने के आधार का फटना; "
                       "आंतरिक लाल-भूरा रंग परिवर्तन; पौधे का गिरना।",
        "cure_en": "No chemical cure. Remove infected plants. Solarize soil before replanting. "
                   "Biocontrol: Trichoderma viride @ 5 kg/ha in soil.",
        "cure_hi": "कोई रासायनिक उपचार नहीं। संक्रमित पौधे हटाएँ। पुनः रोपण से पहले मिट्टी सोलराइज़ करें। "
                   "जैव नियंत्रण: ट्राइकोडर्मा विरिडी @ 5 किग्रा/हेक्टेयर मिट्टी में।",
        "prevention_en": "Use Foc-resistant varieties (Grand Nain, FHIA hybrids). "
                         "Never transplant suckers from infected areas. Improve soil drainage.",
        "prevention_hi": "Foc-प्रतिरोधी किस्में (ग्रैंड नेन, FHIA संकर) उपयोग करें। "
                         "संक्रमित क्षेत्रों के सकर कभी न रोपें। मिट्टी की जल निकासी सुधारें।",
        "pesticide_en": "Preventive soil drench: Carbendazim 50 WP @ 1.0 g/L around healthy plants. "
                        "Biocontrol: Pseudomonas fluorescens @ 10 g/L as soil drench.",
        "pesticide_hi": "निवारक मिट्टी भिगोना: स्वस्थ पौधों के चारों ओर कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली। "
                        "जैव नियंत्रण: स्यूडोमोनस फ्लुओरेसेंस @ 10 ग्राम/ली मिट्टी में।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 13 ────────────────────────────────────────────────────────────────────
    "banana_pestalotiopsis": {
        "name_en": "Banana Pestalotiopsis Leaf Spot",
        "name_hi": "केले का पेस्टालोटिओप्सिस पत्ती धब्बा",
        "cause_en": "Fungus Pestalotiopsis sp. Infects weakened or stressed plants. "
                    "Common in nurseries and under poor nutrition.",
        "cause_hi": "पेस्टालोटिओप्सिस प्रजाति की फफूंद। कमजोर या तनावग्रस्त पौधों को संक्रमित करती है। "
                    "नर्सरी में और कुपोषण में अधिक होता है।",
        "symptoms_en": "Elliptical brown lesions with gray centers and dark borders on leaves; "
                       "lesions may develop pink spore masses; premature leaf death.",
        "symptoms_hi": "पत्तियों पर भूरे केंद्र और गहरे हाशिए वाले अंडाकार भूरे घाव; "
                       "घावों पर गुलाबी बीजाणु पुंज; पत्तियों की समय से पहले मृत्यु।",
        "cure_en": "Remove infected leaves. Apply broad-spectrum fungicide. "
                   "Improve plant nutrition to boost resistance.",
        "cure_hi": "संक्रमित पत्तियाँ हटाएँ। व्यापक-स्पेक्ट्रम फफूंदनाशक लगाएँ। "
                   "प्रतिरोध बढ़ाने के लिए पौध पोषण सुधारें।",
        "prevention_en": "Avoid plant stress. Use balanced fertilizers. Adequate drainage. "
                         "Do not wound plants unnecessarily.",
        "prevention_hi": "पौध तनाव से बचें। संतुलित उर्वरक उपयोग करें। पर्याप्त जल निकासी। "
                         "पौधों को अनावश्यक चोट न दें।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Carbendazim 50 WP @ 1.0 g/L "
                        "OR Copper oxychloride 50 WP @ 3.0 g/L. Spray 2–3 times at 10-day intervals.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली "
                        "अथवा कॉपर ऑक्सीक्लोराइड 50 WP @ 3.0 ग्राम/ली। 10 दिन के अंतराल पर 2–3 छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 14 ────────────────────────────────────────────────────────────────────
    "banana_sigatoka": {
        "name_en": "Banana Yellow Sigatoka (Leaf Spot Disease)",
        "name_hi": "केले का पीला सिगाटोका रोग",
        "cause_en": "Fungus Mycosphaerella musicola. Spreads rapidly in warm, humid, "
                    "wet conditions via wind-borne ascospores.",
        "cause_hi": "माइकोस्फेरेला म्यूजिकोला फफूंद। गर्म, आर्द्र और नम मौसम में "
                    "हवा से फैलते बीजाणुओं द्वारा तेजी से फैलती है।",
        "symptoms_en": "Pale yellow streaks on leaves expanding to brown elliptical spots with "
                       "yellow halos; premature leaf death reduces photosynthesis and yield.",
        "symptoms_hi": "पत्तियों पर हल्की पीली धारियाँ जो पीले घेरे वाले भूरे अंडाकार धब्बों में बदलती हैं; "
                       "समय से पहले पत्ती मृत्यु से प्रकाश संश्लेषण और उपज घटती है।",
        "cure_en": "Apply systemic or contact fungicide at first sign. Remove badly infected leaves. "
                   "Ensure good drainage and plant spacing.",
        "cure_hi": "पहले लक्षण पर प्रणालीगत या संपर्क फफूंदनाशक लगाएँ। बुरी तरह संक्रमित पत्तियाँ हटाएँ। "
                   "अच्छी जल निकासी और पौध अंतराल सुनिश्चित करें।",
        "prevention_en": "Use resistant varieties. Avoid overcrowding. Remove dead leaves regularly. "
                         "Spray fungicide on a calendar schedule in high-pressure seasons.",
        "prevention_hi": "प्रतिरोधी किस्में उपयोग करें। अधिक घनी खेती से बचें। मृत पत्तियाँ नियमित हटाएँ। "
                         "अधिक दबाव के मौसम में कैलेंडर अनुसार फफूंदनाशक छिड़काव करें।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Propiconazole 25 EC @ 1.0 mL/L "
                        "OR Chlorothalonil 75 WP @ 2.0 g/L. Spray every 14–21 days.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली "
                        "अथवा क्लोरोथैलोनिल 75 WP @ 2.0 ग्राम/ली। हर 14–21 दिन पर छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 15 ────────────────────────────────────────────────────────────────────
    "banana_yb_sigatoka": {
        "name_en": "Banana Black/Yellow Sigatoka (Leaf Streak Disease)",
        "name_hi": "केले का काला/पीला सिगाटोका रोग",
        "cause_en": "Mycosphaerella fijiensis (Black Sigatoka) or Pseudocercospora musae. "
                    "Black Sigatoka is more aggressive than Yellow Sigatoka.",
        "cause_hi": "माइकोस्फेरेला फिजिएंसिस (काला सिगाटोका) या स्यूडोसेर्कोस्पोरा म्यूज़ी। "
                    "काला सिगाटोका पीले सिगाटोका से अधिक खतरनाक है।",
        "symptoms_en": "Dark streaks on leaves turning to black-brown necrotic lesions; "
                       "up to 50% yield loss possible; premature fruit ripening.",
        "symptoms_hi": "पत्तियों पर गहरी धारियाँ जो काले-भूरे परिगलित घावों में बदलती हैं; "
                       "50% तक उपज हानि संभव; फलों का समय से पहले पकना।",
        "cure_en": "Apply systemic triazole or strobilurin fungicide. Remove infected leaves. "
                   "Rotate fungicide classes to prevent resistance.",
        "cure_hi": "प्रणालीगत ट्राइएज़ोल या स्ट्रोबिलुरिन फफूंदनाशक लगाएँ। संक्रमित पत्तियाँ हटाएँ। "
                   "प्रतिरोध रोकने के लिए फफूंदनाशक वर्गों को बदलते रहें।",
        "prevention_en": "Plant resistant hybrids. Maintain proper field hygiene. "
                         "Avoid planting in poorly drained soils. Strict monitoring.",
        "prevention_hi": "प्रतिरोधी संकर किस्में लगाएँ। उचित खेत स्वच्छता बनाए रखें। "
                         "खराब जल निकासी वाली मिट्टी में रोपण न करें। कड़ी निगरानी।",
        "pesticide_en": "Propiconazole 25 EC @ 1.0 mL/L OR Trifloxystrobin 25% + Tebuconazole 50% "
                        "@ 0.5 g/L OR Azoxystrobin 23 SC @ 1.0 mL/L. Rotate fungicide groups.",
        "pesticide_hi": "प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली अथवा ट्राइफ्लोक्सीस्ट्रोबिन 25% + टेब्युकोनाज़ोल 50% "
                        "@ 0.5 ग्राम/ली अथवा अज़ोक्सीस्ट्रोबिन 23 SC @ 1.0 मिली/ली। फफूंदनाशक समूहों को बदलते रहें।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 16 ────────────────────────────────────────────────────────────────────
    "black_rust": {
        "name_en": "Wheat Black Rust (Stem Rust)",
        "name_hi": "गेहूँ का काला रतुआ (तना रतुआ)",
        "cause_en": "Fungus Puccinia graminis f.sp. tritici. Uredospores spread by wind "
                    "over long distances. Favored by warm temperatures (18–30°C).",
        "cause_hi": "पक्सिनिया ग्रैमिनिस f.sp. ट्रिटिसी फफूंद। यूरेडोस्पोर हवा से लंबी दूरी तक "
                    "फैलते हैं। गर्म तापमान (18–30°C) अनुकूल।",
        "symptoms_en": "Brick-red to dark brown uredinia (pustules) on stems, leaf sheaths, "
                       "and leaves; pustules rupture releasing rust-colored spores; severe lodging.",
        "symptoms_hi": "तनों, पत्ती आवरण और पत्तियों पर ईंट-लाल से गहरे भूरे यूरेडिनिया (फुंसियाँ); "
                       "फुंसियाँ फटकर रतुआ रंग के बीजाणु छोड़ती हैं; गंभीर आलोढ़न।",
        "cure_en": "Spray triazole fungicide at first sign of disease. "
                   "Early intervention is critical as disease spreads rapidly.",
        "cure_hi": "रोग के पहले संकेत पर ट्राइएज़ोल फफूंदनाशक का छिड़काव करें। "
                   "रोग तेजी से फैलता है इसलिए शीघ्र हस्तक्षेप आवश्यक है।",
        "prevention_en": "Grow resistant varieties (HD-2967, WB-02). Avoid late sowing. "
                         "Destroy volunteer wheat and alternate hosts (barberry).",
        "prevention_hi": "प्रतिरोधी किस्में (HD-2967, WB-02) उगाएँ। देर से बुवाई न करें। "
                         "अनायास उगा गेहूँ और वैकल्पिक पोषक (बर्बेरी) नष्ट करें।",
        "pesticide_en": "Propiconazole 25 EC @ 1.0 mL/L OR Tebuconazole 25.9 EC @ 1.0 mL/L "
                        "OR Hexaconazole 5 EC @ 2.0 mL/L. Apply 500 L spray solution per hectare.",
        "pesticide_hi": "प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली अथवा टेब्युकोनाज़ोल 25.9 EC @ 1.0 मिली/ली "
                        "अथवा हेक्साकोनाज़ोल 5 EC @ 2.0 मिली/ली। 500 ली छिड़काव घोल प्रति हेक्टेयर।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 17 ────────────────────────────────────────────────────────────────────
    "blast": {
        "name_en": "Wheat Blast",
        "name_hi": "गेहूँ का ब्लास्ट रोग",
        "cause_en": "Fungus Magnaporthe oryzae Triticum pathotype (MoT). "
                    "A quarantine pathogen in India; originates from Brazil, "
                    "reported in Bangladesh and potentially threatening South Asia.",
        "cause_hi": "मैग्नापोर्थे ओराइज़ी ट्रिटिकम पैथोटाइप (MoT) फफूंद। "
                    "भारत में यह एक संगरोध रोगज़नक है; ब्राज़ील में उत्पन्न, "
                    "बांग्लादेश में रिपोर्ट और दक्षिण एशिया के लिए खतरा।",
        "symptoms_en": "Bleached white spikes at heading; partial or complete loss of grain; "
                       "brown lesions at node and rachis; characteristic 'white ear' symptom.",
        "symptoms_hi": "बालियाँ निकलते समय सफेद पड़ना; आंशिक या पूर्ण दाना न भरना; "
                       "गाँठ और रेकिस पर भूरे घाव; विशिष्ट 'सफेद बाली' लक्षण।",
        "cure_en": "Apply triazole fungicide at boot leaf stage and at heading. "
                   "Report suspected cases to state agricultural department immediately.",
        "cure_hi": "बूट लीफ अवस्था और बाली निकलते समय ट्राइएज़ोल फफूंदनाशक लगाएँ। "
                   "संदिग्ध मामले राज्य कृषि विभाग को तुरंत सूचित करें।",
        "prevention_en": "Use blast-resistant varieties. Avoid dense sowing. Do not import wheat "
                         "seed from blast-affected countries. Follow ICAR surveillance guidelines.",
        "prevention_hi": "ब्लास्ट-प्रतिरोधी किस्में उपयोग करें। सघन बुवाई न करें। ब्लास्ट-प्रभावित "
                         "देशों से बीज आयात न करें। ICAR निगरानी दिशानिर्देशों का पालन करें।",
        "pesticide_en": "Tebuconazole 25.9 EC @ 1.0 mL/L OR Propiconazole 25 EC @ 1.0 mL/L "
                        "OR Tricyclazole 75 WP @ 0.6 g/L. Spray at boot stage and repeat at heading.",
        "pesticide_hi": "टेब्युकोनाज़ोल 25.9 EC @ 1.0 मिली/ली अथवा प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली "
                        "अथवा ट्राइसाइक्लाज़ोल 75 WP @ 0.6 ग्राम/ली। बूट अवस्था पर छिड़काव और बाली पर दोहराएँ।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 18 ────────────────────────────────────────────────────────────────────
    "blueberry_healthy": {
        "name_en": "Blueberry — Healthy",
        "name_hi": "ब्लूबेरी — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Maintain acidic soil pH (4.5–5.5). Good drainage. "
                         "Regular pruning and balanced fertilization.",
        "prevention_hi": "अम्लीय मिट्टी pH (4.5–5.5) बनाए रखें। अच्छी जल निकासी। "
                         "नियमित छंटाई और संतुलित उर्वरक।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 19 ────────────────────────────────────────────────────────────────────
    "brown_rust": {
        "name_en": "Wheat Brown Rust (Leaf Rust)",
        "name_hi": "गेहूँ का भूरा रतुआ (पत्ती रतुआ)",
        "cause_en": "Fungus Puccinia triticina. Most common rust disease of wheat in India. "
                    "Spreads by wind; favored by mild temperatures (15–22°C).",
        "cause_hi": "पक्सिनिया ट्रिटिसिना फफूंद। भारत में गेहूँ का सबसे आम रतुआ रोग। "
                    "हवा से फैलता है; हल्का तापमान (15–22°C) अनुकूल।",
        "symptoms_en": "Orange-brown circular to oval uredia on upper leaf surface; "
                       "scattered randomly unlike yellow rust; reduced grain weight.",
        "symptoms_hi": "पत्तियों की ऊपरी सतह पर नारंगी-भूरे गोलाकार से अंडाकार यूरेडिया; "
                       "पीले रतुआ के विपरीत बेतरतीब बिखरे हुए; दाने का भार कम।",
        "cure_en": "Spray triazole fungicide at first pustule appearance. "
                   "One well-timed spray at flag leaf stage is most effective.",
        "cure_hi": "पहली फुंसी दिखने पर ट्राइएज़ोल फफूंदनाशक छिड़काव करें। "
                   "ध्वज पत्ती अवस्था पर एक सही समय पर किया छिड़काव सबसे प्रभावी है।",
        "prevention_en": "Grow resistant varieties (PBW-343 resistant lines, HD-2967). "
                         "Timely sowing. Avoid excess nitrogen.",
        "prevention_hi": "प्रतिरोधी किस्में (PBW-343 प्रतिरोधी पंक्तियाँ, HD-2967) उगाएँ। "
                         "समय पर बुवाई। नाइट्रोजन अधिक न दें।",
        "pesticide_en": "Propiconazole 25 EC @ 1.0 mL/L OR Tebuconazole 25.9 EC @ 1.0 mL/L "
                        "OR Mancozeb 75 WP @ 2.0 g/L. Apply 500 L spray solution per ha.",
        "pesticide_hi": "प्रोपिकोनाज़ोल 25 EC @ 1.0 मिली/ली अथवा टेब्युकोनाज़ोल 25.9 EC @ 1.0 मिली/ली "
                        "अथवा मैनकोज़ेब 75 WP @ 2.0 ग्राम/ली। 500 ली छिड़काव घोल प्रति हेक्टेयर।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 20 ────────────────────────────────────────────────────────────────────
    "brown_spot": {
        "name_en": "Rice Brown Spot",
        "name_hi": "धान का भूरा धब्बा रोग",
        "cause_en": "Fungus Bipolaris oryzae (syn. Helminthosporium oryzae). "
                    "Favored by nutrient-deficient (potassium, silicon) soils and high humidity.",
        "cause_hi": "बाइपोलारिस ओराइज़ी फफूंद। पोषक-अपर्याप्त (पोटेशियम, सिलिकॉन) मिट्टी "
                    "और उच्च आर्द्रता में अधिक होता है।",
        "symptoms_en": "Circular to oval brown spots with gray center on leaves; "
                       "spots on glumes cause grain discoloration and chaff; "
                       "seedling blight in severe cases.",
        "symptoms_hi": "पत्तियों पर भूरे धब्बे जिनका केंद्र भूरा-हल्का; "
                       "ग्लूम्स पर धब्बे दाने का रंग बिगाड़ते हैं; "
                       "गंभीर मामलों में पौध झुलसा।",
        "cure_en": "Apply potassium and silicon fertilizers. Spray fungicide when "
                   "more than 10 spots per leaf are visible.",
        "cure_hi": "पोटेशियम और सिलिकॉन उर्वरक दें। जब प्रति पत्ती 10 से अधिक "
                   "धब्बे दिखें तो फफूंदनाशक छिड़काव करें।",
        "prevention_en": "Treat seed with Carbendazim @ 2 g/kg before sowing. "
                         "Apply adequate potash. Avoid water stress. Use healthy seed.",
        "prevention_hi": "बुवाई से पहले बीज को कार्बेन्डाज़िम @ 2 ग्राम/किग्रा से उपचारित करें। "
                         "पर्याप्त पोटाश दें। जल तनाव से बचें। स्वस्थ बीज उपयोग करें।",
        "pesticide_en": "Mancozeb 75 WP @ 2.5 g/L OR Carbendazim 50 WP @ 1.0 g/L "
                        "OR Iprodione 50 WP @ 2.0 g/L. Apply 2 sprays at 10-day intervals.",
        "pesticide_hi": "मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली अथवा कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली "
                        "अथवा इप्रोडिओन 50 WP @ 2.0 ग्राम/ली। 10 दिन के अंतराल पर 2 छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 21 ────────────────────────────────────────────────────────────────────
    "cauliflower_bacterial_spot_rot": {
        "name_en": "Cauliflower Bacterial Spot and Rot",
        "name_hi": "फूलगोभी का जीवाणु धब्बा एवं सड़न",
        "cause_en": "Xanthomonas campestris pv. campestris and soft-rot bacteria "
                    "(Pectobacterium carotovorum). Spread by rain, irrigation and contaminated tools.",
        "cause_hi": "जैन्थोमोनास कैम्पेस्ट्रिस और मृदु सड़न जीवाणु। वर्षा, "
                    "सिंचाई और दूषित औजारों से फैलते हैं।",
        "symptoms_en": "Water-soaked angular spots on leaves turning brown; "
                       "V-shaped lesions from leaf margin (black rot); "
                       "soft, foul-smelling rot of curd.",
        "symptoms_hi": "पत्तियों पर जलसिक्त कोणीय धब्बे जो भूरे होते हैं; "
                       "पत्ती किनारे से V-आकार के घाव (ब्लैक रॉट); दुर्गंधयुक्त मुलायम कर्ड सड़न।",
        "cure_en": "Remove infected plants. Apply copper-based bactericide. "
                   "Avoid overhead irrigation to keep curd dry.",
        "cure_hi": "संक्रमित पौधे हटाएँ। तांबा-आधारित जीवाणुनाशक लगाएँ। "
                   "कर्ड को सूखा रखने के लिए ऊपरी सिंचाई से बचें।",
        "prevention_en": "Use disease-free certified seed. Hot water seed treatment (50°C, 30 min). "
                         "Crop rotation. Avoid waterlogging.",
        "prevention_hi": "रोगमुक्त प्रमाणित बीज उपयोग करें। गर्म पानी बीज उपचार (50°C, 30 मिनट)। "
                         "फसल चक्र। जलभराव से बचें।",
        "pesticide_en": "Copper oxychloride 50 WP @ 3.0 g/L + Streptomycin sulfate @ 0.2 g/L. "
                        "OR Kasugamycin 3 SL @ 2.0 mL/L. Spray every 10 days.",
        "pesticide_hi": "कॉपर ऑक्सीक्लोराइड 50 WP @ 3.0 ग्राम/ली + स्ट्रेप्टोमाइसिन सल्फेट @ 0.2 ग्राम/ली। "
                        "अथवा कसुगामाइसिन 3 SL @ 2.0 मिली/ली। हर 10 दिन पर छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 22 ────────────────────────────────────────────────────────────────────
    "cauliflower_blackrot": {
        "name_en": "Cauliflower Black Rot",
        "name_hi": "फूलगोभी का काला सड़न रोग",
        "cause_en": "Bacterium Xanthomonas campestris pv. campestris. "
                    "Seed-borne; spreads through stomata, hydathodes, and wounds.",
        "cause_hi": "जैन्थोमोनास कैम्पेस्ट्रिस pv. कैम्पेस्ट्रिस जीवाणु। "
                    "बीजजनित; रंध्र, हाइडेथोड और घावों से फैलता है।",
        "symptoms_en": "Yellow V-shaped lesions from leaf margin turning brown-black; "
                       "blackening of vascular tissue visible in cross-section; "
                       "stunted distorted head.",
        "symptoms_hi": "पत्ती किनारे से पीले V-आकार के घाव जो भूरे-काले होते हैं; "
                       "काटने पर संवहनी ऊतक का कालापन दिखता है; अवरुद्ध विकृत सिर।",
        "cure_en": "No curative chemical once systemic. Remove infected plants. "
                   "Destroy crop debris post-harvest.",
        "cure_hi": "प्रणालीगत संक्रमण के बाद कोई उपचारात्मक रसायन नहीं। संक्रमित पौधे हटाएँ। "
                   "फसल के बाद अवशेष नष्ट करें।",
        "prevention_en": "Hot water seed treatment (50°C for 30 min). "
                         "3-year crop rotation avoiding all brassicas. "
                         "Use resistant varieties.",
        "prevention_hi": "गर्म पानी बीज उपचार (50°C पर 30 मिनट)। "
                         "सभी ब्रेसिका से बचते हुए 3 साल का फसल चक्र। "
                         "प्रतिरोधी किस्में उपयोग करें।",
        "pesticide_en": "Seed treatment: Streptomycin sulfate @ 0.5 g/L for 30 min soak. "
                        "Foliar: Copper oxychloride 50 WP @ 3.0 g/L spray at 10-day intervals.",
        "pesticide_hi": "बीज उपचार: स्ट्रेप्टोमाइसिन सल्फेट @ 0.5 ग्राम/ली में 30 मिनट भिगोएँ। "
                        "पत्ती पर: कॉपर ऑक्सीक्लोराइड 50 WP @ 3.0 ग्राम/ली — 10 दिन पर।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 23 ────────────────────────────────────────────────────────────────────
    "cauliflower_downy_mildew": {
        "name_en": "Cauliflower Downy Mildew",
        "name_hi": "फूलगोभी का आसिता / मृदुरोमिल आसिता",
        "cause_en": "Oomycete Peronospora parasitica. Favored by cool, moist conditions "
                    "and poor air circulation.",
        "cause_hi": "पेरोनोस्पोरा पैरासिटिका ओओमाइसीट। ठंडी, नम परिस्थितियाँ और "
                    "खराब वायु संचार में अधिक होता है।",
        "symptoms_en": "Yellow patches on upper leaf surface with white to grayish cottony "
                       "growth underneath; curd turns brown and rots in moist weather.",
        "symptoms_hi": "पत्तियों की ऊपरी सतह पर पीले धब्बे और नीचे सफेद से भूरे रूई जैसी वृद्धि; "
                       "नम मौसम में कर्ड भूरी होकर सड़ जाती है।",
        "cure_en": "Remove infected leaves. Apply systemic or contact fungicide. "
                   "Improve ventilation in dense canopy.",
        "cure_hi": "संक्रमित पत्तियाँ हटाएँ। प्रणालीगत या संपर्क फफूंदनाशक लगाएँ। "
                   "घने आवरण में वायु संचार सुधारें।",
        "prevention_en": "Avoid dense planting. Reduce leaf wetness with drip irrigation. "
                         "Apply preventive fungicide during cool, wet periods.",
        "prevention_hi": "घनी रोपाई से बचें। ड्रिप सिंचाई से पत्ती नमी कम करें। "
                         "ठंडे, नम समय में निवारक फफूंदनाशक लगाएँ।",
        "pesticide_en": "Metalaxyl-M + Mancozeb 72 WP @ 2.5 g/L OR Fosetyl-Aluminium 80 WP @ 2.5 g/L "
                        "OR Cymoxanil + Mancozeb 72 WP @ 3.0 g/L. Spray at 7-day intervals.",
        "pesticide_hi": "मेटालैक्सिल-M + मैनकोज़ेब 72 WP @ 2.5 ग्राम/ली अथवा "
                        "फोसेटिल-एल्युमिनियम 80 WP @ 2.5 ग्राम/ली। 7 दिन के अंतराल पर छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 24 ────────────────────────────────────────────────────────────────────
    "cauliflower_healthy": {
        "name_en": "Cauliflower — Healthy",
        "name_hi": "फूलगोभी — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Adequate boron supplementation prevents browning of curd. "
                         "Balanced NPK, proper spacing, and timely irrigation.",
        "prevention_hi": "पर्याप्त बोरॉन पूरकता कर्ड के भूरेपन को रोकती है। "
                         "संतुलित NPK, उचित अंतराल और समय पर सिंचाई।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 25 ────────────────────────────────────────────────────────────────────
    "cherry_including_sour_healthy": {
        "name_en": "Cherry (Sweet/Sour) — Healthy",
        "name_hi": "चेरी (मीठी/खट्टी) — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Annual pruning, dormant copper spray, and good soil drainage "
                         "maintain cherry health.",
        "prevention_hi": "वार्षिक छंटाई, सुप्त तांबा छिड़काव और अच्छी मिट्टी जल निकासी "
                         "चेरी को स्वस्थ रखती है।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 26 ────────────────────────────────────────────────────────────────────
    "cherry_including_sour_powdery_mildew": {
        "name_en": "Cherry Powdery Mildew",
        "name_hi": "चेरी का चूर्णिल आसिता (पाउडरी मिल्ड्यू)",
        "cause_en": "Fungus Podosphaera clandestina. Favored by warm days, cool nights, "
                    "and dry conditions. Does not require free water to germinate.",
        "cause_hi": "पोडोस्फेरा क्लैंडेस्टिना फफूंद। गर्म दिन, ठंडी रात और शुष्क परिस्थितियाँ अनुकूल। "
                    "अंकुरण के लिए मुक्त जल की आवश्यकता नहीं।",
        "symptoms_en": "White powdery fungal growth on young leaves, shoots, and fruit; "
                       "leaves curl and distort; shoot growth suppressed in severe cases.",
        "symptoms_hi": "युवा पत्तियों, प्ररोहों और फलों पर सफेद पाउडरयुक्त फफूंद वृद्धि; "
                       "पत्तियाँ मुड़ती और विकृत होती हैं; गंभीर मामलों में प्ररोह वृद्धि रुकती है।",
        "cure_en": "Apply sulfur-based or sterol-inhibiting fungicide at first sign. "
                   "Remove and destroy infected shoots.",
        "cure_hi": "पहले लक्षण पर सल्फर-आधारित या स्टेरॉल-अवरोधक फफूंदनाशक लगाएँ। "
                   "संक्रमित प्ररोह हटाकर नष्ट करें।",
        "prevention_en": "Avoid excessive nitrogen. Ensure good air circulation through pruning. "
                         "Apply dormant lime-sulfur spray in late winter.",
        "prevention_hi": "अत्यधिक नाइट्रोजन से बचें। छंटाई के माध्यम से अच्छा वायु संचार सुनिश्चित करें। "
                         "देर सर्दियों में सुप्त चूना-सल्फर छिड़काव करें।",
        "pesticide_en": "Sulfur 80 WDG @ 3.0 g/L OR Myclobutanil 24.5 EC @ 1.0 mL/L "
                        "OR Triadimefon 25 WP @ 1.0 g/L. Spray every 7–10 days during outbreak.",
        "pesticide_hi": "सल्फर 80 WDG @ 3.0 ग्राम/ली अथवा माइक्लोब्युटेनिल 24.5 EC @ 1.0 मिली/ली "
                        "अथवा ट्राइडाइमिफॉन 25 WP @ 1.0 ग्राम/ली। प्रकोप के दौरान 7–10 दिन पर।",
        "severity": "medium",
        "is_healthy": False,
    },

    # ── 27 ────────────────────────────────────────────────────────────────────
    "chilli_anthracnose": {
        "name_en": "Chilli Anthracnose (Die-back & Fruit Rot)",
        "name_hi": "मिर्च का एन्थ्रेक्नोज (डाई-बैक एवं फल सड़न)",
        "cause_en": "Fungi Colletotrichum capsici and C. gloeosporioides. "
                    "Spreads through infected seed and rain splash. Favored by warm, humid weather.",
        "cause_hi": "कोलेटोट्राइकम कैप्सिसी और C. ग्लोयोस्पोरियोइड्स फफूंद। "
                    "संक्रमित बीज और वर्षा छींटों से फैलती है। गर्म, आर्द्र मौसम में अधिक।",
        "symptoms_en": "Circular sunken lesions with salmon-pink spore masses on ripe fruit; "
                       "shoot die-back from tip; dark brown blighted leaves.",
        "symptoms_hi": "पके फलों पर सालमन-गुलाबी बीजाणु पुंज के साथ गोल धँसे घाव; "
                       "नोक से प्ररोह की पीछे से मृत्यु; गहरे भूरे झुलसे पत्ते।",
        "cure_en": "Remove and destroy infected fruit and shoots. Apply systemic fungicide. "
                   "Spray at 10-day intervals during humid periods.",
        "cure_hi": "संक्रमित फल और प्ररोह हटाकर नष्ट करें। प्रणालीगत फफूंदनाशक लगाएँ। "
                   "नम समय में 10 दिन के अंतराल पर छिड़काव।",
        "prevention_en": "Treat seed with Thiram @ 3 g/kg or hot water (55°C, 30 min). "
                         "Crop rotation. Use resistant varieties (LCA-625).",
        "prevention_hi": "बीज को थीरम @ 3 ग्राम/किग्रा या गर्म पानी (55°C, 30 मिनट) से उपचारित करें। "
                         "फसल चक्र। प्रतिरोधी किस्में (LCA-625) उपयोग करें।",
        "pesticide_en": "Carbendazim 50 WP @ 1.0 g/L OR Mancozeb 75 WP @ 2.5 g/L "
                        "OR Azoxystrobin 23 SC @ 1.0 mL/L. Spray from fruit-set stage every 10 days.",
        "pesticide_hi": "कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली अथवा मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली "
                        "अथवा अज़ोक्सीस्ट्रोबिन 23 SC @ 1.0 मिली/ली। फल लगने से हर 10 दिन पर छिड़काव।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 28 ────────────────────────────────────────────────────────────────────
    "chilli_healthy": {
        "name_en": "Chilli — Healthy",
        "name_hi": "मिर्च — स्वस्थ",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy with no visible disease symptoms.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है, कोई रोग लक्षण नहीं।",
        "cure_en": "No treatment needed.",
        "cure_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Use certified disease-free seed. Balanced NPK with calcium and boron. "
                         "Regular scouting for insects and disease.",
        "prevention_hi": "प्रमाणित रोगमुक्त बीज उपयोग करें। कैल्शियम और बोरॉन सहित संतुलित NPK। "
                         "कीट और रोग के लिए नियमित निगरानी।",
        "pesticide_en": "None required.",
        "pesticide_hi": "कोई कीटनाशक आवश्यक नहीं।",
        "severity": "none",
        "is_healthy": True,
    },

    # ── 29 ────────────────────────────────────────────────────────────────────
    "chilli_leafcurl": {
        "name_en": "Chilli Leaf Curl Disease",
        "name_hi": "मिर्च का पत्ती मरोड़ रोग",
        "cause_en": "Chilli leaf curl virus (ChiLCV), a Begomovirus transmitted "
                    "by whitefly Bemisia tabaci in a persistent manner.",
        "cause_hi": "मिर्च पत्ती मरोड़ वायरस (ChiLCV), एक बेगोमोवायरस, जो "
                    "बेमिसिया टेबेसी सफेद मक्खी द्वारा लगातार तरीके से फैलाया जाता है।",
        "symptoms_en": "Severe upward or downward curling of leaves; reduced leaf size; "
                       "thickened veins; stunted plant; flower and fruit drop; "
                       "entire plant may be stunted.",
        "symptoms_hi": "पत्तियों का गंभीर ऊपर या नीचे की ओर मुड़ना; पत्ती आकार में कमी; "
                       "मोटी नसें; अवरुद्ध पौधा; फूल और फल का झड़ना।",
        "cure_en": "No chemical cure for the virus. Manage whitefly vector strictly. "
                   "Remove and destroy infected plants early.",
        "cure_hi": "वायरस का कोई रासायनिक उपचार नहीं। सफेद मक्खी वाहक का कड़ा प्रबंधन। "
                   "संक्रमित पौधे जल्दी हटाकर नष्ट करें।",
        "prevention_en": "Use virus-resistant varieties. Install yellow sticky traps. "
                         "Apply reflective mulch to repel whiteflies. "
                         "Spray insecticide weekly during high-whitefly period.",
        "prevention_hi": "वायरस-प्रतिरोधी किस्में उपयोग करें। पीले चिपचिपे जाल लगाएँ। "
                         "सफेद मक्खी भगाने के लिए परावर्तक मल्च बिछाएँ। "
                         "अधिक सफेद मक्खी अवधि में साप्ताहिक कीटनाशक छिड़काव।",
        "pesticide_en": "Imidacloprid 17.8 SL @ 0.5 mL/L OR Thiamethoxam 25 WG @ 0.3 g/L "
                        "OR Spiromesifen 22.9 SC @ 1.0 mL/L. Spray at 7-day intervals. "
                        "Rotate insecticide groups.",
        "pesticide_hi": "इमिडाक्लोप्रिड 17.8 SL @ 0.5 मिली/ली अथवा थायमेथोक्सम 25 WG @ 0.3 ग्राम/ली "
                        "अथवा स्पाइरोमेसीफेन 22.9 SC @ 1.0 मिली/ली। 7 दिन के अंतराल पर। "
                        "कीटनाशक समूहों को बदलते रहें।",
        "severity": "high",
        "is_healthy": False,
    },

    # ── 30 ────────────────────────────────────────────────────────────────────
    "chilli_leafspot": {
        "name_en": "Chilli Leaf Spot",
        "name_hi": "मिर्च का पत्ती धब्बा रोग",
        "cause_en": "Fungi Cercospora capsici (frogeye spot) and Colletotrichum sp. "
                    "Favored by warm, humid conditions. Spreads by rain and wind.",
        "cause_hi": "सेर्कोस्पोरा कैप्सिसी और कोलेटोट्राइकम प्रजाति फफूंद। "
                    "गर्म, आर्द्र परिस्थितियाँ अनुकूल। वर्षा और हवा से फैलती है।",
        "symptoms_en": "Circular to irregular brown spots with pale gray center and dark margin; "
                       "spots drop out giving shot-hole appearance; heavy defoliation in severe cases.",
        "symptoms_hi": "हल्के भूरे केंद्र और गहरे हाशिए वाले गोल से अनियमित भूरे धब्बे; "
                       "धब्बे गिरकर शॉट-होल का रूप देते हैं; गंभीर मामलों में भारी पत्ती झड़ना।",
        "cure_en": "Remove heavily infected leaves. Apply fungicide spray. "
                   "Ensure good drainage and reduce leaf wetness.",
        "cure_hi": "अत्यधिक संक्रमित पत्तियाँ हटाएँ। फफूंदनाशक छिड़काव करें। "
                   "अच्छी जल निकासी सुनिश्चित करें और पत्ती नमी कम करें।",
        "prevention_en": "Treat seed with Thiram @ 3 g/kg. Crop rotation. "
                         "Avoid overhead irrigation. Use resistant varieties.",
        "prevention_hi": "बीज को थीरम @ 3 ग्राम/किग्रा से उपचारित करें। फसल चक्र। "
                         "ऊपरी सिंचाई से बचें। प्रतिरोधी किस्में उपयोग करें।",
        "pesticide_en": "Carbendazim 50 WP @ 1.0 g/L OR Mancozeb 75 WP @ 2.5 g/L "
                        "OR Chlorothalonil 75 WP @ 2.0 g/L. Spray 2–3 times at 10-day intervals.",
        "pesticide_hi": "कार्बेन्डाज़िम 50 WP @ 1.0 ग्राम/ली अथवा मैनकोज़ेब 75 WP @ 2.5 ग्राम/ली "
                        "अथवा क्लोरोथैलोनिल 75 WP @ 2.0 ग्राम/ली। 10 दिन के अंतराल पर 2–3 छिड़काव।",
        "severity": "medium",
        "is_healthy": False,
    },
}
