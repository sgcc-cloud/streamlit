import streamlit as st

def main():
    # Title of the event
    st.title('Welcome to UWC Ticket Booking Registration')

    # Description
    st.write("""
    Kindly click the link below to register for the event.
    The event is limited to 300 pax.
    """)

    # Counter to keep track of visits
    visit_counter = st.session_state.get('visit_counter', 0)

    # Register button
    if visit_counter < len(url_list):
        url_list = [
            "google.com",
            "yahoo.com",
            "outlook.com",
            "hotmail.com",
            "gmail.com",
            # Add the remaining 27 URLs here
        ]
        next_url = url_list[visit_counter]
        registration_link = f"<a href='{next_url}' target='_blank'>Register</a>"
        st.markdown(registration_link, unsafe_allow_html=True)
    else:
        st.write("Fully Booked")

    # Display the visit counter
    st.write(f"Total Visits: {visit_counter}")

    # Increment the visit counter for the next person
    st.session_state.visit_counter = visit_counter + 1

if __name__ == '__main__':
    main()
