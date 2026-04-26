import streamlit as st
import numpy as np
from supabase import create_client, Client

def format_indian_currency(number):
    s = str(int(number))
    if len(s) <= 3:
        return s
    else:
        last_three = s[-3:]
        remaining = s[:-3]
        # उर्वरित अंकांना दर २ अंकांनंतर स्वल्पविराम (comma) लावणे
        import re
        remaining = re.sub(r'(\d+?)(?=(\d{2})+(?!\d))', r'\1,', remaining)
        return f"{remaining},{last_three}"

# --- Supabase Setup ---

url: str = "https://lbcqixepexpwoqavmfcb.supabase.co"
key: str = "sb_publishable_ZL1rFKd-OiV91WSdx8VbXg_izmfSVp2"
supabase: Client = create_client(url, key)

col1, col2, col3 = st.columns(3)
with col2:
    st.image("pic.jpeg", width=200)

col1, col2, col3 = st.columns([0.6,1.75,0.6])
with col2:
    st.header("दहीहंडी बजेट फॉर्म २०२६")

st.info("आपल्या दहीहंडी उत्सवाचे योग्य नियोजन आणि बजेट ठरवण्यासाठी हा फॉर्म आहे. तुमचे मत आमच्यासाठी महत्त्वाचे आहे, त्यामुळे कृपया संपूर्ण फॉर्म न विसरता भरा.")
st.error("तुम्ही दिलेली सर्व माहिती पूर्णपणे गोपनीय (Private) ठेवली जाईल आणि ती इतर कोणत्याही सदस्यासोबत शेअर केली जाणार नाही. त्यामुळे कोणतीही शंका न " \
"बाळगता मोकळेपणाने हा फॉर्म भरा. याव्यतिरिक्त तुम्हाला तुमचे काही विचार मांडायचे असतील, तर ते खाली दिलेल्या कमेंट बॉक्समध्ये नक्की नोंदवा")

st.divider()
name = st.selectbox("**आपले नाव**", ["Aditya Dhokane", "Akash Barate", "Akash Waghmare", "Aman Danane", "Bhushan Chorghe", "Deepak Jadhav", 
                                     "Ganesh Jawalkar", "Mahesh Barate", "Om Padwal", "Om Jawalkar", "Om Phengse", "Omkar Barate", "Omkar Bharekar", 
                                     "Prasad Khatavkar", "Rohan Thorat", "Shubham Sathe", "Suyash Kadu", "Tushar Amrale", "Vikram Unecha",
                                     "Vishal Waghmare", "Yash Gunjal", "माझे नाव लिस्ट मधे नाही"], index=None, placeholder="निवडा...")

if name == "माझे नाव लिस्ट मधे नाही":
    st.warning("कृपया आपले नाव कमेंट मधे टाकावेत")

st.divider()

sound = st.slider("**साउंड बजेट** (मागील वर्षी ४५,००० होत)", min_value=40000, max_value=150000, step=5000, value=60000, format="₹%d")
sound_name = st.text_input("**साउंड चे नाव**")
st.divider()
light = st.slider("**लाईट बजेट**  (मागील वर्षी ७७,००० होत)", min_value=50000, max_value=200000, step=5000, value=80000, format="₹%d")
light_name = st.text_input("**लाईट चे नाव**")
st.divider()
gen = st.slider("**जनरेटर बजेट**  (मागील वर्षी १४,५०० होत)", min_value=10000, max_value=30000, step=500, value=17000, format="₹%d")
st.divider()
dhol = st.slider("**गोविंदा पतक बजेट**  (मागील वर्षी ५,००० होत)", min_value=0, max_value=15000, step=500, value=7000, format="₹%d")
st.divider()
pavti = st.slider("**पावतीपुस्तक + पत्रिका बजेट**  (मागील वर्षी ६,५०० होत)", min_value=4000, max_value=20000, step=500, value=8000, format="₹%d")
st.divider()
handi_deco = st.slider("**दहीहंडी डेकोरेशनवर बजेट**  (मागील वर्षी ३,५०० होत)", min_value=0, max_value=15000, step=500, value=4000, format="₹%d")
st.divider()
flex = st.slider("**फ्लेक्स + पाड बजेट**  (मागील वर्षी ९,६३२ होत)", min_value=5000, max_value=15000, step=500, value=6000, format="₹%d")
st.divider()
pol = st.slider("**पोलीस चलन**  (मागील वर्षी ५,००० होत)", min_value=0, max_value=20000, step=500, value=8000, format="₹%d")
st.divider()
oper = st.slider("**ऑपरेटर बजेट**  (मागील वर्षी ७,००० होत)", min_value=0, max_value=15000, step=500, value=7000, format="₹%d")
st.divider()
shal = st.slider("**श्हाल नारळ बजेट**  (मागील वर्षी ३,६७० होत)", min_value=3000, max_value=15000, step=500, value=4000, format="₹%d")
st.divider()
crane = st.slider("**क्रेन बजेट**  (मागील वर्षी ०० होत)", min_value=0, max_value=12000, step=500, value=3000, format="₹%d")
st.divider()
other = st.slider("**किरकोळ खर्च**  (मागील वर्षी ७,५७७ होत)", min_value=4000, max_value=15000, step=500, value=8000, format="₹%d")
st.divider()
comment = st.text_area("**कमेंट**", height=150)
st.divider()

list = [name, sound, light, gen, pavti, flex, shal, other]

arr = np.array([sound, light, gen, pavti, flex, shal, crane, other, dhol, handi_deco, pol, oper, crane])

total = np.sum(arr)

# फंक्शन वापरून फॉरमॅटिंग करा
formatted_total = format_indian_currency(total)

st.markdown(
    f"""
    <div style="
        background-color: #e8f4f8; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 5px solid #007bff;
        text-align: center;">
        <p style="font-size: 18px; color: #000; margin-bottom: 5px;">तुम्ही भारलेल्या बजेट नुसार एकूण रक्कम होत आहे</p>
        <h1 style="font-size: 45px; color: #007bff; margin: 0;">₹{formatted_total}</h1>
    </div>
    """, 
    unsafe_allow_html=True
)

st.divider()

# --- Submit to Supabase ---
if all(list):
    if st.button("Submit", type="primary"):
        if name:
            data = {
                "user_name": name,
                "sound_budget": sound,
                "sound_name": sound_name,
                "light_budget": light,
                "light_name": light_name,
                "gen_budget": gen,
                "dhol_budget": dhol,
                "pavti_budget": pavti,
                "handi_deco_budget": handi_deco,
                "flex_budget": flex,
                "police_chalan": pol,
                "operator_budget": oper,
                "shal_naral_budget": shal,
                "crane_budget": crane,
                "other_expenses": other,
                "total_amount": int(total),
                "comment": comment
            }
            
            try:
                response = supabase.table("dahi_handi_budget").insert(data).execute()
                st.success("माहिती यशस्वीरित्या नोंदवली गेली आहे!")
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.warning("पुढे जाण्यासाठी कृपया सर्व भरा.")

# if all(list):
#     if st.button("Submit", type="primary"):
#         st.success("माहिती दिल्याबद्दल धन्यवाद! तुमचा प्रतिसाद यशस्वीरित्या नोंदवला गेला आहे.")
# else:
#     st.warning("पुढे जाण्यासाठी कृपया सर्व भरा.")
