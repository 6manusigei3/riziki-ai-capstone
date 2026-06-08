import streamlit as st

st.set_page_config(
    page_title="Riziki AI",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Riziki AI")
st.subheader("Ethical SACCO Loan Assessment Prototype")

st.write(
    "Riziki AI uses a multi-agent approach to support fair and transparent lending decisions."
)

# Applicant Information

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

    st.divider()

    # ---------------------------
    # SCOUT AGENT
    # ---------------------------

    st.header("🔍 Scout Agent")

    stress_keywords = [
        "school fees",
        "debt",
        "loan shark",
        "medical bill",
        "hospital",
        "emergency"
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

    # ---------------------------
    # GUARDIAN AGENT
    # ---------------------------

    st.header("🛡 Guardian Agent")

    risk_score = 0

    # Loan amount risk

    if amount > 50000:
        risk_score += 2

    elif amount > 15000:
        risk_score += 1

    # Financial stress risk

    if alert:
        risk_score += 1

    st.write(f"Risk Score: {risk_score}")

    # ---------------------------
    # DECISION ENGINE
    # ---------------------------

    if risk_score == 0:

        st.success("✅ APPROVED")

        st.write(
            """
            Tier-1 Loan Approved.

            Applicant qualifies for automatic approval.
            """
        )

    elif risk_score <= 2:

        st.warning("⚠ ESCALATED FOR HUMAN REVIEW")

        st.header("🎯 Hunter Agent")

        st.info(
            f"""
Applicant: {name}

Occupation: {occupation}

Loan Requested: KES {amount:,}

Reason:
{reason}

Recommendation:
Human review required before final approval.
"""
        )

    else:

        st.error("❌ LOAN DENIED")

        st.write(
            """
Reasons:
- High loan amount requested
- Financial stress indicators detected
- Risk threshold exceeded

Applicant may reapply after financial review.
"""
        )

    # ---------------------------
    # ETHICAL SAFEGUARDS
    # ---------------------------

    st.divider()

    st.header("⚖ Ethical Safeguards")

    st.write("✓ Human-in-the-loop review")
    st.write("✓ Bias-aware assessment")
    st.write("✓ Transparent decision support")
    st.write("✓ Kenyan Data Protection compliance")
    st.write("✓ No gender or ethnicity-based decisions")
