import streamlit as st

st.set_page_config(page_title="My Referral Links for reviews on PACE Institute of Technology and Sciences", page_icon="🔗")

st.title("PACE College Review Referrals")
st.write("If you're planning to write a review on our college, these codes might give us both a bonus!")

# List of your 4 website details
websites = [
    {"name": "Shiksha", "url": "https://www.shiksha.com/college-review-rating-form?utm_source=shiksha&utm_medium=referral&utm_campaign=5155073thankyou", "code": "5155073"},
    {"name": "Zollege", "url": "https://zollege.in/write-review?referral_code=4CAE6A9", "code": "4CAE6A9"},
    {"name": "Collegedunia", "url": "https://collegedunia.com/write-review/temp?referral_code=C98F6B5&utm_source=mobile&utm_medium=whatsapp&utm_campaign=thank_you_page", "code": "C98F6B5"},
    {"name": "Collegedekho", "url": "https://www.collegedekho.com/reviews/add-and-earn#tell_us", "code": "CECAE23F"},
]

# Create a 2x2 grid using columns
col1, col2 = st.columns(2)

for i, site in enumerate(websites):
    # Alternate between column 1 and column 2
    target_col = col1 if i % 2 == 0 else col2
    
    with target_col:
        with st.container(border=True):
            st.subheader(site["name"])
            st.write("Use this code to get your bonus:")
            
            # st.code provides an easy "copy" button for your friends
            st.code(site["code"], language=None)
            
            # Link button to go to the site
            st.link_button(f"Go to {site['name']}", site["url"])
            
