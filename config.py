from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_anonymizer import AnonymizerEngine
from presidio_image_redactor import ImageRedactorEngine, ImageAnalyzerEngine


# SCRUBBING CONFIGURATIONS

SCRUB_CONFIG_TRF = {
    "nlp_engine_name": "spacy",
    "models": [{"lang_code": "en", "model_name": "en_core_web_trf"}],
}
SCRUB_PROVIDER_TRF = NlpEngineProvider(nlp_configuration=SCRUB_CONFIG_TRF)
NLP_ENGINE_TRF = SCRUB_PROVIDER_TRF.create_engine()
ANALYZER_TRF = AnalyzerEngine(
    nlp_engine=NLP_ENGINE_TRF,
    supported_languages=["en"]
)
ANONYMIZER = AnonymizerEngine()
IMAGE_REDACTOR = ImageRedactorEngine(ImageAnalyzerEngine(ANALYZER_TRF))

# SCRUB_CONFIG_LG = {
#     "nlp_engine_name": "spacy",
#     "models": [{"lang_code": "en", "model_name": "en_core_web_lg"}],
# }
# SCRUB_PROVIDER_LG = NlpEngineProvider(nlp_configuration=SCRUB_CONFIG_LG)
# NLP_ENGINE_LG = SCRUB_PROVIDER_LG.create_engine()
# ANALYZER_LG = AnalyzerEngine(
#     nlp_engine=NLP_ENGINE_LG,
#     supported_languages=["en"]
# )

SCRUB_IGNORE_ENTITIES = [
    # 'US_PASSPORT',
    # 'US_DRIVER_LICENSE',
    # 'CRYPTO',
    # 'UK_NHS',
    # 'PERSON',
    # 'CREDIT_CARD',
    # 'US_BANK_NUMBER',
    # 'PHONE_NUMBER',
    # 'US_ITIN',
    # 'AU_ABN',
    'DATE_TIME',
    # 'NRP',
    # 'SG_NRIC_FIN',
    # 'AU_ACN',
    # 'IP_ADDRESS',
    # 'EMAIL_ADDRESS',
    'URL',
    # 'IBAN_CODE',
    # 'AU_TFN',
    # 'LOCATION',
    # 'AU_MEDICARE',
    # 'US_SSN',
    # 'MEDICAL_LICENSE'
]
SCRUBBING_ENTITIES = [
    entity
    for entity in ANALYZER_TRF.get_supported_entities()
    if entity not in SCRUB_IGNORE_ENTITIES
]
SCRUB_KEYS_HTML = [
    'text',
    'canonical_text',
    'title',
    'state'
]
DEFAULT_SCRUB_FILL_COLOR = (255,0,0)
