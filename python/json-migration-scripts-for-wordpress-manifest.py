from copy import deepcopy
import encodings
import json

def transform_manifest(input_manifest:dict)->dict:
    """
    Transforming manifest by grouping web_apps intp appLanguages based on 
    languageInEnglishName (lowercased).
    """
    output_manifest=deepcopy(input_manifest)
    web_apps =input_manifest.get("web_apps",[])
    app_language={}
    language_counters={}
    for app in web_apps:
        
        lang_key =app.get("languageInEnglishName","").lower()
        if not lang_key:
            continue
        if lang_key not in language_counters:
            language_counters[lang_key]=0
        language_entry={
            "appId":language_counters[lang_key],
            "appIconUrl":app.get("appIconUrl"),
            "title":app.get("title"),
            "appUrl": app.get("appUrl"),
            "language":app.get("language"),
        }
        language_counters[lang_key]+=1
        app_language.setdefault(lang_key,[]).append(language_entry)
        
    output_manifest["appLanguages"]=app_language
    return output_manifest
        
if __name__=="__main__":
    # add your path to manifest.json.
    with open("/Users/amitkumarsingh/Documents/personal-Github/automation-scripts/python/json-migration-scripts-for-wordpress-manifest/manifest.json","r", encoding="utf-8") as f:
        input_manifest=json.load(f)
        
    updated_manifest=transform_manifest(input_manifest)
    
    with open("manifest_updated.json","w",encoding="utf-8") as f:
        json.dump(updated_manifest,f,indent=2,ensure_ascii=False)
        
    print("✅ Manifest transformed Successfully")