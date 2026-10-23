"""Static rice/paddy disease info (English + Tamil). Index order == model output order."""

CROP_EN, CROP_TA = "Rice / Paddy", "நெல்"

# Order MUST match the model's 6 outputs.
LABELS = ["Bacterial Leaf Blight", "Brown Spot", "Leaf Blast",
          "Sheath Blight", "Tungro", "Leaf Scald", "Healthy"]

# name_ta, cause_en, cause_ta, fixes_en, fixes_ta
INFO = {
    "Bacterial Leaf Blight": (
        "பாக்டீரியா இலைக் கருகல் நோய்",
        "Bacterium (Xanthomonas oryzae); yellow to white streaks with wavy edges starting from leaf tips, worse after rain/flooding and with excess nitrogen.",
        "சாந்தோமோனாஸ் பாக்டீரியா; இலை நுனியிலிருந்து அலை விளிம்புடன் மஞ்சள்-வெள்ளைக் கோடுகள்; மழை, வெள்ளம், அதிக தழைச்சத்து உரத்தில் அதிகரிக்கும்.",
        ["Avoid excess nitrogen fertilizer; split the dose.",
         "Drain the field and avoid water flowing from infected plots.",
         "Spray copper-based bactericide as per label/agri officer advice.",
         "Use resistant varieties and clean seed next season."],
        ["தழைச்சத்து உரத்தை அதிகமாக இடாமல் பிரித்து இடவும்.",
         "வயலில் தேங்கிய நீரை வடித்து, பாதித்த வயலிலிருந்து நீர் பாய்வதைத் தடுக்கவும்.",
         "வேளாண் அலுவலர் ஆலோசனை/லேபிள் படி தாமிர பாக்டீரியா கொல்லி தெளிக்கவும்.",
         "அடுத்த பருவத்தில் நோய் எதிர்ப்பு ரகம் மற்றும் தரமான விதைகளைப் பயன்படுத்தவும்."]),
    "Brown Spot": (
        "பழுப்பு இலைப்புள்ளி நோய்",
        "Fungus (Bipolaris oryzae); oval brown spots with grey centres on leaves; linked to nutrient-poor soil (low potash) and water stress.",
        "பைபோலாரிஸ் பூஞ்சை; இலைகளில் சாம்பல் மையத்துடன் நீள்வட்டப் பழுப்புப் புள்ளிகள்; சத்து குறைந்த மண் (பொட்டாஷ் குறைவு), நீர் பற்றாக்குறையில் அதிகம்.",
        ["Apply balanced fertilizer, especially potash.",
         "Treat seed with a recommended fungicide or Pseudomonas fluorescens.",
         "Spray mancozeb or a recommended fungicide as per label if spreading.",
         "Keep field weed-free and avoid water stress."],
        ["சமச்சீர் உரம், குறிப்பாக சாம்பல் சத்து (பொட்டாஷ்) இடவும்.",
         "விதைகளை பரிந்துரைக்கப்பட்ட பூஞ்சைக்கொல்லி அல்லது சூடோமோனாஸ் புளோரசன்ஸ் கொண்டு நேர்த்தி செய்யவும்.",
         "பரவினால் லேபிள் படி மேன்கோசெப் அல்லது பரிந்துரைக்கப்பட்ட பூஞ்சைக்கொல்லி தெளிக்கவும்.",
         "வயலை களையின்றி வைத்து, நீர் பற்றாக்குறையைத் தவிர்க்கவும்."]),
    "Leaf Blast": (
        "குலை நோய் (இலை)",
        "Fungus (Magnaporthe oryzae); diamond/spindle-shaped spots with grey centres; favoured by cool humid nights, heavy dew and excess nitrogen.",
        "மேக்னபோர்தே பூஞ்சை; சாம்பல் மையத்துடன் வைர/கதிர் வடிவ புள்ளிகள்; குளிர்ந்த ஈர இரவு, அதிக பனி, அதிக தழைச்சத்தில் பரவும்.",
        ["Avoid excess nitrogen; use balanced fertilizer.",
         "Spray tricyclazole or a recommended fungicide as per label.",
         "Use resistant varieties and treated seed.",
         "Remove nearby weed hosts and crop residue."],
        ["அதிக தழைச்சத்தைத் தவிர்த்து சமச்சீர் உரம் இடவும்.",
         "லேபிள் படி டிரைசைக்ளசோல் அல்லது பரிந்துரைக்கப்பட்ட பூஞ்சைக்கொல்லி தெளிக்கவும்.",
         "நோய் எதிர்ப்பு ரகம் மற்றும் நேர்த்தி செய்த விதைகளைப் பயன்படுத்தவும்.",
         "அருகிலுள்ள களைகள் மற்றும் பயிர்க் கழிவுகளை அகற்றவும்."]),
    "Sheath Blight": (
        "உறைக் கருகல் நோய்",
        "Fungus (Rhizoctonia solani); oval greenish-grey lesions on leaf sheaths near the water line; worse with dense planting and high nitrogen.",
        "ரைசோக்டோனியா பூஞ்சை; நீர்மட்டத்துக்கு அருகில் இலை உறையில் பச்சை-சாம்பல் நீள்வட்டத் திட்டுகள்; நெருக்கமான நடவு, அதிக தழைச்சத்தில் அதிகம்.",
        ["Use wider spacing; avoid dense planting.",
         "Drain the field periodically and remove weeds.",
         "Spray validamycin or hexaconazole as per label.",
         "Avoid excess nitrogen."],
        ["நெருக்கமாக நடாமல் போதிய இடைவெளி விடவும்.",
         "வயலில் அவ்வப்போது நீரை வடித்து, களைகளை அகற்றவும்.",
         "லேபிள் படி வாலிடாமைசின் அல்லது ஹெக்சாகோனசோல் தெளிக்கவும்.",
         "அதிக தழைச்சத்தைத் தவிர்க்கவும்."]),
    "Tungro": (
        "துங்ரோ வைரஸ் நோய்",
        "Virus disease spread by green leafhoppers; yellow-orange leaves and stunted plants with fewer tillers. No cure once infected.",
        "பச்சை தத்துப்பூச்சியால் பரவும் வைரஸ் நோய்; இலைகள் மஞ்சள்-ஆரஞ்சாக மாறி, செடி வளர்ச்சி குன்றி, தூர்கள் குறையும். பாதித்த பின் குணப்படுத்த முடியாது.",
        ["Uproot and destroy infected plants early.",
         "Control leafhoppers (light traps, recommended insecticide as per label).",
         "Plant resistant varieties; keep planting time uniform across nearby fields.",
         "Remove weeds and stubble that host the virus."],
        ["பாதித்த செடிகளை ஆரம்பத்திலேயே பிடுங்கி அழிக்கவும்.",
         "தத்துப்பூச்சியைக் கட்டுப்படுத்தவும் (விளக்குப் பொறி, லேபிள் படி பரிந்துரைக்கப்பட்ட பூச்சிக்கொல்லி).",
         "நோய் எதிர்ப்பு ரகங்களை நடவும்; அருகிலுள்ள வயல்களில் ஒரே நேரத்தில் நடவு செய்யவும்.",
         "வைரஸ் தங்கும் களைகள் மற்றும் அடிக்கட்டைகளை அகற்றவும்."]),
    "Leaf Scald": (
        "இலை வெந்து கருகல் நோய்",
        "Fungus (Microdochium oryzae); scalded-looking zonate lesions starting from leaf tips and edges; favoured by high nitrogen and humid weather.",
        "மைக்ரோடோகியம் பூஞ்சை; இலை நுனி, ஓரங்களில் வெந்தது போன்ற வளையத் திட்டுகள்; அதிக தழைச்சத்து, ஈரப்பத வானிலையில் அதிகரிக்கும்.",
        ["Avoid excess nitrogen.",
         "Use clean, treated seed.",
         "Remove infected crop residue after harvest.",
         "Apply a recommended fungicide as per label if spreading."],
        ["அதிக தழைச்சத்தைத் தவிர்க்கவும்.",
         "தரமான, நேர்த்தி செய்த விதைகளைப் பயன்படுத்தவும்.",
         "அறுவடைக்குப் பின் பாதித்த பயிர்க் கழிவுகளை அகற்றவும்.",
         "பரவினால் லேபிள் படி பரிந்துரைக்கப்பட்ட பூஞ்சைக்கொல்லி தெளிக்கவும்."]),
}

