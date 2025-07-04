from aqt import Collection, fields, mw
from aqt.gui_hooks import profile_did_open
from anki.consts import MODEL_STD
from functools import cache
from typing import Any

mcnt_model_name = "Multiple Choice Note Type"
mcnt_card_name = "Multiple Choice Card"

front_template_path = "card-templates/front_template.html"
back_template_path = "card-templates/back_template.html"
styling_template_path = "card-templates/styling.css"

# Get the folder path
def get_addon_path() -> str:
    return mw.addonManager.addonsFolder() + "/" + mw.addonManager.addonFromModule(__name__) + "/"

# Load the template file to text
@cache
def load_template(path: str) -> str:
    with open(get_addon_path() + path, encoding="utf-8") as f:
        return f.read()

def create_note_type(col: Collection) -> dict[str, Any]:
    
    print(f"Creating {mcnt_model_name} note type")

    model = col.models.new(mcnt_model_name)
    model["type"] = MODEL_STD
    model["sortf"] = 0

    # Add Fields
    col.models.add_field(model, col.models.new_field("question"))
    col.models.add_field(model, col.models.new_field("a"))
    col.models.add_field(model, col.models.new_field("b"))
    col.models.add_field(model, col.models.new_field("c"))
    col.models.add_field(model, col.models.new_field("d"))
    col.models.add_field(model, col.models.new_field("e"))
    col.models.add_field(model, col.models.new_field("f"))
    col.models.add_field(model, col.models.new_field("g"))
    col.models.add_field(model, col.models.new_field("h"))
    col.models.add_field(model, col.models.new_field("i"))
    col.models.add_field(model, col.models.new_field("j"))
    col.models.add_field(model, col.models.new_field("answers"))
    col.models.add_field(model, col.models.new_field("ref"))
    col.models.add_field(model, col.models.new_field("explanation"))

    # Create Card Template
    template = col.models.new_template(mcnt_card_name)
    col.models.add_template(model, template)

    if "isShuffle" in config:
        if isinstance(config["isShuffle"], bool):
            isShuffle = config["isShuffle"]
        else:
            isShuffle = False
    else:
        isShuffle = False

    if "isDisplayAnswerLetters" in config:
        if isinstance(config["isDisplayAnswerLetters"], bool):
            isDisplayAnswerLetters = config["isDisplayAnswerLetters"]
        else:
            isDisplayAnswerLetters = False
    else:
        isDisplayAnswerLetters = False

    if "isTTS" in config:
        if isinstance(config["isTTS"], bool):
            isTTS = config["isTTS"]
        else:
            isTTS = False
    else:
        isTTS = False

    if "TTSLang" in config:
        if isinstance(config["TTSLang"], str):
            TTSLang = config["TTSLang"]
        else:
            TTSLang = "en_US"
    else:
        TTSLang = "en_US"
    
    front_template = load_template(front_template_path)
    if isShuffle is True:
        front_template = front_template.replace("isShuffle","true")
    else:
        front_template = front_template.replace("isShuffle","false")
    if isDisplayAnswerLetters is True:
        front_template = front_template.replace("isDisplayAnswerLetters","true")
    else:
        front_template = front_template.replace("isDisplayAnswerLetters","false")
    if isTTS is False:
        front_template = front_template.replace("<div id=\"tts\">{{tts TTSLang speed=0.8 voices=Apple_Samantha,Microsoft_Haruka:question}}</div>","<div id=\"tts\" style=\"width: 0px\"></div>")
    front_template = front_template.replace("TTSLang",TTSLang)
    model["tmpls"][0]["qfmt"] = front_template

    back_template = load_template(back_template_path)
    if isDisplayAnswerLetters is True:
        back_template = back_template.replace("isDisplayAnswerLetters","true")
    else:
        back_template = back_template.replace("isDisplayAnswerLetters","false")
    if isTTS is False:
        back_template = back_template.replace("<legend id=\"tts\"><b>Explanation: {{tts TTSLang speed=0.8 voices=Apple_Samantha,Microsoft_Haruka:explanation}}</b></legend>","<legend id=\"tts\"><b>Explanation: </b></legend>")
    back_template = back_template.replace("TTSLang",TTSLang)
    model["tmpls"][0]["afmt"] = back_template

    styling = load_template(styling_template_path)
    model["css"] = styling

    col.models.add(model)
   
    return model

def update_note_type(col: Collection) -> dict[str, Any]:
    
    model = mw.col.models.by_name(mcnt_model_name)

    print(f"Updating {mcnt_model_name} note type")

    # Update Card Template
    if "isShuffle" in config:
        if isinstance(config["isShuffle"], bool):
            isShuffle = config["isShuffle"]
        else:
            isShuffle = False
    else:
        isShuffle = False

    if "isDisplayAnswerLetters" in config:
        if isinstance(config["isDisplayAnswerLetters"], bool):
            isDisplayAnswerLetters = config["isDisplayAnswerLetters"]
        else:
            isDisplayAnswerLetters = False
    else:
        isDisplayAnswerLetters = False

    if "isTTS" in config:
        if isinstance(config["isTTS"], bool):
            isTTS = config["isTTS"]
        else:
            isTTS = False
    else:
        isTTS = False

    if "TTSLang" in config:
        if isinstance(config["TTSLang"], str):
            TTSLang = config["TTSLang"]
        else:
            TTSLang = "en_US"
    else:
        TTSLang = "en_US"
    
    front_template = load_template(front_template_path)
    if isShuffle is True:
        front_template = front_template.replace("isShuffle","true")
    else:
        front_template = front_template.replace("isShuffle","false")
    if isDisplayAnswerLetters is True:
        front_template = front_template.replace("isDisplayAnswerLetters","true")
    else:
        front_template = front_template.replace("isDisplayAnswerLetters","false")
    if isTTS is False:
        front_template = front_template.replace("<div id=\"tts\">{{tts TTSLang speed=0.8 voices=Apple_Samantha,Microsoft_Haruka:question}}</div>","<div id=\"tts\" style=\"width: 0px\"></div>")
    front_template = front_template.replace("TTSLang",TTSLang)
    model["tmpls"][0]["qfmt"] = front_template

    back_template = load_template(back_template_path)
    if isDisplayAnswerLetters is True:
        back_template = back_template.replace("isDisplayAnswerLetters","true")
    else:
        back_template = back_template.replace("isDisplayAnswerLetters","false")
    if isTTS is False:
        back_template = back_template.replace("<legend id=\"tts\"><b>Explanation: {{tts TTSLang speed=0.8 voices=Apple_Samantha,Microsoft_Haruka:explanation}}</b></legend>","<legend id=\"tts\"><b>Explanation: </b></legend>")
    back_template = back_template.replace("TTSLang",TTSLang)
    model["tmpls"][0]["afmt"] = back_template

    styling = load_template(styling_template_path)
    model["css"] = styling

    col.models.save(model)

    return model

def create_update_note_type():
    model = mw.col.models.by_name(mcnt_model_name)

    if not model:
        create_note_type(mw.col)
    else:
        update_note_type(mw.col)

config = mw.addonManager.getConfig(__name__)

profile_did_open.append(create_update_note_type)
