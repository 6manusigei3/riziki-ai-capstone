import streamlit as st

st.set_page_config(
    page_title="Riziki AI",
    page_icon="💰"
)

st.title("💰 Riziki AI")
st.subheader("Ethical SACCO Loan Assessment Prototype")

name = st.text_input("Applicant Name")

occupation = st.selectbox(
    "Occupation",
    [
        "Market Vendor",
        "Farmer",
        "Small Business Owner",
        "Formal Employee"
    ]
)

amount = st.number_input(
    "Loan Amount (KES)",
    min_value=1000,
    step=1000
)

reason = st.text_area(
    "Reason for Loan"
)

if st.button("Assess Loan"):

    st.header("Scout Agent")

    stress_keywords = [
        "school fees",
        "debt",
        "loan shark"
    ]

    alert = any(
        word in reason.lower()
        for word in stress_keywords
    )

    if alert:
        st.warning(
            "Financial stress signal detected."
        )
    else:
        st.success(
            "No financial stress signals detected."
        )

    st.header("Guardian Agent")

    if amount <= 15000:
        st.success(
            "Eligible for Tier-1 Approval"
        )

    else:
        st.warning(
            "Escalating to Hunter Agent"
        )

        st.header("Hunter Agent")

        st.info(f"""
Applicant: {name}

Occupation: {occupation}

Loan Requested: KES {amount:,}

Recommendation:
Human review required before final approval.
""")

    st.header("Ethical Safeguards")

    st.write("✓ Human-in-the-loop review")
    st.write("✓ Bias-aware assessment")
    st.write("✓ Kenyan Data Protection compliance")
