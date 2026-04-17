import zipfile
import os

# Create final_email_sequence.zip
email_files = [
    'email_1_welcome.html',
    'email_2_cto.html',
    'email_3_cmo.html',
    'email_4_cfo.html',
    'email_5_last_chance.html',
    'email_sequence.md'
]

with zipfile.ZipFile('final_email_sequence.zip', 'w') as zipf:
    for file in email_files:
        if os.path.exists(file):
            zipf.write(file)

# Create final_marketing_assets_bundle.zip
all_assets = [
    'final_ad_copy.html',
    'final_social_posts.csv',
    'final_email_sequence.zip',
    'mars_os_hero.html',
    'mars_os_vision.html',
    'budget_roi_model.json',
    'campaign_calendar.json',
    'CAMPAIGN_STRATEGY.md'
]

with zipfile.ZipFile('final_marketing_assets_bundle.zip', 'w') as zipf:
    for file in all_assets:
        if os.path.exists(file):
            zipf.write(file)

print("Zip files created successfully.")
