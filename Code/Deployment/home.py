import requests
import streamlit as st

from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def home():
    st.title(":blue[Autism Spectrum Disorder]")
    st.write("---")
    
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.title("What is Autism Spectrum Disorder?")
            st.write("""
            Autism spectrum disorder (ASD) is a developmental disability caused by differences in the brain. People with ASD often have problems with social communication and interaction, and restricted or repetitive behaviors or interests. People with ASD may also have different ways of learning, moving, or paying attention.
            """)
        

        with st.container():
            col1, col2 = st.columns([4, 2])
            with col1:
                st.title("What Causes Autism Spectrum Disorder?")
                st.write("""
                The Autism Spectrum Disorder Foundation lists the following as possible causes of ASD:

                :blue[Genetics] : Research suggests that ASD can be caused by a combination of genetic and environmental factors. Some genes have been identified as being associated with an increased risk for ASD, but no single gene has been proven to cause ASD.

                :blue[Environmental factors] : Studies are currently underway to explore whether certain exposure to toxins during pregnancy or after birth can increase the risk for developing ASD.

                :blue[Brain differences] : Differences in certain areas of the brain have been observed in people with ASD, compared to those without ASD. It is not yet known what causes these differences.
                """)

        with st.container():
            col1, col2 = st.columns([4, 2])
            with col1:
                st.title("Signs of autism in adults")

                st.write("""
                Common signs of autism in adults include:

                1. finding it hard to understand what others are thinking or feeling
                2. getting very anxious about social situations
                3. finding it hard to make friends or preferring to be on your own
                4. seeming blunt, rude or not interested in others without meaning to
                5. finding it hard to say how you feel
                6. taking things very literally – for example, you may not understand sarcasm or phrases like "break a leg"
                7. having the same routine every day and getting very anxious if it changes

                Other signs of autism

                You may also have other signs, like:

                1. not understanding social "rules", such as not talking over people
                2. avoiding eye contact
                3. getting too close to other people, or getting very upset if someone touches or gets too close to you
                4. noticing small details, patterns, smells or sounds that others do not
                5. having a very keen interest in certain subjects or activities
                6. liking to plan things carefully before doing them
                """)

                st.write("[Learn More >](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders)")

        # ---- WHAT I DO ----
        with st.container():
            left_column, right_column = st.columns([4, 2])
            with left_column:
                st.title("Relevant statistics ")

                st.write("""
                    The exact prevalence of Autism Spectrum Disorder (ASD) in India is not well-established due to a lack of nationwide studies and consistent diagnostic criteria. However, some studies have estimated that the prevalence of ASD in India is between 1 and 2 per 1000 children.
                    A recent study published in the Indian Journal of Pediatrics in 2020 estimated the prevalence of ASD in children aged 2 to 9 years in Kolkata, India, to be 1.25%. Another study published in the Journal of Autism and Developmental Disorders in 2018 found a prevalence of 0.64% among school-aged children in Chennai, India.

                    • Prevalence of Autism: Between 1 in 500 (2/1,000) to 1 in 166 children (6/1,000) have an Autism Spectrum Disorder (Center for Disease Control).

                    • Prevalence Rate: Approx. 1 in 500 or 0.20% or more than 2,160,000 people in India.

                    • Incidence Rate: Approx. 1 in 90,666 or 11,914 people in India.

                    • Incidence extrapolations for India for Autism: 11,914 per year, 250 per month, 57 per week, 8 per day, 1.4 per hour.

                    • Autism is four times more prevalent in boys than girls in the US (Autism Society of America).

                    • Autism is more common than Down Syndrome, which occurs in 1 out of 800 births.

                    • The rate of incidence of autism is increasing 10-17% per year in the US (Autism Society of America).

                    • Prevalence of autism is expected to reach 4 million people in the next decade in the US (Autism Society of America).
                    """)

if __name__ == "__main__":
    home()