NO_DISEASE = (
    "No clear disease detected", "நோய் தெளிவாகத் தெரியவில்லை",
    "The model is not confident that any of its 6 known rice diseases is present. The leaf may be healthy, or the photo may be unclear.",
    "மாடலுக்குத் தெரிந்த 6 நெல் நோய்களில் எதுவும் உறுதியாகத் தெரியவில்லை. இலை ஆரோக்கியமாக இருக்கலாம் அல்லது படம் தெளிவாக இல்லாமல் இருக்கலாம்.",
    ["Continue normal care and watch the crop weekly.",
     "If symptoms appear, upload a clear close-up of a single leaf.",
     "Confirm with your local agriculture officer if in doubt."],
    ["வழக்கமான பராமரிப்பைத் தொடர்ந்து வாரந்தோறும் பயிரைக் கவனிக்கவும்.",
     "அறிகுறி தென்பட்டால் ஒரு இலையை தெளிவாக அருகில் எடுத்த படத்தை பதிவேற்றவும்.",
     "சந்தேகம் இருந்தால் வேளாண் அலுவலரை அணுகவும்."],
)


def build(label):
    """label=None -> 'no clear disease'."""
    if label is None:
        name_en = NO_DISEASE[0]
        name_ta, cause_en, cause_ta, fix_en, fix_ta = NO_DISEASE[1:]
    else:
        name_en = label
        name_ta, cause_en, cause_ta, fix_en, fix_ta = INFO[label]
    return {
        "plant_en": CROP_EN, "plant_ta": CROP_TA,
        "disease_en": name_en, "disease_ta": name_ta,
        "cause_en": cause_en, "cause_ta": cause_ta,
        "fix_en": fix_en, "fix_ta": fix_ta,
    }
